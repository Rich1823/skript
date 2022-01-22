# Функции могут использоваться со всеми структурами Python, уже известными
# вам. Например, используем функцию get_formatted_name() в цикле while , чтобы
# поприветствовать пользователей более официально. Первая версия программы,
# приветствующей пользователей по имени и фамилии, может выглядеть так:
def get_formatted_name(first_name, last_name):
    full_name = first_name+" "+last_name
    return full_name.title()


while True:
    print("\n Введите ваше имя и фамилию по одильности , по окончанию ввода введите 'выход'")
    f_name=input("Имя:")
    if f_name=='выход':
        break
    l_name=input("Фамимлия:")
    if l_name=='выход':
        break
    get_formatted=get_formatted_name(f_name,l_name)
    print("\nHello," +" "+get_formatted+"!")