## @x_chatID_bot

import telebot
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def welcome(message):
  markup = types.InlineKeyboardMarkup()
  menubutton = types.InlineKeyboardButton('🔘 Menu', callback_data='menu')
  markup.row(menubutton)
  bot.send_message(message.chat.id,
                   "👋 Welcome in our bot ChatID!",
                   reply_markup=markup)


@bot.message_handler(commands=['menu'])
def show_menu(message):
  bot.send_message(message.chat.id, "🔘 Main menu", reply_markup=menu_markup())


@bot.message_handler(commands=['id'])
def get_id(message):
  bot.send_message(message.chat.id,
                   f"🆔 Your ID: {message.from_user.id}",
                   reply_markup=back_to_menu_markup())


@bot.message_handler(commands=['info'])
def show_info(message):
  bot.send_message(
      message.chat.id,
      "ℹ Information about us:\nThe bot made by @riotoffprojects. Well, we hope that bot will make your life more simple.\nThis bot made only for educational purposes and have open-source.\nIts made for get your Telegram ID. And it's safe, absolutely.",
      reply_markup=back_to_menu_markup())


@bot.message_handler(commands=['help'])
def show_help(message):
  bot.send_message(
      message.chat.id,
      "🆘 I can show you your ID.\nPretty good functional and design will make this bot for you more comfort and soft.\n\nCommands list:\n/start\n/menu\n/help\n/id\n/info",
      reply_markup=back_to_menu_markup())


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
  chat_id = callback.message.chat.id
  message_id = callback.message.message_id
  if callback.data == 'menu':
    bot.edit_message_text(chat_id=chat_id,
                          message_id=message_id,
                          text='🔘 Main menu',
                          reply_markup=menu_markup())
  elif callback.data == 'id':
    bot.edit_message_text(chat_id=chat_id,
                          message_id=message_id,
                          text='🆔 Your ID: ' + str(chat_id),
                          reply_markup=back_to_menu_markup())
  elif callback.data == 'info':
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=
        "ℹ Information about us:\nThe bot made by @riotoffprojects. Well, we hope that bot will make your life more simple.\nThis bot made only for educational purposes and have open-source.\nIts made for get your Telegram ID. And it's safe, absolutely.",
        reply_markup=back_to_menu_markup())
  elif callback.data == 'help':
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=
        '🆘 I can show you your ID.\nPretty good functional and design will make this bot for you more comfort and soft.\n\nCommands list:\n/start\n/menu\n/help\n/id\n/info',
        reply_markup=back_to_menu_markup())


def menu_markup():
  markup = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton('🆔 Get ID', callback_data='id')
  button2 = types.InlineKeyboardButton('👥 Get user ID',
                                       callback_data='user_id')
  button3 = types.InlineKeyboardButton('👥 Get group ID',
                                       callback_data='group_id')
  button4 = types.InlineKeyboardButton('ℹ Info', callback_data='info')
  button5 = types.InlineKeyboardButton('🆘 Help', callback_data='help')
  markup.row(button1)
  markup.row(button2, button3)
  markup.row(button4)
  markup.row(button5)

  return markup


def back_to_menu_markup():
  markup = types.InlineKeyboardMarkup()
  button = types.InlineKeyboardButton('🔙 Back', callback_data='menu')
  markup.row(button)

  return markup


bot.polling()
