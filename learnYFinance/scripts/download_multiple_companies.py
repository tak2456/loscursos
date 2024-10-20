# %%
import pandas as pd
import yfinance as yf

tickers = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]

start_date="2020-01-01"
end_date="2024-10-20"

print(f"Downloading data from Yahoo Finance from {start_date} to {end_date} for the following tickers: {tickers}")
all_data = pd.DataFrame()

for ticker in tickers:
    #data = yf.download(ticker, start=start_date, end=end_date)
    data = yf.history(ticker, start=start_date, end=end_date)
    data["Symbol"] = ticker
    all_data = pd.concat([all_data, data])

# %%
all_data.head()

# %%
all_data.info()
# %%
all_data.dtypes
# %%
all_data.describe()
# %%
all_data.to_csv("../data/historical_data.csv")
# %%
