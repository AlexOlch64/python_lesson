# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9


# проверить для
# (просто раскоментировать нужную строку и проверить свой код)

# TODO здесь ваш код
def checking(_envelop_x, _envelop_y, _paper_x, _paper_y):
    if _envelop_x >= _paper_x:
        if _envelop_y >= _paper_y:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

checking(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 9, 8
checking(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 6, 8
checking(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 8, 6
checking(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 3, 4
checking(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 11, 9
checking(envelop_x, envelop_y, paper_x, paper_y)
paper_x, paper_y = 9, 11
checking(envelop_x, envelop_y, paper_x, paper_y)

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)


# (просто раскоментировать нужную строку и проверить свой код)

# TODO здесь ваш код
print("Second Start")
def check_brick(x,y,b_x,b_y,b_z):
    min_1 = b_x
    min_2 = b_y
    if min_1 > min_2:
        min_1 = b_y
        min_2 = b_x
    if b_z < min_2:
        if b_z < min_1:
            min_2 = min_1
            min_1 = b_z
        else:
            min_2 = b_z
    checking(x,y,min_1,min_2)

hole_x, hole_y = 8, 9

brick_x, brick_y, brick_z = 11, 10, 2
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 11, 2, 10
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 10, 11, 2
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 10, 2, 11
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 2, 10, 11
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 2, 11, 10
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 3, 5, 6
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 3, 6, 5
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 6, 3, 5
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 6, 5, 3
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 5, 6, 3
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 5, 3, 6
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 11, 3, 6
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 11, 6, 3
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 6, 11, 3
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 6, 3, 11
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 3, 6, 11
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)

brick_x, brick_y, brick_z = 3, 11, 6
check_brick(hole_x,hole_y,brick_x,brick_y,brick_z)
