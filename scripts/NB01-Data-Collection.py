import requests
import os
import json
from dotenv import load_dotenv
import time

#LOADING API KEY
# The key lives in .env, which is gitignored; .env.example carries the name only.
load_dotenv()

API_KEY = os.getenv("FRED_API_KEY")
print(f"API key loaded: {API_KEY is not None}")

URL_FRED = "https://api.stlouisfed.org/fred/series/observations"

#COLLECTION
def fetch_data():
    # Both series come from the same endpoint and differ only by series_id
    series = ["SP500", "BRMSA0104"]

    for s in series:
        params = {
            "series_id":s,
            "api_key":API_KEY,
            "file_type":"json",
            "observation_start":"2016-07-25",
            "observation_end":"2026-07-22"
        }

        #try and except for catching runtime exceptions - if error, keeps running the code
        try:
            response = requests.get(url=URL_FRED, params=params, timeout=30)

            if 200 <= response.status_code < 300:
                data = response.json()

                with open(f"data/raw/{s}.json","w",encoding="utf-8") as f:
                    json.dump(data, f)

            else:
                print(f"ERROR! The response status code is {response.status_code}.")

        # A timeout or a dropped connection should not end the whole run, so the
        # other series can still be collected, and the message says which failed.
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError) as e:
            print(f"Request failed for {s}: {e}")

        last_element = series[-1]

        # A short pause between api calls - convention
        if s != last_element:
            time.sleep(2)

fetch_data()
