#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код

time_for_Halo = violator_songs_list[3][1]
time_for_EnjoytheSilence = violator_songs_list[5][1]
time_for_clean = violator_songs_list[8][1]
full_time = round(time_for_clean + time_for_EnjoytheSilence + time_for_Halo,2)

print(f'Три песни звучат {full_time} минут')
# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут
time_for_SweetestPerfection = violator_songs_dict['Sweetest Perfection']
time_for_PolicyOfTruth = violator_songs_dict['Policy of Truth']
time_for_BlueDress = violator_songs_dict['Blue Dress']

full_time = round(time_for_SweetestPerfection + time_for_PolicyOfTruth + time_for_BlueDress,2)
# TODO здесь ваш код
print(f'А другие три песни звучат {full_time} минут')