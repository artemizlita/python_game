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
display_width = game_display.display_width
display_height = game_display.display_height
center_x = display_width / 2
center_y = display_height / 2
map_width = 28
map_height = 28
i_width = 540
i_height = 216
island_x = 0
island_y = 0
game_time = 0

display = game_display.display

clock = pygame.time.Clock()

class fleet_object:
    def __init__(self, ships, ms_sail1, ms_sail0, pic_size, deck_size, speed, x, y, target_x, target_y, angle, type,
                 fraction, gold, rank, move=True): #, wood1, wood2, iron, cotton):
        self.ships = ships
        self.ms_sail1 = ms_sail1
        self.ms_sail0 = ms_sail0
        self.pic_size = pic_size
        self.deck_size = deck_size
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
        # self.wood1 = wood1
        # self.wood2 = wood2
        # self.iron = iron
        # self.cotton = cotton

fleets = []

barkas_sail1 = []
barkas_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\barkas\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\barkas\\' + str(i) + '\\sail_0.png')
    barkas_sail1.append(pygame.transform.smoothscale(image_sail_1, (300 / scale, 300 / scale)))
    barkas_sail0.append(pygame.transform.smoothscale(image_sail_0, (300 / scale, 300 / scale)))

pink_sail1 = []
pink_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\pink\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\pink\\' + str(i) + '\\sail_0.png')
    pink_sail1.append(pygame.transform.smoothscale(image_sail_1, (350 / scale, 350 / scale)))
    pink_sail0.append(pygame.transform.smoothscale(image_sail_0, (350 / scale, 350 / scale)))

ladya_sail1 = []
ladya_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\ladya\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\ladya\\' + str(i) + '\\sail_0.png')
    ladya_sail1.append(pygame.transform.smoothscale(image_sail_1, (300 / scale, 300 / scale)))
    ladya_sail0.append(pygame.transform.smoothscale(image_sail_0, (300 / scale, 300 / scale)))

shuna_sail1 = []
shuna_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\shuna\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\shuna\\' + str(i) + '\\sail_0.png')
    shuna_sail1.append(pygame.transform.smoothscale(image_sail_1, (400 / scale, 400 / scale)))
    shuna_sail0.append(pygame.transform.smoothscale(image_sail_0, (400 / scale, 400 / scale)))

lugger_sail1 = []
lugger_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\lugger\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\lugger\\' + str(i) + '\\sail_0.png')
    lugger_sail1.append(pygame.transform.smoothscale(image_sail_1, (500 / scale, 500 / scale)))
    lugger_sail0.append(pygame.transform.smoothscale(image_sail_0, (500 / scale, 500 / scale)))

shlup_sail1 = []
shlup_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\shlup\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\shlup\\' + str(i) + '\\sail_0.png')
    shlup_sail1.append(pygame.transform.smoothscale(image_sail_1, (500 / scale, 500 / scale)))
    shlup_sail0.append(pygame.transform.smoothscale(image_sail_0, (500 / scale, 500 / scale)))

bark_sail1 = []
bark_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\bark\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\bark\\' + str(i) + '\\sail_0.png')
    bark_sail1.append(pygame.transform.smoothscale(image_sail_1, (600 / scale, 600 / scale)))
    bark_sail0.append(pygame.transform.smoothscale(image_sail_0, (600 / scale, 600 / scale)))

fleyt_sail1 = []
fleyt_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\fleyt\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\fleyt\\' + str(i) + '\\sail_0.png')
    fleyt_sail1.append(pygame.transform.smoothscale(image_sail_1, (600 / scale, 600 / scale)))
    fleyt_sail0.append(pygame.transform.smoothscale(image_sail_0, (600 / scale, 600 / scale)))

brig_sail1 = []
brig_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\brig\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\brig\\' + str(i) + '\\sail_0.png')
    brig_sail1.append(pygame.transform.smoothscale(image_sail_1, (700 / scale, 700 / scale)))
    brig_sail0.append(pygame.transform.smoothscale(image_sail_0, (700 / scale, 700 / scale)))

galera_sail1 = []
galera_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\galera\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\galera\\' + str(i) + '\\sail_0.png')
    galera_sail1.append(pygame.transform.smoothscale(image_sail_1, (600 / scale, 600 / scale)))
    galera_sail0.append(pygame.transform.smoothscale(image_sail_0, (600 / scale, 600 / scale)))

pinas_sail1 = []
pinas_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\pinas\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\pinas\\' + str(i) + '\\sail_0.png')
    pinas_sail1.append(pygame.transform.smoothscale(image_sail_1, (900 / scale, 900 / scale)))
    pinas_sail0.append(pygame.transform.smoothscale(image_sail_0, (900 / scale, 900 / scale)))

corvet_sail1 = []
corvet_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\corvet\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\corvet\\' + str(i) + '\\sail_0.png')
    corvet_sail1.append(pygame.transform.smoothscale(image_sail_1, (1000 / scale, 1000 / scale)))
    corvet_sail0.append(pygame.transform.smoothscale(image_sail_0, (1000 / scale, 1000 / scale)))

fregat_sail1 = []
fregat_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\fregat\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\fregat\\' + str(i) + '\\sail_0.png')
    fregat_sail1.append(pygame.transform.smoothscale(image_sail_1, (1100 / scale, 1100 / scale)))
    fregat_sail0.append(pygame.transform.smoothscale(image_sail_0, (1100 / scale, 1100 / scale)))

tradeship_sail1 = []
tradeship_sail0 = []
for i in range(0, 12):
    image_sail_1 = pygame.image.load('global\\tradeship\\' + str(i) + '\\sail_1.png')
    image_sail_0 = pygame.image.load('global\\tradeship\\' + str(i) + '\\sail_0.png')
    tradeship_sail1.append(pygame.transform.smoothscale(image_sail_1, (1300 / scale, 1300 / scale)))
    tradeship_sail0.append(pygame.transform.smoothscale(image_sail_0, (1300 / scale, 1300 / scale)))

ships_dict = {"barkas": [barkas_sail1, barkas_sail0, 300, 70, 1200, 100, 15, 2, 0.8],
              "pink": [pink_sail1, pink_sail0, 350, 70, 1500, 60, 15, 2, 1.2],
              "ladya": [ladya_sail1, ladya_sail0, 300, 75, 1600, 40, 20, 2, 1.2],
              "shuna": [shuna_sail1, shuna_sail0, 400, 90, 2200, 80, 20, 3, 1.2],
              "lugger": [lugger_sail1, lugger_sail0, 500, 100, 3000, 80, 25, 3, 1.6],
              "shlup": [shlup_sail1, shlup_sail0, 500, 100, 3600, 100, 30, 3, 1.2],
              "fleyt": [fleyt_sail1, fleyt_sail0, 600, 120, 4200, 40, 35, 3, 1.6],
              "bark": [bark_sail1, bark_sail0, 600, 120, 5000, 60, 35, 4, 1.6],
              "brig": [brig_sail1, brig_sail0, 700, 140, 7000, 80, 40, 5, 2.0],
              "galera": [galera_sail1, galera_sail0, 600, 170, 10000, 100, 50, 6, 1.6],
              "pinas": [pinas_sail1, pinas_sail0, 900, 190, 12000, 40, 60, 5, 2.0],
              "corvet": [corvet_sail1, corvet_sail0, 1000, 190, 15000, 60, 60, 7, 2.4],
              "fregat": [fregat_sail1, fregat_sail0, 1100, 250, 20000, 80, 75, 8, 2.0],
              "tradeship": [tradeship_sail1, tradeship_sail0, 1300, 270, 22000, 40, 90, 7, 2.4]}

