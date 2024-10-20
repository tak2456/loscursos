#%%
import pandas as pd
from pathlib import Path

path = Path(__file__)
print(path)
path = path.parent.parent / "data" / "historical_techs_data.csv"
print(path)


data = pd.read_csv(path)
#%%
data.head()

# %%
data.tail()
# %%

# %%
data.info()
# %%
# Converts the "Date" column to a datetime object, 
# while making sure that the resulting datetime is timezone-aware (in UTC)
data["Date"] = pd.to_datetime(data["Date"], utc=True)

# %%
data.info()
# %%
data.describe()

# %%
data['Symbol'].unique()

# %%
vc = data['Symbol'].value_counts()
vc
# %%
vc.info()

# %%
data['Symbol'].value_counts().sort_index()
# %%
date_ranges = data.groupby('Symbol')['Date'].agg(['min', 'max'])
date_ranges

# %%
date_ranges.info()
# %%

date_ranges = (
    data.groupby('Symbol')['Date']
        .agg(['min', 'max'])
        .assign(
            duration=lambda x: (x['max'] - x['min']).dt.days,  # Calculate duration in days
            duration_days=lambda x: x['duration'] / 365.25,  # Convert duration to years
            min=lambda x: x['min'].dt.date,  # Convert min to date only
            max=lambda x: x['max'].dt.date   # Convert max to date only
        )
        .sort_values('duration', ascending=False)
)
date_ranges

# %%
split_counts = (
    data[data['Stock Splits'] != 0]
    .groupby('Symbol')['Stock Splits']
    .value_counts()
)
split_counts    
# %%
unstacked_counts = split_counts.unstack()
unstacked_counts.fillna(0, inplace=True)
unstacked_counts
# %%
unstacked_counts.info()

# %%
def plot_stock_price(symbol, start_date, end_date):
    symbol_data=data[(data['Symbol'] == symbol) & 
                     (data['Date'] >= start_date) & 
                     (data['Date'] <= end_date)]
    symbol_data.plot(x='Date', y='Close', title=f'{symbol} Stock Price', ylabel='Price (USD)', xlabel='Date')
    
def plot_stock_price_with_splits(symbol, start_date, end_date):
    symbol_data=data[(data['Symbol'] == symbol) & 
                     (data['Date'] >= start_date) & 
                     (data['Date'] <= end_date)]
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(symbol_data['Date'], symbol_data['Close'], label='Stock Price', color='pink')
    splits = symbol_data[symbol_data['Stock Splits'] != 0]
    # for split_date in splits['Date']:
    #    ax.axvline(x=split_date, color='blue', linestyle='--', label='Stock Split')

    # ax.scatter(splits['Date'], splits['Close'], color='green', s=100, edgecolor='black', label='Stock Split', zorder=5)

    legend_entries = []
    for idx, row in splits.iterrows():
      ax.scatter(row['Date'], row['Close'], color='red', s=100, edgecolor='black', label='Stock Split', zorder=5)
      # Annotate the split ratio
      ax.text(row['Date'], row['Close'], f"{row['Stock Splits']}:1", 
            fontsize=12, ha='center', va='center', color='red', weight='bold')
      # Add entry to legend
      legend_entries.append(f"{row['Date'].date()} - {row['Stock Splits']}:1")

    # Add labels and title
    ax.set_title(f'{symbol} Stock Price with Splits')
    ax.set_ylabel('Price (USD)')
    ax.set_xlabel('Date')

    # Optionally, add a legend for the splits
    handles, labels = ax.get_legend_handles_labels()
    # Create a unique legend with dates and add the stock price
    unique_labels = list(set(legend_entries) | {'Stock Price'})  # Combine the stock price with splits
    
    ax.legend(unique_labels, loc='upper left')


    # Show the plot
    plt.tight_layout()
    plt.show()

# %%
(data[
    (data['Symbol']=='AAPL') & 
    (data['Stock Splits']!=0)
])

# %%
import matplotlib.pyplot as plt
split_counts.unstack().plot(kind='bar', stacked=True)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.title('Stock Splits by Symbol')
plt.xlabel('Stock Symbol')
plt.ylabel('Number of Stock Splits')
plt.xticks(rotation=60)
plt.show()


# %%
start_date='2012-01-01'
end_date='2024-12-31'
#plot_stock_price('AMZN', start_date, end_date)
plot_stock_price_with_splits('AAPL', start_date, end_date)
#plot_stock_price('AAPL', start_date, end_date)
#plot_stock_price('META', start_date, end_date)


# %%
