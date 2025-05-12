#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'grandfather', 'sister', 'IAm']

print(my_family)


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['mother', 175],
    ['father', 177],
    ['grandfather', 160],
    ['sister', 165],
    ['Iam', 195]
]
print(my_family_height)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f'Рост отца - {my_family_height[1][1]} см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

full_height_my_family = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1]
print(f'Общий рост моей семьи - {full_height_my_family} см')