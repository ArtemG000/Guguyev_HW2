# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
#
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
#Artem Guguyev

import string

list_pun = list(string.punctuation)
usr_input = input('Введіть текст хештегу - ')
for n in list_pun:
    usr_input = usr_input.replace(n, ' ')
usr_input = usr_input.split()
for i in (range(len(usr_input))):
    usr_input[i] = usr_input[i].title()
usr_input = ''.join(usr_input)
print(f"#{usr_input[:140]}")

#usr_input = "".join(el for el in usr_input if el not in list_pun).split()
# for i, word in enumerate(usr_input):
#     usr_input[i] = word.title()
# usr_input = ''.join(usr_input)
#
# print(f"#{usr_input[:140]}")

#end_ = '#{}'
#print(end_.format(usr_input[:140]))


# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
