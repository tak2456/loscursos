#%%
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

symbol = 'AMZN'
start_date = '2023-01-01'
end_date = '2023-12-31'

stock = yf.Ticker(symbol)
data = stock.history(start=start_date, end=end_date)

data['20_Day_MA'] = data['Close'].rolling(window=20).mean()

data['Daily_Return'] = data['Close'].pct_change() * 100

print("Data with Moving Average and Daily Returns:")
print(data[['Close', '20_Day_MA', 'Daily_Return']].head(25))

plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['20_Day_MA'], label='20-Day Moving Average', color='yellow')
plt.title(f'{symbol} Closing Price and 20-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# %%
