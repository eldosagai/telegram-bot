import telebot
from telebot import types
from random import choice
import os

users = {}

commands = {
    'start'                : 'fjweoiwe',
    'help'                 : 'hdiwehfihwe',
    'find_out_your_gender' : 'fewihuifweifew'
}

stages = {"sex": "favourite", "favourite":None}

markup_sex = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("male","female")
markup_gender = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add("find out")
markup_favourite = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add("CS:GO","Dota2").add("League of Legends","Clash Royal")
clipboard = [markup_sex, markup_favourite]
token = "5143373838:AAExSHaP4txBV2RMZ2DJf5lONnAampS9goM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['find_out_your_gender'])
def eldos_is_the_best(m):
    i = m.chat.id
    user = users[i]
    sex = user["sex"]
    favourite = user["favourite"]
    if sex == "male":
        if favourite == "CS:GO":
            bot.send_message(i, 'poshel nahui pidaras')
        elif favourite == "Dota2":
            bot.send_message(i, "poshel nahui pidaras")
        elif favourite == "League of Legends":
            bot.send_message(i, "бишкекский гуль")
        elif favourite == "Clash Royal":
            bot.send_message(i, "pidrila228")   
    elif sex == "female":
        if favourite == "CS:GO":
            bot.send_message(i, "zochem")
        elif favourite == "Dota2":
            bot.send_message(i, "smysl?")
        elif favourite == "League of Legends":
            bot.send_message(i, "kak kakat'?")
        elif favourite == "Clash Royal":
            bot.send_message(i, "lol kek")

@bot.message_handler(commands=['start'])
def start_command(m):
    global users 
    users.update({m.chat.id:{"sex": None,"favourite": None,"find out": None, "stage":"sex","markup": 0}})
    bot.send_message(m.chat.id, "What's your sex?", reply_markup=clipboard[users[m.chat.id]["markup"]])


@bot.message_handler(content_types=['text'])
def setting(m):
    global users
    t = m.text
    i = m.chat.id
    valid_answers = {"sex":["male","female"],"favourite":["CS:GO","Dota2","League of Legends","Clash Royal"]}
    valid_now = valid_answers[users[i]["stage"]]
    if t in valid_now:
        users[i][users[i]["stage"]] = t
        users[i]["markup"] = (users[i]["markup"]+1) % len(clipboard)
        users[i]["stage"] = stages[users[i]["stage"]]
        if users[i]["stage"]:
            bot.send_message(i, f"enter your {users[i]['stage']} game", reply_markup=clipboard[users[i]["markup"]])
        else:
            bot.send_message(i, "/find_out_your_gender")
            users[i]["stage"] = "sex"
    else:
            bot.send_message(i, "vvedi suka normal'no", reply_markup=clipboard)

@bot.message_handler(commands=['help'])
def command_help(m): 
    help_text = "The following commands are available: \n"
    for key in commands:
        help_text    += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(m.chat.id, help_text)
        

bot.polling(none_stop=True, interval=0)