import webbrowser
import telebot

token = '2028872894:AAG6128fprnOu0sWKgnshXxfTbmAoF6_Bho'

def get_data():
    req = webbrowser.open_new_tab('https://myfin.by/currency/moskva')
    print(req)


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["HI"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello Boss!")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "many":
            try:
                req = webbrowser.open_new_tab('https://myfin.by/currency/moskva')


            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "AAAAAAAAAAA"
                )
        else:
            bot.send_message(message.chat.id, "Whaaat?Boss!")

    bot.polling()


if __name__ == '__main__':
     telegram_bot(token)