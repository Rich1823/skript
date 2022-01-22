# Объединение дввух сриптов num_json & num_json2 
# Сохраненное любимое число: объедините две программы из упражнения 10-11
# в один файл. Если число уже сохранено, сообщите его пользователю, а если нет — запро-
# сите любимое число пользователя и сохраните в файле. Выполните программу дважды,
# чтобы убедиться в том, что она работае
import json
def num_love():
    """ Запрос любимого числа пользователем """
    numb=int(input("Введите ваше любимое число :"))
    filename='numb_love.json'
    with open (filename,'w') as obj:
        json.dump(numb,obj)
    
def usr():
    """ Проверка,было ли введенно число ранее """
    try:
        filename='numb_love.json'
        with open(filename) as obj:
           num_love1=json.load(obj)
           print("Вашим любимым числом яляется :"+str(num_love1))

    except FileNotFoundError:
        num_love()       
        
usr()