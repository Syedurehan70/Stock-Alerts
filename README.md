# Stock-Alerts

So this program is about getting alert on your email when the stock in which you're interested in goes up or down to a considerable margin.

We're using two API's here, "alphavantage" and "newsapi.org"
The fisrt one return a data which contains the performance of the stock we've mentioned in parameters, other one extracts the news related to that stock and shows
why stock is behaving in a way it is behaving right now.

Obviously, you can change stock name and company as per your preferrence,
Than we have some constants, and api_keys.

We want to compare the performance of two days, yesterday and day before yesterday, so after setting program to give us required dates relative to current date, we've converted
data from API's to JSON formmat and extracted the prices on mentioned dates from it.

Than we subtract those price and pull out percentage increease or decrease, if percent is above 5% mark, we've gathered the top 3 articles related to stock name
and sent a notification email.
