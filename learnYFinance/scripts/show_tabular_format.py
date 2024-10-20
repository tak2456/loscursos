#%%
import yfinance as yf
import pandas as pd
from tabulate import tabulate

symbol = "AAPL"
start_date = "2023-01-01"
end_date = "2024-10-20"

stock = yf.Ticker(symbol)
historical_data = stock.history(start=start_date, end=end_date)

#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)

print(f"Data for {symbol} from {start_date} to {end_date}")

formatted_data = pd.concat([historical_data.head(5), historical_data.tail(5)])
print(tabulate(formatted_data, headers='keys', tablefmt='psql'))

print("\nShowing only the first and last 5 rows of data:")
print(tabulate(formatted_data, headers='keys', tablefmt='grid'))

# %%
