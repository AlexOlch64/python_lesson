#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб


# TODO здесь ваш код
table_code = goods['Стол']
table_item = store[table_code]
table_item_first = table_item[0]
table_item_second = table_item[1]
sum_table_first = table_item_first['quantity'] * table_item_first['price']
sum_table_second = table_item_second['quantity'] * table_item_second['price']
full_price_table = sum_table_first + sum_table_second
table_quantity = table_item_first['quantity'] + table_item_second['quantity']
print('Стол -', table_quantity, 'шт, стоимость', full_price_table, 'руб')

sofa_code = goods['Диван']
sofa_item = store[sofa_code]
sofa_item_first = sofa_item[0]
sofa_item_second = sofa_item[1]
sum_sofa_first = sofa_item_first['quantity'] * sofa_item_first['price']
sum_sofa_second = sofa_item_second['quantity'] * sofa_item_second['price']
full_price_sofa = sum_sofa_first + sum_sofa_second
sofa_quantity = sofa_item_first['quantity'] + sofa_item_second['quantity']
print('Диван -', sofa_quantity, 'шт, стоимость', full_price_sofa, 'руб')

chair_code = goods['Стул']
chair_item = store[chair_code]
chair_item_first = chair_item[0]
chair_item_second = chair_item[1]
chair_item_third = chair_item[2]
sum_chair_first = chair_item_first['quantity'] * chair_item_first['price']
sum_chair_second = chair_item_second['quantity'] * chair_item_second['price']
sum_chair_third = chair_item_third['quantity'] * chair_item_third['price']
full_price_chair = sum_chair_first + sum_chair_second + sum_chair_third
chair_quantity = chair_item_first['quantity'] + chair_item_second['quantity'] + chair_item_third['quantity']
print('Стул -', chair_quantity, 'шт, стоимость', full_price_chair, 'руб')