fraction_relations = {'RED': 0, 'GREEN': 0, 'BLUE': 0, 'PIRATE': 0}

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
                                       i[1] + j * i_height - i_height/2, i[0] + i[2] * i_width + i_width*1.5, i[1] + j * i_height + i_height/2):
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
            forposts.append([fx, fy, forpost, list(ships_dict.keys())[trade_ship1], list(ships_dict.keys())[trade_ship2], fraction, land])
        if land == 'sand':
            for i in range(0, width):
                for j in range(0, height):
                    if not ((ax + i * i_width == fx - i_width) and (ay + j * i_height == fy - i_height)):
                        if (j == 0):
                            if i == 0:
                                for k in range(7):
                                    palms.append([randint(ax + i * i_width + 64, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height + 128, ay + (j + 1) * i_height)])
                            elif i == width - 1:
                                for k in range(7):
                                    palms.append([randint(ax + i * i_width, ax + (i + 1) * i_width - 64),
                                                  randint(ay + j * i_height + 128, ay + (j + 1) * i_height)])
                            else:
                                for k in range(8):
                                    palms.append([randint(ax + i * i_width, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height + 128, ay + (j + 1) * i_height)])
                        else:
                            if i == 0:
                                for k in range(14):
                                    palms.append([randint(ax + i * i_width + 64, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height)])
                            elif i == width - 1:
                                for k in range(14):
                                    palms.append([randint(ax + i * i_width, ax + (i + 1) * i_width - 64),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height)])
                            else:
                                for k in range(16):
                                    palms.append([randint(ax + i * i_width, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height)])
            palms.sort(key=palm_key)
        elif land == 'grass':
            for i in range(0, width):
                for j in range(0, height):
                    if not ((ax + i * i_width == fx - i_width) and (ay + j * i_height == fy - i_height)):
                        if (j == 0):
                            if i == 0:
                                for k in range(1):
                                    trees.append([randint(ax + i * i_width + 72, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height + 180, ay + (j + 1) * i_height - 1)])
                            elif i == width - 1:
                                for k in range(1):
                                    trees.append([randint(ax + i * i_width, ax + (i + 1) * i_width - 72),
                                                  randint(ay + j * i_height + 180, ay + (j + 1) * i_height - 1)])
                            else:
                                for k in range(1):
                                    trees.append([randint(ax + i * i_width, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height + 180, ay + (j + 1) * i_height - 1)])
                        else:
                            if i == 0:
                                for k in range(5):
                                    trees.append([randint(ax + i * i_width + 72, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height - 1)])
                            elif i == width - 1:
                                for k in range(5):
                                    trees.append([randint(ax + i * i_width, ax + (i + 1) * i_width - 72),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height - 1)])
                            else:
                                for k in range(6):
                                    trees.append([randint(ax + i * i_width, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height - 1)])
            trees.sort(key=palm_key)
        elif land == 'snow':
            for i in range(0, width):
                for j in range(1, height):
                    if not ((ax + i * i_width == fx - i_width) and (ay + j * i_height == fy - i_height)):
                        if (j == 1):
                            if i == 0:
                                for k in range(6):
                                    ship_trees.append([randint(ax + i * i_width + 72, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height + 72, ay + (j + 1) * i_height - 2)])
                            elif i == width - 1:
                                for k in range(6):
                                    ship_trees.append([randint(ax + i * i_width, ax + (i + 1) * i_width - 72),
                                                  randint(ay + j * i_height + 72, ay + (j + 1) * i_height - 2)])
                            else:
                                for k in range(6):
                                    ship_trees.append([randint(ax + i * i_width, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height + 72, ay + (j + 1) * i_height - 2)])
                        else:
                            if i == 0:
                                for k in range(8):
                                    ship_trees.append([randint(ax + i * i_width + 72, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height - 2)])
                            elif i == width - 1:
                                for k in range(8):
                                    ship_trees.append([randint(ax + i * i_width, ax + (i + 1) * i_width - 72),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height - 2)])
                            else:
                                for k in range(9):
                                    ship_trees.append([randint(ax + i * i_width, ax + (i + 1) * i_width),
                                                  randint(ay + j * i_height, ay + (j + 1) * i_height - 2)])
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
        fleet.x += 0.64 * speed
        fleet.y += -0.32 * speed
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
        fleet.x += 0.63 * speed
        fleet.y += 0.32 * speed
    elif angle == 6:
        fleet.x += 0 * speed
        fleet.y += 0.41 * speed
    elif angle == 7:
        fleet.x += -0.64 * speed
        fleet.y += 0.32 * speed
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

def traders_generate(fleet_rank, fraction):
    our_forposts = []
    for forpost in forposts:
        if forpost[5] == fraction:
            our_forposts.append(forpost)
    f = randint(0, len(our_forposts) - 1)
    x = our_forposts[f][0] + randint(0, i_width) - i_width
    y = our_forposts[f][1] + i_height/2
    k = randint(0, len(forposts) - 1)
    gip = ((forposts[k][0] - i_width/2 + island_x - x) ** 2 + 6.25 * (forposts[k][1] + i_height/2 + island_y - y) ** 2) ** 0.5
    while gip <= i_width/2:
        k = randint(0, len(forposts) - 1)
        gip = ((forposts[k][0] - i_width/2 + island_x - x) ** 2 + 6.25 * (forposts[k][1] + i_height/2 + island_y - y) ** 2) ** 0.5
    target_x = forposts[k][0] - i_width/2
    target_y = forposts[k][1] + i_height/2
    if our_forposts[f][6] == 'sand':
        if our_forposts[f][2] == 1:
            fleets.append(fleet_object([["ladya", 20, 20, 2, 1.2]], ladya_sail1, ladya_sail0, 300, 75, 1.2,
                                       island_x + x, island_y + y, target_x, target_y, 0, 1, fraction, randint(160, 320), fleet_rank))
            guard_type = randint(0, 1)
            if guard_type == 0:
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15, 15, 2, 1.2])
                    fleets[len(fleets) - 1].gold += randint(120, 240)
            else:
                shuna_count = randint(0, 1)
                for j in range(shuna_count):
                    fleets[len(fleets) - 1].ships.append(["shuna", 20, 20, 3, 1.2])
                    fleets[len(fleets) - 1].gold += randint(220, 440)
        elif our_forposts[f][2] == 2:
            fleets.append(fleet_object([["fleyt", 35, 35, 3, 1.6], ["fleyt", 35, 35, 3, 1.6]], fleyt_sail1, fleyt_sail0, 600, 120, 1.6,
                                       island_x + x, island_y + y, target_x, target_y, 0, 1, fraction, randint(450, 900), fleet_rank))
            guard_type = randint(0, 1)
            if guard_type == 0:
                bark_count = randint(0, 1)
                for j in range(bark_count):
                    fleets[len(fleets) - 1].ships.append(["bark", 35, 35, 4, 1.6])
                    fleets[len(fleets) - 1].gold += randint(550, 1100)
            else:
                brig_count = randint(0, 1)
                for j in range(brig_count):
                    fleets[len(fleets) - 1].ships.append(["brig", 40, 40, 5, 2.0])
                    fleets[len(fleets) - 1].gold += randint(700, 1400)
        elif our_forposts[f][2] == 3:
            fleets.append(fleet_object([["pinas", 60, 60, 5, 2.0], ["pinas", 60, 60, 5, 2.0]], pinas_sail1, pinas_sail0, 900, 190, 2.0,
                                       island_x + x, island_y + y, target_x, target_y, 0, 1, fraction, randint(1200, 2400), fleet_rank))
            corvet_count = randint(0, 1)
            for j in range(corvet_count):
                fleets[len(fleets) - 1].ships.append(["corvet", 60, 60, 7, 2.4])
                fleets[len(fleets) - 1].gold += randint(1500, 3000)
    elif our_forposts[f][6] == 'grass':
        if our_forposts[f][2] == 1:
            fleets.append(fleet_object([["ladya", 20, 20, 2, 1.2], ["ladya", 20, 20, 2, 1.2]], ladya_sail1, ladya_sail0, 300, 75, 1.2,
                                       island_x + x, island_y + y, target_x, target_y, 0, 1, fraction, randint(320, 640), fleet_rank))
            pink_count = randint(0, 1)
            for j in range(pink_count):
                fleets[len(fleets) - 1].ships.append(["pink", 15, 15, 2, 1.2])
                fleets[len(fleets) - 1].gold += randint(150, 300)
            shuna_count = randint(0, 1)
            for j in range(shuna_count):
                fleets[len(fleets) - 1].ships.append(["shuna", 20, 20, 3, 1.2])
                fleets[len(fleets) - 1].gold += randint(220, 440)
        elif our_forposts[f][2] == 2:
            fleets.append(fleet_object([["fleyt", 35, 35, 3, 1.6], ["fleyt", 35, 35, 3, 1.6], ["fleyt", 35, 35, 3, 1.6]],
                                       fleyt_sail1, fleyt_sail0, 600, 120, 1.6, island_x + x, island_y + y, target_x, target_y,
                                       0, 1, fraction, randint(900, 1800), fleet_rank))
            bark_count = randint(0, 1)
            for j in range(bark_count):
                fleets[len(fleets) - 1].ships.append(["bark", 35, 35, 4, 1.6])
                fleets[len(fleets) - 1].gold += randint(550, 1100)
            brig_count = randint(0, 1)
            for j in range(brig_count):
                fleets[len(fleets) - 1].ships.append(["brig", 40, 40, 5, 2.0])
                fleets[len(fleets) - 1].gold += randint(700, 1400)
        elif our_forposts[f][2] == 3:
            fleets.append(fleet_object([["pinas", 60, 60, 5, 2.0], ["pinas", 60, 60, 5, 2.0], ["pinas", 60, 60, 5, 2.0]],
                                       pinas_sail1, pinas_sail0, 900, 190, 2.0, island_x + x, island_y + y, target_x, target_y,
                                       0, 1, fraction, randint(2400, 4800), fleet_rank))
            corvet_count = randint(0, 2)
            for j in range(corvet_count):
                fleets[len(fleets) - 1].ships.append(["corvet", 60, 60, 7, 2.4])
                fleets[len(fleets) - 1].gold += randint(1500, 3000)

