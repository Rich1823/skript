# Создание словаря в словаре для перебора информации о пользователях
# пример работы со словарями , items позволяет вывести и ключи и значение привязонное к ключу 
name_info = {'vasa': {'siti': 'vologda', 'name': 'vasa', 'um': 'baklan'},
             'luza': {'siti': 'msk', 'name': 'luza', 'um': '90%'}, }
for name_1, info_1 in name_info.items():
    print(name_1+"\t"+info_1['siti']+"\n"+info_1['um'])
