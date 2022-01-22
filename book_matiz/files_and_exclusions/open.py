# Для себя попытаю разобраться с открытиями и закрытиями файлов txt файл с инфой для ввода инф. назвал также
files=['open.txt','open2.txt']
def on (file):
    try:
        with open (file) as fl:
            print(fl.read())
    except FileNotFoundError:
        print("Нет файла в дириктории которую вы указыаете.")
for i in files:
    on(i)
   """ Получилось ,дело было в with Ps узнать подробне способы открытия нескольких файлов """