def pirates_generate(fleet_rank):
    cross_island = True
    while cross_island:
        cross_island = False
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
                               -i_width * 3 / 2, -i_height * 3 / 2, i_width * 3 / 2, i_height * 3 / 2):
            cross_island = True
        for forpost in forposts:
            fx = forpost[0]
            fy = forpost[1]
            if island_intersection(x + island_x, y + island_y, x + island_x, y + island_y,
                                   island_x + fx - 2*i_width, island_y + fy - i_height, island_x + fx + i_width, island_y + fy + 2*i_height):
                cross_island = True
    if islands[i][4] == 'sand':
        if fleet_rank == 0:
            fleet_type = randint(0, 2)
            if fleet_type == 0:
                fleets.append(fleet_object([["barkas", 15, 15, 2, 0.8]], barkas_sail1, barkas_sail0, 300, 70, 0.8,
                                           island_x + x, island_y + y, x, y, 0, 2, '-', randint(120, 240), fleet_rank))
                barkas_count = randint(0, 1)
                for j in range(barkas_count):
                    fleets[len(fleets) - 1].ships.append(["barkas", 15, 15, 2, 0.8])
                    fleets[len(fleets) - 1].gold += randint(120, 240)
            elif fleet_type == 1:
                fleets.append(fleet_object([["pink", 15, 15, 2, 1.2]], pink_sail1, pink_sail0, 350, 70, 1.2,
                                           island_x + x, island_y + y, x, y, 0, 2, '-', randint(150, 300), fleet_rank))
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15, 15, 2, 1.2])
                    fleets[len(fleets) - 1].gold += randint(150, 300)
            elif fleet_type == 2:
                fleets.append(fleet_object([["shuna", 20, 20, 3, 1.2]], shuna_sail1, shuna_sail0, 400, 90, 1.2,
                                           island_x + x, island_y + y, x, y, 0, 2, '-', randint(220, 440), fleet_rank))
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15, 15, 2, 1.2])
                    fleets[len(fleets) - 1].gold += randint(150, 300)
        elif fleet_rank == 1:
            fleet_type = randint(0, 1)
            if fleet_type == 0:
                fleets.append(fleet_object([["shlup", 30, 30, 3, 1.2]], shlup_sail1, shlup_sail0, 500, 100, 1.2,
                                           island_x + x, island_y + y, x, y, 0, 2, 0, randint(350, 700), fleet_rank))
                shlup_count = randint(1, 2)
                for j in range(shlup_count):
                    fleets[len(fleets) - 1].ships.append(["shlup", 30, 30, 3, 1.2])
                    fleets[len(fleets) - 1].gold += randint(350, 700)
            elif fleet_type == 1:
                fleets.append(fleet_object([["bark", 35, 35, 4, 1.6]], bark_sail1, bark_sail0, 600, 120, 1.2,
                                           island_x + x, island_y + y, x, y, 0, 2, 0, randint(550, 1100), fleet_rank))
                bark_count = randint(0, 1)
                for j in range(bark_count):
                    fleets[len(fleets) - 1].ships.append(["bark", 35, 35, 4, 1.6])
                    fleets[len(fleets) - 1].gold += randint(550, 1100)
                shlup_count = randint(0, 1)
                for j in range(shlup_count):
                    fleets[len(fleets) - 1].ships.append(["shlup", 30, 30, 3, 1.2])
                    fleets[len(fleets) - 1].gold += randint(350, 700)
        elif fleet_rank == 2:
            fleets.append(fleet_object([["galera", 50, 50, 6, 1.6]], galera_sail1, galera_sail0, 600, 170, 1.6,
                                        island_x + x, island_y + y, x, y, 0, 2, 0, randint(1000, 2000), fleet_rank))
            galera_count = randint(1, 2)
            for j in range(galera_count):
                fleets[len(fleets) - 1].ships.append(["galera", 50, 50, 6, 1.6])
                fleets[len(fleets) - 1].gold += randint(1000, 2000)
    elif islands[i][4] == 'grass' or islands[i][4] == 'snow':
        if fleet_rank == 0:
            fleet_type = randint(0, 2)
            if fleet_type == 0:
                fleets.append(fleet_object([["pink", 15, 15, 2, 1.2]], pink_sail1, pink_sail0, 350, 90, 0.8,
                                           island_x + x, island_y + y, x, y, 0, 2, '-', randint(150, 300), fleet_rank))
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15, 15, 2, 1.2])
                    fleets[len(fleets) - 1].gold += randint(150, 300)
                barkas_count = randint(1, 2)
                for j in range(barkas_count):
                    fleets[len(fleets) - 1].ships.append(["barkas", 15, 15, 2, 0.8])
                    fleets[len(fleets) - 1].gold += randint(120, 240)
            elif fleet_type == 1:
                fleets.append(fleet_object([["shuna", 20, 20, 3, 1.2]], shuna_sail1, shuna_sail0, 400, 90, 1.2,
                                           island_x + x, island_y + y, x, y, 0, 2, '-', randint(220, 440), fleet_rank))
                shuna_count = randint(0, 1)
                for j in range(shuna_count):
                    fleets[len(fleets) - 1].ships.append(["shuna", 20, 20, 3, 1.2])
                    fleets[len(fleets) - 1].gold += randint(220, 440)
                pink_count = randint(1, 2)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15, 15, 2, 1.2])
                    fleets[len(fleets) - 1].gold += randint(150, 300)
            elif fleet_type == 2:
                fleets.append(fleet_object([["lugger", 25, 25, 3, 1.6]], lugger_sail1, lugger_sail0, 500, 100, 1.2,
                                           island_x + x, island_y + y, x, y, 0, 2, '-', randint(300, 600), fleet_rank))
                shuna_count = 1
                for j in range(shuna_count):
                    fleets[len(fleets) - 1].ships.append(["shuna", 20, 20, 3, 1.2])
                    fleets[len(fleets) - 1].gold += randint(22, 440)
                lugger_count = randint(0, 1)
                for j in range(lugger_count):
                    fleets[len(fleets) - 1].ships.append(["lugger", 25, 25, 3, 1.6])
                    fleets[len(fleets) - 1].gold += randint(300, 600)
                pink_count = randint(0, 1)
                for j in range(pink_count):
                    fleets[len(fleets) - 1].ships.append(["pink", 15, 15, 2, 1.2])
                    fleets[len(fleets) - 1].gold += randint(150, 300)
        elif fleet_rank == 1:
            fleet_type = randint(0, 1)
            if fleet_type == 0:
                fleets.append(fleet_object([["bark", 35, 35, 4, 1.6]], bark_sail1, bark_sail0, 600, 120, 1.2,
                                           island_x + x, island_y + y, x, y, 0, 2, '-', randint(550, 1100), fleet_rank))
                shlup_count = randint(2, 3)
                for j in range(shlup_count):
                    fleets[len(fleets) - 1].ships.append(["shlup", 30, 30, 3, 1.2])
                    fleets[len(fleets) - 1].gold += randint(350, 700)
                bark_count = randint(0, 1)
                for j in range(bark_count):
                    fleets[len(fleets) - 1].ships.append(["bark", 35, 35, 4, 1.6])
                    fleets[len(fleets) - 1].gold += randint(550, 1100)
            elif fleet_type == 1:
                fleets.append(fleet_object([["brig", 40, 40, 5, 2.0]], brig_sail1, brig_sail0, 700, 140, 1.6,
                                           island_x + x, island_y + y, x, y, 0, 2, '-', randint(700, 1400), fleet_rank))
                brig_count = randint(0, 1)
                for j in range(brig_count):
                    fleets[len(fleets) - 1].ships.append(["brig", 40, 40, 5, 2.0])
                    fleets[len(fleets) - 1].gold += randint(700, 1400)
                bark_count = randint(2, 3)
                for j in range(bark_count):
                    fleets[len(fleets) - 1].ships.append(["bark", 35, 35, 4, 1.6])
                    fleets[len(fleets) - 1].gold += randint(550, 1100)
        elif fleet_rank == 2:
            fleets.append(fleet_object([["corvet", 60, 60, 7, 2.4]], corvet_sail1, corvet_sail0, 1000, 190, 1.6,
                                        island_x + x, island_y + y, x, y, 0, 2, 0, randint(1500, 3000), fleet_rank))
            galera_count = randint(2, 3)
            for j in range(galera_count):
                fleets[len(fleets) - 1].ships.append(["galera", 50, 50, 6, 1.6])
                fleets[len(fleets) - 1].gold += randint(1000, 2000)
            corvet_count = randint(0, 1)
            for j in range(corvet_count):
                fleets[len(fleets) - 1].ships.append(["corvet", 60, 60, 7, 2.4])
                fleets[len(fleets) - 1].gold += randint(1500, 3000)

def war_fleet_generate(fleet_rank, fraction):
    towns = []
    for forpost in forposts:
        if forpost[5] == fraction:
            towns.append(forpost)
    f = randint(0, len(towns) - 1)
    x = towns[f][0] + randint(0, i_width) - i_width
    y = towns[f][1] + i_height
    if towns[f][2] == 1:
        fleets.append(fleet_object([["lugger", 25, 25, 3, 1.6]], lugger_sail1, lugger_sail0, 500, 100, 1.6,
                                   island_x + x, island_y + y, x, y, 0, 3, fraction, randint(300, 600), towns[f][2]))
        lugger_count = randint(1, 3)
        for j in range(lugger_count):
            fleets[len(fleets) - 1].ships.append(["lugger", 25, 25, 3, 1.6])
            fleets[len(fleets) - 1].gold += randint(300, 600)
    elif towns[f][2] == 2:
        fleets.append(fleet_object([["brig", 40, 40, 5, 2.0]], brig_sail1, brig_sail0, 700, 140, 2.0,
                                   island_x + x, island_y + y, x, y, 0, 3, fraction, randint(700, 1400), towns[f][2]))
        brig_count = randint(2, 4)
        for j in range(brig_count):
            fleets[len(fleets) - 1].ships.append(["brig", 40, 40, 5, 2.0])
            fleets[len(fleets) - 1].gold += randint(700, 1400)
    elif towns[f][2] == 3:
        fleets.append(fleet_object([["corvet", 60, 60, 7, 2.4]], corvet_sail1, corvet_sail0, 1000, 190, 1.6,
                                   island_x + x, island_y + y, x, y, 0, 2, 0, randint(1500, 3000), towns[f][2]))
        corvet_count = randint(2, 4)
        for j in range(corvet_count):
            fleets[len(fleets) - 1].ships.append(["corvet", 60, 60, 7, 2.4])
            fleets[len(fleets) - 1].gold += randint(1500, 3000)

