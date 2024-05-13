import telebot 
from telebot import types

bot = telebot.TeleBot('6870851634:AAGjf3ZBmYB4ZP9DAD9MqE4qSIdORrQlhdw')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('имя'))
    markup.add(types.KeyboardButton('возраст'))
    markup.add(types.KeyboardButton('пол'))
    bot.send_message(message.chat.id, 'hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'имя':
        bot.send_message(message.chat.id, 'Oomat')
    elif message.text == 'возраст':
        bot.send_message(message.chat.id, '16')
    elif message.text == 'пол':
        bot.send_message(message.chat.id, 'мужской')
    



@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('перейти на сайт', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('удалть',callback_data='delete'))
    markup.add(types.InlineKeyboardButton('изменить', callback_data='edit'))
    bot.reply_to(message, 'what a gorgeous picture', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('editted text', callback.message.chat.id,  callback.message.message_id)























bot.polling(none_stop=True)