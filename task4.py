# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

words_list = list(input('Введите строку: ').split())
i = 1
for word in words_list:
    print(f'{i} {word[:10]}')
    i += 1