def fishers_generate(fleet_rank, fraction):
    camps = []
    for forpost in forposts:
        if forpost[5] == fraction:
            camps.append(forpost)
    f = randint(0, len(camps) - 1)
    x = camps[f][0] + randint(0, i_width) - i_width
    y = camps[f][1] + i_height/2
    if camps[f][2] == 1:
        fleets.append(fleet_object([["barkas", 15, 15, 2, 0.8]], barkas_sail1, barkas_sail0, 300, 70, 0.8,
                                    island_x + x, island_y + y, x, y, 0, 4, fraction, 0, camps[f][2]))
        barkas_count = randint(0, 1)
        for j in range(barkas_count):
            fleets[len(fleets) - 1].ships.append(["barkas", 15, 15, 2, 0.8])
            fleets[len(fleets) - 1].gold += 0
    elif camps[f][2] == 2:
        fleets.append(fleet_object([["shlup", 30, 30, 3, 1.2]], shlup_sail1, shlup_sail0, 500, 100, 1.2,
                                   island_x + x, island_y + y, x, y, 0, 4, fraction, 0, camps[f][2]))
        shlup_count = randint(1, 2)
        for j in range(shlup_count):
            fleets[len(fleets) - 1].ships.append(["shlup", 30, 30, 3, 1.2])
            fleets[len(fleets) - 1].gold += 0
    elif camps[f][2] == 3:
        fleets.append(fleet_object([["galera", 50, 50, 6, 1.6]], galera_sail1, galera_sail0, 600, 170, 1.6,
                                   island_x + x, island_y + y, x, y, 0, 4, fraction, 0, camps[f][2]))
        galera_count = randint(1, 2)
        for j in range(galera_count):
            fleets[len(fleets) - 1].ships.append(["galera", 50, 50, 6, 1.6])
            fleets[len(fleets) - 1].gold += 0

def battle_with_player(fleet):
    fleets[0].ships = game_display.battle(fleets[0].ships, fleet.ships)
    if len(fleets[0].ships) > 0:
        fleets[0].gold += fleet.gold
        fleets.remove(fleet)
        rank = randint(0, 1)
        pirates_generate(rank)
        fleets[0].ships.sort(key=ships_speed_key)
        if (len(fleets[0].ships) > 0):
            fleets[0].speed = fleets[0].ships[0][4]
        fleets[0].ships.sort(key=ships_rank_key)
        if (len(fleets[0].ships) > 0):
            fleets[0].ms_sail1 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][0]
            fleets[0].ms_sail0 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][1]
            fleets[0].pic_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][2]
            fleets[0].deck_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][3]
    else:
        quit()

def auto_battle_step(fleet, other_fleet):
    if (len(other_fleet.ships) > 0) and (len(fleet.ships) > 0):
        r1 = randint(0, len(fleet.ships) - 1)
        r2 = randint(0, len(other_fleet.ships) - 1)
        rt1 = randint(0, len(fleet.ships) - 1)
        rt2 = randint(0, len(other_fleet.ships) - 1)
        fleet.ships[rt1][1] -= randint(other_fleet.ships[r2][3] - 2, other_fleet.ships[r2][3])
        other_fleet.ships[rt2][1] -= randint(fleet.ships[r1][3] - 2, fleet.ships[r1][3])
        if fleet.ships[rt1][1] <= 0:
            fleet.ships.remove(fleet.ships[rt1])
            fleet.ships.sort(key=ships_speed_key)
            if (len(fleet.ships) > 0):
                fleet.speed = fleet.ships[0][4]
            fleet.ships.sort(key=ships_rank_key)
            if (len(fleet.ships) > 0):
                fleet.ms_sail1 = ships_dict[fleet.ships[len(fleet.ships) - 1][0]][0]
                fleet.ms_sail0 = ships_dict[fleet.ships[len(fleet.ships) - 1][0]][1]
                fleet.pic_size = ships_dict[fleet.ships[len(fleet.ships) - 1][0]][2]
                fleet.deck_size = ships_dict[fleet.ships[len(fleet.ships) - 1][0]][3]
        if other_fleet.ships[rt2][1] <= 0:
            other_fleet.ships.remove(other_fleet.ships[rt2])
            other_fleet.ships.sort(key=ships_speed_key)
            if (len(other_fleet.ships) > 0):
                other_fleet.speed = other_fleet.ships[0][4]
            other_fleet.ships.sort(key=ships_rank_key)
            if (len(other_fleet.ships) > 0):
                other_fleet.ms_sail1 = ships_dict[other_fleet.ships[len(other_fleet.ships) - 1][0]][0]
                other_fleet.ms_sail0 = ships_dict[other_fleet.ships[len(other_fleet.ships) - 1][0]][1]
                other_fleet.pic_size = ships_dict[other_fleet.ships[len(other_fleet.ships) - 1][0]][2]
                other_fleet.deck_size = ships_dict[other_fleet.ships[len(other_fleet.ships) - 1][0]][3]
    elif (len(other_fleet.ships) > 0) and (len(fleet.ships) == 0):
        sum = 0
        for ship in other_fleet.ships:
            sum += ships_dict[ship[0]][4] // 2
        other_fleet.gold += fleet.gold
        if other_fleet.gold > sum:
            other_fleet.gold = sum
        new_fleet_generate(fleet)
        fleets.remove(fleet)
    elif (len(other_fleet.ships) == 0) and (len(fleet.ships) > 0):
        sum = 0
        for ship in fleet.ships:
            sum += ships_dict[ship[0]][4] // 2
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
    r = randint(0, game_time // 6)
    if r <= 600 and game_time // 6 <= 1800:
        rank = 0
    elif 600 < r <= 1800:
        rank = 1
    else:
        rank = 2
    if fleet.type == 1:
        traders_generate(rank, fleet.fraction)
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
        war_fleet_generate(rank, fleet.fraction)
    elif fleet.type == 4:
        fishers_generate(rank, fleet.fraction)
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

#################################################game_generating########################################################

def run_game():
    global scale, game, game_time
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
        coord = f.render('generate (PIRATE) fraction island; (snow) biom', True, (255, 0, 0))
        display.blit(coord, (10, 10 + text))
        text += 36
        pygame.display.update()

    k = 0
    land = 'snow'
    while k < 100:
        need_island = True
        k = 0
        forp = randint(0, 3)
        if forp == 0:
            forpost = 1
            fraction = 'PIRATE'
        else:
            forpost = 0
            fraction = '-'
        while need_island and k < 100:
            need_island = island_generate(forpost, fraction, 'snow')
            k += 1
        if not (need_island):
            f = pygame.font.Font(None, 36)
            coord = f.render('generate (' + fraction + ') fraction island; (' + land + ') biom', True, (255, 0, 0))
            display.blit(coord, (10, 10 + text))
            text += 36
            pygame.display.update()

    for grass in range(1):
        f = randint(0, 2)
        if f == 0:
            fraction = 'RED'
        elif f == 1:
            fraction = 'GREEN'
        elif f == 2:
            fraction = 'BLUE'
        need_island = True
        while need_island:
            need_island = island_generate(1, fraction, 'grass')
        if not (need_island):
            f = pygame.font.Font(None, 36)
            coord = f.render('generate (' + fraction + ') fraction island; (grass) biom', True, (255, 0, 0))
            display.blit(coord, (10, 10 + text))
            text += 36
            pygame.display.update()

    # for sand in range(map_width // 2 - 8):
    #     f = randint(0, 2)
    #     if f == 0:
    #         fraction = 'RED'
    #     elif f == 1:
    #         fraction = 'GREEN'
    #     elif f == 2:
    #         fraction = 'BLUE'
    #     need_island = True
    #     while need_island:
    #         need_island = island_generate(1, fraction, 'sand')

    k = 0
    land = 'sand'
    while k < 100 or land == 'grass':
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
        else:
            land = 'sand'
        while need_island and k < 100:
            need_island = island_generate(forpost, fraction, land)
            k += 1
        if not(need_island):
            f = pygame.font.Font(None, 36)
            coord = f.render('generate (' + fraction + ') fraction island; (' + land + ') biom', True, (255, 0, 0))
            display.blit(coord, (10, 10 + text))
            text += 36
            pygame.display.update()

    # fleets.append(fleet_object([["tradeship", 90, 90, 7, 2.4]], tradeship_sail1, tradeship_sail0, 1300, 270, 2.4, 0, 0, 0, 0, 0, 0, '-', 1000, 0))
    fleets.append(fleet_object([["pink", 15, 15, 2, 1.2]], pink_sail1, pink_sail0, 350, 75, 1.2, 0, 0, 0, 0, 0, 0, '-', 1000, 0))
    fleets[0].move = False

    for forpost in forposts:
        if forpost[5] != 'PIRATE':
            traders_generate(0, forpost[5])
            war_fleet_generate(0, forpost[5])
            fishers_generate(0, forpost[5])
    for island in islands:
        pirates_generate(0)

    sand_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1ne.png'),
                                            ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nse.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nsw.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nswe.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nw.png'),
                                            ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nwe.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1se.png'),
                                            ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1sw.png'),
                                            ((i_width + 16) / scale, (i_height + 184) / scale))
    sand_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1swe.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))

    grass_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1ne.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nse.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nsw.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nswe.png'),
                                               ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nw.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nwe.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1se.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1sw.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    grass_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1swe.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))

    snow_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1ne.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nse.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nsw.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nswe.png'),
                                               ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nw.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nwe.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1se.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1sw.png'),
                                             ((i_width + 16) / scale, (i_height + 184) / scale))
    snow_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1swe.png'),
                                              ((i_width + 16) / scale, (i_height + 184) / scale))

    image_forpost1 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost1.png'),
                                                  ((i_width + 16) / scale, (i_height + 184) / scale))
    image_forpost2 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost2.png'),
                                                  ((i_width + 16) / scale, (i_height + 184) / scale))
    image_forpost3 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost3.png'),
                                                  ((i_width + 16) / scale, (i_height + 204) / scale))
    image_forpost_zone = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost_zone.png'),
                                                      ((i_width + 16) / scale, (i_height + 184) / scale))

    image_palm = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\palm.png'),
                                              (128 / scale, 256 / scale))
    image_tree = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\tree.png'),
                                              (144 / scale, 376 / scale))
    image_ship_tree = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\ship_tree.png'),
                                              (96 / scale, 576 / scale))

