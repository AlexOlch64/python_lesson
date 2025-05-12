#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# TODO здесь заполнение словаря
distance_moscow_london = ((sites['Moscow'][0] - sites["London"][0]) ** 2 + (sites['Moscow'][1] - sites["London"][1]) ** 2) ** .5
distance_moscow_paris = ((sites['Moscow'][0] - sites["Paris"][0]) ** 2 + (sites['Moscow'][1] - sites["Paris"][1]) ** 2) **.5

distance_london_moscow = distance_moscow_london
distance_london_paris = ((sites['London'][0] - sites["Paris"][0]) ** 2 + (sites['London'][1] - sites["Paris"][1]) ** 2) **.5

distance_paris_moscow = distance_moscow_paris
distance_paris_london = distance_london_paris


print(distance_moscow_paris,distance_moscow_london, distance_paris_london,distance_paris_moscow, distance_london_moscow, distance_london_paris)

distances['Moscow'] = {'London' : distance_moscow_london, 'Paris' : distance_moscow_paris}
distances['London'] = {'Moscow' : distance_london_moscow, 'Paris' : distance_london_paris}
distances['Paris'] = {'Moscow' : distance_paris_moscow, 'London' : distance_paris_london}

pprint.pprint(distances)


