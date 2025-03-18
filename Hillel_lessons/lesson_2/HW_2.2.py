#На запит від програми, користувач вводить 5-ти значне ціле, позитивне число. Вам необхідно "перевернути" цє число задом наперед, тобто щоб у результаті вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.
#Artem Guguyev

user_data = int(float(input("Введіть ціле невід'ємне п'ятизначне число: "))) #12345
com_1 = int(user_data // 10000)
com_2 = int(user_data // 1000 - (user_data // 10000) * 10)
com_3 = int((user_data % 1000 - user_data % 100) / 100)
com_4 = int((user_data % 100 - user_data % 10) / 10)
com_5 = int(user_data % 10)
reversed_user_data = com_5 * 10000 + com_4 * 1000 + com_3 * 100 + com_2 * 10 + com_1
if user_data >= 100_000 or user_data < 0:
    print("Число не в робочому діапазоні")
else:
    print(reversed_user_data)