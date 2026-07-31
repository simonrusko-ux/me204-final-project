# ME204 Final Project: S&P 500 vs. Savings Account: A 10-Year Comparison

| GitHub username  | LSE ID       |
| ---------------- | ------------ |
| `simonrusko-ux`  | `250085411`   |

## Overview

If money had gone into the S&P 500 ten years ago instead of into a savings
account, what would the difference be today? The pipeline collects two FRED
series, puts them on a common monthly footing, and compares what $1,000 became in
each. The answer for a general reader is at
[simonrusko-ux.github.io/me204-final-project](https://simonrusko-ux.github.io/me204-final-project/simonrusko-ux).

## Data sources

Both series come from the **FRED API** (Federal Reserve Bank of St. Louis),
endpoint `https://api.stlouisfed.org/fred/series/observations`. No supplementary
or manually collected data is used.

| Series | What it is | Frequency | Units |
| --- | --- | --- | --- |
| `SP500` | S&P 500 index, price only | daily, business days | index level |
| `BRMSA0104` | Bankrate national average savings APY | weekly | percent per year |

Two things about this pair drive the whole of NB02. They arrive at different
frequencies, and they are different kinds of number: one is a price level, the
other is already a rate. `SP500` is also the shorter series, so it sets the
window at **2016-07-25 to 2026-07-22**. Those dates are hard-coded in NB01 rather
than derived from today, so that reruns keep matching the figures on the website.

## How to reproduce

**Credentials.** Request a free API key at
[fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html),
then copy `.env.example` to `.env` and fill in the key. `.env` is gitignored and
is not part of this repository.

```bash
cp .env.example .env      # then edit, setting FRED_API_KEY
```

**Environment.** Python 3.14, with:

```bash
pip install requests pandas plotly python-dotenv kaleido
```

`kaleido` is only needed for the PNG export at the end of NB03; everything else
runs without it.

**Run the files in this order.** NB01 and NB02 are run from the repository root.
NB03 is a notebook and is opened from `scripts/`, which is why its paths start
`../data/` while the scripts' paths do not.

```bash
python scripts/NB01-Data-Collection.py
python scripts/NB02-Data-Transformation.py
# then open scripts/NB03-simonrusko-ux-Data-Analysis.ipynb and Run All
```

| File | Reads | Does | Writes |
| --- | --- | --- | --- |
| `scripts/NB01-Data-Collection.py` | FRED API | one request per series, fixed date window | `data/raw/SP500.json`, `data/raw/BRMSA0104.json` |
| `scripts/NB02-Data-Transformation.py` | `data/raw/*.json` | drops FRED's `"."` missing markers, averages each series by month, converts both to a monthly return in percent | `data/processed/monthly_returns.csv` |
| `scripts/NB03-simonrusko-ux-Data-Analysis.ipynb` | `data/processed/monthly_returns.csv` | compounds the returns, compares by calendar year, builds the two charts | `docs/finding1-growth.{html,png}`, `docs/finding2-by-year.{html,png}` |

`monthly_returns.csv` holds 240 rows. **One row is one series in one month**, and
`return_pct` is that month's return in percent for both series — the S&P figure
from the change in the index, the savings figure from the annual yield divided by
twelve.

Rerunning NB03 overwrites the four chart files under `docs/`, which is how the
published page is kept in step with the analysis. The site itself is served by
GitHub Pages from `main` → `/docs`.

## Note on structure

NB01 and NB02 are Python scripts rather than Jupyter notebooks, so this project
uses a `scripts/` folder instead of the `notebooks/` folder given in the brief.
File names keep the `NB` prefix, which numbers the pipeline stage.
