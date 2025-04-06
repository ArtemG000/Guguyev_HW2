# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.
#Artem Guguyev

import random

def common_elements():
    list_1 = []
    num = 0
    while num < random.randint(10, 100):
        num += 1
        list_1.append(random.randint(0, 1000))
    l3 = set([i for i in list_1 if i % 3 == 0])
    l5 = set([i for i in list_1 if i % 5 == 0])
    print(list_1, l3, l5, sep= '\n\n', end = '\n\n')
    common_elements = l3.intersection(l5)
    #common_elements = l5.intersection(l3)
    #common_elements = l3 & l5
    return common_elements
print(common_elements())