#####################################################start_timer########################################################

    while game:
        sum = 0
        t0 = time.clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((0, 162, 232))

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

########################################################movement########################################################

        t0 = time.clock()

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
                    if island_intersection(fx, fy, fleet.target_x, fleet.target_y, ax - 60, ay - 24, dx + 60, dy + 24):
                        ax -= fleet.deck_size
                        ay -= fleet.deck_size / 2.5
                        dx += fleet.deck_size
                        dy += fleet.deck_size / 2.5
                        if islands_check(fx, fy, ax, ay, 24):
                            if ((ax - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5 < gip:
                                gip = ((ax - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5
                                target_x = ax
                                target_y = ay
                        if islands_check(fx, fy, ax, dy, 24):
                            if ((ax - fleet.target_x) ** 2 + (dy - fleet.target_y) ** 2) ** 0.5 < gip:
                                gip = ((ax - fleet.target_x) ** 2 + (dy - fleet.target_y) ** 2) ** 0.5
                                target_x = ax
                                target_y = dy
                        if islands_check(fx, fy, dx, ay, 24):
                            if ((dx - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5 < gip:
                                gip = ((dx - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5
                                target_x = dx
                                target_y = ay
                        if islands_check(fx, fy, dx, dy, 24):
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
                    fleet_move(fleet, fleet.angle, fleet.speed * 5)
                    if islands_check(fleet.x - island_x, fleet.y - island_y, fleet.x - island_x, fleet.y - island_y, fleet.deck_size / 2.5):
                        if fleet.angle == 6:
                            island_x += 0 * fleet.speed * 5
                            island_y += -0.41 * fleet.speed * 5
                        elif fleet.angle == 7:
                            island_x += 0.64 * fleet.speed * 5
                            island_y += -0.32 * fleet.speed * 5
                        elif fleet.angle == 8:
                            island_x += 0.9 * fleet.speed * 5
                            island_y += -0.2 * fleet.speed * 5
                        elif fleet.angle == 9:
                            island_x += 1.025 * fleet.speed * 5
                            island_y += 0 * fleet.speed * 5
                        elif fleet.angle == 10:
                            island_x += 0.9 * fleet.speed * 5
                            island_y += 0.2 * fleet.speed * 5
                        elif fleet.angle == 11:
                            island_x += 0.64 * fleet.speed * 5
                            island_y += 0.32 * fleet.speed * 5
                        elif fleet.angle == 0:
                            island_x += 0 * fleet.speed * 5
                            island_y += 0.41 * fleet.speed * 5
                        elif fleet.angle == 1:
                            island_x += -0.64 * fleet.speed * 5
                            island_y += 0.32 * fleet.speed * 5
                        elif fleet.angle == 2:
                            island_x += -0.9 * fleet.speed * 5
                            island_y += 0.2 * fleet.speed * 5
                        elif fleet.angle == 3:
                            island_x += -1.025 * fleet.speed * 5
                            island_y += 0 * fleet.speed * 5
                        elif fleet.angle == 4:
                            island_x += -0.9 * fleet.speed * 5
                            island_y += -0.2 * fleet.speed * 5
                        elif fleet.angle == 5:
                            island_x += -0.64 * fleet.speed * 5
                            island_y += -0.32 * fleet.speed * 5
                        for other_fleet in fleets:
                            if other_fleet != fleets[0]:
                                fleet_move(other_fleet, (fleets[0].angle + 6) % 12, fleets[0].speed * 5)
                    else:
                        fleet.move = False
                    fleet.x = 0
                    fleet.y = 0
                else:
                    fleet_move(fleet, fleet.angle, fleet.speed * 5)

        sum += time.clock() - t0
        print("movement ", time.clock() - t0)

###################################################change_target########################################################

        t0 = time.clock()

        for fleet in fleets:
            if fleet != fleets[0]:
                if fleet.type == 1:
                    gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                    if gip < 32:
                        while gip < i_width/2:
                            k = randint(0, len(forposts) - 1)
                            gip = ((forposts[k][0] - i_width/2 + island_x - fleet.x) ** 2 + 6.25 * (forposts[k][1] + i_height/2 + island_y - fleet.y) ** 2) ** 0.5
                        fleet.target_x = forposts[k][0] - i_width/2
                        fleet.target_y = forposts[k][1] + i_height/2
                        profit = 0
                        max = 0
                        for ship in fleet.ships:
                            profit += randint(0, ships_dict[ship[0]][4] // 10)
                            max += ships_dict[ship[0]][4] // 2
                        fleet.gold += profit
                        if fleet.gold > max:
                            fleet.gold = max
                        for ship in fleet.ships:
                            while fleet.gold > 0 and ship[2] > ship[1]:
                                ship[1] += 1
                                fleet.gold -= 80
                            if fleet.gold < 0:
                                ship[1] -= 1
                                fleet.gold += 80
                elif fleet.type == 2:
                    mingip = (fleet.rank + 2) * i_width / 2
                    for other_fleet in fleets:
                        if (other_fleet.type == 0) or (other_fleet.type == 1) or (other_fleet.type == 4):
                            gip = ((fleet.x - other_fleet.x) ** 2 + 6.25 * (fleet.y - other_fleet.y) ** 2) ** 0.5
                            if gip < mingip:
                                fleet.target_x = -island_x + other_fleet.x
                                fleet.target_y = -island_y + other_fleet.y
                                mingip = gip
                    if mingip >= (fleet.rank + 2) * i_width / 2:
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
                    mingip = (fleet.rank + 2) * i_width / 2
                    for other_fleet in fleets:
                        if other_fleet.type == 2 or (other_fleet.type == 0 and fraction_relations[fleet.fraction] < 0):
                            gip = ((fleet.x - other_fleet.x) ** 2 + 6.25 * (fleet.y - other_fleet.y) ** 2) ** 0.5
                            if gip < mingip:
                                fleet.target_x = -island_x + other_fleet.x
                                fleet.target_y = -island_y + other_fleet.y
                                mingip = gip
                    if mingip >= (fleet.rank + 2) * i_width / 2:
                        # gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                        if (-i_width / 2 < fleet.target_x + island_x - fleet.x < i_width / 2) or (
                            -i_height / 2 < fleet.target_y + island_y - fleet.y < i_height / 2):
                            mingip = ((forposts[0][0] - i_width/2 + island_x - fleet.x) ** 2 + 6.25 * (forposts[0][1] + i_height/2 + island_y - fleet.y) ** 2) ** 0.5
                            k = 0
                            for f in range(0, len(forposts)):
                                gip = ((forposts[f][0] - i_width/2 + island_x - fleet.x) ** 2 + 6.25 * (forposts[f][1] + i_height/2 + island_y - fleet.y) ** 2) ** 0.5
                                if gip < mingip:
                                    mingip = gip
                                    k = f
                            fleet.target_x = forposts[k][0] - i_width/2
                            fleet.target_y = forposts[k][1] + i_height/2
                            if mingip < i_width / 2:
                                fleet.move = False
                                fleet_move(fleet, (fleet.angle + 6) % 12, fleet.speed * 5)
                                if fleet.rank == 0:
                                    for ship in fleet.ships:
                                        while fleet.gold > 0 and ship[2] > ship[1]:
                                            ship[1] += 1
                                            fleet.gold -= 80
                                        if fleet.gold < 0:
                                            ship[1] -= 1
                                            fleet.gold += 80
                                        while fleet.gold >= 3000 and len(fleet.ships) < 5:
                                            fleet.gold -= 3000
                                            fleet.ships.append(["lugger", 25, 25, 3, 1.6])
                                elif fleet.rank == 1:
                                    for ship in fleet.ships:
                                        while fleet.gold > 0 and ship[2] > ship[1]:
                                            ship[1] += 1
                                            fleet.gold -= 120
                                        if fleet.gold < 0:
                                            ship[1] -= 1
                                            fleet.gold += 120
                                        while fleet.gold >= 7000 and len(fleet.ships) < 5:
                                            fleet.gold -= 7000
                                            fleet.ships.append(["brig", 40, 40, 5, 2.0])
                                elif fleet.rank == 2:
                                    for ship in fleet.ships:
                                        while fleet.gold > 0 and ship[2] > ship[1]:
                                            ship[1] += 1
                                            fleet.gold -= 160
                                        if fleet.gold < 0:
                                            ship[1] -= 1
                                            fleet.gold += 160
                                        while fleet.gold >= 15000 and len(fleet.ships) < 5:
                                            fleet.gold -= 15000
                                            fleet.ships.append(["corvet", 60, 60, 7, 2.4])
                elif fleet.type == 4:
                    gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                    if gip < 32:
                        mingip = ((forposts[0][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                   forposts[0][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                        k = 0
                        for f in range(0, len(forposts)):
                            gip = ((forposts[f][0] - i_width / 2 + island_x - fleet.x) ** 2 + 6.25 * (
                                    forposts[f][1] + i_height / 2 + island_y - fleet.y) ** 2) ** 0.5
                            if gip < mingip:
                                mingip = gip
                                k = f
                        max_gold = 0
                        for ship in other_fleet.ships:
                            max_gold += ships_dict[ship[0]][4] // 2
                        if mingip < 32 and fleet.gold > 0:
                            fleet.move = False
                            fleet_move(fleet, (fleet.angle + 6) % 12, fleet.speed * 5)
                            if fleet.rank == 0:
                                for ship in fleet.ships:
                                    while fleet.gold > 0 and ship[2] > ship[1]:
                                        ship[1] += 1
                                        fleet.gold -= 80
                                    if fleet.gold < 0:
                                        ship[1] -= 1
                                        fleet.gold += 80
                            elif fleet.rank == 1:
                                for ship in fleet.ships:
                                    while fleet.gold > 0 and ship[2] > ship[1]:
                                        ship[1] += 1
                                        fleet.gold -= 120
                                    if fleet.gold < 0:
                                        ship[1] -= 1
                                        fleet.gold += 120
                            elif fleet.rank == 2:
                                for ship in fleet.ships:
                                    while fleet.gold > 0 and ship[2] > ship[1]:
                                        ship[1] += 1
                                        fleet.gold -= 160
                                    if fleet.gold < 0:
                                        ship[1] -= 1
                                        fleet.gold += 160
                            fleet.gold -= 10
                            if fleet.gold < 0:
                                fleet.gold = 0
                        elif (mingip > i_width) or (fleet.gold > max_gold):
                            fleet.target_x = forposts[k][0] - i_width / 2
                            fleet.target_y = forposts[k][1] + i_height / 2
                        else:
                            in_island = True
                            while in_island:
                                in_island = False
                                fx = -island_x + fleet.x + randint(-i_width / 2, i_width / 2)
                                fy = -island_y + fleet.y + randint(0, i_height / 4)
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
                                fleet.gold += ships_dict[ship[0]][4] // 20

        sum += time.clock() - t0
        print("change_target ", time.clock() - t0)

########################################################painting########################################################

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
                rect = image_palm.get_rect(center=(center_x + (island_x + palm[0]) / scale, center_y + (island_y + palm[1]) / scale))
                surf, r = rot_center(image_palm, rect, 0)
                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting palms ", time.clock() - t0)
        t0 = time.clock()

        for tree in trees:
            if (-display_width - 72 < island_x + tree[0] < display_width + 72) and (
                -display_height - 188 < island_y + tree[1] < display_height + 188):
                rect = image_tree.get_rect(center=(center_x + (island_x + tree[0]) / scale, center_y + (island_y + tree[1]) / scale))
                surf, r = rot_center(image_tree, rect, 0)
                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting trees ", time.clock() - t0)
        t0 = time.clock()

        for ship_tree in ship_trees:
            if (-display_width - 48 < island_x + ship_tree[0] < display_width + 48) and (
                -display_height - 288 < island_y + ship_tree[1] < display_height + 288):
                rect = image_ship_tree.get_rect(center=(center_x + (island_x + ship_tree[0]) / scale, center_y + (island_y + ship_tree[1]) / scale))
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
            if (-display_width - fleet.pic_size < fleet.x < display_width + fleet.pic_size) and (
                -display_height - fleet.pic_size < fleet.y < display_height + fleet.pic_size):
                if fleet.move == True:
                    image = fleet.ms_sail1[fleet.angle]
                else:
                    image = fleet.ms_sail0[fleet.angle]
                rect = image.get_rect(center=(center_x + fleet.x / scale, center_y + fleet.y / scale))
                surf, r = rot_center(image, rect, 0)
                display.blit(surf, r)

        sum += time.clock() - t0
        print("painting fleets ", time.clock() - t0)

##########################################################info##########################################################

        t0 = time.clock()

        for fleet in fleets:
            if (-display_width - fleet.pic_size < fleet.x < display_width + fleet.pic_size) and (
                    -display_height - fleet.pic_size < fleet.y < display_height + fleet.pic_size):
                if fleet.fraction == 'RED':
                    color = (255, 0, 0)
                elif fleet.fraction == 'GREEN':
                    color = (0, 255, 0)
                elif fleet.fraction == 'BLUE':
                    color = (0, 0, 255)
                # f = pygame.font.Font(None, 22)
                # gold = f.render('GOLD: ' + str(int(fleet.gold)), True, (255, 0, 0))
                # display.blit(gold, (center_x + (fleet.x - 50) / scale, center_y + (fleet.y - 70) / scale))
                if fleet.type == 0:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('PLAYER', True, (192, 192, 192))
                    display.blit(info, (center_x + (fleet.x - 50) / scale, center_y + (fleet.y - 48) / scale))
                elif fleet.type == 1:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('TRADERS', True, color)
                    display.blit(info, (center_x + (fleet.x - 70) / scale, center_y + (fleet.y - 48) / scale))
                elif fleet.type == 2:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('PIRATES', True, (64, 64, 64))
                    display.blit(info, (center_x + (fleet.x - 60) / scale, center_y + (fleet.y - 48) / scale))
                elif fleet.type == 3:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('WARRIORS', True, color)
                    display.blit(info, (center_x + (fleet.x - 70) / scale, center_y + (fleet.y - 48) / scale))
                elif fleet.type == 4:
                    f = pygame.font.Font(None, 48 // scale)
                    info = f.render('FISHERS', True, color)
                    display.blit(info, (center_x + (fleet.x - 60) / scale, center_y + (fleet.y - 48) / scale))
                k = 0
                f = pygame.font.SysFont(None, 32 // scale)
                for ship in fleet.ships:
                    info = f.render(ship[0] + " " + str(ship[1]) + "/" + str(ship[2]), True, (0, 0, 0))
                    display.blit(info, (center_x + (fleet.x - 50) / scale, center_y + (fleet.y + k) / scale))
                    k += 32

        sum += time.clock() - t0
        print("info fleets ", time.clock() - t0)
        t0 = time.clock()

        f = pygame.font.Font(None, 36)
        coord = f.render('GOLD: ' + str(int(fleets[0].gold)), True, (255, 0, 0))
        display.blit(coord, (10, 10))
        f = pygame.font.Font(None, 36)
        forp = f.render(str(game_time // 6), True, (255, 0, 0))
        display.blit(forp, (display_width - 80, 10))
        f = pygame.font.Font(None, 20)
        coord = f.render("(m) - minimap       (Esc) - close game", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 90))
        coord = f.render("(a)/(d) - turn            (w)/(s) - move/stop", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 70))
        coord = f.render("buy/sold/repair ships in forpost zone", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 50))
        coord = f.render("(1)/(2)/(3)/(4)/(5) - change flagman ship", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 30))

        f = pygame.font.Font(None, 36)
        forp = f.render('RED relations:      ' + str(fraction_relations['RED']), True, (255, 0, 0))
        display.blit(forp, (display_width - 250, display_height - 108))
        forp = f.render('GREEN relations: ' + str(fraction_relations['GREEN']), True, (0, 255, 0))
        display.blit(forp, (display_width - 250, display_height - 72))
        forp = f.render('BLUE relations:    ' + str(fraction_relations['BLUE']), True, (0, 0, 255))
        display.blit(forp, (display_width - 250, display_height - 36))

        if stop > 0:
            stop -= 1

        sum += time.clock() - t0
        print("info ", time.clock() - t0)

################################################forpost_interface#######################################################

        t0 = time.clock()

        for forpost in forposts:
            fx = forpost[0] - i_width/2
            fy = forpost[1] + i_height/2
            if (-i_width/2 < fx + island_x < i_width/2) and (-i_height/2 < fy + island_y < i_height/2):
                if not(forpost_zone):
                    f = pygame.font.Font(None, 36)
                    b = f.render('press Z to dock', True, (0, 0, 255))
                    display.blit(b, (display_width / 2 - 70, 0.5 * display_height - 50))
                    if fraction_relations[forpost[5]] < 0:
                        f = pygame.font.Font(None, 36)
                        b = f.render('cost ' + str(fraction_relations[forpost[5]] * (-1000)) + ' GOLD', True, (255, 255, 0))
                        display.blit(b, (display_width / 2 - 50, 0.5 * display_height - 14))
                    if keys[pygame.K_z]:
                        if fleets[0].gold > fraction_relations[forpost[5]] * (-1000):
                            fraction_relations[forpost[5]] = 0
                            fleets[0].gold -= fraction_relations[forpost[5]] * (-1000)
                            fleets[0].x = 99999
                            fleets[0].y = 99999
                            fleets[0].move = 0
                            forpost_zone = True
                else:
                    if forpost[2] == 1:
                        forpost_type = 'CAMP'
                    elif forpost[2] == 2:
                        forpost_type = 'TOWN'
                    elif forpost[2] == 3:
                        forpost_type = 'CITY'
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
                    display.blit(forp, (display_width - 80, 10))

                    step = -display_width * 0.4

                    if forpost[3] != '-':
                        name = pygame.font.Font(None, 32)
                        b1 = name.render('buy ship - (Q)', True, (255, 0, 0))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 - 200))
                        image = pygame.transform.smoothscale(ships_dict[forpost[3]][1][(game_time // 5) % 12],
                                                            (ships_dict[forpost[3]][2] / 2, ships_dict[forpost[3]][2] / 2))
                        rect = image.get_rect(center=(0.1 * display_width, center_y * 2 / 3))
                        surf, r = rot_center(image, rect, 0)
                        display.blit(surf, r)
                        name = pygame.font.Font(None, 32)
                        b1 = name.render(forpost[3], True, (0, 0, 0))
                        display.blit(b1, (0.1 * display_width - 30, center_y * 2 / 3 + 30))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('health:  ' + str(ships_dict[forpost[3]][6]) + ' / ' + str(ships_dict[forpost[3]][6]), True, (255, 0, 0))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 + 62))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('speed: ' + str(int(ships_dict[forpost[3]][8] * 5)) + ' knots', True, (0, 0, 255))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 + 86))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('turn speed: ' + str(ships_dict[forpost[3]][5]) + '%', True, (0, 0, 255))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 + 110))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('cost: ' + str(ships_dict[forpost[3]][4]) + ' gold', True, (64, 64, 64))
                        display.blit(b1, (0.1 * display_width - 50, center_y * 2 / 3 + 134))

                    if forpost[4] != '-':
                        name = pygame.font.Font(None, 32)
                        b1 = name.render('buy ship - (E)', True, (255, 0, 0))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 - 200))
                        image = pygame.transform.smoothscale(ships_dict[forpost[4]][1][(game_time // 5) % 12],
                                                            (ships_dict[forpost[4]][2] / 2, ships_dict[forpost[4]][2] / 2))
                        rect = image.get_rect(center=(0.9 * display_width, center_y * 2 / 3))
                        surf, r = rot_center(image, rect, 0)
                        display.blit(surf, r)
                        name = pygame.font.Font(None, 32)
                        b1 = name.render(forpost[4], True, (0, 0, 0))
                        display.blit(b1, (0.9 * display_width - 30, center_y * 2 / 3 + 30))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('health:  ' + str(ships_dict[forpost[4]][6]) + ' / ' + str(ships_dict[forpost[4]][6]), True, (255, 0, 0))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 + 62))
                        b1 = name.render('speed: ' + str(int(ships_dict[forpost[4]][8] * 5)) + ' knots', True, (0, 0, 255))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 + 86))
                        b1 = name.render('turn speed: ' + str(ships_dict[forpost[4]][5]) + '%', True, (0, 0, 255))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 + 110))
                        b1 = name.render('cost: ' + str(ships_dict[forpost[4]][4]) + ' gold', True, (64, 64, 64))
                        display.blit(b1, (0.9 * display_width - 50, center_y * 2 / 3 + 134))

                    for m in range(len(fleets[0].ships)):
                        ship = fleets[0].ships[m]
                        if m == menu:
                            image = pygame.transform.smoothscale(ships_dict[ship[0]][0][(game_time // 5) % 12],
                                                             (ships_dict[ship[0]][2] / 2, ships_dict[ship[0]][2] / 2))
                            color = (0, 0, 255)
                        else:
                            image = pygame.transform.smoothscale(ships_dict[ship[0]][1][(game_time // 5) % 12],
                                                             (ships_dict[ship[0]][2] / 2,ships_dict[ship[0]][2] / 2))
                            color = (0, 0, 0)
                        rect = image.get_rect(center=(center_x + step, center_y * 5 / 3))
                        surf, r = rot_center(image, rect, 0)
                        display.blit(surf, r)
                        name = pygame.font.Font(None, 32)
                        b1 = name.render(ship[0], True, color)
                        display.blit(b1, (center_x + step - 30, center_y * 5 / 3 + 30))
                        name = pygame.font.Font(None, 24)
                        b1 = name.render('health:  ' + str(int(ship[1])) + ' / ' + str(int(ship[2])), True, (255, 0, 0))
                        display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 62))
                        if menu == m:
                            if ships_dict[ship[0]][4] <= 3000:
                                cost = 80
                            else:
                                cost = 120
                            name = pygame.font.Font(None, 24)
                            b1 = name.render('repair: ' + str((ship[2] - ship[1]) * cost) + ' gold - (R)', True, (64, 64, 64))
                            display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 86))
                            name = pygame.font.Font(None, 24)
                            b1 = name.render('sold: ' + str(int(ship[1] / ship[2] * ships_dict[ship[0]][4] // 2)) + ' gold - (T)', True, (64, 64, 64))
                            display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 110))
                        step += display_width * 0.2
                    f = pygame.font.Font(None, 36)
                    b = f.render('press X to leave', True, (255, 0, 0))
                    display.blit(b, (display_width / 2 - 90, 10))
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
                        if ships_dict[fleets[0].ships[menu][0]][4] <= 3000:
                            cost = 80
                        else:
                            cost = 120
                        while fleets[0].gold > 0 and fleets[0].ships[menu][2] > fleets[0].ships[menu][1]:
                            fleets[0].ships[menu][1] += 1
                            fleets[0].gold -= cost
                        if fleets[0].gold < 0:
                            fleets[0].ships[menu][1] -= 1
                            fleets[0].gold += cost
                    elif keys[pygame.K_t]:
                        if stop == 0:
                            if len(fleets[0].ships) >= 2:
                                fleets[0].gold += (fleets[0].ships[menu][1] / fleets[0].ships[menu][2] * ships_dict[fleets[0].ships[menu][0]][4]) // 2
                                fleets[0].ships.remove(fleets[0].ships[menu])
                                stop = 10
                                if menu > len(fleets[0].ships) - 1:
                                    menu -= 1
                                fleets[0].ships.sort(key=ships_speed_key)
                                if (len(fleets[0].ships) > 0):
                                    fleets[0].speed = fleets[0].ships[0][4]
                                fleets[0].ships.sort(key=ships_rank_key)
                                fleets[0].ms_sail1 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][0]
                                fleets[0].ms_sail0 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][1]
                                fleets[0].pic_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][2]
                                fleets[0].deck_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][3]
                    elif keys[pygame.K_q]:
                        if forpost[3] != '-' and (len(fleets[0].ships) < 5) and fleets[0].gold >= ships_dict[forpost[3]][4]:
                            fleets[0].gold -= ships_dict[forpost[3]][4]
                            fleets[0].ships.append([forpost[3], ships_dict[forpost[3]][6], ships_dict[forpost[3]][6],
                                                    ships_dict[forpost[3]][7], ships_dict[forpost[3]][8]])
                            fleets[0].ships.sort(key=ships_speed_key)
                            if (len(fleets[0].ships) > 0):
                                fleets[0].speed = fleets[0].ships[0][4]
                            fleets[0].ships.sort(key=ships_rank_key)
                            fleets[0].ms_sail1 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][0]
                            fleets[0].ms_sail0 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][1]
                            fleets[0].pic_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][2]
                            fleets[0].deck_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][3]
                            forpost[3] = '-'
                    elif keys[pygame.K_e]:
                        if forpost[4] != '-' and (len(fleets[0].ships) < 5) and fleets[0].gold >= ships_dict[forpost[4]][4]:
                            fleets[0].gold -= ships_dict[forpost[4]][4]
                            fleets[0].ships.append([forpost[4], ships_dict[forpost[4]][6], ships_dict[forpost[4]][6],
                                                    ships_dict[forpost[4]][7], ships_dict[forpost[4]][8]])
                            fleets[0].ships.sort(key=ships_speed_key)
                            if (len(fleets[0].ships) > 0):
                                fleets[0].speed = fleets[0].ships[0][4]
                            fleets[0].ships.sort(key=ships_rank_key)
                            fleets[0].ms_sail1 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][0]
                            fleets[0].ms_sail0 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][1]
                            fleets[0].pic_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][2]
                            fleets[0].deck_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][3]
                            forpost[4] = '-'
                    elif keys[pygame.K_x]:
                        fleets[0].x = 0
                        fleets[0].y = 0
                        forpost_zone = False
                        menu = 0

