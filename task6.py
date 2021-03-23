# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# Ввод справочника товаров.
# нет проверки соответствия введенной строки ожидаемому типу.
attribute = {'название': str, 'цена': int, 'количество': int, 'ед.': str}
goods = list()
stop = False
count = 1
print('Для окончания ввода списка товаров в ответе введите "end" вместо названия товара.')
while True:
    product = dict()
    for i in attribute:
        product.update({i: attribute.setdefault(i)(input(f'{i}: '))})
        if product.setdefault(i) == 'end':
            stop = True
            break
    if stop is True:
        break
    goods.append((count, product))
    count += 1
tmp_goods = goods.copy()
print('[')
for i in range(len(goods)):
    print(tmp_goods.pop(0))
print(']')
# Cбор аналитики о товарах.
for i in attribute:
    tmp_goods, attrib_values = goods.copy(), list()
    for x in range(len(goods)):
        tmp = list(tmp_goods.pop(0))
        attrib_values.append(tmp.pop(1).setdefault(i))
    print(f'{i}: ', list(set(attrib_values))) if i == 'ед.' else print(f'{i}: ', attrib_values)
