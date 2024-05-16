import telebot
from telebot import types
import webbrowser
import sqlite3

bot = telebot.TeleBot('6870851634:AAGjf3ZBmYB4ZP9DAD9MqE4qSIdORrQlhdw')
name = None

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('name'))
    markup.add(types.InlineKeyboardButton('age'))
    markup.add(types.InlineKeyboardButton('sex'))
    bot.send_message(message.chat.id, '<b>hello, my dear</b> <em>friend</em>', parse_mode="html", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)



@bot.message_handler(commands=['login'])
def login(message):
    conn = sqlite3.connect('oomat.sql')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), password varchar(50))')
    conn.commit()
    cursor.close()
    conn.close()


    bot.send_message(message.chat.id, 'Регистрация, введите имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'введите пароль')
    bot.register_next_step_handler(message, password)
    
def password(message):
    password = message.text.strip()

    conn = sqlite3.connect('oomat.sql')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, password) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cursor.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('список пользователей', callback_data="users"))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('oomat.sql')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    info = ''
    for i in users:
        info += f'Имя: {i[1]}, пароль: {i[2]}\n'

    cursor.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)



def on_click(message):
    if message.text == 'name':
        bot.send_message(message.chat.id, 'Oomat')
    elif message.text == 'age':
            bot.send_message(message.chat.id, '16')
    elif message.text == 'sex':
          bot.send_message(message.chat.id, 'мужской')


@bot.message_handler(commands=['website', 'site'])
def site(message):
    bot.send_message(message.chat.id, 'https://www.youtube.com/')


@bot.message_handler(commands=['browser'])
def browser(message):
    webbrowser.open('https://www.youtube.com/')
 

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
    f'hello, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id,
        f'hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')


@bot.message_handler(content_types='photo')
def photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('перейти по ссылке', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('удалить', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('мзменить', callback_data='edit'))
    bot.reply_to(message, 'красавчик', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('editted text', callback.message.chat.id, callback.message.message_id)



bot.polling(non_stop=True)
