import telebot
from telebot import apihelper
from telebot.types import Message
import pyowm


#apihelper.proxy = {'https': 'socks5://54.37.18.209:58072'}
bot = telebot.TeleBot("1037420963:AAH2MooU13r-LIZ5h5RWqyOPm9U5eNLE5qc")


owm = pyowm.OWM('31c500a5d252323b3c085d510cacf4e4')
#city = 'Sankt-Peterburg'
#observation = owm.weather_at_place(city)
#w = observation.get_weather()





@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        #user_markup.row('/start', '\u26c5\ufe0f', '\ud83d\udcb2', '\ud83c\udfb2')
        user_markup.row('/start', '\ud83d\udcb2', '\u26c5\ufe0f', '\ud83c\udfb2')
        bot.send_message(message.from_user.id, "Давай начнём.\nНапиши мне \'привет\'", reply_markup=user_markup)


        
'''
@bot.message_handler(commands=['\u26c5\ufe0f']) #weather
def send_welcome(message):
        city = 'Sankt-Peterburg'
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        bot.send_message(message.from_user.id, "В Санкт-Петербурге сейчас " + str(w.get_temperature('celsius')['temp']))


@bot.message_handler(commands=['\ud83d\udcb2']) #exchange rates
def send_welcome(message):
        bot.send_message(message.from_user.id, "Курс валют на сегодня:\nДоллар = 62.05р.\nЕвро = 69.24р.")
'''  
                
        

@bot.message_handler(content_types=['text'])
def handle_text(message):
        if message.text == 'привет' or message.text == 'Привет':
                bot.send_message(message.chat.id, 'И тебе привет, ' + message.from_user.first_name + '!' + '\nЯ умею показывать температуру за окном, курс валют и отвечать непониманием на твои сообщения)\nВыбери команду из меню или напиши мне что-нибудь.')
        elif message.text == 'пока' or message.text == 'Пока':
                bot.send_message(message.chat.id, 'Успехов в новом году!\nЗаходи ещё, позже у меня будет больше возможностей с:')       
        elif message.text == '\u26c5\ufe0f':
                city = 'Sankt-Peterburg'
                observation = owm.weather_at_place(city)
                w = observation.get_weather()
                bot.send_message(message.from_user.id, "В Санкт-Петербурге сейчас " + str(w.get_temperature('celsius')['temp']))
        else:
                echo_all(message)

                                               
@bot.message_handler(func=lambda m: True)
def echo_all(message):
        bot.reply_to(message, 'чё ' + message.text + '?')



bot.polling(none_stop=True, interval=0)




