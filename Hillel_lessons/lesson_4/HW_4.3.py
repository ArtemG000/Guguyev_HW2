# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
# Artem Guguyev

import random

list_1 = []
rang = 0
while rang < random.randint(3,10):
    rang += 1
    list_1.append(random.randint(0, 100))
print(list_1)
list_2 = [list_1[0], list_1[2], list_1[-2]]
print(list_2)
