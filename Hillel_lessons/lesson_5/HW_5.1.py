# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
#
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
#Artem Guguyev


import keyword
import string

list_names = keyword.kwlist
list_punk = list(string.punctuation)
list_punk.append(' ')
list_punk.remove('_')

#_ #=> True
#__ #=> False
#___ #=> False
#x #=> True
#get_value #=> True
#get value #=> False
#get!value #=> False
#some_super_puper_value #=> True
#Get_value #=> False
#get_Value #=> False
#getValue #=> False
#3m #=> False
#m3 #=> True
#assert #=> False
#assert_exception #=> True

usr_input = input('Введіть назву змінної - ').strip()
for i in usr_input:
    if i in list_punk:
        tr_umova = False
        break
    else:
        tr_umova = True
# if not any(symb in list_punk for symb in usr_input):
#     tr_umova = True
# else:
#     tr_umova = False
print( usr_input[0].isdigit() == False and
usr_input.lower() == usr_input and
tr_umova and
usr_input not in list_names and
'__' not in usr_input
)