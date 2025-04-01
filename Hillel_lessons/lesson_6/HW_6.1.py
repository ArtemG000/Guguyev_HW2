# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
#
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
#
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# Artem Guguyev

import string

voc = list(string.ascii_letters)
usr_input = input('Please enter two letters separated by a hyphen - ').replace('-', ' ').split()
usr_input[0] = voc.index(usr_input[0])
usr_input[1] = voc.index(usr_input[1]) + 1
# for el in voc:
#     if el == usr_input[0]:
#         usr_input[0] = voc.index(el)
#     if el == usr_input[1]:
#         usr_input[1] = voc.index(el)
# if usr_input[0] >= usr_input[1]:
#     print(''.join(voc[usr_input[1]:(usr_input[0]+1)]))
# else:
#     print(''.join(voc[usr_input[0]:(usr_input[1]+1)]))
print(''.join(voc[usr_input[0]:(usr_input[1])]))

