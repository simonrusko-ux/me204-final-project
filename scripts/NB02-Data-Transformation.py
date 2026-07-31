import json
import pandas as pd


#Collecting data rows
def load_data_rows(series_id: str) -> pd.DataFrame:
   
    with open(f"data/raw/{series_id}.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data["observations"])
    df = df[["date", "value"]]
    df["series"] = series_id

    return df


#Computing monthly mean both for s&p and brmsa0104
def get_mean_month(df: pd.DataFrame) -> pd.DataFrame:
   
    df = df.loc[df["value"] != "."].copy()
    df["value"] = pd.to_numeric(df["value"])
    df["date"] = df["date"].str[:7]

    monthly = (
        df.groupby(["series", "date"])["value"].mean().reset_index()
    )

    return monthly


#transforming to monthly percentage for sp500
def transform_pct_sp500() -> pd.DataFrame:

    df_sp500 = load_data_rows("SP500")
    df_mean_sp500 = get_mean_month(df_sp500)

    #using .pct_change function for comparing monht with a previous month
    #also, converting value points to %
    df_mean_sp500["value"] = df_mean_sp500["value"].pct_change() * 100

    # The first month has nothing to compare against and comes out as NaN.
    df_mean_sp500 = df_mean_sp500.dropna(subset="value")

    df_mean_sp500 = df_mean_sp500.rename(columns={"value":"return_pct"})
    return df_mean_sp500


#transforming to monthly percentage for brmsa0104
def transform_pct_brmsa() -> pd.DataFrame:

    df_brmsa0104 = load_data_rows("BRMSA0104")
    df_mean_brmsa0104 = get_mean_month(df_brmsa0104)

    #from yearly mean to mean per month
    df_mean_brmsa0104["value"] = df_mean_brmsa0104["value"] / 12

    df_mean_brmsa0104 = df_mean_brmsa0104.rename(columns={"value":"return_pct"})
    return df_mean_brmsa0104


def put_to_csv():

    brmsa0104 = transform_pct_brmsa()
    sp500 = transform_pct_sp500()

    #concatenating both tables together
    df = pd.concat([brmsa0104, sp500])

    #s&p starting from August, brmsa0104 from July, so I had to get rid of the first month
    #to keep my starting date consistent
    df = df.drop(index=0)

    #putting the data into csv format
    with open("data/processed/monthly_returns.csv","w",encoding="utf-8") as f:
        df.to_csv(f, index=False)


put_to_csv()
