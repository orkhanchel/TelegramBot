import telebot
from telebot import types

bot = telebot.TeleBot('6696768538:AAEkR68OIIcvJHM7_mG-OCQ-VzTHpnVAONU')



name = ''
surname = ''
age = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Чтобы зарегистрироваться, напиши /reg")

@bot.message_handler(commands=['reg'])
def start_registration(message):
    bot.send_message(message.chat.id, "Как тебя зовут?")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.chat.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    try:
        age = int(message.text)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
        bot.send_message(message.chat.id, text=question, reply_markup=keyboard)
    except Exception as e:
        bot.reply_to(message, 'Пожалуйста, введите возраст цифрами')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        # здесь можно сохранить данные
        bot.send_message(call.message.chat.id, 'Запомню :)')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Давай попробуем еще раз. Напиши /reg')

bot.polling(none_stop=True)
