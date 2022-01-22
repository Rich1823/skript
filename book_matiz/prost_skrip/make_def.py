def make_shirt(make='L', shirt='I love Python3'):
    print("Футболка которую вы заказали будет имень \t" +
          make+"\tразмер"+"\nТак же будет иметь надпись:\t"+shirt)


make1 = input("Введите размер футболки :")
shirt1 = input("Введите надпись на фашей футболки :")
if make1 == "" and shirt1 == "":
    make_shirt()
else:
    make_shirt(make1, shirt1)
