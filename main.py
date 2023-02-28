import requests
import json  # импортируем необходимую библиотеку
import telebot
TOKEN = "6241454432:AAFkB-PtjYHwwGyr2KqxwNYKBsZUMWK3vJk"
bot = telebot.TeleBot("6241454432:AAFkB-PtjYHwwGyr2KqxwNYKBsZUMWK3vJk")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    print(message.text)
    bot.send_message(message.chat.id, f"Welcome, \ {message.chat.username}")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice Photo )))')



bot.polling(none_stop=True)
