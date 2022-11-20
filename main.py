import eel
import telebot

TOKEN = "5926563162:AAH7UDzLrUsnfkqCAmjpjntb6UF8mI2KE0g"

bot = telebot.TeleBot(TOKEN)

@eel.expose
def send_message(char_id, message):
    bot.send_message(char_id, message)
    return "Сообщение отправлено!"


eel.init('web')
eel.start('index.html', size=(700, 700))