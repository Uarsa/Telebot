import telebot
from telebot import apihelper
from telebot.types import Message
import pyowm


#apihelper.proxy = {'https': 'socks5://54.37.18.209:58072'}
bot = telebot.TeleBot("1037420963:AAH2MooU13r-LIZ5h5RWqyOPm9U5eNLE5qc")


owm = pyowm.OWM('31c500a5d252323b3c085d510cacf4e4')
city = 'Sankt-Peterburg'
observation = owm.weather_at_place(city)
w = observation.get_weather()


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('/start', '/погода', '/курс_валют')
        bot.send_message(message.from_user.id, "Давай начнём с:\nНапиши мне \'привет\'", reply_markup=user_markup)


        

@bot.message_handler(commands=['погода'])
def send_welcome(message):
        bot.send_message(message.from_user.id, "В Санкт-Петербурге сейчас " + str(w.get_temperature('celsius')['temp']))

@bot.message_handler(commands=['курс_валют'])
def send_welcome(message):
        bot.send_message(message.from_user.id, "Курс валют на сегодня:\nДоллар = 62.17р.\nЕвро = 69.73р.")


@bot.message_handler(content_types=['text'])
def handle_text(message):
        if message.text == 'привет' OR message.text == 'Привет':
                bot.send_message(message.chat.id, 'И тебе привет!\nЯ умею показывать температуру за окном,' +
                'курс валют и поддерживать с тобой разговор.\nВыбери команду из меню или напиши мне что-нибудь с:')
        elif message.text == 'пока':
                bot.send_message(message.chat.id, 'Поки =*\nЗаходи ещё, позже у меня будет больше возможностей :з')
        else:
                echo_all(message)

                                               
@bot.message_handler(func=lambda m: True)
def echo_all(message):
        bot.reply_to(message, 'чё ' + message.text + '?')



bot.polling(none_stop=True, interval=0)




