animals = ["dog", "cat", "cow"]
for animal in animals:  # перебор списка животных
    if animal == ("cow"):# Условие для (коровы выводится отдельное сообщение)
        print("\nThe cow gives milk and her farm house ")
        break # Прекращиения цикла for
    print("\nA\t"+(str(animal))+"\twould make a great pet")
