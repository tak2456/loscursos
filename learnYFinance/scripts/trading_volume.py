#%%
import yfinance as yf
import matplotlib.pyplot as plt

symbol = 'AMZN'
start_date = '2022-01-01'
end_date = '2024-12-31'

stock = yf.Ticker(symbol)
data = stock.history(start=start_date, end=end_date)

fig, ax1 = plt.subplots(figsize=(14, 7))

ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price', color='tab:blue')
ax1.plot(data.index, data['Close'], color='tab:blue', label='Close Price')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Volume', color='tab:orange')
ax2.bar(data.index, data['Volume'], color='tab:orange', alpha=0.3, label='Volume')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title(f'{symbol} Stock Price and Volume')
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1,0.9))
plt.grid(True)
plt.show()

# %%
