# Гостевая книга: напишите цикл while, который в цикле запрашивает у пользователей
# имена. При вводе каждого имени выведите на экран приветствие и добавьте строку с со-
# общением в файл с именем guest_book.txt. Проследите за тем, чтобы каждое сообщение
# размещалось в отдельной строке файла
file = "/home/richard/workspace/Python_data/data_output/guest_book.txt"
while True:
    name = input("Имя :").title()
    if name == 'st':
        break
    print("hello\t"+name)
    with open(file,"a")as f:
        f.write(name+"\n")