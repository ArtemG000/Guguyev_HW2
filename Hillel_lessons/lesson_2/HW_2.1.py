# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого друкує на екрані стовпчик цифр, з якого це число складається.
#Завдання необхідно вирішити, використовуючи методи поділу (підказка // і % або divmod). Виведення в стовпчик можна зробити за допомогою 4-х функцій print.
#Artem Guguyev

# num_user = int(input('Введіть чотиризначне число= '))
# fourth_digit = num_user % 10
# third_digit = int((num_user % 100 - num_user % 10) / 10)
# second_digit = int((num_user % 1000 - num_user % 100) / 100)
# first_digit = int((num_user % 10000 - num_user % 1000) / 1000)
# print(first_digit)
# print(second_digit)
# print(third_digit)
# print(fourth_digit)

print("Зазначте,що програма працює з невід'ємними числами до 9999  ")
num_user1 = int(input('Введіть чотиризначне число= '))
first_digit = int(num_user1 // 1000)
second_digit = int(num_user1 // 100 - first_digit * 10)
third_digit = int((num_user1 % 100 - num_user1 % 10) / 10)
fourth_digit = int(num_user1 % 10)
print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)