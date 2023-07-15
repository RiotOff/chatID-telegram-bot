### @x_chatID_bot

import telebot
from telebot import types

bot = telebot.TeleBot("")
previous_command = ""

@bot.message_handler(commands=["start"])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    menubutton = types.InlineKeyboardButton('')
    bot.send_message(message.chat.id, "👋 Welcome to ChatID bot!\nTo get help write /help command.")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "🆘 I can show you your ID.\nPretty good functional and design will make this bot for you more comfort and soft.\n\nCommands list:\n/start\n/menu\n/help\n/id\n/info")

@bot.message_handler(commands=["menu"])
def menu(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('🆔 Get my ID', callback_data='id')
    markup.row(button1)
    button2 = types.InlineKeyboardButton('ℹ Info', callback_data='info')
    button3 = types.InlineKeyboardButton('🆘 Help', callback_data='help')
    markup.row(button2, button3)

    bot.send_message(message.chat.id, '🔘 Main menu', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'id':
        id(callback.message)
    elif callback.data == 'info':
        info(callback.message)
    elif callback.data == 'help':
        help(callback.message)

@bot.message_handler(commands=["id"])
def id(message):
    id = message.from_user.id
    bot.send_message(message.chat.id, f"🆔 Your ID: {id}")

@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.chat.id, "ℹ Information about us:\nThe bot made by @riotoffprojects. Well, we hope that bot will make your life more simple.\nThis bot made only for educational purposes and have open-source.\nIts made for get your Telegram ID. And it's safe, absolutely.")



bot.infinity_polling()