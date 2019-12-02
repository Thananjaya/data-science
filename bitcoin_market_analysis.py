import pandas as pd
import matplotlib.pyplot as plt

# reading the json file as dataframe using read_json
bt = pd.read_json('https://api.coinmarketcap.com/v1/ticker/')
print(bt.info(), 'General information of the data frame\n')

# We dont need the coins which  dont have US market
# Soo filtering only those coins that have US market
just_usd_market = bt[['id', 'market_cap_usd']]
cap = just_usd_market[just_usd_market.market_cap_usd > 0]
print(cap.count(), 'Checking the total observations of the market cap usd.')

#calculate the percentage in US market using assign function
#visualizing it in the bar plot with the log scale in y axis, cause percentage is very small when compared to tht US market
total_sum = cap.market_cap_usd.sum()
cap10 = cap.head(10).set_index('id')
cap10 = cap10.assign(market_cap_perc= lambda x : (x.market_cap_usd/total_sum)*100)
cap10.plot.bar(title='Top 10 market capitalization', logy=True)
plt.ylabel('% of total cap')
plt.xlabel('USD')
# plt.show()

#checking the changes in the market cap for 24h time period
volatility = bt[['id', 'percent_change_24h', 'percent_change_7d']]
volatility = volatility.set_index('id')
volatility = volatility.sort_values('percent_change_24h')
print(volatility.head(), '\nChecking the market changes per 24h time period\n')
print('it looks like the changes are huge\n')


#ploting the top 10 winners and tht top 10 loosers in the US market as per 24h change
def top10_winners_loosers(volatility_series, title):
  # Making the subplot and the figure for two side by side plots, where 10 represents width and 6 represents height
  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
  ax = volatility_series[:10].plot.bar(ax=axes[0], color='blue')
  fig.suptitle(title)
  ax.set_ylabel("percentage change per 24h")


  ax = volatility_series[-10:].plot.bar(ax=axes[1], color='red')
  plt.show()

top10_winners_loosers(volatility['percent_change_24h'].sort_values().dropna(), '24 hours top losers and winners')
