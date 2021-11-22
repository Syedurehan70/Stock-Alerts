import requests
import datetime as dt
import smtplib

MY_EMAIL = "usamatest32@gmail.com"
PASSWORD = "Angela$32"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "5JD81ZK40NCDLCC3"
NEWS_API = "3675f39d45c24c7888422ab410877ccb"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

# today's date
today = dt.date.today()
# yesterday's date
yesterday = today - dt.timedelta(days=1)

data = response.json()
daily_series = data["Time Series (Daily)"]
# Getting yesterday's closing stock price.
yesterday_closing_price = float(daily_series[str(yesterday)]["4. close"])

# Getting the day before yesterday's closing stock price
day_before_yesterday = yesterday - dt.timedelta(days=1)
day_before_yesterday_price = float(daily_series[str(day_before_yesterday)]["4. close"])

# Found the positive difference between 1 and 2. e.g. 40 - 20 = -20.
diff = abs(yesterday_closing_price - day_before_yesterday_price)

if yesterday_closing_price > day_before_yesterday_price:
    up = "increases"
else:
    up = "decreases"

# Worked out the percentage difference in price.
percent_diff = round((diff)/(yesterday_closing_price)*100, 2)

# If TODO4 percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if percent_diff > 0.1:
    news_parameters = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,

    }
    response_2 = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response_2.raise_for_status()
    articles = response_2.json()['articles']

# Using Python slice operator to create a list that contains the first 3 articles.
    top_three_articles = articles[:3]

# Creating a new list of the first 3 article's headline and description using list comprehension.
    formatted_list = [f"Headline: {article['title']}. \n\nBrief: {article['description']}"
                      for article in top_three_articles]
    # builts a connection between email and email provider's server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # securing the connection we built, by transport layer security
        connection.starttls()
        # logging in
        connection.login(user=MY_EMAIL, password=PASSWORD)
        for i in formatted_list:
            # sending mail, before \n\n there's a  subject and after there is a body of code
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="syedusama70@gmail.com",
                                msg=f"Subject: {STOCK_NAME}: {up} {percent_diff}% \n\n{i}")