#######################################################minimap##########################################################

        if keys[pygame.K_m]:
            display.fill((0, 162, 232))
            m_sand_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1ne.png'),((i_width+16) / 17, (i_height+184) / 17))
            m_sand_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nse.png'),((i_width+16) / 17, (i_height+184) / 17))
            m_sand_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nsw.png'),((i_width+16) / 17, (i_height+184) / 17))
            m_sand_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nswe.png'),((i_width+16) / 17, (i_height+184) / 17))
            m_sand_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nw.png'),((i_width+16) / 17, (i_height+184) / 17))
            m_sand_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1nwe.png'),((i_width+16) / 17, (i_height+184) / 17))
            m_sand_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1se.png'),((i_width+16) / 17, (i_height+184) / 17))
            m_sand_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1sw.png'),((i_width+16) / 17, (i_height+184) / 17))
            m_sand_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\sand\\1swe.png'),((i_width+16) / 17, (i_height+184) / 17))

            m_grass_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1ne.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_grass_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nse.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_grass_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nsw.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_grass_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nswe.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_grass_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nw.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_grass_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1nwe.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_grass_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1se.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_grass_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1sw.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_grass_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\grass\\1swe.png'),((i_width + 16) / 17, (i_height + 184) / 17))

            m_snow_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1ne.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_snow_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nse.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_snow_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nsw.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_snow_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nswe.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_snow_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nw.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_snow_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1nwe.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_snow_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1se.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_snow_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1sw.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_snow_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\snow\\1swe.png'),((i_width + 16) / 17, (i_height + 184) / 17))

            m_image_forpost1 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost1.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_image_forpost2 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost2.png'),((i_width + 16) / 17, (i_height + 184) / 17))
            m_image_forpost3 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost3.png'),((i_width + 16) / 17, (i_height + 204) / 17))

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
                elif forpost[5] == 'PIRATE':
                    color = (0, 0, 0)
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
            for fleet in fleets:
                if (math.fabs(fleet.x) < display_width) and (math.fabs(fleet.y) < display_height):
                    if fleet.move == True:
                        image = pygame.transform.smoothscale(fleet.ms_sail1[fleet.angle], (fleet.pic_size / 16, fleet.pic_size / 16))
                    else:
                        image = pygame.transform.smoothscale(fleet.ms_sail0[fleet.angle], (fleet.pic_size / 16, fleet.pic_size / 16))
                    rect = image.get_rect(center=(center_x + (fleet.x - island_x) / 16, center_y * 2/3 + (fleet.y - island_y) / 16))
                    surf, r = rot_center(image, rect, 0)
                    display.blit(surf, r)
            step = -display_width * 0.4
            for ship in fleets[0].ships:
                image = pygame.transform.smoothscale(ships_dict[ship[0]][0][(game_time // 5) % 12], (ships_dict[ship[0]][2] / 2, ships_dict[ship[0]][2] / 2))
                rect = image.get_rect(center=(center_x + step, center_y * 5 / 3))
                surf, r = rot_center(image, rect, 0)
                display.blit(surf, r)
                name = pygame.font.Font(None, 32)
                b1 = name.render(ship[0], True, (0, 0, 0))
                display.blit(b1, (center_x + step - 30, center_y * 5 / 3 + 30))
                name = pygame.font.Font(None, 24)
                b1 = name.render('health:  ' + str(int(ship[1])) + ' / ' + str(int(ship[2])), True, (255, 0, 0))
                display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 62))
                name = pygame.font.Font(None, 24)
                b1 = name.render('speed: ' + str(int(ship[4] * 5)) + ' knots', True, (0, 0, 255))
                display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 86))
                name = pygame.font.Font(None, 24)
                b1 = name.render('turn speed: ' + str(ships_dict[ship[0]][5]) + '%', True, (0, 0, 255))
                display.blit(b1, (center_x + step - 50, center_y * 5 / 3 + 110))
                step += display_width * 0.2

        sum += time.clock() - t0
        print("other ", time.clock() - t0)

