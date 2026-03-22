import telebot
import sqlite3
from config import DATABASE
from config import token
from create_db import DB_Manager

manager = DB_Manager(DATABASE)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def message_start(message):
    bot.reply_to(message, "Привет, {name}!".format(name=message.from_user.first_name))
    bot.send_message(message.chat.id, 'Я скидываю расписание на будни')
    bot.send_message(message.chat.id, 'Вот команды:'
                                       '/monday - расписание на понедельник'
                                       '/tuesday - расписание на вторник'
                                       '/wednesday - распиание на среду'
                                       '/thursday - расписание на четверг'
                                       '/friday - расписание на пятницу')
    
@bot.message_handler(commands=['monday'])
def get_monday_schedule(message):
    monday_schedule = manager.get_monday_schedule()
    bot.reply_to(message, monday_schedule)

@bot.message_handler(commands=['tuesday'])
def get_tuesday_schedule(message):
    tuesday_schedule = manager.get_tuesday_schedule
    bot.reply_to(message, tuesday_schedule)

@bot.message_handler(commands=['wednesday'])
def get_wednesday_schedule(message):
    wednesday_schedule = manager.get_wednesday_schedule
    bot.reply_to(message, wednesday_schedule)
    
@bot.message_handler(commands=['thursday'])
def get_thursday_schedule(message):
    thursday_schedule = manager.get_thursday_schedule
    bot.reply_to(message, thursday_schedule)
    
@bot.message_handler(commands=['friday'])
def get_friday_schedule(message):
    friday_schedule = manager.get_friday_schedule
    bot.reply_to(message, friday_schedule)


bot.infinity_polling()