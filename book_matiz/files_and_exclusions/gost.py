# 10.3
# Гость: напишите программу, которая запрашивает у пользователя его имя. Введенный
# ответ сохраняется в файле с именем guest.txt.
guest="/home/richard/workspace/Python_data/data_output/guest.txt"
name=input("Введите ваше имя :")
with open(guest,'w') as file:
    file.write(name)