import Cub
# вся задача описана в файле Cub

def vvod(num1):
    if num1 == 6:
        my.roll_die()
    elif num1 == 10:
        my.roll_die1()
    elif num1 == 20:
        my.roll_die2()


vod = int(input("Есть три кубика 6,10,20 Каким вы будете играть ?:"))
my = Cub.Die()
vvod(vod)
