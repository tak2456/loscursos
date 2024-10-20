#%%
import yfinance as yf
import matplotlib.pyplot as plt
ticker = "TSLA"
tesla = yf.Ticker(ticker)
hist = tesla.history(period="6mo")
monthly_volume = hist['Volume'].resample('M').sum()
plt.figure(figsize=(8, 8))
plt.pie(monthly_volume, labels=monthly_volume.index.strftime('%b %Y'), autopct='%1.1f%%', colors=plt.cm.Paired(range(len(monthly_volume))))
plt.title('Monthly Trading Volume Distribution for Tesla (TSLA)')
plt.show()

# %%
