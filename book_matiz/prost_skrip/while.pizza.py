print("Введите дополненияк Пицце по одному за раз , Как перечислите все дополнения то для выхода введите слово 'всё'")
dop = (" ")
dop_1 = ("")
while dop != "всё":

    dop = input("Введите дополнение :")
    if dop == "всё":
        break
    dop_1 += dop+","
print("Ваши дополнения к пицце : "+"\n"+dop_1)
