from bin.settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'WT................D.....D.....W',
    'W.................W.....W.....W',
    'W.................W.....W.....W',
    'W.................W.....W.....W',
    'W.................W.....W.....W',
    'W.................W.....W.....W',
    'W.................WWWDWWWWWWDWW'
    'WWWWWWWW..........D...........W'
    'W......WWWWWWWWWWWWWWWWW......W'
    'W......W...............W......W'
    'W......W...............WWWWDWWW'
    'W......W...............W......W'
    'W......W...............W......W'
    'W......W...............W......W'
    'W......W...............W......W'
    'W......W...............W......W'
    'W......W...............W......W'
    'W......W...............W......W'
    'W......W...............W......W'
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]
second_floor = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W'
    'W....W'
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
