def name_tri(name, last, numb=""):
    if numb:
        return (name+" " + last + " " + numb)
    else:
        return(name+" "+last)


name_1, numb_1, last_1 = input("Имя:"), input("возрост:"), input('фамилия:')
out = name_tri(name_1, last_1, numb_1).title()
print(out)
