#Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення - якщо користувач ввів yes (можна просто y),
# то нове обчислення, інакше - закінчення роботи.


print('Welcome to simple calculator')
while True:
    user_input_number_1 = float(input('Enter first number - '))
    user_input_number_2 = float(input('Enter second number - '))
    user_input_act = input('Choose action ( + , - . * . / ) - ').strip()

    if user_input_number_2 == 0 and user_input_act == '/':
        print('Division by zero is impossible')

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
        print('Action isn\'t reconized')
        break

    if 'y' in input('Start from the beginning? (print "yes" to start again) - ' ).lower().strip():
        continue
    else:
        print('The end')
        break