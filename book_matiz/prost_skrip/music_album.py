# Альбом: напишите функцию make_album(), которая строит словарь с описанием му-
# зыкального альбома. Функция должна получать имя исполнителя и название альбома
# и возвращать словарь, содержащий эти два вида информации. Используйте функцию
# для создания трех словарей, представляющих разные альбомы. Выведите все возвраща-
# емые значения, чтобы показать, что информация правильно сохраняется во всех трех
# словарях.
# Добавьте в make_album() дополнительный параметр для сохранения количества дорожек
# в альбоме. Если в строку вызова включено значение количества дорожек, добавьте это зна-
# чение в словарь альбома. Создайте как минимум один новый вызов функции с передачей
# количества дорожек в альбоме
def make_album(art, album, trek1=""):
    if trek1 == "":
        art_album = {art: album}
    else:
        art_album = {art: {album: trek1}}
    return art_album


print("Для прекращения ввода в Исполнителях введите 'q'")
alb1 = []
while True:
    art1 = input("Исполнитель:")
    if art1 == "q":
        break
    album1 = input("Альбом:")
    trek = input("Коли чество треков в альбоме:")
    make_album_new = make_album(art1, album1, trek)
    alb1 += [make_album_new]
print(alb1)
