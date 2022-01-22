from os import write


file = "/home/richard/workspace/Python_data/files_for_work_introductory_data/proba1.txt"
out_txt="/home/richard/workspace/Python_data/data_output/with_proba.txt"
with open(file) as file_object:#открытие файла с данными
    lines = file_object.readlines()
    string =[]
    for line in lines:
        string += list(line.strip().split())
num=sum([int(i)for i in string])
with open(out_txt,'w') as out: #Здесь прщисходит запись в файл PS записывать можно только в формате str
    out.write(str(num))

                
