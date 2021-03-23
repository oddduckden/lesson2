# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

source_list = [10, 6, 5, 5, 2, 1]
print('Исходный рейтинг: ', *source_list)
# в условии на первой итерации элемент добавили к списку, на последующих размер списка уже фиксированный,
# предположительно с изъятием элемента, добавленного на предыдущей итерации. Похоже на добавление отзыва с
# возможностью передумать.
i = 0
print('Для окончания в ответе введите "end".')
while True:
    tmp = input('Введите значение рейтинга: ')
    if tmp == 'end':
        break
    if i != 0:
        source_list.pop(-1)
    source_list.append(int(tmp))
    i += 1
    output_list = source_list.copy()
    output_list.sort()
    output_list.reverse()
    print('Новый рейтинг :', *output_list)
