import pygame
import math
import game_display
import copy
import time
from random import randint

pygame.init()
pygame.font.init()

game = True
scale = 2
speed_mode = 5
display_width = game_display.display_width
display_height = game_display.display_height
center_x = display_width / 2
center_y = display_height / 2
map_width = 20
map_height = 20
i_width = 540
i_height = 216
island_x = 0
island_y = 0

display = game_display.display

clock = pygame.time.Clock()

class fleet_object:
    def __init__(self, ships, speed, x, y, target_x, target_y, angle, type,
                 fraction, gold, rank, move=True):
        self.ships = ships
        self.speed = speed
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.angle = angle
        self.type = type
        self.fraction = fraction
        self.gold = gold
        self.rank = rank
        self.move = move

class ship_type:
    def __init__(self, ms_sail1, ms_sail0, pic_size, deck_size, cost, t_speed, max_hp, gun_count, speed):
        self.ms_sail1 = ms_sail1
        self.ms_sail0 = ms_sail0
        self.pic_size = pic_size
        self.deck_size = deck_size
        self.cost = cost
        self.t_speed = t_speed
        self.max_hp = max_hp
        self.gun_count = gun_count
        self.speed = speed

class forpost:
    def __init__(self, x, y, rank, sold_1, sold_2, fraction, land):
        self.x = x
        self.y = y
        self.rank = rank
        self.sold_1 = sold_1
        self.sold_2 = sold_2
        self.fraction = fraction
        self.land = land

fleets = []

wave_step = []
wave_step.append(pygame.image.load('global\\waves\\0.png').convert_alpha())
wave_step.append(pygame.image.load('global\\waves\\1.png').convert_alpha())
wave_step.append(pygame.image.load('global\\waves\\2.png').convert_alpha())
wave_step.append(pygame.image.load('global\\waves\\3.png').convert_alpha())
wave_step.append(pygame.image.load('global\\waves\\4.png').convert_alpha())
wave_step.append(pygame.image.load('global\\waves\\5.png').convert_alpha())
wave_step.append(pygame.image.load('global\\waves\\6.png').convert_alpha())

waves = []

barkas_sail1 = []
barkas_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\barkas\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\barkas\\' + str(i) + '\\sail_0.png').convert_alpha()
    barkas_sail1.append(pygame.transform.smoothscale(image_sail_1, (300 / scale, 300 / scale)))
    barkas_sail0.append(pygame.transform.smoothscale(image_sail_0, (300 / scale, 300 / scale)))

pink_sail1 = []
pink_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\pink\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\pink\\' + str(i) + '\\sail_0.png').convert_alpha()
    pink_sail1.append(pygame.transform.smoothscale(image_sail_1, (350 / scale, 350 / scale)))
    pink_sail0.append(pygame.transform.smoothscale(image_sail_0, (350 / scale, 350 / scale)))

ladya_sail1 = []
ladya_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\ladya\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\ladya\\' + str(i) + '\\sail_0.png').convert_alpha()
    ladya_sail1.append(pygame.transform.smoothscale(image_sail_1, (300 / scale, 300 / scale)))
    ladya_sail0.append(pygame.transform.smoothscale(image_sail_0, (300 / scale, 300 / scale)))

shuna_sail1 = []
shuna_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\shuna\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\shuna\\' + str(i) + '\\sail_0.png').convert_alpha()
    shuna_sail1.append(pygame.transform.smoothscale(image_sail_1, (400 / scale, 400 / scale)))
    shuna_sail0.append(pygame.transform.smoothscale(image_sail_0, (400 / scale, 400 / scale)))

lugger_sail1 = []
lugger_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\lugger\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\lugger\\' + str(i) + '\\sail_0.png').convert_alpha()
    lugger_sail1.append(pygame.transform.smoothscale(image_sail_1, (500 / scale, 500 / scale)))
    lugger_sail0.append(pygame.transform.smoothscale(image_sail_0, (500 / scale, 500 / scale)))

shlup_sail1 = []
shlup_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\shlup\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\shlup\\' + str(i) + '\\sail_0.png').convert_alpha()
    shlup_sail1.append(pygame.transform.smoothscale(image_sail_1, (500 / scale, 500 / scale)))
    shlup_sail0.append(pygame.transform.smoothscale(image_sail_0, (500 / scale, 500 / scale)))

bark_sail1 = []
bark_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\bark\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\bark\\' + str(i) + '\\sail_0.png').convert_alpha()
    bark_sail1.append(pygame.transform.smoothscale(image_sail_1, (600 / scale, 600 / scale)))
    bark_sail0.append(pygame.transform.smoothscale(image_sail_0, (600 / scale, 600 / scale)))

fleyt_sail1 = []
fleyt_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\fleyt\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\fleyt\\' + str(i) + '\\sail_0.png').convert_alpha()
    fleyt_sail1.append(pygame.transform.smoothscale(image_sail_1, (600 / scale, 600 / scale)))
    fleyt_sail0.append(pygame.transform.smoothscale(image_sail_0, (600 / scale, 600 / scale)))

brig_sail1 = []
brig_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\brig\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\brig\\' + str(i) + '\\sail_0.png').convert_alpha()
    brig_sail1.append(pygame.transform.smoothscale(image_sail_1, (700 / scale, 700 / scale)))
    brig_sail0.append(pygame.transform.smoothscale(image_sail_0, (700 / scale, 700 / scale)))

galera_sail1 = []
galera_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\galera\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\galera\\' + str(i) + '\\sail_0.png').convert_alpha()
    galera_sail1.append(pygame.transform.smoothscale(image_sail_1, (600 / scale, 600 / scale)))
    galera_sail0.append(pygame.transform.smoothscale(image_sail_0, (600 / scale, 600 / scale)))

pinas_sail1 = []
pinas_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\pinas\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\pinas\\' + str(i) + '\\sail_0.png').convert_alpha()
    pinas_sail1.append(pygame.transform.smoothscale(image_sail_1, (900 / scale, 900 / scale)))
    pinas_sail0.append(pygame.transform.smoothscale(image_sail_0, (900 / scale, 900 / scale)))

corvet_sail1 = []
corvet_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\corvet\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\corvet\\' + str(i) + '\\sail_0.png').convert_alpha()
    corvet_sail1.append(pygame.transform.smoothscale(image_sail_1, (1000 / scale, 1000 / scale)))
    corvet_sail0.append(pygame.transform.smoothscale(image_sail_0, (1000 / scale, 1000 / scale)))

fregat_sail1 = []
fregat_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\fregat\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\fregat\\' + str(i) + '\\sail_0.png').convert_alpha()
    fregat_sail1.append(pygame.transform.smoothscale(image_sail_1, (1100 / scale, 1100 / scale)))
    fregat_sail0.append(pygame.transform.smoothscale(image_sail_0, (1100 / scale, 1100 / scale)))

galeon_sail1 = []
galeon_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\galeon\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\galeon\\' + str(i) + '\\sail_0.png').convert_alpha()
    galeon_sail1.append(pygame.transform.smoothscale(image_sail_1, (1300 / scale, 1300 / scale)))
    galeon_sail0.append(pygame.transform.smoothscale(image_sail_0, (1300 / scale, 1300 / scale)))

warship_sail1 = []
warship_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\warship\\' + str(i) + '\\sail_1.png').convert_alpha()
    image_sail_0 = pygame.image.load('global\\warship\\' + str(i) + '\\sail_0.png').convert_alpha()
    warship_sail1.append(pygame.transform.smoothscale(image_sail_1, (1300 / scale, 1300 / scale)))
    warship_sail0.append(pygame.transform.smoothscale(image_sail_0, (1300 / scale, 1300 / scale)))

ship_stats = {"barkas": ship_type(barkas_sail1, barkas_sail0, 300, 70, 1200, 100, 15, 2, 0.8),
              "pink": ship_type(pink_sail1, pink_sail0, 350, 70, 1600, 80, 15, 2, 1.2),
              "shuna": ship_type(shuna_sail1, shuna_sail0, 400, 90, 2500, 60, 20, 3, 1.6),
              "lugger": ship_type(lugger_sail1, lugger_sail0, 500, 100, 3200, 80, 25, 3, 1.6),
              "ladya": ship_type(ladya_sail1, ladya_sail0, 300, 75, 1500, 40, 20, 2, 1.2),
              "shlup": ship_type(shlup_sail1, shlup_sail0, 500, 100, 3600, 100, 30, 3, 1.6),
              "bark": ship_type(bark_sail1, bark_sail0, 600, 120, 5500, 60, 35, 4, 2.0),
              "brig": ship_type(brig_sail1, brig_sail0, 700, 140, 7000, 80, 40, 5, 2.0),
              "fleyt": ship_type(fleyt_sail1, fleyt_sail0, 600, 120, 4200, 40, 40, 3, 1.6),
              "galera": ship_type(galera_sail1, galera_sail0, 600, 170, 12000, 100, 50, 6, 2.0),
              "corvet": ship_type(corvet_sail1, corvet_sail0, 1000, 190, 15000, 60, 60, 7, 2.4),
              "pinas": ship_type(pinas_sail1, pinas_sail0, 900, 190, 10000, 40, 60, 5, 2.0),
              "fregat": ship_type(fregat_sail1, fregat_sail0, 1100, 250, 22000, 80, 75, 8, 2.4),
              "warship": ship_type(warship_sail1, warship_sail0, 1300, 270, 30000, 80, 90, 9, 2.8),
              "galeon": ship_type(galeon_sail1, galeon_sail0, 1300, 270, 25000, 40, 90, 7, 2.4)}

game_time = 1199 * 6

fraction_relations = {'PLAYER': 0, 'RED': 10, 'GREEN': 10, 'BLUE': 10, 'PIRATE': 0}

fraction_war_fleet_count = {'PLAYER': 0, 'RED': 0, 'GREEN': 0, 'BLUE': 0}

player_fraction = False

player_trade_forpost = '-'

fraction_wars = {'PLAYER': {'PLAYER': False, 'RED': False, 'GREEN': False, 'BLUE': False, 'PIRATE': False},
                 'RED': {'PLAYER': False, 'RED': False, 'GREEN': False, 'BLUE': False, 'PIRATE': False},
                 'GREEN': {'PLAYER': False, 'RED': False, 'GREEN': False, 'BLUE': False, 'PIRATE': False},
                 'BLUE': {'PLAYER': False, 'RED': False, 'GREEN': False, 'BLUE': False, 'PIRATE': False},
                 'PIRATE': {'PLAYER': False, 'RED': False, 'GREEN': False, 'BLUE': False, 'PIRATE': False}}

islands = []

forposts = []

palms = []

trees = []

ship_trees = []

def island_intersection(x1, y1, x2, y2, ax, ay, dx, dy):
    if x1 == x2 and y1 == y2:
        if (ax <= x1 <= dx) and (ay <= y1 <= dy):
            return True
        else:
            return False
    elif x1 == x2 and y1 != y2:
        if (ax <= x1 <= dx) and ((min(y1, y2) <= ay <= max(y1, y2)) or (min(y1, y2) <= dy <= max(y1, y2))):
            return True
        else:
            return False
    elif x1 != x2 and y1 == y2:
        if (ay <= y1 <= dy) and ((min(x1, x2) <= ax <= max(x1, x2)) or (min(x1, x2) <= dx <= max(x1, x2))):
            return True
        else:
            return False
    else:
        kx = (y2 - y1) / (x2 - x1)
        bx = y2 - kx * x2
        ky = (x2 - x1) / (y2 - y1)
        by = x2 - ky * y2
        if ((ay <= kx * ax + bx <= dy) and (min(x1, x2) <= ax <= max(x1, x2)) or (ay <= kx * dx + bx <= dy) and (min(x1, x2) <= dx <= max(x1, x2))) or (
            (ax <= ky * ay + by <= dx) and (min(y1, y2) <= ay <= max(y1, y2)) or (ax <= ky * dy + by <= dx) and (min(y1, y2) <= dy <= max(y1, y2))):
            return True
        else:
            return False

def palm_key(palm):
    return palm[1]

def ways_key(ways):
    return ways[2]

def ships_speed_key(ship):
    return ship[4]

def ships_rank_key(ship):
    return ship[3]

