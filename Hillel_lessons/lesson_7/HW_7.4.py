# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів, за наступними правилом:
# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.
#Artem Guguyev


def common_elements():
    l3 = set([i for i in range(100) if i % 3 == 0])
    l5 = set([i for i in range(100) if i % 5 == 0])
    common_elements = l3.intersection(l5)
    #common_elements = l5.intersection(l3)
    #common_elements = l3 & l5
    return common_elements



assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
