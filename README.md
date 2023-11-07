# TelegramBot

from colorama import init

init()
from colorama import Fore, Back, Style

print(Fore.YELLOW)
a = int(input("Vvedite rezultat ekzamenov: " + Fore.RED + " "))
print(Fore.CYAN)
if a > 90:
    print(Fore.WHITE + "Vawa ocenka" + Fore.BLUE + " A!")
elif a > 80:
    print("Vawa ocenka B!")
elif a > 70:
    print("Vawa ocenka C!")
elif a > 60:
    print("Vawa ocenka" + Fore.WHITE + " D!")

else:
    print(Fore.RED + "Vi ne prowli ekzamen")


def david():
    for step in range(6):
        for i in range(3):
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.right(60)


x, y, z = 5, 45, 20
print('%02d:%02d:%02d' % (x, y, z))

import turtle

turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('green', 'yellow')
turtle.speed(5)

import turtle

turtle.shape('turtle')
turtle.color('red', 'yellow')


def well():
    for step in range(6):
        turtle.forward(60)
        turtle.right(60)
        turtle.end_fill()
        turtle.pensize()


well()

import telebot

bot = telebot.TeleBot("6318259440:AAFNttM_5RUeUzRtXEHkr1qMWJjIGXSn9v4")


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, 'salam')


bot.polling(none_stop=True)