########################################################battle##########################################################

        t0 = time.clock()

        for fleet in fleets:
            if fleet.type == 0:
                for other_fleet in fleets:
                    if other_fleet.type == 1 or other_fleet.type == 3 or other_fleet.type == 4:
                        gip = ((other_fleet.x - fleet.x) ** 2 + 6.25 * (other_fleet.y - fleet.y) ** 2) ** 0.5
                        if (gip < other_fleet.deck_size + fleet.deck_size):
                            f = pygame.font.Font(None, 36)
                            b = f.render('press F to fight', True, (255, 0, 0))
                            display.blit(b, (display_width / 2 - 70, 0.5 * display_height - 80))
                            if keys[pygame.K_f]:
                                fraction_relations[other_fleet.fraction] -= len(other_fleet.ships)
                                battle_with_player(other_fleet)
            elif fleet.type == 1:
                gip = ((fleets[0].x - fleet.x) ** 2 + 6.25 * (fleets[0].y - fleet.y) ** 2) ** 0.5
                if (gip < fleets[0].deck_size + fleet.deck_size and fraction_relations[fleet.fraction] < 0):
                    fraction_relations[fleet.fraction] -= len(fleet.ships)
                    battle_with_player(fleet)
            elif fleet.type == 2:
                for other_fleet in fleets:
                    if other_fleet.type == 0 or other_fleet.type == 1 or other_fleet.type == 4:
                        gip = ((other_fleet.x - fleet.x) ** 2 + 6.25 * (other_fleet.y - fleet.y) ** 2) ** 0.5
                        if (gip < other_fleet.deck_size + fleet.deck_size) and (fleet.target_x // 1 == (-island_x + other_fleet.x) // 1) and (
                            fleet.target_y // 1 == (-island_y + other_fleet.y) // 1):
                            if other_fleet == fleets[0]:
                                battle_with_player(fleet)
                            else:
                                auto_battle_step(fleet, other_fleet)
            elif fleet.type == 3:
                for other_fleet in fleets:
                    if other_fleet.type == 2 or (other_fleet.type == 0 and fraction_relations[fleet.fraction] < 0):
                        gip = ((other_fleet.x - fleet.x) ** 2 + 6.25 * (other_fleet.y - fleet.y) ** 2) ** 0.5
                        # target_gip = ((other_fleet.x - island_x - other_fleet.target_x) ** 2
                        #               + (other_fleet.y - island_y - other_fleet.target_y) ** 2) ** 0.5
                        if (gip < other_fleet.deck_size + fleet.deck_size) and (fleet.target_x // 1 == (-island_x + other_fleet.x) // 1) and (
                            fleet.target_y // 1 == (-island_y + other_fleet.y) // 1):
                            if other_fleet == fleets[0]:
                                battle_with_player(fleet)
                            else:
                                auto_battle_step(fleet, other_fleet)
            elif fleet.type == 4:
                gip = ((fleets[0].x - fleet.x) ** 2 + 6.25 * (fleets[0].y - fleet.y) ** 2) ** 0.5
                if (gip < fleets[0].deck_size + fleet.deck_size and fraction_relations[fleet.fraction] < 0):
                    fraction_relations[fleet.fraction] -= len(fleet.ships)
                    battle_with_player(fleet)

        f = pygame.font.Font(None, 36)
        forp = f.render(str(sum * 10), True, (255, 0, 0))
        display.blit(forp, (display_width - 80, 50))

        pygame.display.update()
        game_time += 1
        if game_time % (600 * 6) == 0:
            for forpost in forposts:
                if forpost[6] == 'grass':
                    forpost[2] = 2
        if game_time % (1800 * 6) == 0:
            for forpost in forposts:
                if forpost[6] == 'grass':
                    forpost[2] = 3
                elif forpost[6] == 'sand':
                    forpost[2] = 2
        if game_time % (300 * 6) == 0:
            for forpost in forposts:
                if forpost[2] == 1:
                    trade_ship = randint(0, 4)
                    forpost[3] = list(ships_dict.keys())[trade_ship]
                    trade_ship = randint(0, 4)
                    forpost[4] = list(ships_dict.keys())[trade_ship]
                elif forpost[2] == 2:
                    trade_ship = randint(5, 8)
                    forpost[3] = list(ships_dict.keys())[trade_ship]
                    trade_ship = randint(5, 8)
                    forpost[4] = list(ships_dict.keys())[trade_ship]
                elif forpost[2] == 3:
                    trade_ship = randint(9, 12)
                    forpost[3] = list(ships_dict.keys())[trade_ship]
                    trade_ship = randint(9, 12)
                    forpost[4] = list(ships_dict.keys())[trade_ship]

        sum += time.clock() - t0
        print("battle ", time.clock() - t0)
        print('SUM:', sum)
        print()

        clock.tick(10)

run_game()