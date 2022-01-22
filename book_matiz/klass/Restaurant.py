# Проба создание класса , бесцельно эксперементирование.
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("имя вашего ресторана :"+self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self, x):
        if x == "y":
            print("Ресторан "+" "+self.restaurant_name +
                  " " + self.cuisine_type+"\tГотов к работе!")
        else:
            print("К сожелению придётся подождать открытие ")

x= input("y:")
info=input("y:")
res_n,res_c=("Макдак","Закусочная")
m=Restaurant(res_n,res_c)
m.open_restaurant(x)
if info=="y":
    (m.describe_restaurant())