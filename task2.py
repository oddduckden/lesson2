# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

source_string = input('Введите через запятую элементы списока: ')
while source_string:
    source_string = input('Введите через запятую элементы списока: ')
source_list = list(source_string.split(', '))