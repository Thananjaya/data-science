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

#calculate the cercentage in US market using assign function
total_sum = cap.market_cap_usd.sum()
cap10 = cap.head(10).set_index('id')
cap10 = cap10.assign(market_cap_perc= lambda x : (x.market_cap_usd/total_sum)*100)
ax = cap10.plot.bar(title='Top 10 market capitalization')
ax.set_ylabel('% of total cap')
plt.xlabel('USD')
plt.show()
