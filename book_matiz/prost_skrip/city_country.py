#def and while функция получает название города и страну где он находиться
# возвращает три пары,через запятую
def city_country(name_city, name_strana):
    city_country1 = name_city+" "+name_strana+","
    return city_country1.title()


print("\nВведите по очередно название трех Городов и название трех странн в которых они находятся :")
x = 0
y = ""
while x != 3:
    c_name = input("Город:")
    st_name = input("Страна:")
    city = city_country(c_name, st_name)
    y += city
    x += 1
print(y)
