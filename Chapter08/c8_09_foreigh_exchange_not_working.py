from pandas_datareader.oanda import get_oanda_currency_historical_rates
start, end = "2016-01-01", "2016-06-01"
quote_currency = "USD"
base_currency = ["EUR", "GBP", "JPY"]
df_rates = get_oanda_currency_historical_rates(start, end,quote_currency=quote_currency,base_currency=base_currency)
print(df_rates)


