#Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.
#Зробити перевірку на те, що при діленні дільник не дорівнює 0!
#Artem Guguyev

print('Вітаємо в простому калькуляторі!')
user_input_number_1 = float(input('Введіть перше число - '))
user_input_number_2 = float(input('Введіть друге число - '))
user_input_act = input('Введіть дію ( + , - . * . / ) - ')
#if user_input_act != '+' and user_input_act != '-' and user_input_act != '*' and user_input_act != '/':
    #print('Дія не розпізнана')

if user_input_number_2 == 0 and user_input_act == '/':
    print('Ділення на нуль неможливо')
if user_input_act == '+':
    result_ = user_input_number_1 + user_input_number_2
    print(result_)
elif user_input_act == '-':
    result_ = user_input_number_1 - user_input_number_2
    print(result_)
elif user_input_act == '*':
    result_ = user_input_number_1 * user_input_number_2
    print(result_)
elif user_input_act == '/' and user_input_number_2 != 0:
    result_ = user_input_number_1 / user_input_number_2
    print(result_)
else:
    print('Дія не розпізнана')
print('Кінець')
#Не подобається мені, що при введенні знаку дії не дозволяються пробіли.