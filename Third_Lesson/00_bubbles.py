# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd
from simple_draw import clear_screen

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
point = sd.get_point(300,300)
radius = 50
for _ in range (3):
    sd.circle(point, radius,(1,1,1),1)
    radius += 5
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def drow_bubble(point_x, point_y, step):
    center = sd.get_point(point_x, point_y)
    radius = 50
    for _ in range(3):
        sd.circle(center, radius, (1, 1, 1), 1)
        radius += step
drow_bubble(100,100,10)
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for i in range(100,1000,100):
    drow_bubble(i,100,10)
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for p_y in range(100,301,100):
    for p_x in range(100,1001,100):
        drow_bubble(p_x,p_y,10)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
clear_screen()
for _ in range(100):
    point = sd.random_point()
    radius = randint(10,100)
    color_num = randint(1,99)
    for _ in range(3):
        sd.circle(point, radius, (color_num,color_num,color_num), 1)
        radius += 5
sd.pause()




