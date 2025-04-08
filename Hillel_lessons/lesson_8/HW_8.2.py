# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
#Artem Guguyev

import string
def is_palindrome(text):

    text_lst = list(text.lower())
    list_pun = list(string.punctuation)
    list_pun.append(' ')
    text_norm = [wort for wort in text_lst if wort not in list_pun]
    text_rev = text_norm[::-1]
    return text_norm == text_rev


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