def island_generate(forpost, fraction, land):
    if land == 'sand':
        width = randint(2, 3)
        height = randint(2, 3)
    elif land == 'grass':
        width = randint(3, 5)
        height = randint(3, 5)
    elif land == 'snow':
        width = randint(3, 6)
        height = randint(3, 4)
    if land == 'snow':
        ax = (randint(0, map_width - width) - map_width // 2) * i_width
        ay = (randint(0, map_height // 4 - height - 1) - map_height // 2) * i_height
    else:
        ax = (randint(0, map_width - width) - map_width // 2) * i_width
        ay = (randint(map_width // 4, map_height - height) - map_height // 2) * i_height
    w = width * i_width
    h = height * i_height
    may_be_add = True
    if 0 >= ax and (ax + w) >= 0 and 0 >= ay and (ay + h) >= 0:
        may_be_add = False
    for i in islands:
        for j in range(-1, i[3] + 2):
            for a in range(width + 1):
                if island_intersection(ax + a * i_width, ay, ax + a * i_width, ay + h, i[0] - i_width*1.5,
                                       i[1] + j * i_height - i_height/2, i[0] + i[2] * i_width + i_width * 1.5, i[1] + j * i_height + i_height/2):
                    may_be_add = False
    if may_be_add:
        islands.append([ax, ay, width, height, land])
        fx = 1
        fy = 1
        if forpost != 0:
            fx = ax + randint(1, width) * i_width
            fy = ay + h
            trade_ship1 = randint(0, 4)
            trade_ship2 = randint(0, 4)
            forposts.append([fx, fy, forpost, list(ship_stats.keys())[trade_ship1], list(ship_stats.keys())[trade_ship2], fraction, land])
        if land == 'sand':
            for i in range(0, width):
                for j in range(0, height):
                    if not ((ax + i * i_width == fx - i_width) and (ay + j * i_height == fy - i_height)):
                        if (j == 0):
                            add_palm = []
                            for k in range(6):
                                palm_intersection = True
                                error = 0
                                while palm_intersection and error < 100:
                                    error += 1
                                    palm_intersection = False
                                    x = randint(ax + i * i_width + 64, ax + (i + 1) * i_width - 64)
                                    y = randint(ay + j * i_height + 128, ay + (j + 1) * i_height - 15)
                                    for palm in add_palm:
                                        gip = ((x - palm[0]) ** 2 + 6.25 * (y - palm[1]) ** 2) ** 0.5
                                        if gip < 72:
                                            palm_intersection = True
                                add_palm.append([x, y])
                            for k in range(6):
                                palms.append(add_palm[k])
                        else:
                            add_palm = []
                            for k in range(11):
                                palm_intersection = True
                                error = 0
                                while palm_intersection and error < 100:
                                    error += 1
                                    palm_intersection = False
                                    x = randint(ax + i * i_width + 64, ax + (i + 1) * i_width - 64)
                                    y = randint(ay + j * i_height, ay + (j + 1) * i_height - 15)
                                    for palm in add_palm:
                                        gip = ((x - palm[0]) ** 2 + 6.25 * (y - palm[1]) ** 2) ** 0.5
                                        if gip < 72:
                                            palm_intersection = True
                                add_palm.append([x, y])
                            for k in range(11):
                                palms.append(add_palm[k])
            palms.sort(key=palm_key)
        elif land == 'grass':
            for i in range(0, width):
                for j in range(0, height):
                    if not ((ax + i * i_width == fx - i_width) and (ay + j * i_height == fy - i_height)):
                        if (j == 0):
                            add_tree = []
                            for k in range(1):
                                tree_intersection = True
                                error = 0
                                while tree_intersection and error < 100:
                                    error += 1
                                    tree_intersection = False
                                    x = randint(ax + i * i_width + 72, ax + (i + 1) * i_width - 72)
                                    y = randint(ay + j * i_height + 180, ay + (j + 1) * i_height - 28)
                                    for tree in add_tree:
                                        gip = ((x - tree[0]) ** 2 + 6.25 * (y - tree[1]) ** 2) ** 0.5
                                        if gip < 144:
                                            tree_intersection = True
                                add_tree.append([x, y])
                            for k in range(1):
                                trees.append(add_tree[k])
                        else:
                            add_tree = []
                            error = 0
                            for k in range(6):
                                error += 1
                                tree_intersection = True
                                while tree_intersection:
                                    tree_intersection = False
                                    x = randint(ax + i * i_width + 72, ax + (i + 1) * i_width - 72)
                                    y = randint(ay + j * i_height, ay + (j + 1) * i_height - 28)
                                    for tree in add_tree:
                                        gip = ((x - tree[0]) ** 2 + 6.25 * (y - tree[1]) ** 2) ** 0.5
                                        if gip < 144:
                                            tree_intersection = True
                                add_tree.append([x, y])
                            for k in range(6):
                                trees.append(add_tree[k])
            trees.sort(key=palm_key)
        elif land == 'snow':
            for i in range(0, width):
                for j in range(1, height):
                    if not ((ax + i * i_width == fx - i_width) and (ay + j * i_height == fy - i_height)):
                        if (j == 1):
                            add_ship_tree = []
                            for k in range(6):
                                ship_tree_intersection = True
                                error = 0
                                while ship_tree_intersection and error < 100:
                                    error += 1
                                    ship_tree_intersection = False
                                    x = randint(ax + i * i_width + 48, ax + (i + 1) * i_width - 48)
                                    y = randint(ay + j * i_height + 72, ay + (j + 1) * i_height - 28)
                                    for ship_tree in add_ship_tree:
                                        gip = ((x - ship_tree[0]) ** 2 + 6.25 * (y - ship_tree[1]) ** 2) ** 0.5
                                        if gip < 144:
                                            ship_tree_intersection = True
                                add_ship_tree.append([x, y])
                            for k in range(6):
                                ship_trees.append(add_ship_tree[k])
                        else:
                            add_ship_tree = []
                            for k in range(9):
                                ship_tree_intersection = True
                                error = 0
                                while ship_tree_intersection and error < 100:
                                    error += 1
                                    ship_tree_intersection = False
                                    x = randint(ax + i * i_width + 48, ax + (i + 1) * i_width - 48)
                                    y = randint(ay + j * i_height, ay + (j + 1) * i_height - 28)
                                    for ship_tree in add_ship_tree:
                                        gip = ((x - ship_tree[0]) ** 2 + 6.25 * (y - ship_tree[1]) ** 2) ** 0.5
                                        if gip < 144:
                                            ship_tree_intersection = True
                                add_ship_tree.append([x, y])
                            for k in range(9):
                                ship_trees.append(add_ship_tree[k])
            ship_trees.sort(key=palm_key)
        return False
    else:
        return True

def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

def fleet_move(fleet, angle, speed):
    if angle == 0:
        fleet.x += 0 * speed
        fleet.y += -0.41 * speed
    elif angle == 1:
        fleet.x += 0.65 * speed
        fleet.y += -0.325 * speed
    elif angle == 2:
        fleet.x += 0.9 * speed
        fleet.y += -0.2 * speed
    elif angle == 3:
        fleet.x += 1.025 * speed
        fleet.y += 0 * speed
    elif angle == 4:
        fleet.x += 0.9 * speed
        fleet.y += 0.2 * speed
    elif angle == 5:
        fleet.x += 0.65 * speed
        fleet.y += 0.325 * speed
    elif angle == 6:
        fleet.x += 0 * speed
        fleet.y += 0.41 * speed
    elif angle == 7:
        fleet.x += -0.65 * speed
        fleet.y += 0.325 * speed
    elif angle == 8:
        fleet.x += -0.9 * speed
        fleet.y += 0.2 * speed
    elif angle == 9:
        fleet.x += -1.025 * speed
        fleet.y += 0 * speed
    elif angle == 10:
        fleet.x += -0.9 * speed
        fleet.y += -0.2 * speed
    elif angle == 11:
        fleet.x += -0.65 * speed
        fleet.y += -0.325 * speed

def angle_to_radian(angle):
    if angle == 0:
        return 0
    elif angle == 1:
        return math.atan(6 / 3)
    elif angle == 2:
        return math.atan(9 / 2)
    elif angle == 3:
        return 0.5 * math.pi
    elif angle == 4:
        return math.pi - math.atan(9 / 2)
    elif angle == 5:
        return math.pi - math.atan(6 / 3)
    elif angle == 6:
        return math.pi
    elif angle == 7:
        return math.pi + math.atan(6 / 3)
    elif angle == 8:
        return math.pi + math.atan(9 / 2)
    elif angle == 9:
        return 1.5 * math.pi
    elif angle == 10:
        return 2 * math.pi - math.atan(9 / 2)
    elif angle == 11:
        return 2 * math.pi - math.atan(6 / 3)

def rotate_to_target(fleet, target_x, target_y):
    x1 = fleet.x
    y1 = fleet.y
    x2 = target_x
    y2 = target_y
    angle = fleet.angle

    gip = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if gip > 0:
        pi = math.pi
        if (x1 - x2 >= 0):
            i_angle = math.acos((y2 - y1) / gip)
        else:
            i_angle = 2 * pi - math.acos((y2 - y1) / gip)

        a = angle_to_radian(angle)
        dif = a - i_angle

        if (-pi < dif < 0) or (pi < dif < 2 * pi):
            fleet.move = False
            fleet.angle -= 1
            if fleet.angle < 0:
                fleet.angle = 11
            a = angle_to_radian(fleet.angle)
            dif = a - i_angle
            if (-2 * pi <= dif <= -pi) or (0 <= dif <= pi):
                fleet.move = True
                fleet.angle += 1
                if fleet.angle >= 12:
                    fleet.angle = 0
        elif (-2 * pi < dif < -pi) or (0 < dif < pi):
            fleet.move = False
            fleet.angle += 1
            if fleet.angle >= 12:
                fleet.angle = 0
            a = angle_to_radian(fleet.angle)
            dif = a - i_angle
            if (-pi <= dif <= 0) or (pi <= dif <= 2 * pi):
                fleet.move = True
                fleet.angle -= 1
                if fleet.angle < 0:
                    fleet.angle = 11
        else:
            fleet.move = False

def islands_check(x, y, t_x, t_y, r):
    for i in islands:
        ax = i[0] - 2.5 * r
        ay = i[1] - r
        dx = i[0] + i[2] * i_width + 2.5 * r
        dy = i[1] + i[3] * i_height + r
        if island_intersection(x, y, t_x, t_y, ax, ay, dx, dy):
            return False
    return True

def traders_generate(fraction):
    our_forposts = []
    for forpost in forposts:
        if forpost[5] == fraction:
            our_forposts.append(forpost)
    f = randint(0, len(our_forposts) - 1)
    x = our_forposts[f][0] + randint(0, i_width) - i_width
    y = our_forposts[f][1] + i_height / 2
    k = randint(0, len(forposts) - 1)
    gip = ((forposts[k][0] - i_width/2 + island_x - x) ** 2 + 6.25 * (forposts[k][1] + i_height/2 + island_y - y) ** 2) ** 0.5
    while gip <= i_width/2 or forposts[k][5] == 'PIRATE':
        k = randint(0, len(forposts) - 1)
        gip = ((forposts[k][0] - i_width/2 + island_x - x) ** 2 + 6.25 * (forposts[k][1] + i_height/2 + island_y - y) ** 2) ** 0.5
    target_x = forposts[k][0] - i_width/2
    target_y = forposts[k][1] + i_height/2
    if our_forposts[f][6] == 'sand':
        if our_forposts[f][2] == 1:
            fleets.append(fleet_object([["ladya", 20]], 1.2, island_x + x, island_y + y, target_x, target_y,
                                       0, 1, fraction, randint(ship_stats["ladya"].cost // 2, ship_stats["ladya"].cost), our_forposts[f][2] - 1))
            pink_count = randint(0, 1)
            for j in range(pink_count):
                fleets[len(fleets) - 1].ships.append(["pink", 15])
                fleets[len(fleets) - 1].gold += randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2)
        elif our_forposts[f][2] == 2:
            fleets.append(fleet_object([["fleyt", 40]], 1.6, island_x + x, island_y + y, target_x, target_y,
                                       0, 1, fraction, randint(ship_stats["fleyt"].cost // 2, ship_stats["fleyt"].cost), our_forposts[f][2] - 1))
            bark_count = randint(0, 1)
            for j in range(bark_count):
                fleets[len(fleets) - 1].ships.append(["bark", 35])
                fleets[len(fleets) - 1].gold += randint(ship_stats["bark"].cost // 4, ship_stats["bark"].cost // 2)
            shlup_count = randint(0, 1)
            for j in range(shlup_count):
                fleets[len(fleets) - 1].ships.append(["shlup", 35])
                fleets[len(fleets) - 1].gold += randint(ship_stats["shlup"].cost // 4, ship_stats["shlup"].cost // 2)
        elif our_forposts[f][2] == 3:
            fleets.append(fleet_object([["pinas", 60]], 2.0, island_x + x, island_y + y, target_x, target_y,
                                       0, 1, fraction, randint(ship_stats["pinas"].cost // 2, ship_stats["pinas"].cost), our_forposts[f][2] - 1))
            galera_count = randint(1, 2)
            for j in range(galera_count):
                fleets[len(fleets) - 1].ships.append(["galera", 50])
                fleets[len(fleets) - 1].gold += randint(ship_stats["galera"].cost // 4, ship_stats["galera"].cost // 2)
    elif our_forposts[f][6] == 'grass':
        if our_forposts[f][2] == 1:
            fleets.append(fleet_object([["ladya", 20], ["ladya", 20]], 1.2, island_x + x, island_y + y, target_x, target_y,
                                        0, 1, fraction, randint(ship_stats["ladya"].cost, ship_stats["ladya"].cost * 2), our_forposts[f][2] - 1))
            pink_count = randint(0, 1)
            for j in range(pink_count):
                fleets[len(fleets) - 1].ships.append(["pink", 15])
                fleets[len(fleets) - 1].gold += randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2)
            shuna_count = randint(0, 1)
            for j in range(shuna_count):
                fleets[len(fleets) - 1].ships.append(["shuna", 20])
                fleets[len(fleets) - 1].gold += randint(ship_stats["shuna"].cost // 4, ship_stats["shuna"].cost // 2)
        elif our_forposts[f][2] == 2:
            fleets.append(fleet_object([["fleyt", 40], ["fleyt", 40]], 1.6, island_x + x, island_y + y, target_x, target_y,
                                       0, 1, fraction, randint(ship_stats["fleyt"].cost, ship_stats["fleyt"].cost * 2), our_forposts[f][2] - 1))
            bark_count = randint(1, 2)
            for j in range(bark_count):
                fleets[len(fleets) - 1].ships.append(["bark", 35])
                fleets[len(fleets) - 1].gold += randint(ship_stats["bark"].cost // 4, ship_stats["bark"].cost // 2)
            shlup_count = randint(0, 1)
            for j in range(shlup_count):
                fleets[len(fleets) - 1].ships.append(["shlup", 35])
                fleets[len(fleets) - 1].gold += randint(ship_stats["shlup"].cost // 4, ship_stats["shlup"].cost // 2)
        elif our_forposts[f][2] == 3:
            fleets.append(fleet_object([["pinas", 60], ["pinas", 60]], 2.0, island_x + x, island_y + y, target_x, target_y,
                                       0, 1, fraction, randint(ship_stats["pinas"].cost, ship_stats["pinas"].cost * 2), our_forposts[f][2] - 1))
            galera_count = randint(1, 2)
            for j in range(galera_count):
                fleets[len(fleets) - 1].ships.append(["galera", 50])
                fleets[len(fleets) - 1].gold += randint(ship_stats["galera"].cost // 4, ship_stats["galera"].cost // 2)
            corvet_count = randint(0, 1)
            for j in range(corvet_count):
                fleets[len(fleets) - 1].ships.append(["corvet", 60])
                fleets[len(fleets) - 1].gold += randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2)
        elif our_forposts[f][2] == 4:
            fleets.append(fleet_object([["galeon", 90], ["galeon", 90]], 2.4, island_x + x, island_y + y, target_x, target_y,
                                       0, 1, fraction, randint(ship_stats["galeon"].cost, ship_stats["galeon"].cost * 2), our_forposts[f][2] - 1))
            fregat_count = randint(1, 2)
            for j in range(fregat_count):
                fleets[len(fleets) - 1].ships.append(["fregat", 75])
                fleets[len(fleets) - 1].gold += randint(ship_stats["fregat"].cost // 4, ship_stats["fregat"].cost // 2)
            warship_count = randint(0, 1)
            for j in range(warship_count):
                fleets[len(fleets) - 1].ships.append(["warship", 90])
                fleets[len(fleets) - 1].gold += randint(ship_stats["warship"].cost // 4, ship_stats["warship"].cost // 2)

def pirates_generate(fleet_rank):
    cross_player_and_forposts = True
    while cross_player_and_forposts:
        cross_player_and_forposts = False
        side = randint(1, 4)
        i = randint(0, len(islands) - 1)
        if side == 1:
            x = randint(islands[i][0] - i_width / 2, islands[i][0] + islands[i][2] * i_width + i_width / 2)
            y = islands[i][1] - i_height / 2
        elif side == 2:
            x = randint(islands[i][0] - i_width / 2, islands[i][0] + islands[i][2] * i_width + i_width / 2)
            y = islands[i][1] + islands[i][3] * i_height + i_height / 2
        elif side == 3:
            x = islands[i][0] - i_width / 2
            y = randint(islands[i][1] - i_height / 2, islands[i][1] + islands[i][3] * i_height + i_height / 2)
        elif side == 4:
            x = islands[i][0] + islands[i][2] * i_width + i_width / 2
            y = randint(islands[i][1] - i_height / 2, islands[i][1] + islands[i][3] * i_height + i_height / 2)
        if island_intersection(x + island_x, y + island_y, x + island_x, y + island_y,
                               -i_width * 4, -i_height * 4, i_width * 4, i_height * 4):
            cross_player_and_forposts = True
        for forpost in forposts:
            fx = forpost[0]
            fy = forpost[1]
            if island_intersection(x + island_x, y + island_y, x + island_x, y + island_y,
                                   island_x + fx - 2 * i_width, island_y + fy - i_height, island_x + fx + i_width, island_y + fy + 2 * i_height):
                cross_player_and_forposts = True
    if islands[i][4] == 'sand':
        if fleet_rank == 0:
            fleet_type = randint(0, 2)
            if fleet_type == 0:
                fleets.append(fleet_object([["barkas", 15]], 0.8, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["barkas"].cost // 4, ship_stats["barkas"].cost // 2), fleet_rank))
                barkas_count = randint(0, 1)
                for j in range(barkas_count):
                    fleets[len(fleets) - 1].ships.append(["barkas", 15])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["barkas"].cost // 4, ship_stats["barkas"].cost // 2)
            elif fleet_type == 1:
                fleets.append(fleet_object([["pink", 15]], 1.2, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2), fleet_rank))
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2)
            elif fleet_type == 2:
                fleets.append(fleet_object([["shuna", 20]], 1.6, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["shuna"].cost // 4, ship_stats["shuna"].cost // 2), fleet_rank))
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2)
                    fleets[len(fleets) - 1].speed = 1.2
        elif fleet_rank == 1:
            fleet_type = randint(0, 1)
            if fleet_type == 0:
                fleets.append(fleet_object([["shlup", 30]], 1.6, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["shlup"].cost // 4, ship_stats["shlup"].cost // 2), fleet_rank))
                shlup_count = randint(1, 2)
                for j in range(shlup_count):
                    fleets[len(fleets) - 1].ships.append(["shlup", 35])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["shlup"].cost // 4, ship_stats["shlup"].cost // 2)
            elif fleet_type == 1:
                fleets.append(fleet_object([["bark", 35], ["bark", 35]], 2.0, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["bark"].cost // 4, ship_stats["bark"].cost // 2), fleet_rank))
                shlup_count = randint(0, 1)
                for j in range(shlup_count):
                    fleets[len(fleets) - 1].ships.append(["shlup", 30])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["shlup"].cost // 4, ship_stats["shlup"].cost // 2)
                    fleets[len(fleets) - 1].speed = 1.6
        elif fleet_rank == 2:
            fleet_type = randint(0, 1)
            if fleet_type == 0:
                fleets.append(fleet_object([["galera", 50]], 2.0, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["galera"].cost // 4, ship_stats["galera"].cost // 2), fleet_rank))
                galera_count = randint(0, 1)
                for j in range(galera_count):
                    fleets[len(fleets) - 1].ships.append(["galera", 50])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["galera"].cost // 4, ship_stats["galera"].cost // 2)
                brig_count = randint(0, 1)
                for j in range(brig_count):
                    fleets[len(fleets) - 1].ships.append(["brig", 40])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["brig"].cost // 4, ship_stats["brig"].cost // 2)
            if fleet_type == 1:
                fleets.append(fleet_object([["corvet", 60]], 2.4, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2), fleet_rank))
                corvet_count = randint(0, 1)
                for j in range(corvet_count):
                    fleets[len(fleets) - 1].ships.append(["corvet", 60])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2)
                galera_count = randint(0, 1)
                for j in range(galera_count):
                    fleets[len(fleets) - 1].ships.append(["galera", 50])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["galera"].cost // 4, ship_stats["galera"].cost // 2)
                    fleets[len(fleets) - 1].speed = 2.0
        elif fleet_rank == 3:
            fleets.append(fleet_object([["fregat", 75]], 2.4, island_x + x, island_y + y, x, y,
                                       0, 2, '-', randint(ship_stats["fregat"].cost // 4, ship_stats["fregat"].cost // 2), fleet_rank))
            fregat_count = randint(0, 1)
            for j in range(fregat_count):
                fleets[len(fleets) - 1].ships.append(["fregat", 75])
                fleets[len(fleets) - 1].gold += randint(ship_stats["fregat"].cost // 4, ship_stats["fregat"].cost // 2)
            corvet_count = randint(0, 1)
            for j in range(corvet_count):
                fleets[len(fleets) - 1].ships.append(["corvet", 60])
                fleets[len(fleets) - 1].gold += randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2)
    elif islands[i][4] == 'grass' or islands[i][4] == 'snow':
        if fleet_rank == 0:
            fleet_type = randint(0, 2)
            if fleet_type == 0:
                fleets.append(fleet_object([["pink", 15]], 0.8, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2), fleet_rank))
                barkas_count = randint(1, 2)
                for j in range(barkas_count):
                    fleets[len(fleets) - 1].ships.append(["barkas", 15])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["barkas"].cost // 4,ship_stats["barkas"].cost // 2)
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2)
            elif fleet_type == 1:
                fleets.append(fleet_object([["shuna", 20]], 1.2, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["shuna"].cost // 4, ship_stats["shuna"].cost // 2), fleet_rank))
                shuna_count = randint(0, 1)
                for j in range(shuna_count):
                    fleets[len(fleets) - 1].ships.append(["shuna", 20])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["shuna"].cost // 4, ship_stats["shuna"].cost // 2)
                pink_count = randint(1, 2)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2)
            elif fleet_type == 2:
                fleets.append(fleet_object([["lugger", 25]], 1.6, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["lugger"].cost // 4, ship_stats["lugger"].cost // 2), fleet_rank))
                shuna_count = randint(1, 2)
                for j in range(shuna_count):
                    fleets[len(fleets) - 1].ships.append(["shuna", 20])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["shuna"].cost // 4, ship_stats["shuna"].cost // 2)
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2)
                    fleets[len(fleets) - 1].speed = 1.2
        elif fleet_rank == 1:
            fleet_type = randint(0, 1)
            if fleet_type == 0:
                fleets.append(fleet_object([["bark", 35]], 1.6, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["bark"].cost // 4, ship_stats["bark"].cost // 2), fleet_rank))
                shlup_count = randint(2, 3)
                for j in range(shlup_count):
                    fleets[len(fleets) - 1].ships.append(["shlup", 30])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["shlup"].cost // 4, ship_stats["shlup"].cost // 2)
                bark_count = randint(0, 1)
                for j in range(bark_count):
                    fleets[len(fleets) - 1].ships.append(["bark", 35])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["bark"].cost // 4, ship_stats["bark"].cost // 2)
            elif fleet_type == 1:
                fleets.append(fleet_object([["brig", 40]], 2.0, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["brig"].cost // 4, ship_stats["brig"].cost // 2), fleet_rank))
                brig_count = randint(0, 1)
                for j in range(brig_count):
                    fleets[len(fleets) - 1].ships.append(["brig", 40])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["brig"].cost // 4, ship_stats["brig"].cost // 2)
                bark_count = randint(1, 2)
                for j in range(bark_count):
                    fleets[len(fleets) - 1].ships.append(["bark", 35])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["bark"].cost // 4, ship_stats["bark"].cost // 2)
                shlup_count = randint(0, 1)
                for j in range(shlup_count):
                    fleets[len(fleets) - 1].ships.append(["shlup", 30])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["shlup"].cost // 4, ship_stats["shlup"].cost // 2)
                    fleets[len(fleets) - 1].speed = 1.6
        elif fleet_rank == 2:
            fleet_type = randint(0, 1)
            if fleet_type == 0:
                fleets.append(fleet_object([["galera", 50]], 2.0, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["galera"].cost // 4, ship_stats["galera"].cost // 2), fleet_rank))
                galera_count = randint(1, 2)
                for j in range(galera_count):
                    fleets[len(fleets) - 1].ships.append(["galera", 50])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["galera"].cost // 4, ship_stats["galera"].cost // 2)
                brig_count = randint(1, 2)
                for j in range(brig_count):
                    fleets[len(fleets) - 1].ships.append(["brig", 40])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["brig"].cost // 4, ship_stats["brig"].cost // 2)
            elif fleet_type == 1:
                fleets.append(fleet_object([["corvet", 60]], 2.0, island_x + x, island_y + y, x, y,
                                           0, 2, '-', randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2), fleet_rank))
                galera_count = randint(2, 3)
                for j in range(galera_count):
                    fleets[len(fleets) - 1].ships.append(["galera", 50])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["galera"].cost // 4, ship_stats["galera"].cost // 2)
                corvet_count = randint(0, 1)
                for j in range(corvet_count):
                    fleets[len(fleets) - 1].ships.append(["corvet", 60])
                    fleets[len(fleets) - 1].gold += randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2)
        elif fleet_rank == 3:
            fleets.append(fleet_object([["fregat", 75]], 2.4, island_x + x, island_y + y, x, y,
                                       0, 2, '-', randint(ship_stats["fregat"].cost // 4, ship_stats["fregat"].cost // 2), fleet_rank))
            fregat_count = randint(1, 2)
            for j in range(fregat_count):
                fleets[len(fleets) - 1].ships.append(["fregat", 75])
                fleets[len(fleets) - 1].gold += randint(ship_stats["fregat"].cost // 4, ship_stats["fregat"].cost // 2)
            corvet_count = randint(1, 2)
            for j in range(corvet_count):
                fleets[len(fleets) - 1].ships.append(["corvet", 60])
                fleets[len(fleets) - 1].gold += randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2)

def war_fleet_generate(fraction):
    towns = []
    for forpost in forposts:
        if forpost[5] == fraction:
            towns.append(forpost)
    f = randint(0, len(towns) - 1)
    cross_player = True
    while cross_player:
        cross_player = False
        side = randint(1, 3)
        if side == 1:
            x = towns[f][0] - i_width * 1.5
            y = towns[f][1] + randint(0.5 * i_height, i_height * 1.5)
        elif side == 2:
            x = towns[f][0] + randint(0, 2 * i_width) - i_width * 1.5
            y = towns[f][1] + i_height * 1.5
        elif side == 3:
            x = towns[f][0] + i_width * 0.5
            y = towns[f][1] + randint(0.5 * i_height, i_height * 1.5)
        if island_intersection(x + island_x, y + island_y, x + island_x, y + island_y,
                               -i_width + 1, -i_height + 1, i_width / 2 - 1, i_height / 2 - 1) and fraction != 'PLAYER':
            cross_player = True
    if towns[f][2] == 1:
        fleets.append(fleet_object([["lugger", 25]], 1.6, island_x + x, island_y + y, x, y,
                                   0, 3, fraction, randint(ship_stats["lugger"].cost // 4, ship_stats["lugger"].cost // 2), towns[f][2] - 1))
        lugger_count = randint(1, 3)
        for j in range(lugger_count):
            fleets[len(fleets) - 1].ships.append(["lugger", 25])
            fleets[len(fleets) - 1].gold += randint(ship_stats["lugger"].cost // 4, ship_stats["lugger"].cost // 2)
    elif towns[f][2] == 2:
        fleets.append(fleet_object([["brig", 40]], 2.0, island_x + x, island_y + y, x, y,
                                   0, 3, fraction, randint(ship_stats["brig"].cost // 4, ship_stats["brig"].cost // 2), towns[f][2] - 1))
        brig_count = randint(2, 4)
        for j in range(brig_count):
            fleets[len(fleets) - 1].ships.append(["brig", 40])
            fleets[len(fleets) - 1].gold += randint(ship_stats["brig"].cost // 4, ship_stats["brig"].cost // 2)
    elif towns[f][2] == 3:
        fleets.append(fleet_object([["corvet", 60]], 2.4, island_x + x, island_y + y, x, y,
                                   0, 3, fraction, randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2), towns[f][2] - 1))
        corvet_count = randint(2, 4)
        for j in range(corvet_count):
            fleets[len(fleets) - 1].ships.append(["corvet", 60])
            fleets[len(fleets) - 1].gold += randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2)
    elif towns[f][2] == 4:
        fleets.append(fleet_object([["warship", 90]], 2.8, island_x + x, island_y + y, x, y,
                                   0, 3, fraction, randint(ship_stats["warship"].cost // 4, ship_stats["warship"].cost // 2), towns[f][2] - 1))
        warship_count = randint(2, 4)
        for j in range(warship_count):
            fleets[len(fleets) - 1].ships.append(["warship", 90])
            fleets[len(fleets) - 1].gold += randint(ship_stats["warship"].cost // 4, ship_stats["warship"].cost // 2)

def fishers_generate(fraction):
    camps = []
    for forpost in forposts:
        if forpost[5] == fraction:
            camps.append(forpost)
    f = randint(0, len(camps) - 1)
    x = camps[f][0] - i_width/2
    y = camps[f][1] + i_height/2
    if camps[f][2] == 1:
        fleets.append(fleet_object([["barkas", 15]], 0.8, island_x + x, island_y + y, x, y,
                                   0, 4, fraction, 0, camps[f][2] - 1))
        barkas_count = randint(0, 1)
        for j in range(barkas_count):
            fleets[len(fleets) - 1].ships.append(["barkas", 15])
            fleets[len(fleets) - 1].gold += 0
    elif camps[f][2] == 2:
        fleets.append(fleet_object([["shlup", 30]], 1.6, island_x + x, island_y + y, x, y,
                                   0, 4, fraction, 0, camps[f][2] - 1))
        shlup_count = randint(1, 2)
        for j in range(shlup_count):
            fleets[len(fleets) - 1].ships.append(["shlup", 30])
            fleets[len(fleets) - 1].gold += 0
    elif camps[f][2] == 3:
        fleets.append(fleet_object([["galera", 50]], 2.0, island_x + x, island_y + y, x, y,
                                   0, 4, fraction, 0, camps[f][2] - 1))
        galera_count = randint(0, 1)
        for j in range(galera_count):
            fleets[len(fleets) - 1].ships.append(["galera", 50])
            fleets[len(fleets) - 1].gold += 0
    elif camps[f][2] == 4:
        fleets.append(fleet_object([["galera", 50]], 2.0, island_x + x, island_y + y, x, y,
                                   0, 4, fraction, 0, camps[f][2] - 1))
        galera_count = randint(1, 2)
        for j in range(galera_count):
            fleets[len(fleets) - 1].ships.append(["galera", 50])
            fleets[len(fleets) - 1].gold += 0

def mercenaries_generate(fraction):
    pirate_bases = []
    for forpost in forposts:
        if forpost[5] == 'PIRATE':
            pirate_bases.append(forpost)
    f = randint(0, len(pirate_bases) - 1)
    cross_player = True
    while cross_player:
        cross_player = False
        side = randint(1, 3)
        if side == 1:
            x = pirate_bases[f][0] - i_width * 1.5
            y = pirate_bases[f][1] + randint(0.5 * i_height, i_height * 1.5)
        elif side == 2:
            x = pirate_bases[f][0] + randint(0, 2 * i_width) - i_width * 1.5
            y = pirate_bases[f][1] + i_height * 1.5
        elif side == 3:
            x = pirate_bases[f][0] + i_width * 0.5
            y = pirate_bases[f][1] + randint(0.5 * i_height, i_height * 1.5)
        if island_intersection(x + island_x, y + island_y, x + island_x, y + island_y,
                               -i_width + 1, -i_height + 1, i_width / 2 - 1, i_height / 2 - 1):
            cross_player = True
    if pirate_bases[f][2] == 1:
        fleets.append(fleet_object([["lugger", 25]], 1.6, island_x + x, island_y + y, x, y, 0, 5, fraction,
                                   randint(ship_stats["lugger"].cost // 4, ship_stats["lugger"].cost // 2), pirate_bases[f][2] - 1))
        shuna_count = randint(1, 2)
        for j in range(shuna_count):
            fleets[len(fleets) - 1].ships.append(["shuna", 20])
            fleets[len(fleets) - 1].gold += randint(ship_stats["shuna"].cost // 4, ship_stats["shuna"].cost // 2)
        pink_count = randint(0, 1)
        for j in range(pink_count):
            fleets[len(fleets) - 1].ships.append(["pink", 15])
            fleets[len(fleets) - 1].gold += randint(ship_stats["pink"].cost // 4, ship_stats["pink"].cost // 2)
            fleets[len(fleets) - 1].speed = 1.2
    elif pirate_bases[f][2] == 2:
        fleets.append(fleet_object([["brig", 40]], 2.0, island_x + x, island_y + y, x, y, 0, 5, fraction,
                                   randint(ship_stats["brig"].cost // 4, ship_stats["brig"].cost // 2), pirate_bases[f][2] - 1))
        brig_count = randint(0, 1)
        for j in range(brig_count):
            fleets[len(fleets) - 1].ships.append(["brig", 40])
            fleets[len(fleets) - 1].gold += randint(ship_stats["brig"].cost // 4, ship_stats["brig"].cost // 2)
        bark_count = randint(1, 2)
        for j in range(bark_count):
            fleets[len(fleets) - 1].ships.append(["bark", 35])
            fleets[len(fleets) - 1].gold += randint(ship_stats["bark"].cost // 4, ship_stats["bark"].cost // 2)
        shlup_count = randint(0, 1)
        for j in range(shlup_count):
            fleets[len(fleets) - 1].ships.append(["shlup", 30])
            fleets[len(fleets) - 1].gold += randint(ship_stats["shlup"].cost // 4, ship_stats["shlup"].cost // 2)
            fleets[len(fleets) - 1].speed = 1.2
    elif pirate_bases[f][2] == 3:
        fleets.append(fleet_object([["corvet", 60]], 2.0, island_x + x, island_y + y, x, y, 0, 5, fraction,
                                    randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2), pirate_bases[f][2] - 1))
        galera_count = randint(2, 3)
        for j in range(galera_count):
            fleets[len(fleets) - 1].ships.append(["galera", 50])
            fleets[len(fleets) - 1].gold += 0
        corvet_count = randint(0, 1)
        for j in range(corvet_count):
            fleets[len(fleets) - 1].ships.append(["corvet", 60])
            fleets[len(fleets) - 1].gold += randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2)
    elif pirate_bases[f][2] == 4:
        fleets.append(fleet_object([["fregat", 75]], 2.4, island_x + x, island_y + y, x, y, 0, 5, fraction,
                                   randint(ship_stats["fregat"].cost // 4, ship_stats["fregat"].cost // 2), pirate_bases[f][2] - 1))
        fregat_count = randint(1, 2)
        for j in range(fregat_count):
            fleets[len(fleets) - 1].ships.append(["fregat", 75])
            fleets[len(fleets) - 1].gold += randint(ship_stats["fregat"].cost // 4, ship_stats["fregat"].cost // 2)
        corvet_count = randint(1, 2)
        for j in range(corvet_count):
            fleets[len(fleets) - 1].ships.append(["corvet", 60])
            fleets[len(fleets) - 1].gold += randint(ship_stats["corvet"].cost // 4, ship_stats["corvet"].cost // 2)

def battle_with_player(fleet):
    fleets[0].ships = game_display.battle(fleets[0].ships, fleet.ships, fleet.type, fleet.fraction)
    if len(fleets[0].ships) > 0:
        max_gold = 0
        for ship in fleets[0].ships:
            if ship[0] in ['ladya', 'fleyt', 'pinas', 'galeon']:
                max_gold += 2 * ship_stats[ship[0]].cost
            else:
                max_gold += ship_stats[ship[0]].cost
        fleets[0].gold += fleet.gold
        if fleets[0].gold > max_gold:
            fleets[0].gold = max_gold
        new_fleet_generate(fleet)
        fleets.remove(fleet)
        fleets[0].speed = 2.8
        for ship in fleets[0].ships:
            if ship_stats[ship[0]].speed < fleets[0].speed:
                fleets[0].speed = ship_stats[ship[0]].speed
    else:
        quit()

def auto_battle_step(fleet, other_fleet):
    while (len(other_fleet.ships) > 0) and (len(fleet.ships) > 0):
        r1 = randint(0, len(fleet.ships) - 1)
        r2 = randint(0, len(other_fleet.ships) - 1)
        rt1 = randint(0, len(fleet.ships) - 1)
        rt2 = randint(0, len(other_fleet.ships) - 1)
        fleet.ships[rt1][1] -= randint(ship_stats[other_fleet.ships[r2][0]].gun_count - 2, ship_stats[other_fleet.ships[r2][0]].gun_count)
        other_fleet.ships[rt2][1] -= randint(ship_stats[fleet.ships[r1][0]].gun_count - 2, ship_stats[fleet.ships[r1][0]].gun_count)
        if fleet.ships[rt1][1] <= 0:
            fleet.ships.remove(fleet.ships[rt1])
            fleet.speed = 2.8
            for ship in fleet.ships:
                if ship_stats[ship[0]].speed < fleet.speed:
                    fleet.speed = ship_stats[ship[0]].speed
        if other_fleet.ships[rt2][1] <= 0:
            other_fleet.ships.remove(other_fleet.ships[rt2])
            other_fleet.speed = 2.8
            for ship in other_fleet.ships:
                if ship_stats[ship[0]].speed < other_fleet.speed:
                    other_fleet.speed = ship_stats[ship[0]].speed
    if (len(other_fleet.ships) > 0) and (len(fleet.ships) == 0):
        sum = 0
        for ship in other_fleet.ships:
            sum += ship_stats[ship[0]].cost
        other_fleet.gold += fleet.gold
        if other_fleet.gold > sum:
            other_fleet.gold = sum
        new_fleet_generate(fleet)
        fleets.remove(fleet)
    elif (len(other_fleet.ships) == 0) and (len(fleet.ships) > 0):
        sum = 0
        for ship in fleet.ships:
            sum += ship_stats[ship[0]].cost
        fleet.gold += other_fleet.gold
        if fleet.gold > sum:
            fleet.gold = sum
        new_fleet_generate(other_fleet)
        fleets.remove(other_fleet)
    elif (len(fleet.ships) == 0) and (len(other_fleet.ships) == 0):
        new_fleet_generate(fleet)
        new_fleet_generate(other_fleet)
        fleets.remove(fleet)
        fleets.remove(other_fleet)

def new_fleet_generate(fleet):
    r = randint(0, min(game_time // 6, 6000))
    if game_time // 6 >= 2400 and r < 1200:
        r = 1200
    if game_time // 6 >= 4200 and r < 2400:
        r = 2400
    if r < 1200:
        rank = 0
    elif 1200 <= r < 2400:
        rank = 1
    elif 2400 <= r < 4200:
        rank = 2
    else:
        rank = 3
    if fleet.type == 1:
        traders_generate(fleet.fraction)
        if not(fraction_wars[fleet.fraction]['RED'] or fraction_wars[fleet.fraction]['GREEN']
               or fraction_wars[fleet.fraction]['BLUE'] or fraction_wars[fleet.fraction]['PLAYER']):
            mingip = -1
            b_f_num = -1
            for b_f in range(len(fleets) - 1):
                if fleets[b_f].type == 3 and fleet.fraction == fleets[b_f].fraction:
                    if mingip == -1:
                        mingip = ((fleet.x - fleets[b_f].x) ** 2 + (fleet.y - fleets[b_f].y) ** 2) ** 0.5
                        b_f_num = b_f
                    else:
                        gip = ((fleet.x - fleets[b_f].x) ** 2 + (fleet.y - fleets[b_f].y) ** 2) ** 0.5
                        if gip < mingip:
                            mingip = gip
                            b_f_num = b_f
            fleets[b_f_num].target_x = -island_x + fleet.x
            fleets[b_f_num].target_y = -island_y + fleet.y
    elif fleet.type == 2:
        pirates_generate(rank)
    elif fleet.type == 3:
        fraction_war_fleet_count[fleet.fraction] -= 1
        fwfc = copy.copy(fraction_war_fleet_count)
        for forpost in forposts:
            if forpost[5] != 'PIRATE':
                fwfc[forpost[5]] -= 1
        generate_fraction = []
        if fwfc['RED'] < 0:
            generate_fraction.append('RED')
        elif fwfc['GREEN'] < 0:
            generate_fraction.append('GREEN')
        elif fwfc['BLUE'] < 0:
            generate_fraction.append('BLUE')
        elif fwfc['PLAYER'] < 0:
            generate_fraction.append('PLAYER')
        if len(generate_fraction) == 1:
            fg = 0
        else:
            fg = randint(0, len(generate_fraction) - 1)
        war_fleet_generate(generate_fraction[fg])
        fraction_war_fleet_count[generate_fraction[fg]] += 1
    elif fleet.type == 4:
        fishers_generate(fleet.fraction)
        mingip = -1
        b_f_num = -1
        for b_f in range(len(fleets) - 1):
            if fleets[b_f].type == 3 and fleet.fraction == fleets[b_f].fraction:
                if mingip == -1:
                    mingip = ((fleet.x - fleets[b_f].x) ** 2 + (fleet.y - fleets[b_f].y) ** 2) ** 0.5
                    b_f_num = b_f
                else:
                    gip = ((fleet.x - fleets[b_f].x) ** 2 + (fleet.y - fleets[b_f].y) ** 2) ** 0.5
                    if gip < mingip:
                        mingip = gip
                        b_f_num = b_f
        fleets[b_f_num].target_x = -island_x + fleet.x
        fleets[b_f_num].target_y = -island_y + fleet.y
    elif fleet.type == 5:
        fwfc = copy.copy(fraction_war_fleet_count)
        fwfc.pop('PLAYER')
        mercenaries_generate(min(fwfc, key=fwfc.get))

#################################################game_generating########################################################

def run_game():
    global scale, game, game_time, speed_mode, player_fraction, player_trade_forpost
    global island_x, island_y
    forpost_zone = False
    menu = 0
    stop = 0

    text = 0
    need_island = True
    while need_island:
        need_island = island_generate(1, 'PIRATE', 'snow')
    if not (need_island):
        f = pygame.font.Font(None, 36)
        coord = f.render('generate (PIRATE) fraction island; (snow) biom', True, (153, 217, 234))
        display.blit(coord, (10, 10 + text))
        text += 36
        pygame.display.update()

    k = 0
    land = 'snow'
    while k < 500:
        need_island = True
        k = 0
        forp = randint(0, 1)
        if forp == 0:
            forpost = 1
            fraction = 'PIRATE'
        else:
            forpost = 0
            fraction = '-'
        while need_island and k < 500:
            need_island = island_generate(forpost, fraction, 'snow')
            k += 1
        if not (need_island):
            f = pygame.font.Font(None, 36)
            coord = f.render('generate (' + fraction + ') fraction island; (' + land + ') biom', True, (153, 217, 234))
            display.blit(coord, (10, 10 + text))
            text += 36
            pygame.display.update()

    for forp in range(1):
        f = randint(0, 2)
        if f == 0:
            fraction = 'RED'
        elif f == 1:
            fraction = 'GREEN'
        elif f == 2:
            fraction = 'BLUE'
        land = 'grass'
        color = (181, 230, 29)
        need_island = True
        while need_island:
            need_island = island_generate(1, fraction, land)
        if not (need_island):
            f = pygame.font.Font(None, 36)
            coord = f.render('generate (' + fraction + ') fraction island; (' + land + ') biom', True, color)
            display.blit(coord, (10, 10 + text))
            text += 36
            pygame.display.update()

    k = 0
    land = 'sand'
    while k < 500 or land == 'grass':
        need_island = True
        k = 0
        forp = randint(0, 1)
        f = randint(0, 2)
        if forp == 0:
            forpost = 1
            if f == 0:
                fraction = 'RED'
            elif f == 1:
                fraction = 'GREEN'
            elif f == 2:
                fraction = 'BLUE'
        else:
            forpost = 0
            fraction = '-'
        l = randint(0, 2)
        if l == 0:
            land = 'grass'
            color = (181, 230, 29)
        else:
            land = 'sand'
            color = (255, 242, 0)
        while need_island and k < 500:
            need_island = island_generate(forpost, fraction, land)
            k += 1
        if not(need_island):
            f = pygame.font.Font(None, 36)
            coord = f.render('generate (' + fraction + ') fraction island; (' + land + ') biom', True, color)
            display.blit(coord, (10, 10 + text))
            text += 36
            pygame.display.update()

    fleets.append(fleet_object([["lugger", 25], ["lugger", 25], ["lugger", 25]], 1.6, 0, 0, 0, 0, 0, 0,
                               'PLAYER', randint(ship_stats["lugger"].cost * 3 // 4, ship_stats["lugger"].cost * 3 // 2), 0))
    # fleets.append(fleet_object([["ladya", 20]], 1.2, 0, 0, 0, 0, 0, 0, 'PLAYER',
    #                            randint(ship_stats["ladya"].cost // 2, ship_stats["ladya"].cost), 0))
    fleets[0].move = False

    # fleets[0].ships = game_display.battle(fleets[0].ships,
    #                                       [["warship", 90], ["warship", 90], ["warship", 90], ["warship", 90], ["warship", 90]], 5, 'RED')

    for forpost in forposts:
        if forpost[5] != 'PIRATE':
            traders_generate(forpost[5])
            war_fleet_generate(forpost[5])
            fishers_generate(forpost[5])
            fraction_war_fleet_count[forpost[5]] += 1
        pirates_generate(0)
    for forpost in forposts:
        if forpost[5] == 'PIRATE':
            fwfc = copy.copy(fraction_war_fleet_count)
            fwfc.pop('PLAYER')
            mercenaries_generate(min(fwfc, key=fwfc.get))
    for island in islands:
        pirates_generate(0)

    for i in range(448):
        waves.append([randint(int(island_x - 2 * display_width), int(island_x + 2 * display_width)),
                      randint(int(island_y - 2 * display_height), int(island_y + 2 * display_height)), i // 32])

#####################################################map_sprites########################################################

    sand_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1ne.png').convert_alpha(),
                                            ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nse.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nsw.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nswe.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nw.png').convert_alpha(),
                                            ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nwe.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1se.png').convert_alpha(),
                                            ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1sw.png').convert_alpha(),
                                            ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1swe.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))

    grass_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1ne.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nse.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nsw.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nswe.png').convert_alpha(),
                                               ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nw.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nwe.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1se.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1sw.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1swe.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))

    snow_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1ne.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nse.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nsw.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nswe.png').convert_alpha(),
                                               ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nw.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nwe.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1se.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1sw.png').convert_alpha(),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1swe.png').convert_alpha(),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))

    image_forpost1 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost1.png').convert_alpha(),
                                                  ((i_width + 16) / scale, (i_height + 184) / scale))
    image_forpost2 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost2.png').convert_alpha(),
                                                  ((i_width + 16) / scale, (i_height + 184) / scale))
    image_forpost3 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost3.png').convert_alpha(),
                                                  ((i_width + 16) / scale, (i_height + 204) / scale))
    image_forpost4 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost4.png').convert_alpha(),
                                                  ((i_width + 16) / scale, (i_height + 264) / scale))
    image_forpost_zone = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost_zone.png').convert_alpha(),
                                                      ((i_width + 16) / scale, (i_height + 184) / scale))

    image_palm = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\palm.png').convert_alpha(),
                                              (128 / scale, 256 / scale))
    image_tree = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\tree.png').convert_alpha(),
                                              (144 / scale, 376 / scale))
    image_ship_tree = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\ship_tree.png').convert_alpha(),
                                              (96 / scale, 576 / scale))

##################################################minimap_sprites#######################################################

    m_sand_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1ne.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_sand_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nse.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_sand_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nsw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_sand_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nswe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_sand_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_sand_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nwe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_sand_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1se.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_sand_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1sw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_sand_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1swe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))

    m_grass_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1ne.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_grass_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nse.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_grass_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nsw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_grass_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nswe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_grass_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_grass_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nwe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_grass_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1se.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_grass_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1sw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_grass_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1swe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))

    m_snow_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1ne.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_snow_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nse.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_snow_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nsw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_snow_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nswe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_snow_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_snow_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nwe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_snow_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1se.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_snow_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1sw.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_snow_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1swe.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))

    m_image_forpost1 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost1.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_image_forpost2 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost2.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 184) / 17))
    m_image_forpost3 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost3.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 204) / 17))
    m_image_forpost4 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost4.png').convert_alpha(),
                                              ((i_width + 16) / 17, (i_height + 264) / 17))

#####################################################start_timer########################################################

    while game:
        sum = 0
        t0 = time.clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((0, 162, 232))

        for i in range(32):
            waves.append([randint(int(-island_x - 2 * display_width), int(-island_x + 2 * display_width)),
                          randint(int(-island_y - 2 * display_height), int(-island_y + 2 * display_height)), 0])

        keys = pygame.key.get_pressed()
        if not(forpost_zone):
            if keys[pygame.K_w]:
                fleets[0].move = True
            elif keys[pygame.K_s]:
                fleets[0].move = False
            if keys[pygame.K_d]:
                fleets[0].angle += 1
                if fleets[0].angle >= 12:
                    fleets[0].angle = 0
            elif keys[pygame.K_a]:
                fleets[0].angle -= 1
                if fleets[0].angle < 0:
                    fleets[0].angle = 11
            if keys[pygame.K_2]:
                if (len(fleets[0].ships) >= 2) and (stop == 0):
                    stop = 10
                    fleets[0].ships[0], fleets[0].ships[1] = fleets[0].ships[1], fleets[0].ships[0]
            elif keys[pygame.K_3]:
                if (len(fleets[0].ships) >= 3) and (stop == 0):
                    stop = 10
                    fleets[0].ships[0], fleets[0].ships[2] = fleets[0].ships[2], fleets[0].ships[0]
            elif keys[pygame.K_4]:
                if (len(fleets[0].ships) >= 4) and (stop == 0):
                    stop = 10
                    fleets[0].ships[0], fleets[0].ships[3] = fleets[0].ships[3], fleets[0].ships[0]
            elif keys[pygame.K_5]:
                if (len(fleets[0].ships) >= 5) and (stop == 0):
                    stop = 10
                    fleets[0].ships[0], fleets[0].ships[4] = fleets[0].ships[4], fleets[0].ships[0]
        if keys[pygame.K_ESCAPE]:
            quit()

        sum += time.clock() - t0
        print("start ", time.clock() - t0)
        t0 = time.clock()

########################################################movement########################################################


        for fleet in fleets:
            if fleet != fleets[0]:
                fx = fleet.x - island_x
                fy = fleet.y - island_y
                gip = 99999
                target_x = 99999
                target_y = 99999
                for i in islands:
                    ax = i[0]
                    ay = i[1]
                    dx = i[0] + i[2] * i_width
                    dy = i[1] + i[3] * i_height
                    r_x = 25
                    r_y = r_x / 2.5
                    if island_intersection(fx, fy, fleet.target_x, fleet.target_y, ax - r_x, ay - r_y, dx + r_x, dy + r_y):
                        ax -= ship_stats[fleet.ships[0][0]].deck_size / 2
                        ay -= ship_stats[fleet.ships[0][0]].deck_size / 5
                        dx += ship_stats[fleet.ships[0][0]].deck_size / 2
                        dy += ship_stats[fleet.ships[0][0]].deck_size / 5
                        if islands_check(fx, fy, ax, ay, r_y):
                            if ((ax - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5 < gip:
                                gip = ((ax - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5
                                target_x = ax
                                target_y = ay
                        if islands_check(fx, fy, ax, dy, r_y):
                            if ((ax - fleet.target_x) ** 2 + (dy - fleet.target_y) ** 2) ** 0.5 < gip:
                                gip = ((ax - fleet.target_x) ** 2 + (dy - fleet.target_y) ** 2) ** 0.5
                                target_x = ax
                                target_y = dy
                        if islands_check(fx, fy, dx, ay, r_y):
                            if ((dx - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5 < gip:
                                gip = ((dx - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5
                                target_x = dx
                                target_y = ay
                        if islands_check(fx, fy, dx, dy, r_y):
                            if ((dx - fleet.target_x) ** 2 + (dy - fleet.target_y) ** 2) ** 0.5 < gip:
                                gip = ((dx - fleet.target_x) ** 2 + (dy - fleet.target_y) ** 2) ** 0.5
                                target_x = dx
                                target_y = dy
                if target_x != 99999:
                    rotate_to_target(fleet, island_x + target_x, island_y + target_y)
                else:
                    rotate_to_target(fleet, island_x + fleet.target_x, island_y + fleet.target_y)

        for fleet in fleets:
            if fleet.move == True:
                if fleet == fleets[0]:
                    fleet_move(fleet, fleet.angle, fleet.speed * speed_mode)
                    deck_size = 0
                    for ship in fleets[0].ships:
                        deck_size = ship_stats[ship[0]].deck_size / 2.5
                    if islands_check(fleet.x - island_x, fleet.y - island_y, fleet.x - island_x, fleet.y - island_y, deck_size / 2.5):
                        if fleet.angle == 6:
                            island_x += 0 * fleet.speed * speed_mode
                            island_y += -0.41 * fleet.speed * speed_mode
                        elif fleet.angle == 7:
                            island_x += 0.64 * fleet.speed * speed_mode
                            island_y += -0.32 * fleet.speed * speed_mode
                        elif fleet.angle == 8:
                            island_x += 0.9 * fleet.speed * speed_mode
                            island_y += -0.2 * fleet.speed * speed_mode
                        elif fleet.angle == 9:
                            island_x += 1.025 * fleet.speed * speed_mode
                            island_y += 0 * fleet.speed * speed_mode
                        elif fleet.angle == 10:
                            island_x += 0.9 * fleet.speed * speed_mode
                            island_y += 0.2 * fleet.speed * speed_mode
                        elif fleet.angle == 11:
                            island_x += 0.64 * fleet.speed * speed_mode
                            island_y += 0.32 * fleet.speed * speed_mode
                        elif fleet.angle == 0:
                            island_x += 0 * fleet.speed * speed_mode
                            island_y += 0.41 * fleet.speed * speed_mode
                        elif fleet.angle == 1:
                            island_x += -0.64 * fleet.speed * speed_mode
                            island_y += 0.32 * fleet.speed * speed_mode
                        elif fleet.angle == 2:
                            island_x += -0.9 * fleet.speed * speed_mode
                            island_y += 0.2 * fleet.speed * speed_mode
                        elif fleet.angle == 3:
                            island_x += -1.025 * fleet.speed * speed_mode
                            island_y += 0 * fleet.speed * speed_mode
                        elif fleet.angle == 4:
                            island_x += -0.9 * fleet.speed * speed_mode
                            island_y += -0.2 * fleet.speed * speed_mode
                        elif fleet.angle == 5:
                            island_x += -0.64 * fleet.speed * speed_mode
                            island_y += -0.32 * fleet.speed * speed_mode
                        for other_fleet in fleets:
                            if other_fleet != fleets[0]:
                                fleet_move(other_fleet, (fleets[0].angle + 6) % 12, fleets[0].speed * speed_mode)
                    else:
                        fleet.move = False
                        fleet_move(fleet, (fleets[0].angle + 6) % 12, fleet.speed * speed_mode)
                    fleet.x = 0
                    fleet.y = 0
                else:
                    fleet_move(fleet, fleet.angle, fleet.speed * speed_mode)
                    if not(islands_check(fleet.x - island_x, fleet.y - island_y, fleet.x - island_x, fleet.y - island_y, 10)):
                        fleet_move(fleet, (fleet.angle + 6) % 12, fleet.speed * speed_mode)

        sum += time.clock() - t0
        print("movement ", time.clock() - t0)
        t0 = time.clock()

###################################################change_target########################################################

        for fleet in fleets:
            if fleet != fleets[0]:
                if fleet.type == 1:
                    gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                    if gip < 32:
                        k = 0
                        forposts_to_trade = []
                        for forpost in forposts:
                            gip = ((forpost[0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                    forpost[1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                            if gip > i_width/2 and forpost[5] != 'PIRATE' and fraction_wars[fleet.fraction][forpost[5]] == False:
                                forposts_to_trade.append(forpost)
                        if len(forposts_to_trade) != 0:
                            if len(forposts_to_trade) == 1:
                                k = 0
                            else:
                                k = randint(0, len(forposts_to_trade) - 1)
                            fleet.target_x = forposts_to_trade[k][0] - i_width/2
                            fleet.target_y = forposts_to_trade[k][1] + i_height/2
                        profit = 0
                        max_trade_ships = 0
                        max_gold = 0
                        if forpost[0] != fleet.target_x and forpost[1] != fleet.target_y:
                            for ship in fleet.ships:
                                if ship[0] in ['ladya', 'fleyt', 'pinas', 'galeon']:
                                    max_trade_ships += 1
                                    max_gold += 2 * ship_stats[ship[0]].cost
                                    if max_trade_ships <= 2:
                                        profit += randint(ship_stats[ship[0]].max_hp // 2, ship_stats[ship[0]].max_hp) * (
                                                    (fleet.target_x - forpost[0]) ** 2 + (fleet.target_y - forpost[1]) ** 2) ** 0.5 / i_width
                            else:
                                max_gold += ship_stats[ship[0]].cost
                        else:
                            fleet.move = False
                            fleet_move(fleet, (fleet.angle + 6) % 12, fleet.speed * speed_mode)
                        fleet.gold += profit
                        if fleet.gold > max_gold:
                            fleet.gold = max_gold
                        if fleet.rank == 0:
                            repair_cost = 20
                            t = randint(1, 4)
                        elif fleet.rank == 1:
                            repair_cost = 30
                            t = randint(5, 8)
                        elif fleet.rank == 2:
                            repair_cost = 40
                            t = randint(9, 11)
                        elif fleet.rank == 3:
                            repair_cost = 50
                            t = randint(12, 14)
                        for ship in fleet.ships:
                            while fleet.gold > 0 and ship_stats[ship[0]].max_hp > ship[1]:
                                ship[1] += 1
                                fleet.gold -= repair_cost
                            if fleet.gold < 0:
                                ship[1] -= 1
                                fleet.gold += repair_cost
                        trade_ship = list(ship_stats.keys())[t]
                        while fleet.gold >= ship_stats[trade_ship].cost and len(fleet.ships) < 5:
                            fleet.gold -= ship_stats[trade_ship].cost
                            fleet.ships.append([trade_ship, ship_stats[trade_ship].max_hp])
                            if ship_stats[trade_ship].speed < fleet.speed:
                                fleet.speed = ship_stats[trade_ship].speed
                elif fleet.type == 2:
                    mingip = (fleet.rank + 3) * i_width / 2
                    for other_fleet in fleets:
                        if (other_fleet.type == 0) or (other_fleet.type == 1) or (other_fleet.type == 4):
                            gip = ((fleet.x - other_fleet.x) ** 2 + 6.25 * (fleet.y - other_fleet.y) ** 2) ** 0.5
                            if gip < mingip:
                                fleet.target_x = -island_x + other_fleet.x
                                fleet.target_y = -island_y + other_fleet.y
                                mingip = gip
                    max_gold = 0
                    for ship in fleet.ships:
                        if ship[0] in ['ladya', 'fleyt', 'pinas', 'galeon']:
                            max_gold += 2 * ship_stats[ship[0]].cost
                        else:
                            max_gold += ship_stats[ship[0]].cost
                    if fleet.gold >= max_gold:
                        mingip = 99999
                        k = -1
                        for f in range(0, len(forposts)):
                            gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                    forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                            if gip < mingip and forposts[f][5] == 'PIRATE':
                                mingip = gip
                                k = f
                        fleet.target_x = forposts[k][0] - i_width / 2
                        fleet.target_y = forposts[k][1] + i_height / 2
                        if mingip < i_width / 2:
                            if fleet.rank == 0:
                                repair_cost = 20
                                t = randint(1, 3)
                            elif fleet.rank == 1:
                                repair_cost = 30
                                t = randint(5, 7)
                            elif fleet.rank == 2:
                                repair_cost = 40
                                t = randint(9, 10)
                            elif fleet.rank == 3:
                                repair_cost = 50
                                t = randint(12, 13)
                            for ship in fleet.ships:
                                while fleet.gold > 0 and ship_stats[ship[0]].max_hp > ship[1]:
                                    ship[1] += 1
                                    fleet.gold -= repair_cost
                                if fleet.gold < 0:
                                    ship[1] -= 1
                                    fleet.gold += repair_cost
                            trade_ship = list(ship_stats.keys())[t]
                            while fleet.gold >= ship_stats[trade_ship].cost and len(fleet.ships) < 5:
                                fleet.gold -= ship_stats[trade_ship].cost
                                fleet.ships.append([trade_ship, ship_stats[trade_ship].max_hp])
                                if ship_stats[trade_ship].speed < fleet.speed:
                                    fleet.speed = ship_stats[trade_ship].speed
                    elif mingip >= (fleet.rank + 3) * i_width / 2:
                        gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                        if gip < 32:
                            side = randint(1, 4)
                            i = randint(0, len(islands) - 1)
                            if side == 1:
                                fleet.target_x = randint(islands[i][0] - i_width / 2, islands[i][0] + islands[i][2] * i_width + i_width / 2)
                                fleet.target_y = islands[i][1] - i_height / 2
                            elif side == 2:
                                fleet.target_x = randint(islands[i][0] - i_width / 2, islands[i][0] + islands[i][2] * i_width + i_width / 2)
                                fleet.target_y = islands[i][1] + islands[i][3] * i_height + i_height / 2
                            elif side == 3:
                                fleet.target_x = islands[i][0] - i_width / 2
                                fleet.target_y = randint(islands[i][1] - i_height / 2, islands[i][1] + islands[i][3] * i_height + i_height / 2)
                            elif side == 4:
                                fleet.target_x = islands[i][0] + islands[i][2] * i_width + i_width / 2
                                fleet.target_y = randint(islands[i][1] - i_height / 2, islands[i][1] + islands[i][3] * i_height + i_height / 2)
                elif fleet.type == 3:
                    mingip = (fleet.rank + 3) * i_width / 2
                    for other_fleet in fleets:
                        if other_fleet.type == 2 or (other_fleet.type == 0 and fraction_relations[fleet.fraction] < 0) or (
                           other_fleet.type in [0, 1, 3, 4, 5] and fraction_wars[fleet.fraction][other_fleet.fraction] == True):
                            gip = ((fleet.x - other_fleet.x) ** 2 + 6.25 * (fleet.y - other_fleet.y) ** 2) ** 0.5
                            if gip < mingip:
                                fleet.target_x = -island_x + other_fleet.x
                                fleet.target_y = -island_y + other_fleet.y
                                mingip = gip

                    if mingip >= (fleet.rank + 3) * i_width / 2:
                        gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                        if gip < i_width / 2:
                            fractions = []
                            there_war = False
                            if fraction_wars[fleet.fraction]['PLAYER']:
                                fractions.append('PLAYER')
                                there_war = True
                            if fraction_wars[fleet.fraction]['RED']:
                                fractions.append('RED')
                                there_war = True
                            if fraction_wars[fleet.fraction]['GREEN']:
                                fractions.append('GREEN')
                                there_war = True
                            if fraction_wars[fleet.fraction]['BLUE']:
                                fractions.append('BLUE')
                                there_war = True
                            if there_war:
                                mingip = 99999
                                k = -1
                                for f in range(0, len(forposts)):
                                    gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                            forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                                    if gip < mingip and (forposts[f][5] in fractions):
                                        mingip = gip
                                        k = f
                            if not(there_war) or k == -1:
                                mingip = 99999
                                k = -1
                                for f in range(0, len(forposts)):
                                    gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                            forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                                    if gip < mingip and forposts[f][5] == fleet.fraction:
                                        mingip = gip
                                        k = f
                            fleet.target_x = forposts[k][0] - i_width / 2
                            fleet.target_y = forposts[k][1] + i_height / 2

                    mingip = 99999
                    k = -1
                    for f in range(0, len(forposts)):
                        gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                        if gip < mingip:
                            mingip = gip
                            k = f

                    if mingip < i_width / 2:
                        if forposts[k][5] == fleet.fraction and (fleet.target_x == forposts[k][0] - i_width / 2) and (fleet.target_y == forposts[k][1] + i_height / 2):
                            fleet.move = False
                            fleet_move(fleet, (fleet.angle + 6) % 12, fleet.speed * speed_mode)
                            for other_fleet in fleets:
                                if other_fleet.type == 3 and other_fleet.fraction == fleet.fraction and (other_fleet != fleet) and (
                                    fleet.target_x == forposts[k][0] - i_width / 2) and (fleet.target_y == forposts[k][1] + i_height / 2) and (
                                    fleet.target_x == other_fleet.target_x) and (fleet.target_y == other_fleet.target_y):
                                    gip = ((fleet.x - other_fleet.x) ** 2 + 6.25 * (
                                            fleet.y - other_fleet.y) ** 2) ** 0.5
                                    if gip < (ship_stats[other_fleet.ships[0][0]].deck_size + ship_stats[fleet.ships[0][0]].deck_size) / 3:
                                        new_forposts = []
                                        for f in range(0, len(forposts)):
                                            if f != k and forposts[f][5] == fleet.fraction:
                                                new_forposts.append(forposts[f])
                                        if len(new_forposts) == 1:
                                            fleet.target_x = new_forposts[0][0] - i_width / 2
                                            fleet.target_y = new_forposts[0][1] + i_height / 2
                                        elif len(new_forposts) > 1:
                                            n_f = randint(0, len(new_forposts) - 1)
                                            fleet.target_x = new_forposts[n_f][0] - i_width / 2
                                            fleet.target_y = new_forposts[n_f][1] + i_height / 2
                        if forposts[k][5] != fleet.fraction and fraction_wars[forposts[k][5]][fleet.fraction] == True:
                            mingip_fishers = 99999
                            k_fishers = -1
                            mingip_traders = 99999
                            k_traders = -1
                            for f in range(0, len(fleets)):
                                if fleets[f].type == 1 and fleets[f].fraction == forposts[k][5]:
                                    gip = ((fleet.x - fleets[f].x) ** 2 + 6.25 * (fleet.y - fleets[f].y) ** 2) ** 0.5
                                    if gip < mingip_traders:
                                        mingip_traders = gip
                                        k_traders = f
                                if fleets[f].type == 4 and fleets[f].fraction == forposts[k][5]:
                                    gip = ((fleet.x - fleets[f].x) ** 2 + 6.25 * (
                                                fleet.y - fleets[f].y) ** 2) ** 0.5
                                    if gip < mingip_fishers:
                                        mingip_fishers = gip
                                        k_fishers = f
                            fleets[k_fishers].fraction = fleet.fraction
                            fleets[k_traders].fraction = fleet.fraction
                            forposts[k][5] = fleet.fraction
                        if forposts[k][5] == fleet.fraction:
                            if fleet.rank == 0:
                                for ship in fleet.ships:
                                    while fleet.gold > 0 and ship_stats[ship[0]].max_hp > ship[1]:
                                        ship[1] += 1
                                        fleet.gold -= 20
                                    if fleet.gold < 0:
                                        ship[1] -= 1
                                        fleet.gold += 20
                                while fleet.gold >= 3000 and len(fleet.ships) < 5:
                                    fleet.gold -= 3000
                                    fleet.ships.append(["lugger", 25])
                            elif fleet.rank == 1:
                                for ship in fleet.ships:
                                    while fleet.gold > 0 and ship_stats[ship[0]].max_hp > ship[1]:
                                        ship[1] += 1
                                        fleet.gold -= 30
                                    if fleet.gold < 0:
                                        ship[1] -= 1
                                        fleet.gold += 30
                                while fleet.gold >= 7000 and len(fleet.ships) < 5:
                                    fleet.gold -= 7000
                                    fleet.ships.append(["brig", 40])
                            elif fleet.rank == 2:
                                for ship in fleet.ships:
                                    while fleet.gold > 0 and ship_stats[ship[0]].max_hp > ship[1]:
                                        ship[1] += 1
                                        fleet.gold -= 40
                                    if fleet.gold < 0:
                                        ship[1] -= 1
                                        fleet.gold += 40
                                while fleet.gold >= 15000 and len(fleet.ships) < 5:
                                    fleet.gold -= 15000
                                    fleet.ships.append(["corvet", 60])
                            elif fleet.rank == 3:
                                for ship in fleet.ships:
                                    while fleet.gold > 0 and ship_stats[ship[0]].max_hp > ship[1]:
                                        ship[1] += 1
                                        fleet.gold -= 50
                                    if fleet.gold < 0:
                                        ship[1] -= 1
                                        fleet.gold += 50
                                while fleet.gold >= 30000 and len(fleet.ships) < 5:
                                    fleet.gold -= 30000
                                    fleet.ships.append(["warship", 90])
                elif fleet.type == 4:
                    gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                    if gip < 32:
                        mingip = 99999
                        k = -1
                        for f in range(0, len(forposts)):
                            gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                    forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                            if gip < mingip and fleet.fraction == forposts[f][5]:
                                mingip = gip
                                k = f
                        max_gold = 0
                        for ship in other_fleet.ships:
                            max_gold += ship_stats[ship[0]].cost
                        if mingip < 32 and fleet.gold > 0:
                            fleet.move = False
                            fleet_move(fleet, (fleet.angle + 6) % 12, fleet.speed * speed_mode)
                            if fleet.rank == 0 or fleet.rank == 1:
                                repair_cost = 20
                            elif fleet.rank == 2:
                                repair_cost = 30
                            elif fleet.rank == 3:
                                repair_cost = 40
                            for ship in fleet.ships:
                                while fleet.gold > 0 and ship_stats[ship[0]].max_hp > ship[1]:
                                    ship[1] += 1
                                    fleet.gold -= repair_cost
                                if fleet.gold < 0:
                                    ship[1] -= 1
                                    fleet.gold += repair_cost
                            fleet.gold -= 100
                            if fleet.gold < 0:
                                fleet.gold = 0
                        elif (mingip > i_width) or (fleet.gold >= max_gold):
                            fleet.target_x = forposts[k][0] - i_width / 2
                            fleet.target_y = forposts[k][1] + i_height / 2
                        else:
                            in_island = True
                            while in_island:
                                in_island = False
                                fx = forposts[k][0] - i_width / 2 + randint(-i_width, i_width)
                                fy = forposts[k][1] + i_height / 2 + randint(0, i_height)
                                for i in islands:
                                    ax = i[0]
                                    ay = i[1]
                                    dx = i[0] + i[2] * i_width
                                    dy = i[1] + i[3] * i_height
                                    if island_intersection(fx, fy, fx, fy, ax - 60, ay - 24, dx + 60, dy + 24):
                                        in_island = True
                            fleet.target_x = fx
                            fleet.target_y = fy
                            for ship in fleet.ships:
                                fleet.gold += randint(ship_stats[ship[0]].max_hp // 20, ship_stats[ship[0]].max_hp // 10)
                elif fleet.type == 5:
                    mingip = (fleet.rank + 3) * i_width / 2
                    for other_fleet in fleets:
                        if (other_fleet.type == 0 and fraction_relations[fleet.fraction] < 0) or (
                           other_fleet.type in [0, 1, 3, 4, 5] and fraction_wars[fleet.fraction][other_fleet.fraction] == True):
                            gip = ((fleet.x - other_fleet.x) ** 2 + 6.25 * (fleet.y - other_fleet.y) ** 2) ** 0.5
                            if gip < mingip:
                                fleet.target_x = -island_x + other_fleet.x
                                fleet.target_y = -island_y + other_fleet.y
                                mingip = gip

                    if mingip >= (fleet.rank + 3) * i_width / 2:
                        gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                        if gip < i_width / 2:
                            fractions = []
                            there_war = False
                            if fraction_wars[fleet.fraction]['PLAYER']:
                                fractions.append('PLAYER')
                                there_war = True
                            if fraction_wars[fleet.fraction]['RED']:
                                fractions.append('RED')
                                there_war = True
                            if fraction_wars[fleet.fraction]['GREEN']:
                                fractions.append('GREEN')
                                there_war = True
                            if fraction_wars[fleet.fraction]['BLUE']:
                                fractions.append('BLUE')
                                there_war = True
                            if there_war:
                                mingip = 99999
                                k = -1
                                for f in range(0, len(forposts)):
                                    gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                            forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                                    if gip < mingip and (forposts[f][5] in fractions):
                                        mingip = gip
                                        k = f
                            if not(there_war) or k == -1:
                                mingip = 99999
                                k = -1
                                for f in range(0, len(forposts)):
                                    gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                            forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                                    if gip < mingip and forposts[f][5] == 'PIRATE':
                                        mingip = gip
                                        k = f
                            fleet.target_x = forposts[k][0] - i_width / 2
                            fleet.target_y = forposts[k][1] + i_height / 2

                    mingip = 99999
                    k = -1
                    for f in range(0, len(forposts)):
                        gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                        if gip < mingip:
                            mingip = gip
                            k = f

                    if mingip < i_width / 2:
                        if forposts[k][5] == 'PIRATE' and (fleet.target_x == forposts[k][0] - i_width / 2) and (fleet.target_y == forposts[k][1] + i_height / 2):
                            fleet.move = False
                            fleet_move(fleet, (fleet.angle + 6) % 12, fleet.speed * speed_mode)
                            for other_fleet in fleets:
                                if other_fleet.type == 5 and other_fleet.fraction == fleet.fraction and (other_fleet != fleet) and (
                                    fleet.target_x == forposts[k][0] - i_width / 2) and (fleet.target_y == forposts[k][1] + i_height / 2) and (
                                    fleet.target_x == other_fleet.target_x) and (fleet.target_y == other_fleet.target_y):
                                    gip = ((fleet.x - other_fleet.x) ** 2 + 6.25 * (
                                            fleet.y - other_fleet.y) ** 2) ** 0.5
                                    if gip < (ship_stats[other_fleet.ships[0][0]].deck_size + ship_stats[fleet.ships[0][0]].deck_size) / 2:
                                        new_forposts = []
                                        for f in range(0, len(forposts)):
                                            if f != k and forposts[f][5] == 'PIRATE':
                                                new_forposts.append(forposts[f])
                                        if len(new_forposts) == 1:
                                            fleet.target_x = new_forposts[0][0] - i_width / 2
                                            fleet.target_y = new_forposts[0][1] + i_height / 2
                                        elif len(new_forposts) > 1:
                                            n_f = randint(0, len(new_forposts) - 1)
                                            fleet.target_x = new_forposts[n_f][0] - i_width / 2
                                            fleet.target_y = new_forposts[n_f][1] + i_height / 2
                        if forposts[k][5] != fleet.fraction and fraction_wars[forposts[k][5]][fleet.fraction] == True:
                            mingip_fishers = 99999
                            k_fishers = -1
                            mingip_traders = 99999
                            k_traders = -1
                            for f in range(0, len(fleets)):
                                if fleets[f].type == 1 and fleets[f].fraction == forposts[k][5]:
                                    gip = ((fleet.x - fleets[f].x) ** 2 + 6.25 * (fleet.y - fleets[f].y) ** 2) ** 0.5
                                    if gip < mingip_traders:
                                        mingip_traders = gip
                                        k_traders = f
                                if fleets[f].type == 4 and fleets[f].fraction == forposts[k][5]:
                                    gip = ((fleet.x - fleets[f].x) ** 2 + 6.25 * (
                                                fleet.y - fleets[f].y) ** 2) ** 0.5
                                    if gip < mingip_fishers:
                                        mingip_fishers = gip
                                        k_fishers = f
                            fleets[k_fishers].fraction = fleet.fraction
                            fleets[k_traders].fraction = fleet.fraction
                            forposts[k][5] = fleet.fraction
                        if forposts[k][5] == fleet.fraction:
                            if fleet.rank == 0:
                                repair_cost = 20
                                t = randint(1, 3)
                            elif fleet.rank == 1:
                                repair_cost = 30
                                t = randint(5, 7)
                            elif fleet.rank == 2:
                                repair_cost = 40
                                t = randint(9, 10)
                            elif fleet.rank == 3:
                                repair_cost = 50
                                t = randint(12, 13)
                            for ship in fleet.ships:
                                while fleet.gold > 0 and ship_stats[ship[0]].max_hp > ship[1]:
                                    ship[1] += 1
                                    fleet.gold -= repair_cost
                                if fleet.gold < 0:
                                    ship[1] -= 1
                                    fleet.gold += repair_cost
                            trade_ship = list(ship_stats.keys())[t]
                            while fleet.gold >= ship_stats[trade_ship].cost and len(fleet.ships) < 5:
                                fleet.gold -= ship_stats[trade_ship].cost
                                fleet.ships.append([trade_ship, ship_stats[trade_ship].max_hp])
                                if ship_stats[trade_ship].speed < fleet.speed:
                                    fleet.speed = ship_stats[trade_ship].speed
                        fwfc = copy.copy(fraction_war_fleet_count)
                        fwfc.pop('PLAYER')
                        if min(fwfc, key=fwfc.get) != fleet.fraction:
                            new_fleet_generate(fleet)
                            fleets.remove(fleet)

        sum += time.clock() - t0
        print("change_target ", time.clock() - t0)
        t0 = time.clock()

########################################################painting########################################################


        for wave in waves:
            image = pygame.transform.smoothscale(wave_step[wave[2] // 2], (24 / scale, 13 / scale))
            rect = image.get_rect(center=(center_x + (island_x + wave[0]) / scale, center_y + (island_y + wave[1]) / scale))
            surf, r = rot_center(image, rect, 0)
            display.blit(surf, r)
            wave[2] += 1
            if wave[2] >= 14:
                waves.remove(wave)

        sum += time.clock() - t0
        print("painting waves ", time.clock() - t0)
        t0 = time.clock()

        for island in islands:
            ax = island[0]
            ay = island[1]
            w = island[2]
            h = island[3]
            if island[4] == 'sand':
                for i in range(1, w + 1):
                    for j in range(1, h + 1):
                        if i == 1 and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width/2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1se.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1se, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1sw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1sw, rect, 0)
                                display.blit(surf, r)
                        elif i == 1 and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1ne.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1ne, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1nw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1nw, rect, 0)
                                display.blit(surf, r)
                        elif i == 1 and j != 1 and j != h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1nse.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1nse, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j != 1 and j != h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1nsw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1nsw, rect, 0)
                                display.blit(surf, r)
                        elif i != 1 and i != w and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1swe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1swe, rect, 0)
                                display.blit(surf, r)
                        elif i != 1 and i != w and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1nwe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1nwe, rect, 0)
                                display.blit(surf, r)
                        else:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = sand_1nswe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                            center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(sand_1nswe, rect, 0)
                                display.blit(surf, r)
            elif island[4] == 'grass':
                for i in range(1, w + 1):
                    for j in range(1, h + 1):
                        if i == 1 and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1se.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1se, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1sw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1sw, rect, 0)
                                display.blit(surf, r)
                        elif i == 1 and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1ne.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1ne, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1nw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1nw, rect, 0)
                                display.blit(surf, r)
                        elif i == 1 and j != 1 and j != h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1nse.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1nse, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j != 1 and j != h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1nsw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1nsw, rect, 0)
                                display.blit(surf, r)
                        elif i != 1 and i != w and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1swe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1swe, rect, 0)
                                display.blit(surf, r)
                        elif i != 1 and i != w and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1nwe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1nwe, rect, 0)
                                display.blit(surf, r)
                        else:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = grass_1nswe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                            center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(grass_1nswe, rect, 0)
                                display.blit(surf, r)
            elif island[4] == 'snow':
                for i in range(1, w + 1):
                    for j in range(1, h + 1):
                        if i == 1 and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1se.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1se, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1sw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1sw, rect, 0)
                                display.blit(surf, r)
                        elif i == 1 and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1ne.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1ne, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1nw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                          center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1nw, rect, 0)
                                display.blit(surf, r)
                        elif i == 1 and j != 1 and j != h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1nse.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1nse, rect, 0)
                                display.blit(surf, r)
                        elif i == w and j != 1 and j != h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1nsw.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1nsw, rect, 0)
                                display.blit(surf, r)
                        elif i != 1 and i != w and j == 1:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1swe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1swe, rect, 0)
                                display.blit(surf, r)
                        elif i != 1 and i != w and j == h:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1nwe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                           center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1nwe, rect, 0)
                                display.blit(surf, r)
                        else:
                            if (-display_width - i_width < island_x + ax + i_width * i - i_width / 2 < display_width + i_width) and (
                                -display_height - i_height < island_y + ay + i_height * j - i_height / 2 < display_height + i_height):
                                rect = snow_1nswe.get_rect(center=(center_x + (island_x + ax + i_width * i - i_width/2) / scale,
                                                            center_y + (island_y + ay + i_height * j - i_height/2) / scale))
                                surf, r = rot_center(snow_1nswe, rect, 0)
                                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting islands ", time.clock() - t0)
        t0 = time.clock()

        for palm in palms:
            if (-display_width - 72 < island_x + palm[0] < display_width + 72) and (
                -display_height - 188 < island_y + palm[1] < display_height + 188):
                rect = image_palm.get_rect(center=(center_x + island_x / scale + int(palm[0]) // scale,
                                                   center_y + island_y / scale + int(palm[1]) // scale))
                surf, r = rot_center(image_palm, rect, 0)
                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting palms ", time.clock() - t0)
        t0 = time.clock()

        for tree in trees:
            if (-display_width - 72 < island_x + tree[0] < display_width + 72) and (
                -display_height - 188 < island_y + tree[1] < display_height + 188):
                rect = image_tree.get_rect(center=(center_x + island_x / scale + int(tree[0]) // scale,
                                                   center_y + island_y / scale + int(tree[1]) // scale))
                surf, r = rot_center(image_tree, rect, 0)
                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting trees ", time.clock() - t0)
        t0 = time.clock()

        for ship_tree in ship_trees:
            if (-display_width - 48 < island_x + ship_tree[0] < display_width + 48) and (
                -display_height - 288 < island_y + ship_tree[1] < display_height + 288):
                rect = image_ship_tree.get_rect(center=(center_x + island_x / scale + int(ship_tree[0]) // scale,
                                                        center_y + island_y / scale + int(ship_tree[1]) // scale))
                surf, r = rot_center(image_ship_tree, rect, 0)
                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting ship_trees ", time.clock() - t0)
        t0 = time.clock()

        for forpost in forposts:
            fx = forpost[0]
            fy = forpost[1]
            if (-display_width - i_width - 16 < island_x + fx - i_width/2 < display_width + i_width + 16) and (
                -display_height - 2 * i_height - 16 < island_y + fy - i_height/2 < display_height + i_height + 16):
                if forpost[5] == 'RED':
                    color = (255, 0, 0)
                elif forpost[5] == 'GREEN':
                    color = (0, 255, 0)
                elif forpost[5] == 'BLUE':
                    color = (0, 0, 255)
                elif forpost[5] == 'PLAYER':
                    color = (255, 0, 255)
                elif forpost[5] == 'PIRATE':
                    color = (0, 0, 0)
                if forpost[2] == 1:
                    rect = image_forpost1.get_rect(center=(center_x + (island_x + fx - i_width/2) / scale,
                                                           center_y + (island_y + fy - i_height/2) / scale))
                    surf, r = rot_center(image_forpost1, rect, 0)
                    display.blit(surf, r)
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('CAMP', True, color)
                    display.blit(info, (center_x - 20 + (island_x + fx - i_width / 2) / scale,
                                        center_y + (island_y + fy - i_height / 2) / scale))
                elif forpost[2] == 2:
                    rect = image_forpost2.get_rect(center=(center_x + (island_x + fx - i_width / 2) / scale,
                                                           center_y + (island_y + fy - i_height / 2) / scale))
                    surf, r = rot_center(image_forpost2, rect, 0)
                    display.blit(surf, r)
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('TOWN', True, color)
                    display.blit(info, (center_x - 20 + (island_x + fx - i_width / 2) / scale,
                                        center_y + (island_y + fy - i_height / 2) / scale))
                elif forpost[2] == 3:
                    rect = image_forpost3.get_rect(center=(center_x + (island_x + fx - i_width / 2) / scale,
                                                           center_y + (island_y + fy - i_height / 2) / scale))
                    surf, r = rot_center(image_forpost3, rect, 0)
                    display.blit(surf, r)
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('CITY', True, color)
                    display.blit(info, (center_x - 20 + (island_x + fx - i_width / 2) / scale,
                                        center_y + (island_y + fy - (i_height - 10) / 2) / scale))
                elif forpost[2] == 4:
                    rect = image_forpost4.get_rect(center=(center_x + (island_x + fx - i_width / 2) / scale,
                                                           center_y + (island_y + fy - i_height / 2) / scale))
                    surf, r = rot_center(image_forpost4, rect, 0)
                    display.blit(surf, r)
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('CASTLE', True, color)
                    display.blit(info, (center_x - 20 + (island_x + fx - i_width / 2) / scale,
                                        center_y + (island_y + fy - (i_height - 10) / 2) / scale))
                rect = image_forpost_zone.get_rect(center=(center_x + (island_x + fx - i_width/2) / scale,
                                                           center_y + (island_y + fy + i_height/2) / scale))
                surf, r = rot_center(image_forpost_zone, rect, 0)
                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting forposts ", time.clock() - t0)
        t0 = time.clock()

        fleets_paint = copy.copy(fleets)
        fleets_paint.sort(key=lambda f: f.y)
        for fleet in fleets_paint:
            if (-display_width - ship_stats[fleet.ships[0][0]].pic_size < fleet.x < display_width + ship_stats[fleet.ships[0][0]].pic_size) and (
                -display_height - ship_stats[fleet.ships[0][0]].pic_size < fleet.y < display_height + ship_stats[fleet.ships[0][0]].pic_size):
                if fleet.move == True:
                    image = ship_stats[fleet.ships[0][0]].ms_sail1[fleet.angle]
                else:
                    image = ship_stats[fleet.ships[0][0]].ms_sail0[fleet.angle]
                rect = image.get_rect(center=(center_x + fleet.x / scale, center_y + fleet.y / scale))
                surf, r = rot_center(image, rect, 0)
                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting fleets ", time.clock() - t0)
        t0 = time.clock()

##########################################################info##########################################################

        for fleet in fleets:
            if (-display_width - ship_stats[fleet.ships[0][0]].pic_size < fleet.x < display_width + ship_stats[fleet.ships[0][0]].pic_size) and (
                    -display_height - ship_stats[fleet.ships[0][0]].pic_size < fleet.y < display_height + ship_stats[fleet.ships[0][0]].pic_size):
                if fleet.fraction == 'PLAYER':
                    color = (255, 0, 255)
                if fleet.fraction == 'RED':
                    color = (255, 0, 0)
                elif fleet.fraction == 'GREEN':
                    color = (0, 255, 0)
                elif fleet.fraction == 'BLUE':
                    color = (0, 0, 255)
                # f = pygame.font.Font(None, 22)
                # gold = f.render('GOLD: ' + str(int(fleet.gold)), True, (255, 0, 255))
                # display.blit(gold, (center_x + (fleet.x - 50) / scale, center_y + (fleet.y - 70) / scale))
                if fleet.type == 0:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('PLAYER', True, (255, 0, 255))
                    info_rect = info.get_rect(center=(center_x + fleet.x / scale, center_y + (fleet.y - 48) / scale))
                    display.blit(info, info_rect)
                elif fleet.type == 1:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('TRADERS', True, color)
                    info_rect = info.get_rect(center=(center_x + fleet.x / scale, center_y + (fleet.y - 48) / scale))
                    display.blit(info, info_rect)
                elif fleet.type == 2:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('PIRATES', True, (64, 64, 64))
                    info_rect = info.get_rect(center=(center_x + fleet.x / scale, center_y + (fleet.y - 48) / scale))
                    display.blit(info, info_rect)
                elif fleet.type == 3:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('WARRIORS', True, color)
                    info_rect = info.get_rect(center=(center_x + fleet.x / scale, center_y + (fleet.y - 48) / scale))
                    display.blit(info, info_rect)
                elif fleet.type == 4:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('FISHERS', True, color)
                    info_rect = info.get_rect(center=(center_x + fleet.x / scale, center_y + (fleet.y - 48) / scale))
                    display.blit(info, info_rect)
                elif fleet.type == 5:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('MERCENARIES', True, color)
                    info_rect = info.get_rect(center=(center_x + fleet.x / scale, center_y + (fleet.y - 48) / scale))
                    display.blit(info, info_rect)
                k = 0
                f = pygame.font.SysFont(None, 32 // scale)
                for ship in fleet.ships:
                    info = f.render(ship[0] + " " + str(ship[1]) + "/" + str(ship_stats[ship[0]].max_hp), True, (0, 0, 0))
                    display.blit(info, (center_x + (fleet.x - 50) / scale, center_y + (fleet.y + k) / scale))
                    k += 32

        sum += time.clock() - t0
        print("info fleets ", time.clock() - t0)
        t0 = time.clock()

        max_gold = 0
        max_trade_ships = 0
        for ship in fleets[0].ships:
            if ship[0] in ['ladya', 'fleyt', 'pinas', 'galeon']:
                max_gold += 2 * ship_stats[ship[0]].cost
                if max_trade_ships < 2:
                    f = pygame.font.Font(None, 36)
                    coord = f.render(ship[0], True, (255, 0, 0))
                    display.blit(coord, (10 + max_trade_ships * 90, 46))
                max_trade_ships += 1
            else:
                max_gold += ship_stats[ship[0]].cost
        f = pygame.font.Font(None, 36)
        coord = f.render('GOLD: ' + str(int(fleets[0].gold)) + '/' + str(max_gold), True, (255, 0, 0))
        display.blit(coord, (10, 10))
        f = pygame.font.Font(None, 36)
        forp = f.render(str(game_time // 6), True, (255, 0, 0))
        display.blit(forp, (display_width - 80, 10))
        f = pygame.font.Font(None, 20)
        coord = f.render("(M) - minimap; (A)/(D) - turn; (W)/(S) - move/stop; (Esc) - close game;", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 150))
        coord = f.render("(1)/(2)/(3)/(4)/(5) - swap ships in fleet; 10/20/30/40 points to capture.", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 130))
        coord = f.render("Farm gold killing fleets or swiming between forposts with trade ships.", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 110))
        coord = f.render("Buy/sold/repair ships in forpost zones. When fractions in war - kill", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 90))
        coord = f.render("enemy fleets to take relation points for this fraction. You can capture", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 70))
        coord = f.render("forpost friendly fractions and create PLAYER fraction. After capture", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 50))
        coord = f.render("forposts for free. Captures all RED/GREEN/BLUE forposts to win.", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 30))

        f = pygame.font.Font(None, 30)
        forp = f.render('RED: ' + str(fraction_relations['RED']), True, (255, 0, 0))
        forp_rect = forp.get_rect(center=(display_width - 300, display_height - 125))
        display.blit(forp, forp_rect)
        forp = f.render('BLUE: ' + str(fraction_relations['BLUE']), True, (0, 0, 255))
        forp_rect = forp.get_rect(center=(display_width - 100, display_height - 125))
        display.blit(forp, forp_rect)
        forp = f.render('GREEN: ' + str(fraction_relations['GREEN']), True, (0, 255, 0))
        forp_rect = forp.get_rect(center=(display_width - 200, display_height - 25))
        display.blit(forp, forp_rect)

        if player_fraction:
            forp = f.render('PLAYER', True, (255, 0, 255))
            forp_rect = forp.get_rect(center=(display_width - 200, display_height - 75))
            display.blit(forp, forp_rect)

        if fraction_wars['RED']['BLUE'] == True:
            f = pygame.font.Font(None, 30)
            forp = f.render('WAR', True, (0, 0, 0))
            forp_rect = forp.get_rect(center=(display_width - 200, display_height - 125))
            display.blit(forp, forp_rect)
        if fraction_wars['RED']['GREEN'] == True:
            f = pygame.font.Font(None, 30)
            forp = f.render('WAR', True, (0, 0, 0))
            forp_rect = forp.get_rect(center=(display_width - 250, display_height - 75))
            display.blit(forp, forp_rect)
        if fraction_wars['BLUE']['GREEN'] == True:
            f = pygame.font.Font(None, 30)
            forp = f.render('WAR', True, (0, 0, 0))
            forp_rect = forp.get_rect(center=(display_width - 150, display_height - 75))
            display.blit(forp, forp_rect)
        if fraction_wars['RED']['PLAYER'] == True:
            f = pygame.font.Font(None, 30)
            forp = f.render('WAR', True, (0, 0, 0))
            forp_rect = forp.get_rect(center=(display_width - 250, display_height - 100))
            display.blit(forp, forp_rect)
        if fraction_wars['GREEN']['PLAYER'] == True:
            f = pygame.font.Font(None, 30)
            forp = f.render('WAR', True, (0, 0, 0))
            forp_rect = forp.get_rect(center=(display_width - 200, display_height - 50))
            display.blit(forp, forp_rect)
        if fraction_wars['BLUE']['PLAYER'] == True:
            f = pygame.font.Font(None, 30)
            forp = f.render('WAR', True, (0, 0, 0))
            forp_rect = forp.get_rect(center=(display_width - 150, display_height - 100))
            display.blit(forp, forp_rect)

        if stop > 0:
            stop -= 1

        sum += time.clock() - t0
        print("info ", time.clock() - t0)
        t0 = time.clock()

################################################forpost_interface#######################################################

        for forpost in forposts:
            fx = forpost[0] - i_width/2
            fy = forpost[1] + i_height/2
            if (-i_width/2 < fx + island_x < i_width/2) and (-i_height/2 < fy + island_y < i_height/2):
                if not(forpost_zone):
                    if not(player_fraction) or player_fraction and fraction_wars['PLAYER'][forpost[5]] == False:
                        f = pygame.font.Font(None, 36)
                        b = f.render('press (Z) to dock', True, (0, 0, 0))
                        b_rect = b.get_rect(center=(0.5 * display_width, 0.5 * display_height - 80))
                        display.blit(b, b_rect)
                    if fraction_relations[forpost[5]] < 0 and not(player_fraction):
                        f = pygame.font.Font(None, 36)
                        b = f.render('cost ' + str(fraction_relations[forpost[5]] * (-1000)) + ' GOLD', True, (255, 255, 0))
                        display.blit(b, (display_width / 2 - 50, 0.5 * display_height - 14))
                    if keys[pygame.K_z]:
                        if (fleets[0].gold >= fraction_relations[forpost[5]] * (-1000)) and not(player_fraction):
                            if fraction_relations[forpost[5]] < 0:
                                fleets[0].gold -= fraction_relations[forpost[5]] * (-1000)
                                fraction_relations[forpost[5]] = 0
                            fleets[0].x = 99999
                            fleets[0].y = 99999
                            fleets[0].move = 0
                            forpost_zone = True
                        elif player_fraction and fraction_wars['PLAYER'][forpost[5]] == False:
                            fleets[0].x = 99999
                            fleets[0].y = 99999
                            fleets[0].move = 0
                            forpost_zone = True
                    if not(player_fraction) and fraction_relations[forpost[5]] >= forpost[2] * 10 or player_fraction and (
                            forpost[5] not in ['PLAYER', 'PIRATE']):
                        f = pygame.font.Font(None, 36)
                        b = f.render('press (C) to capture', True, (255, 255, 255))
                        b_rect = b.get_rect(center=(0.5 * display_width, 0.5 * display_height - 110))
                        display.blit(b, b_rect)
                        if keys[pygame.K_c]:
                            player_fraction = True
                            fraction_wars['PLAYER'][forpost[5]] = True
                            fraction_wars[forpost[5]]['PLAYER'] = True
                            fraction_relations['RED'] = 0
                            fraction_relations['GREEN'] = 0
                            fraction_relations['BLUE'] = 0
                            mingip_fishers = 99999
                            k_fishers = -1
                            mingip_traders = 99999
                            k_traders = -1
                            for f in range(0, len(fleets)):
                                if fleets[f].type == 1 and fleets[f].fraction == forpost[5]:
                                    gip = ((fleets[0].x - fleets[f].x) ** 2 + 6.25 * (fleets[0].y - fleets[f].y) ** 2) ** 0.5
                                    if gip < mingip_traders:
                                        mingip_traders = gip
                                        k_traders = f
                                if fleets[f].type == 4 and fleets[f].fraction == forpost[5]:
                                    gip = ((fleets[0].x - fleets[f].x) ** 2 + 6.25 * (
                                            fleets[0].y - fleets[f].y) ** 2) ** 0.5
                                    if gip < mingip_fishers:
                                        mingip_fishers = gip
                                        k_fishers = f
                            fleets[k_fishers].fraction = 'PLAYER'
                            fleets[k_traders].fraction = 'PLAYER'
                            forpost[5] = 'PLAYER'
                else:
                    if player_trade_forpost == '-':
                        player_trade_forpost = forpost
                    if forpost[5] != 'PIRATE' and player_trade_forpost != forpost:
                        profit = 0
                        max_trade_ships = 0
                        max_gold = 0
                        for ship in fleets[0].ships:
                            if ship[0] in ['ladya', 'fleyt', 'pinas', 'galeon']:
                                max_trade_ships += 1
                                max_gold += 2 * ship_stats[ship[0]].cost
                                if max_trade_ships <= 2:
                                    profit += randint(ship_stats[ship[0]].max_hp // 2, ship_stats[ship[0]].max_hp) * (
                                            (player_trade_forpost[0] - forpost[0]) ** 2 + (player_trade_forpost[1] - forpost[1]) ** 2) ** 0.5 / i_width
                            else:
                                max_gold += ship_stats[ship[0]].cost
                        fleets[0].gold += profit
                        if fleets[0].gold >= max_gold:
                            fleets[0].gold = max_gold
                        player_trade_forpost = forpost
                    if forpost[2] == 1:
                        forpost_type = 'CAMP'
                    elif forpost[2] == 2:
                        forpost_type = 'TOWN'
                    elif forpost[2] == 3:
                        forpost_type = 'CITY'
                    elif forpost[2] == 4:
                        forpost_type = 'CASTLE'
                    if forpost[6] == 'sand':
                        color = (255, 242, 0)
                    elif forpost[6] == 'grass':
                        color = (181, 230, 29)
                    elif forpost[6] == 'snow':
                        color = (153, 217, 234)
                    pygame.draw.rect(display, color, (0, 0, 0.2 * display_width, display_height))
                    pygame.draw.rect(display, (0, 0, 0), (0.2 * display_width - 5, 0, 5, display_height))
                    pygame.draw.rect(display, color, (0.8 * display_width, 0, 0.2 * display_width, display_height))
                    pygame.draw.rect(display, (0, 0, 0), (0.8 * display_width, 0, 5, display_height))
                    pygame.draw.rect(display, color, (0, 0, display_width, 50))
                    pygame.draw.rect(display, (0, 0, 0), (0, 45, display_width, 5))
                    pygame.draw.rect(display, color, (0, center_y * 4 / 3, display_width, display_height / 3))
                    pygame.draw.rect(display, (0, 0, 0), (0, center_y * 4 / 3, display_width, 5))
                    f = pygame.font.Font(None, 36)
                    coord = f.render('GOLD: ' + str(int(fleets[0].gold)), True, (255, 0, 0))
                    display.blit(coord, (10, 10))
                    f = pygame.font.Font(None, 36)
                    forp = f.render(forpost_type, True, (255, 0, 0))
                    display.blit(forp, (display_width - 120, 10))

                    step = -display_width * 0.4

                    if forpost[3] != '-':
                        name = pygame.font.Font(None, 32)
                        b1 = name.render('buy ship - (Q)', True, (255, 0, 0))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 - 200))
                        image = pygame.transform.smoothscale(ship_stats[forpost[3]].ms_sail1[(game_time // 5) % 12],
                                                            (ship_stats[forpost[3]].pic_size / 2, ship_stats[forpost[3]].pic_size / 2))
                        rect = image.get_rect(center=(0.1 * display_width, center_y * 2 / 3))
                        surf, r = rot_center(image, rect, 0)
                        display.blit(surf, r)
                        name = pygame.font.Font(None, 32)
                        b1 = name.render(forpost[3], True, (0, 0, 0))
                        display.blit(b1, (0.1 * display_width - 30, center_y * 2 / 3 + 30))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('health:  ' + str(ship_stats[forpost[3]].max_hp) + ' / ' + str(ship_stats[forpost[3]].max_hp), True, (255, 0, 0))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 + 62))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('speed: ' + str(int(ship_stats[forpost[3]].speed * 5)) + ' knots', True, (0, 0, 255))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 + 86))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('turn speed: ' + str(ship_stats[forpost[3]].t_speed) + '%', True, (0, 0, 255))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 + 110))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('cost: ' + str(ship_stats[forpost[3]].cost) + ' gold', True, (64, 64, 64))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 + 134))

                    if forpost[4] != '-':
                        name = pygame.font.Font(None, 32)
                        b1 = name.render('buy ship - (E)', True, (255, 0, 0))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 - 200))
                        image = pygame.transform.smoothscale(ship_stats[forpost[4]].ms_sail1[(game_time // 5) % 12],
                                                             (ship_stats[forpost[4]].pic_size / 2, ship_stats[forpost[4]].pic_size / 2))
                        rect = image.get_rect(center=(0.9 * display_width, center_y * 2 / 3))
                        surf, r = rot_center(image, rect, 0)
                        display.blit(surf, r)
                        name = pygame.font.Font(None, 32)
                        b1 = name.render(forpost[4], True, (0, 0, 0))
                        display.blit(b1, (0.9 * display_width - 30, center_y * 2 / 3 + 30))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('health:  ' + str(ship_stats[forpost[4]].max_hp) + ' / ' + str(ship_stats[forpost[4]].max_hp), True, (255, 0, 0))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 + 62))
                        b1 = name.render('speed: ' + str(int(ship_stats[forpost[4]].speed * 5)) + ' knots', True, (0, 0, 255))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 + 86))
                        b1 = name.render('turn speed: ' + str(ship_stats[forpost[4]].t_speed) + '%', True, (0, 0, 255))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 + 110))
                        b1 = name.render('cost: ' + str(ship_stats[forpost[4]].cost) + ' gold', True, (64, 64, 64))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 + 134))

                    for m in range(len(fleets[0].ships)):
                        ship = fleets[0].ships[m]
                        if m == menu:
                            image = pygame.transform.smoothscale(ship_stats[ship[0]].ms_sail1[(game_time // 5) % 12],
                                                             (ship_stats[ship[0]].pic_size / 2, ship_stats[ship[0]].pic_size / 2))
                            color = (0, 0, 255)
                        else:
                            image = pygame.transform.smoothscale(ship_stats[ship[0]].ms_sail0[(game_time // 5) % 12],
                                                             (ship_stats[ship[0]].pic_size / 2, ship_stats[ship[0]].pic_size / 2))
                            color = (0, 0, 0)
                        rect = image.get_rect(center=(center_x + step, center_y * 5 / 3))
                        surf, r = rot_center(image, rect, 0)
                        display.blit(surf, r)
                        name = pygame.font.Font(None, 32)
                        b1 = name.render(ship[0], True, color)
                        display.blit(b1, (center_x + step - 30, center_y * 5 / 3 + 30))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('health:  ' + str(int(ship[1])) + ' / ' + str(int(ship_stats[ship[0]].max_hp)), True, (255, 0, 0))
                        display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 62))
                        if menu == m:
                            if ship_stats[ship[0]].cost <= 3000:
                                cost = 20
                            elif ship_stats[ship[0]].cost <= 7000:
                                cost = 30
                            elif ship_stats[ship[0]].cost <= 15000:
                                cost = 40
                            else:
                                cost = 50
                            name = pygame.font.Font(None, 24)
                            hp = ship[1]
                            max_hp = ship_stats[ship[0]].max_hp
                            b1 = name.render('repair: ' + str((max_hp - hp) * cost) + ' gold - (R)', True, (64, 64, 64))
                            display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 86))
                            name = pygame.font.Font(None, 24)
                            b1 = name.render('sold: ' + str(int(hp / max_hp * ship_stats[ship[0]].cost // 4)) + ' gold - (T)', True, (64, 64, 64))
                            display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 110))
                        step += display_width * 0.2
                    f = pygame.font.Font(None, 36)
                    b = f.render('press (X) to leave', True, (0, 0, 0))
                    b_rect = b.get_rect(center=(0.5 * display_width, 28))
                    display.blit(b, b_rect)
                    if keys[pygame.K_a]:
                        if stop == 0:
                            if menu > 0:
                                menu -= 1
                            else:
                                menu = len(fleets[0].ships) - 1
                            stop = 5
                    elif keys[pygame.K_d]:
                        if stop == 0:
                            if menu < len(fleets[0].ships) - 1:
                                menu += 1
                            else:
                                menu = 0
                            stop = 5
                    elif keys[pygame.K_r]:
                        if ship_stats[ship[0]].cost <= 3000:
                            repair_cost = 20
                        elif ship_stats[ship[0]].cost <= 7000:
                            repair_cost = 30
                        elif ship_stats[ship[0]].cost <= 15000:
                            repair_cost = 40
                        else:
                            repair_cost = 50
                        while fleets[0].gold > 0 and ship_stats[fleets[0].ships[menu][0]].max_hp > fleets[0].ships[menu][1]:
                            fleets[0].ships[menu][1] += 1
                            fleets[0].gold -= repair_cost
                        if fleets[0].gold < 0:
                            fleets[0].ships[menu][1] -= 1
                            fleets[0].gold += repair_cost
                    elif keys[pygame.K_t]:
                        if stop == 0:
                            if len(fleets[0].ships) >= 2:
                                max_gold = 0
                                for ship in fleets[0].ships:
                                    if ship[0] in ['ladya', 'fleyt', 'pinas', 'galeon']:
                                        max_gold += 2 * ship_stats[ship[0]].cost
                                    else:
                                        max_gold += ship_stats[ship[0]].cost
                                fleets[0].gold += (fleets[0].ships[menu][1] / ship_stats[fleets[0].ships[menu][0]].max_hp
                                                   * ship_stats[fleets[0].ships[menu][0]].cost) // 4
                                if fleets[0].gold > max_gold:
                                    fleets[0].gold = max_gold
                                fleets[0].ships.remove(fleets[0].ships[menu])
                                stop = 10
                                if menu > len(fleets[0].ships) - 1:
                                    menu -= 1
                                fleets[0].speed = 2.8
                                for ship in fleets[0].ships:
                                    if ship_stats[ship[0]].speed < fleets[0].speed:
                                        fleets[0].speed = ship_stats[ship[0]].speed
                    elif keys[pygame.K_q]:
                        if forpost[3] != '-' and (len(fleets[0].ships) < 5) and fleets[0].gold >= ship_stats[forpost[3]].cost:
                            fleets[0].gold -= ship_stats[forpost[3]].cost
                            fleets[0].ships.append([forpost[3], ship_stats[forpost[3]].max_hp])
                            if ship_stats[forpost[3]].speed < fleets[0].speed:
                                fleets[0].speed = ship_stats[forpost[3]].speed
                            forpost[3] = '-'
                    elif keys[pygame.K_e]:
                        if forpost[4] != '-' and (len(fleets[0].ships) < 5) and fleets[0].gold >= ship_stats[forpost[4]].cost:
                            fleets[0].gold -= ship_stats[forpost[4]].cost
                            fleets[0].ships.append([forpost[4], ship_stats[forpost[4]].max_hp])
                            if ship_stats[forpost[4]].speed < fleets[0].speed:
                                fleets[0].speed = ship_stats[forpost[4]].speed
                            forpost[4] = '-'
                    elif keys[pygame.K_x]:
                        fleets[0].x = 0
                        fleets[0].y = 0
                        forpost_zone = False
                        menu = 0

#######################################################minimap##########################################################

        if keys[pygame.K_m]:
            display.fill((0, 162, 232))

            for island in islands:
                ax = island[0]
                ay = island[1]
                w = island[2]
                h = island[3]
                if island[4] == 'sand':
                    for i in range(1, w + 1):
                        for j in range(1, h + 1):
                            if i == 1 and j == 1:
                                rect = m_sand_1se.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1se, rect, 0)
                            elif i == w and j == 1:
                                rect = m_sand_1sw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1sw, rect, 0)
                            elif i == 1 and j == h:
                                rect = m_sand_1ne.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1ne, rect, 0)
                            elif i == w and j == h:
                                rect = m_sand_1nw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1nw, rect, 0)
                            elif i == 1 and j != 1 and j != h:
                                rect = m_sand_1nse.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1nse, rect, 0)
                            elif i == w and j != 1 and j != h:
                                rect = m_sand_1nsw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1nsw, rect, 0)
                            elif i != 1 and i != w and j == 1:
                                rect = m_sand_1swe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1swe, rect, 0)
                            elif i != 1 and i != w and j == h:
                                rect = m_sand_1nwe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1nwe, rect, 0)
                            else:
                                rect = m_sand_1nswe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                                center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_sand_1nswe, rect, 0)
                            display.blit(surf, r)
                elif island[4] == 'grass':
                    for i in range(1, w + 1):
                        for j in range(1, h + 1):
                            if i == 1 and j == 1:
                                rect = m_grass_1se.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1se, rect, 0)
                            elif i == w and j == 1:
                                rect = m_grass_1sw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1sw, rect, 0)
                            elif i == 1 and j == h:
                                rect = m_grass_1ne.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1ne, rect, 0)
                            elif i == w and j == h:
                                rect = m_grass_1nw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1nw, rect, 0)
                            elif i == 1 and j != 1 and j != h:
                                rect = m_grass_1nse.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1nse, rect, 0)
                            elif i == w and j != 1 and j != h:
                                rect = m_grass_1nsw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1nsw, rect, 0)
                            elif i != 1 and i != w and j == 1:
                                rect = m_grass_1swe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1swe, rect, 0)
                            elif i != 1 and i != w and j == h:
                                rect = m_grass_1nwe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1nwe, rect, 0)
                            else:
                                rect = m_grass_1nswe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                                center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_grass_1nswe, rect, 0)
                            display.blit(surf, r)
                elif island[4] == 'snow':
                    for i in range(1, w + 1):
                        for j in range(1, h + 1):
                            if i == 1 and j == 1:
                                rect = m_snow_1se.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1se, rect, 0)
                            elif i == w and j == 1:
                                rect = m_snow_1sw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1sw, rect, 0)
                            elif i == 1 and j == h:
                                rect = m_snow_1ne.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1ne, rect, 0)
                            elif i == w and j == h:
                                rect = m_snow_1nw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                              center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1nw, rect, 0)
                            elif i == 1 and j != 1 and j != h:
                                rect = m_snow_1nse.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1nse, rect, 0)
                            elif i == w and j != 1 and j != h:
                                rect = m_snow_1nsw.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1nsw, rect, 0)
                            elif i != 1 and i != w and j == 1:
                                rect = m_snow_1swe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1swe, rect, 0)
                            elif i != 1 and i != w and j == h:
                                rect = m_snow_1nwe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                               center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1nwe, rect, 0)
                            else:
                                rect = m_snow_1nswe.get_rect(center=(center_x + (ax + i_width * i - i_width/2) / 16,
                                                                center_y * 2/3 + (ay + i_height * j - i_height/2) / 16))
                                surf, r = rot_center(m_snow_1nswe, rect, 0)
                            display.blit(surf, r)

            for forpost in forposts:
                fx = forpost[0]
                fy = forpost[1]
                if forpost[5] == 'RED':
                    color = (255, 0, 0)
                elif forpost[5] == 'GREEN':
                    color = (0, 255, 0)
                elif forpost[5] == 'BLUE':
                    color = (0, 0, 255)
                elif forpost[5] == 'PLAYER':
                    color = (255, 0, 255)
                elif forpost[5] == 'PIRATE':
                    color = (64, 64, 64)
                if forpost[2] == 1:
                    rect = m_image_forpost1.get_rect(center=(center_x + (fx - i_width/2) / 16, center_y * 2/3 + (fy - i_height/2) / 16))
                    surf, r = rot_center(m_image_forpost1, rect, 0)
                    display.blit(surf, r)
                    f = pygame.font.Font(None, 24 // scale)
                    info = f.render('CAMP', True, color)
                    display.blit(info, (center_x - 10 + (fx - i_width / 2) / 16,
                                        center_y * 2/3 + (fy + i_height / 2) / 16))
                elif forpost[2] == 2:
                    rect = m_image_forpost2.get_rect(center=(center_x + (fx - i_width / 2) / 16, center_y * 2/3 + (fy - i_height / 2) / 16))
                    surf, r = rot_center(m_image_forpost2, rect, 0)
                    display.blit(surf, r)
                    f = pygame.font.Font(None, 24 // scale)
                    info = f.render('TOWN', True, color)
                    display.blit(info, (center_x - 10 + (fx - i_width / 2) / 16,
                                        center_y * 2/3 + (fy + i_height / 2) / 16))
                elif forpost[2] == 3:
                    rect = m_image_forpost3.get_rect(center=(center_x + (fx - i_width / 2) / 16, center_y * 2/3 + (fy - i_height / 2) / 16))
                    surf, r = rot_center(m_image_forpost3, rect, 0)
                    display.blit(surf, r)
                    f = pygame.font.Font(None, 24 // scale)
                    info = f.render('CITY', True, color)
                    display.blit(info, (center_x - 10 + (fx - i_width / 2) / 16,
                                        center_y * 2/3 + (fy + (i_height - 10) / 2) / 16))
                elif forpost[2] == 4:
                    rect = m_image_forpost4.get_rect(center=(center_x + (fx - i_width / 2) / 16, center_y * 2/3 + (fy - i_height / 2) / 16))
                    surf, r = rot_center(m_image_forpost4, rect, 0)
                    display.blit(surf, r)
                    f = pygame.font.Font(None, 24 // scale)
                    info = f.render('CASTLE', True, color)
                    display.blit(info, (center_x - 10 + (fx - i_width / 2) / 16,
                                        center_y * 2/3 + (fy + (i_height - 10) / 2) / 16))
            fleets_paint = copy.copy(fleets)
            fleets_paint.sort(key=lambda f: f.y)
            for fleet in fleets_paint:
                if (-display_width - ship_stats[fleet.ships[0][0]].pic_size / 8 < fleet.x < display_width + ship_stats[fleet.ships[0][0]].pic_size / 8) and (
                    -display_height - ship_stats[fleet.ships[0][0]].pic_size / 8 < fleet.y < display_height + ship_stats[fleet.ships[0][0]].pic_size / 8):
                    if fleet.move == True:
                        image = pygame.transform.smoothscale(ship_stats[fleet.ships[0][0]].ms_sail1[fleet.angle],
                                (ship_stats[fleet.ships[0][0]].pic_size / 16, ship_stats[fleet.ships[0][0]].pic_size / 16))
                    else:
                        image = pygame.transform.smoothscale(ship_stats[fleet.ships[0][0]].ms_sail0[fleet.angle],
                                (ship_stats[fleet.ships[0][0]].pic_size / 16, ship_stats[fleet.ships[0][0]].pic_size / 16))
                    rect = image.get_rect(center=(center_x + (fleet.x - island_x) / 16, center_y * 2/3 + (fleet.y - island_y) / 16))
                    surf, r = rot_center(image, rect, 0)
                    display.blit(surf, r)
            step = -display_width * 0.4
            for ship in fleets[0].ships:
                image = pygame.transform.smoothscale(ship_stats[ship[0]].ms_sail1[(game_time // 5) % 12],
                                                     (ship_stats[ship[0]].pic_size / 2, ship_stats[ship[0]].pic_size / 2))
                rect = image.get_rect(center=(center_x + step, center_y * 5 / 3))
                surf, r = rot_center(image, rect, 0)
                display.blit(surf, r)
                name = pygame.font.Font(None, 32)
                b1 = name.render(ship[0], True, (0, 0, 0))
                display.blit(b1, (center_x + step - 30, center_y * 5 / 3 + 30))
                name = pygame.font.Font(None, 24)
                b1 = name.render('health:  ' + str(int(ship[1])) + ' / ' + str(int(ship_stats[ship[0]].max_hp)), True, (255, 0, 0))
                display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 62))
                name = pygame.font.Font(None, 24)
                b1 = name.render('speed: ' + str(int(ship_stats[ship[0]].speed * 5)) + ' knots', True, (0, 0, 255))
                display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 86))
                name = pygame.font.Font(None, 24)
                b1 = name.render('turn speed: ' + str(ship_stats[ship[0]].t_speed) + '%', True, (0, 0, 255))
                display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 110))
                step += display_width * 0.2

        sum += time.clock() - t0
        print("other ", time.clock() - t0)
        t0 = time.clock()

