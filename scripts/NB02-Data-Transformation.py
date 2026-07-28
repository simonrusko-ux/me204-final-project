import json
import pandas as pd


#SERIES = ["SP500", "BRMSA0104"]

def load_data_rows(series_id: str) -> pd.DataFrame:

    with open(f"data/raw/{series_id}.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data["observations"])
    df = df[["date", "value"]]
    df["series"] = series_id

    return df


def get_mean_month(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.loc[df["value"] != "."].copy()
    df["value"] = pd.to_numeric(df["value"])
    df["date"] = df["date"].str[:7]

    df_mean_montly = (
        df.groupby(["series", "date"])["value"].mean().reset_index()
    )

    return df_mean_montly





df = load_data_rows("BRMSA0104")

get = get_mean_month(df)

print(get)



