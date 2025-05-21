# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (600,300)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

x1, x2, y1, y2 = 50, 350, 50, 450
for i in range(7):
    start = sd.get_point(x1,y1)
    finish = sd.get_point(x2,y2)
    sd.line(start,finish,rainbow_colors[i],4)
    x1 += 5
    x2 += 5
    sd.clear_screen()
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
x1, y1 = 500, -300
radius = 500
for i in range(7):
    start = sd.get_point(x1,y1)
    sd.circle(start,radius,rainbow_colors[i],9)
    radius += 10
sd.pause()
