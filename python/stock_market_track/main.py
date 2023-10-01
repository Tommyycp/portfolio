from datetime import date, timedelta
import requests


def telegram_sendtext(bot_message):
    bot_token = '6380210169:AAEHwvLZAIzSNv5R0yMjmPUoykZzyqyOTzU'
    bot_chatID = '6244133571'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


dt = date.today()
if dt.weekday() == 0:
    yesterday_date = dt - timedelta(3)
    day_before_yesterday_date = dt - timedelta(4)
else:
    yesterday_date = dt - timedelta(1)
    day_before_yesterday_date = dt - timedelta(2)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

PARAMS_STOCK = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": "TNRO4SAE3DQFLWFR"
}

PARAMS_NEWS = {
    "q": "Tesla",
    "apiKey": "4b4cfa2ccd6144bab448506d8ecdb192",
    "from": day_before_yesterday_date,
    "to": dt,
    "langauge": "en",
    "sortBy": "popularity",
}

stock_data_connection = requests.get(url="https://www.alphavantage.co/query?", params=PARAMS_STOCK)
stock_data = stock_data_connection.json()
close_price_yesetrday = stock_data["Time Series (60min)"][f"{yesterday_date} 19:00:00"]["4. close"]
close_pirce_day_before = stock_data["Time Series (60min)"][f"{day_before_yesterday_date} 19:00:00"]["4. close"]
difference = (float(close_price_yesetrday) - float(close_pirce_day_before)) / float(close_pirce_day_before) * 100
print(difference)

stock_news_connection = requests.get(url="https://newsapi.org/v2/everything?", params=PARAMS_NEWS)
stock_news_data = stock_news_connection.json()
top_three_headlines = ""

for i in stock_news_data["articles"][1:4]:
    top_three_headlines = top_three_headlines + i["title"] + f"\n\n" + i["description"] + f"\n\n"

if abs(difference) >= 3:
    telegram_message = f"{STOCK} changes {difference} between {yesterday_date} and {day_before_yesterday_date} \n\n" \
                       f"Please check the headlines as below \n\n" \
                       f"{top_three_headlines}"
    telegram_sendtext(telegram_message)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
