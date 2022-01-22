# Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt. Сохраните минимум
# три клички кошек в первом файле и три клички собак во втором. Напишите программу,
# которая пытается прочитать эти файлы и выводит их содержимое на экран. Заключите
# свой код в блок try-except для перехвата исключения FileNotFoundError и вывода понятного
# сообщения об отсутствии файла. Переместите один из файлов в другое место файловой
# системы; убедитесь в том, что код блока except выполняется, как и положено
file_cat = '/home/richard/workspace/Python_data/files_for_work_introductory_data/cat.txt'
file_dog = '/home/richard/workspace/Python_data/files_for_work_introductory_data/dog.txt'
try:
    with open (file_cat,file_dog ) as (file_object , file2): 
        print(file_object)
except ValueError:
    print("отсутствует файл в данной директории:")
# Спросить почему не получается