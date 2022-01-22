# Опрос: напишите цикл while, в котором программа спрашивает у пользователя, по-
# чему ему нравится программировать. Каждый раз, когда пользователь вводит очередную
# причину, сохраните текст его ответа в файл
# так же в начале файла имя того кто отвечал сделаю это через класс

file_out = "/home/richard/workspace/Python_data/data_output/out_gost.txt"


class Opros():
    def __init__(self, name):
        self.out = ""
        self.name = name

    def hi(self):
        print("Здравствуйте\t"+self.name+"!")
        caused = input("Какой язык программирования вам нравиться? :")
        while True:
            print("Что именно вас прилекло в \t" + caused)
            caused2 = input("Расскажите подробней чем он вам нравиться:")
            break
        with open(file_out, "a") as f_o :
            f_o.write(name +"\n"+caused+"\n"+caused2)
name=input("Ваше имя :")
m=Opros(name)
m.hi()