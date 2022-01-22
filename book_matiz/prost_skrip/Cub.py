#  9-14. Запуск из файла cub_zapusk.py
# Cub.py:модуль random содержит функции для генерирования случайных чисел раз-
# ными способами. Функция randint() возвращает целое число в заданном диапазоне. Следу-
# ющий код возвращает число от 1 до 6:
# from random import randint
# x = randint(1, 6)
# Создайте класс Die с одним атрибутом с именем sides, который содержит значение по умол-
# чанию 6. Напишите метод roll_die() для вывода случайного числа от 1 до количества сторон
# кубика. Создайте экземпляр, моделирующий 6-гранный кубик, и имитируйте 10 бросков.
# Создайте модели 10- и 20-гранного кубика. Имитируйте 10 бросков каждого кубика
from random import randint


class Die():
    def __init__(self):
        self.sides = 6
        self.sides1 = 10
        self.sides2 = 20
        self.numb = 0
        self.out = ""

    def roll_die(self):
        while self.numb != 10:
            bros = str(randint(0, self.sides))
            self.numb += 1
            self.out += " "+bros
        print("Ваш результат : "+self.out)

    def roll_die1(self):
        while self.numb != 10:
            bros = str(randint(0, self.sides1))
            self.numb += 1
            self.out += " "+bros
        print("Ваш результат : "+self.out)

    def roll_die2(self):
        while self.numb != 10:
            bros = str(randint(0, self.sides2))
            self.numb += 1
            self.out += " "+bros
        print("Ваш результат : "+self.out)


    