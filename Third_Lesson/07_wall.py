# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw
from simple_draw import rectangle, COLOR_BLUE, COLOR_RED

simple_draw.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
x1, y1, x2, y2 = 0, 0, 100, 50
for j in range(20):
    for i in range (20):
        start = simple_draw.get_point(x1, y1)
        finish = simple_draw.get_point(x2, y2)
        rectangle(start, finish, COLOR_RED, 1)
        x1 += 100
        x2 += 100
    if (j % 2 != 0):
        x1, x2 = 0, 100
    else:
        x1, x2 = -50, 50
    y1 += 50
    y2 += 50
simple_draw.pause()
