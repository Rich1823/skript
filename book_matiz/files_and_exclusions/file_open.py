# Этот скрипт открывает файл и выводит содержимое на экрон
x= '/home/richard/workspace/Python_data/files_for_work_introductory_data/pi_digits.txt'

with open (x)  as file_object:
    contents = file_object.read()
    print(contents.rstrip())