########################################################battle##########################################################

        for fleet in fleets:
            if fleet.type == 0:
                for other_fleet in fleets:
                    if (other_fleet.type in [0, 1, 3, 4, 5]) and (fleet.fraction != other_fleet.fraction):
                        gip = ((other_fleet.x - fleet.x) ** 2 + 6.25 * (other_fleet.y - fleet.y) ** 2) ** 0.5
                        if len(fleet.ships) > 0 and len(other_fleet.ships) > 0:
                            battle_radius = (ship_stats[other_fleet.ships[0][0]].deck_size + ship_stats[fleet.ships[0][0]].deck_size) / 2
                            if (gip < battle_radius):
                                f = pygame.font.Font(None, 36)
                                if other_fleet.fraction == 'RED':
                                    color = (255, 0, 0)
                                elif other_fleet.fraction == 'GREEN':
                                    color = (0, 255, 0)
                                elif other_fleet.fraction == 'BLUE':
                                    color = (0, 0, 255)
                                b = f.render('press (F) to attack', True, color)
                                b_rect = b.get_rect(center=(0.5 * display_width, 0.5 * display_height - 50))
                                display.blit(b, b_rect)
                                if keys[pygame.K_f]:
                                    if not(player_fraction):
                                        fraction_relations[other_fleet.fraction] -= len(other_fleet.ships)
                                        if fraction_wars['RED'][other_fleet.fraction] == True:
                                            fraction_relations['RED'] += len(other_fleet.ships)
                                        if fraction_wars['GREEN'][other_fleet.fraction] == True:
                                            fraction_relations['GREEN'] += len(other_fleet.ships)
                                        if fraction_wars['BLUE'][other_fleet.fraction] == True:
                                            fraction_relations['BLUE'] += len(other_fleet.ships)
                                    else:
                                        fraction_wars[fleets[0].fraction][other_fleet.fraction] = True
                                        fraction_wars[other_fleet.fraction][fleets[0].fraction] = True
                                    battle_with_player(other_fleet)
            # elif fleet.type == 1:
            #     gip = ((fleets[0].x - fleet.x) ** 2 + 6.25 * (fleets[0].y - fleet.y) ** 2) ** 0.5
            #     if len(fleet.ships) > 0 and len(fleets[0].ships) > 0:
            #         battle_radius = (ship_stats[fleets[0].ships[0][0]].deck_size + ship_stats[fleet.ships[0][0]].deck_size) / 2
            #         if (gip < battle_radius and ((not(player_fraction) and fraction_relations[fleet.fraction] < 0)) or (
            #             player_fraction and fraction_wars['PLAYER'][fleet.fraction] == True)):
            #             if not (player_fraction):
            #                 fraction_relations[fleet.fraction] -= len(fleet.ships)
            #                 if fraction_wars['RED'][fleet.fraction] == True:
            #                     fraction_relations['RED'] += len(fleet.ships)
            #                 if fraction_wars['GREEN'][fleet.fraction] == True:
            #                     fraction_relations['GREEN'] += len(fleet.ships)
            #                 if fraction_wars['BLUE'][fleet.fraction] == True:
            #                     fraction_relations['BLUE'] += len(fleet.ships)
            #             battle_with_player(fleet)
            elif fleet.type == 2:
                for other_fleet in fleets:
                    if other_fleet.type == 0 or other_fleet.type == 1 or other_fleet.type == 4:
                        gip = ((other_fleet.x - fleet.x) ** 2 + 6.25 * (other_fleet.y - fleet.y) ** 2) ** 0.5
                        if len(fleet.ships) > 0 and len(other_fleet.ships) > 0 and (
                            fleet in fleets) and (other_fleet in fleets):
                            battle_radius = (ship_stats[other_fleet.ships[0][0]].deck_size + ship_stats[fleet.ships[0][0]].deck_size) / 2
                            if (gip < battle_radius):
                                if other_fleet == fleets[0]:
                                    battle_with_player(fleet)
                                else:
                                    auto_battle_step(fleet, other_fleet)
            elif fleet.type == 3:
                for other_fleet in fleets:
                    if other_fleet.type == 2 or (other_fleet.type == 0 and fraction_relations[fleet.fraction] < 0) or (
                       (other_fleet.type in [0, 1, 3, 4, 5]) and fraction_wars[fleet.fraction][other_fleet.fraction] == True):
                        gip = ((other_fleet.x - fleet.x) ** 2 + 6.25 * (other_fleet.y - fleet.y) ** 2) ** 0.5
                        if len(fleet.ships) > 0 and len(other_fleet.ships) > 0 and (
                            fleet in fleets) and (other_fleet in fleets):
                            battle_radius = (ship_stats[other_fleet.ships[0][0]].deck_size + ship_stats[fleet.ships[0][0]].deck_size) / 2
                            if (gip < battle_radius):
                                if other_fleet == fleets[0]:
                                    if not (player_fraction):
                                        fraction_relations[fleet.fraction] -= len(fleet.ships)
                                        if fraction_wars['RED'][fleet.fraction] == True:
                                            fraction_relations['RED'] += len(fleet.ships)
                                        if fraction_wars['GREEN'][fleet.fraction] == True:
                                            fraction_relations['GREEN'] += len(fleet.ships)
                                        if fraction_wars['BLUE'][fleet.fraction] == True:
                                            fraction_relations['BLUE'] += len(fleet.ships)
                                    battle_with_player(fleet)
                                else:
                                    auto_battle_step(fleet, other_fleet)
            # elif fleet.type == 4:
            #     gip = ((fleets[0].x - fleet.x) ** 2 + 6.25 * (fleets[0].y - fleet.y) ** 2) ** 0.5
            #     if len(fleet.ships) > 0 and len(other_fleet.ships) > 0:
            #         battle_radius = (ship_stats[other_fleet.ships[0][0]].deck_size + ship_stats[fleet.ships[0][0]].deck_size) / 2
            #         if (gip < battle_radius and ((not (player_fraction) and fraction_relations[fleet.fraction] < 0)) or (
            #             player_fraction and fraction_wars['PLAYER'][fleet.fraction] == True)):
            #             if not (player_fraction):
            #                 fraction_relations[fleet.fraction] -= len(fleet.ships)
            #                 if fraction_wars['RED'][fleet.fraction] == True:
            #                     fraction_relations['RED'] += len(fleet.ships)
            #                 if fraction_wars['GREEN'][fleet.fraction] == True:
            #                     fraction_relations['GREEN'] += len(fleet.ships)
            #                 if fraction_wars['BLUE'][fleet.fraction] == True:
            #                     fraction_relations['BLUE'] += len(fleet.ships)
            #             battle_with_player(fleet)
            elif fleet.type == 5:
                for other_fleet in fleets:
                    if (other_fleet.type == 0 and fraction_relations[fleet.fraction] < 0) or (
                       (other_fleet.type in [0, 1, 3, 4, 5]) and fraction_wars[fleet.fraction][other_fleet.fraction] == True):
                        gip = ((other_fleet.x - fleet.x) ** 2 + 6.25 * (other_fleet.y - fleet.y) ** 2) ** 0.5
                        if len(fleet.ships) > 0 and len(other_fleet.ships) > 0 and (
                            fleet in fleets) and (other_fleet in fleets):
                            battle_radius = (ship_stats[other_fleet.ships[0][0]].deck_size + ship_stats[fleet.ships[0][0]].deck_size) / 2
                            if (gip < battle_radius):
                                if other_fleet == fleets[0]:
                                    if not (player_fraction):
                                        fraction_relations[fleet.fraction] -= len(fleet.ships)
                                        if fraction_wars['RED'][fleet.fraction] == True:
                                            fraction_relations['RED'] += len(fleet.ships)
                                        if fraction_wars['GREEN'][fleet.fraction] == True:
                                            fraction_relations['GREEN'] += len(fleet.ships)
                                        if fraction_wars['BLUE'][fleet.fraction] == True:
                                            fraction_relations['BLUE'] += len(fleet.ships)
                                    battle_with_player(fleet)
                                else:
                                    auto_battle_step(fleet, other_fleet)

        f = pygame.font.Font(None, 36)
        forp = f.render(str(sum * 10), True, (255, 0, 0))
        display.blit(forp, (display_width - 80, 50))

        pygame.display.update()

        war_generate = ['RED', 'GREEN', 'BLUE']
        if player_fraction:
            war_generate.append('PLAYER')

        for one_side in war_generate:
            for two_side in war_generate:
                if one_side != two_side:
                    war = randint(0, 1200 * 6)
                    if war == 1200:
                        fraction_wars[one_side][two_side] = not(fraction_wars[one_side][two_side])
                        fraction_wars[two_side][one_side] = not(fraction_wars[two_side][one_side])

        game_time += 1
        if game_time == 4200 * 6:
            for forpost in forposts:
                if forpost[6] == 'grass' or forpost[6] == 'snow':
                    forpost[2] = 4
                elif forpost[6] == 'sand':
                    forpost[2] = 3
        elif game_time == 2400 * 6:
            for forpost in forposts:
                if forpost[6] == 'grass' or forpost[6] == 'snow':
                    forpost[2] = 3
                elif forpost[6] == 'sand':
                    forpost[2] = 2
        elif game_time == 1200 * 6:
            for forpost in forposts:
                if forpost[6] == 'grass' or forpost[6] == 'snow':
                    forpost[2] = 2
        if game_time % (300 * 6) == 0:
            for forpost in forposts:
                if forpost[2] == 1:
                    trade_ship = randint(0, 4)
                    forpost[3] = list(ship_stats.keys())[trade_ship]
                    trade_ship = randint(0, 4)
                    forpost[4] = list(ship_stats.keys())[trade_ship]
                elif forpost[2] == 2:
                    trade_ship = randint(5, 8)
                    forpost[3] = list(ship_stats.keys())[trade_ship]
                    trade_ship = randint(5, 8)
                    forpost[4] = list(ship_stats.keys())[trade_ship]
                elif forpost[2] == 3:
                    trade_ship = randint(9, 11)
                    forpost[3] = list(ship_stats.keys())[trade_ship]
                    trade_ship = randint(9, 11)
                    forpost[4] = list(ship_stats.keys())[trade_ship]
                elif forpost[2] == 4:
                    trade_ship = randint(12, 14)
                    forpost[3] = list(ship_stats.keys())[trade_ship]
                    trade_ship = randint(12, 14)
                    forpost[4] = list(ship_stats.keys())[trade_ship]

        end_game = True
        for forpost in forposts:
            if forpost[5] in ['RED', 'GREEN', 'BLUE']:
                end_game = False
        if end_game:
            game = False
            f = pygame.font.Font(None, 72)
            b = f.render('PLAYER FRACTION WINS!', True, (255, 255, 255))
            b_rect = b.get_rect(center=(0.5 * display_width, 0.5 * display_height))
            display.blit(b, b_rect)
            pygame.display.update()
            time.sleep(3)

        sum += time.clock() - t0
        print("battle ", time.clock() - t0)
        print('SUM:', sum)
        print()

        clock.tick(10)

run_game()