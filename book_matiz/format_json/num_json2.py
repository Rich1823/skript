# Напишите другую программу, которая читает это значение и выводит сообщение: «Я знаю
# ваше любимое число! Это _____».
import json
filename = 'usr_num.json'


def num_love():
    with open(filename) as obj:
        usr = json.load(obj)
        print("Я знаю аше любимое число  " +str(usr))


num_love()
