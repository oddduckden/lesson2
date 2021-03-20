# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

# test string: 1,eee, r, (1, 2), azaza, {A, B, C},[2, 2, 5]

source_string = input('Введите через запятую элементы списока: ')
while not source_string:
    source_string = input('Введите через запятую элементы списка: ')
# парсинг введенной строки в список
source_string = source_string.replace(' ', '')
skip_it = False
converted_string = str()
for i in source_string:
    if i in ('[', '{', '('):
        skip_it = True
    elif i in (']', '}', ')'):
        skip_it = False
    if i == ',' and not skip_it:
        converted_string = converted_string + ';'
    elif i == ',' and skip_it:
        converted_string = converted_string + ', '
    else:
        converted_string = converted_string + i
source_list = list(converted_string.split(';'))
# попарная перестановка с учетом нечетного
result = list()
last_element = str()
if len(source_list) % 2 != 0:
    last_element = source_list.pop(-1)
for i, j in zip(*[iter(source_list)]*2):
    i, j = j, i
    result.append(i)
    result.append(j)
if last_element:
    result.append(last_element)
print(', '.join(result))
