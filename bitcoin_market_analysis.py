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
