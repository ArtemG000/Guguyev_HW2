# Для списку цілих чисел потрібно знайти суму елементів із парними індексами [0-й, 2-й, 4-й ітд], потім перемножити цю суму на останній елемент вхідного масиву.
# Не забудьте, що перший елемент масиву має індекс 0
# Для порожнього масиву результат завжди 0.
#Artem Guguyev


#list_1 = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88
#list_1 = [1, 3, 5] #=> 30
#list_1 = [6] #=> 36
list_1 = []# => 0

while list_1:
    list_2 = list_1[::2]
    print((sum(list_2)) * list_1[-1])
    break
else:
    print(list_1)