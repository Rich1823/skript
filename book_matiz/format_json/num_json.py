# 10-11. Любимое число: напишите программу, которая запрашивает у пользователя его лю-
# бимое число. Воспользуйтесь функцией json.dump() для сохранения этого числа в файле.

import json
def numb():

    usr_num = int(input("Ваше любимое число :"))
    file_name = "usr_num.json"
    with open(file_name, "w") as obj:
        json.dump(usr_num,obj)
        print("yes")
numb()