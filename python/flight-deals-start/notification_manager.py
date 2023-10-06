import requests


def telegram_sendtext(bot_message):
    bot_token = '6380210169:AAEHwvLZAIzSNv5R0yMjmPUoykZzyqyOTzU'
    bot_chatID = '6244133571'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self,destination, date, price):
        self.message = f"Flights to {destination} on {date} only costs {price}"
        self.send_message()

    def send_message(self):
        telegram_sendtext(self.message)