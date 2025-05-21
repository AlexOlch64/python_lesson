# -*- coding: utf-8 -*-
from ctypes import c_uint16
from random import randint

# (определение функций)
import simple_draw
from simple_draw import COLOR_RED

simple_draw.resolution = (1200,600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile(x_center, y_center):
    print(x_center,y_center)
    center_circle = simple_draw.get_point(x_center,y_center)
    simple_draw.circle(center_circle,50, COLOR_RED, 3)
    x_center_left_eyes = x_center - 20
    y_center_left_eyes = y_center + 10
    x_center_right_eyes = x_center + 20
    y_center_right_eyes = y_center + 10
    center_circle_left = simple_draw.get_point(x_center_left_eyes,y_center_left_eyes)
    center_circle_right = simple_draw.get_point(x_center_right_eyes,y_center_right_eyes)
    simple_draw.circle(center_circle_left,5,COLOR_RED,20)
    simple_draw.circle(center_circle_right,5,COLOR_RED,20)

    x1 = x_center - 30
    y1 = y_center - 15
    x2 = x_center - 10
    y2 = y_center - 25
    x3 = x_center + 10
    y3 = y_center - 25
    x4 = x_center + 30
    y4 = y_center - 15

    broken1 = simple_draw.get_point(x1,y1)
    broken2 = simple_draw.get_point(x2,y2)
    broken3 = simple_draw.get_point(x3,y3)
    broken4 = simple_draw.get_point(x4,y4)
    brokens_list = [broken1, broken2, broken3, broken4]
    simple_draw.lines(brokens_list, COLOR_RED, False, 3)
for _ in range(10):
    x_center = randint(100,500)
    y_center = randint(100,500)
    smile(x_center,y_center)
simple_draw.pause()
