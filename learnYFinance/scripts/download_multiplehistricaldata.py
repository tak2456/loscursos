# %%
import pandas as pd
import yfinance as yf

mytickers = ["AMZN", "GOOG", "MSFT", "TSLA", "AAPL", "META", "NVDA"]
tickers = yf.Tickers(mytickers)

# access each ticker using (example)
tickers.tickers['MSFT'].info
tickers.tickers['AMZN'].history(period="1m")
tickers.tickers['GOOG'].actions

#%%
all_data = pd.DataFrame()
for ticker in mytickers:
    data = tickers.tickers[ticker].history(period="max")
    data["Symbol"] = ticker
    all_data = pd.concat([all_data, data])

# %%
all_data.head()
# %%
all_data.info()
# %%
all_data.to_csv("../data/historical_techs_data.csv")

# %%
