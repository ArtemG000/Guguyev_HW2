# # for i in  range(5 ,16 ,2 ):
# #     print("El: ", i)
# #
# # print("\n\n\n\n\n")
# # some_text = "Some Text"
# # for i in some_text:
# #     # if i != "e":
# #         # print(i)
#
#
# # i = 2
# # while i < 256:
# #     i *= 2
# #     print(i)
#
# work = True
# while work:
#     user_input = input("Vvedit` 'STOP': ")
#     if user_input.upper() == 'STOP':
#         work = False
#     else:
#         print("we are ready!")
# print(' While loop is done!')

#
# for i in "Hello World!":
#     if i.lower() == 'h':
#        print("Found")
#        break
# else:
#     print('Not found')
#
#
# x = 2
# y = 4 / 2
# print(id(x))
# print(id(y))
# if x == y:
#     print(1)
# if x is y:
#     print(2)
# else:
#     print('lol')

orange_price = 15
tea_price = 10
apple_price = 5
print('orange price =', orange_price)
print('tea price =', tea_price)
print('apple price =', apple_price)
my_money = float(input('Write how much money You have ='))
print(my_money)
if my_money >= orange_price:
    my_money -= orange_price
    print('I buy oranges and i have rest money: ', my_money)
    if my_money >= tea_price:
        my_money -= tea_price
        print('I buy tea and i have rest money: ', my_money)
        if my_money >= apple_price:
            my_money -= apple_price
            print('I buy apples and i have rest money: ', my_money)
            if my_money == 0:
                print('Oh God.... I have no money')
            else:
                print('I have more money - ', my_money)
        else:
            print('I don`t have enough money for apples, but i have bought oranges and tea and have more money- ', my_money)
    elif my_money >= apple_price:
        my_money -= apple_price
        print('I have bought oranges, but i don`t have enough money for tea, so i decided to buy apples and have more money - ', my_money)
    else:
        print('I have bought only oranges, but i have money for beer- ', my_money)
elif my_money >= tea_price:
    my_money -= tea_price
    print('I have bought tea and have so much money- ', my_money)
elif my_money >= apple_price:
    my_money -= apple_price
    print('I have bought apples and have so much money- ', my_money)
else:
    print('i don`t have enough money for this purchase, because i have only -', my_money)
print('End of Purchase!')

