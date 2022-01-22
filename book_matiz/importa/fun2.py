# fun2.py
# здесь будет написана сама анкета с вопросами
import fun1

while True:
    name = input("Здравствуйте как я могу к вам обращаться? :").title()
    let = input("Сколько вам лет? :")
    let1 = fun1.let(let)
    if let1 == False:
        print(name+" "+"к сожилению ваш возрост не подходит для анкеты.")
        break
    city = input("В каком городе вы проживаете? :")
    o_sebe = input("Расскажите о себе, кем работаете? , чем увлекаетесь ?,если ли у вас домашние животные?:")
    break
print(fun1.ank(name, let, city, o_sebe))

