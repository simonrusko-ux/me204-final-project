# S&P 500 vs. Savings Account: A 10-Year Comparison

*Šimon Rusko — `simonrusko-ux`*

## The question

**If I had put money into the S&P 500 ten years ago instead of leaving it in a
savings account, what would the difference be today?**


## Where the numbers come from

Both series were downloaded from FRED, the public data service run by the Federal Reserve Bank of St. Louis. The market side is the S&P 500, an index that tracks the share prices of five hundred of the largest companies listed in the United States. The savings side is the national average savings-account rate in the US, compiled by Bankrate from a weekly survey of the largest banks.

The comparison runs from August 2016 to July 2026, one hundred and twenty months — as far back as FRED's daily S&P 500 record goes. Everything here was downloaded on 22 July 2026 and is fixed to that date.

## Finding 1 — $1,000 became $3,463, or $1,023

<iframe src="finding1-growth.html" width="100%" height="525" frameborder="0"
        scrolling="no" style="border:0;"
        title="Value of $1,000 invested, 2016 to 2026"></iframe>

<!-- If the interactive chart above does not load, replace the iframe with:
     ![Value of $1,000 invested](finding1-growth.png) -->


## Finding 2 — the market won 7 years out of 9, not 9 out of 9

<iframe src="finding2-by-year.html" width="100%" height="565" frameborder="0"
        scrolling="no" style="border:0;"
        title="Return by calendar year, 2017 to 2025"></iframe>

<!-- If the interactive chart above does not load, replace the iframe with:
     ![Return by calendar year](finding2-by-year.png) -->



## What it means



## What this comparison cannot tell you

---

*Data: [FRED](https://fred.stlouisfed.org/), series `SP500` and `BRMSA0104`,
retrieved 22 July 2026. Analysis:
[`NB03-simonrusko-ux-Data-Analysis.ipynb`](https://github.com/simonrusko-ux/me204-final-project/blob/main/scripts/NB03-simonrusko-ux-Data-Analysis.ipynb).*
