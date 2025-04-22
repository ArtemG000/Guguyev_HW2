# Ваше завдання написати функцію, яка прочитає заданий файл, очистить текст від html-тегів і запише цей текст в інший файл.
# html-тег завжди починається з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що між ними.
# Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити, та ім'я файлу,
# куди потрібно записати очищений текст. Ім'я файлу, куди потрібно писати, можна задати за замовчуванням.
#Artem Guguyev

import codecs

def rem(line : str) -> str:
    """
    Функція залишає лише текст з файлу, який знаходиться між символами ">" та "<"
    """
    starts = []
    end = []
    text = ''
    for i in range(len(line)):
        if line[i] == '<':
            starts.append(i)
        elif line[i] == '>':
            end.append(i)
    for j in range(len(starts) - 1):
        text = text + line[end[j] + 1: starts[j+1]]
    return text

# empty = codecs.open(r'C:\IT\Projects\GUGUYEV.txt', 'w', 'utf-8')

def delete_html_tags(html_file, result_file='cleaned.txt'):
    empty = codecs.open(result_file, 'w', 'utf-8')
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.readlines()
        for i in html:
            if rem(i) != '':
                empty.write('\n' + rem(i))
            else:
                continue
    empty.close()
    return f'text added to {result_file}'
a = delete_html_tags(r'C:\IT\Projects\draft.html', r'C:\IT\Projects\GUGUYEV.txt')
print(a)