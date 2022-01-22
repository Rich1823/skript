# Проверка пользователя: последняя версия remember_me.py предполагает, что поль-
# зователь либо уже ввел свое имя, либо программа выполняется впервые. Ее нужно из-
# менить на тот случай, если текущий пользователь не является тем человеком, который
# последним использовал программу
# Ps Провестри рефакторинг
import json


class Usr():
    def __init__(self, name):
        self.file_name = name

    def usr_seve(self, name):
        """ Сохранение никнейма """
        with open(self.file_name, 'w') as file:
            json.dump(name, file)

    def usr_name(self):
        """ Проверка: существует файл с именем пользователя или нет   """
        try:
            with open(self.file_name) as file:
                self.file2 = json.load(file)
                on.usr_name1()
        except FileNotFoundError:
            usr_name = input("Введите ваше имя :")
            self.usr_seve(usr_name)

    def usr_name1(self):
        """ Делается запрос Юзеру его акаунт? """
        print("Имя пользователя  " + self.file2+" ?")
        usr_out = input("y или n :")
        if usr_out == "n":
            usr_new = input("Введите новое имя пользователя :")
            self.usr_seve(usr_new)
            print("Вы вошли как пользователь "+usr_new.title())
        else:
            print("Вы вошли как пользователь "+self.file2+'!')


on = Usr("usr_name.json")
(on.usr_name())
