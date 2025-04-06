# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.
# Artem Guguyev


# usr_input = list(input('Enter a number - '))
# usr_input = eval(' * '.join(usr_input))
# while usr_input > 9:
#     usr_input = list(str(usr_input))
#     usr_input = eval(' * '.join(usr_input))
# print(usr_input)
usr_input = int(input('Enter a number - '))
while usr_input > 9:
    usr_input = list(str(usr_input))
    usr_input = eval(' * '.join(usr_input))
print(usr_input)