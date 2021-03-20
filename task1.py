# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

test_list = [1, 0b1111, 'azaza', 4.28, True, {'f': 6, 's': 19}, ('red', 'green', 'blue'), complex(5, (3 ** 0.5))]
reference_type = ('int', 'int', 'str', 'float', 'bool', 'dict', 'tuple', 'complex')
print('el_value ; detected_type ; reference_type ; correct')

for el, ref in zip(test_list, reference_type):
    print(el, ';', type(el), ';', ref, '; ', end='')
    if str(type(el)).count(ref) == 1:
        print(True)
    else:
        print(False)
