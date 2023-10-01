import requests

API_KEY = "69f04e4613056b159c2761a9d9e664d2"
PARAMETERS = {
    "lat":22.3193,
    "lon":114.1694,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"
}

connection = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=PARAMETERS)
data = connection.json()
data = data["hourly"][:12]

def telegram_bot_sendtext(bot_message):
    bot_token = '6380210169:AAEHwvLZAIzSNv5R0yMjmPUoykZzyqyOTzU'
    bot_chatID = '6244133571'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


will_rain = False
for i in range(len(data)):
    weather_code = data[i]["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True
        break

if will_rain:
    telegram_bot_sendtext("It's gonna rain.")

