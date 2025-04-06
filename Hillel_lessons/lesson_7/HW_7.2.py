#На вхід функції correct_sentence передається речення. Необхідно повернути його виправлену копію так, щоб воно завжди починалося з великої літери та закінчувалося крапкою.
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою, додавати ще одну не потрібно, це буде помилкою.
# Вхідні аргументи: string.
# Вихідні аргументи: string.
#Artem Guguyev


def correct_sentence(text):
    text = text.rstrip('.').capitalize() + '.'
    return text
#assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
#assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
#assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
#assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
