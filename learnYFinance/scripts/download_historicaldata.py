# %%
import yfinance as yahooFinance
import pandas as pd
import re

# %%
meta = yahooFinance.Ticker("META")
meta

amzn = yahooFinance.Ticker("AMZN")
amzn
# %%
meta.info

# %%
len(meta.info.keys())
# %%
list(meta.info.keys())

# %%
[k for k in meta.info.keys() if k.startswith("sector")]

# %%
search_string = "ticker"
[func for func in dir(yahooFinance) if re.search(rf"{search_string}", func, re.IGNORECASE)]

# %%
search_string = "csv"
[func for func in dir(pd) if re.search(rf"{search_string}", func, re.IGNORECASE)]
[func for func in dir(pd.DataFrame) if re.search(rf"{search_string}", func, re.IGNORECASE)]

# %%
pd.DataFrame.to_csv?

# %%
print(f"CEO of {meta.info['shortName']} is {meta.info['companyOfficers'][0]['name']}")
print(f"CEO of {amzn.info['shortName']} is {amzn.info['companyOfficers'][0]['name']}")
# %%

for key, value in meta.info.items():
    print(key, ":", value)

# %%
print('\n'.join(f"{key}: {value}" for key, value in meta.info.items()))

# %%
# Valid options are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y and ytd.
#print(meta.history(period="max"))
hist = meta.history(period="1y")
print(hist)
# %%
meta.history_metadata

# %%
print(meta.actions)
print(meta.dividends)
print(meta.splits)
print(meta.capital_gains)
# %%
meta.calendar
# %%
import datetime as dt

startDate = dt.datetime(2019, 5, 31) 
endDate = dt.datetime(2021, 1, 30)
old_hist = meta.history(start=startDate, end=endDate)
# print(old_hist)
old_hist.info()

# %%
hist.to_csv("../data/meta_1y.csv")