# return возвращает результат из функции
def formatted_name(first_name, last_name):
    full_name = first_name+" "+last_name
    return full_name


name = input("Введите ваше имя :").title()
last = input("Введите вашу фамилию :").title()
out = formatted_name(name, last)
print("Здравстуйте"+" "+out)
