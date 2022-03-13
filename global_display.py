import pygame
import math
import game_display
from random import randint

pygame.init()
pygame.font.init()

scale = 2
display_width = 1200
display_height = 900
center_x = display_width / 2
center_y = display_height / 2
map_width = 20
map_height = 20
island_x = 0
island_y = 0

display = game_display.display

clock = pygame.time.Clock()

class fleet_object:
    def __init__(self, ships, ms_sail1, ms_sail0, pic_size, deck_size, speed, x, y, target_x, target_y, angle, type, gold, move=True): #, wood1, wood2, iron, cotton):
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
        self.move = move
        self.gold = gold
        # self.wood1 = wood1
        # self.wood2 = wood2
        # self.iron = iron
        # self.cotton = cotton

fleets = []

barkas_sail1 = []
barkas_sail0 = []
for i in range(0, 12):
    barkas_sail1.append(pygame.image.load('global\\barkas\\' + str(i) + '\\sail_1.png'))
    barkas_sail0.append(pygame.image.load('global\\barkas\\' + str(i) + '\\sail_0.png'))

pink_sail1 = []
pink_sail0 = []
for i in range(0, 12):
    pink_sail1.append(pygame.image.load('global\\pink\\' + str(i) + '\\sail_1.png'))
    pink_sail0.append(pygame.image.load('global\\pink\\' + str(i) + '\\sail_0.png'))

ladya_sail1 = []
ladya_sail0 = []
for i in range(0, 12):
    ladya_sail1.append(pygame.image.load('global\\ladya\\' + str(i) + '\\sail_1.png'))
    ladya_sail0.append(pygame.image.load('global\\ladya\\' + str(i) + '\\sail_0.png'))

shuna_sail1 = []
shuna_sail0 = []
for i in range(0, 12):
    shuna_sail1.append(pygame.image.load('global\\shuna\\' + str(i) + '\\sail_1.png'))
    shuna_sail0.append(pygame.image.load('global\\shuna\\' + str(i) + '\\sail_0.png'))

ships_dict = {"barkas": [barkas_sail1, barkas_sail0, 300, 70],
              "pink": [pink_sail1, pink_sail0, 375, 70],
              "ladya": [ladya_sail1, ladya_sail0, 300, 75],
              "shuna": [shuna_sail1, shuna_sail0, 400, 90]}

islands = []

forposts = []

palms = []

def island_intersection(x1, y1, x2, y2, ax, ay, dx, dy):
    if x1 == x2 and y1 == y2:
        if (ax <= x1 <= dx) and (ay <= y1 <= dy):
            return True
        else:
            return False
    elif x1 == x2 and y1 != y2:
        if (ax <= x1 <= dx) and ((ay <= y1 <= dy) or (ay <= y2 <= dy)):
            return True
        else:
            return False
    elif x1 != x2 and y1 == y2:
        if ((ax <= x1 <= dx) or (ax <= x2 <= dx)) and (ay <= y1 <= dy):
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

def island_generate(type, forpost):
    if type == 0:
        width = randint(2, 5)
        height = randint(2, 5)
        ax = (randint(0, map_width - width) - map_width // 2) * 384
        ay = (randint(0, map_height - height) - map_height // 2) * 128
        w = width * 384
        h = height * 128
        may_be_add = True
        if 0 >= ax and (ax + w) >= 0 and 0 >= ay and (ay + h) >= 0:
            may_be_add = False
        for i in islands:
            for j in range(i[3] + 2):
                for a in range(width + 3):
                    if island_intersection(ax + a * 384, ay, ax + a * 384, ay + h, i[0] - 192, i[1] + j * 128 - 64, i[0] + i[2] * 384 + 192, i[1] + j * 128 + 64):
                        may_be_add = False
        if may_be_add:
            islands.append([ax, ay, width, height])
            fx = 1
            fy = 1
            if forpost:
                fx = ax + randint(1, width) * 384
                fy = ay + h
                forposts.append([fx, fy])
            for i in range(0, width):
                for j in range(0, height):
                    if not ((ax + i * 384 == fx - 384) and (ay + j * 128 == fy - 128)):
                        for k in range(10):
                            palms.append([randint(ax + i * 384, ax + (i + 1) * 384), randint(ay + j * 128, ay + (j + 1) * 128)])
            palms.sort(key=palm_key)
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
        if (-2 * pi < dif < -pi) or (0 < dif < pi):
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
        if (-pi < dif < 0) or (pi < dif < 2 * pi):
            fleet.move = True
            fleet.angle -= 1
            if fleet.angle < 0:
                fleet.angle = 11

def islands_check(x, y, t_x, t_y, r):
    for i in islands:
        ax = i[0] - 2.5 * r
        ay = i[1] - r
        dx = i[0] + i[2] * 384 + 2.5 * r
        dy = i[1] + i[3] * 128 + r
        if island_intersection(x, y, t_x, t_y, ax, ay, dx, dy):
            return False
    return True

def traders_generate():
    cross_island = True
    while cross_island:
        x = randint(0, map_width * 384) - map_width // 2 * 384
        y = randint(0, map_height * 128) - map_height // 2 * 128
        if islands_check(x, y, x, y, 32):
            cross_island = False
    fleets.append(fleet_object([["ladya", 20, 20, 2, 1.2]], ladya_sail1, ladya_sail0, 300, 75, 1.2,
                               island_x + x, island_y + y, island_x + x, island_y + y, 0, 1, 1000))
    ladya_count = randint(0, 2)
    for j in range(ladya_count):
        fleets[len(fleets) - 1].ships.append(["ladya", 20, 20, 2, 1.2])
        fleets[len(fleets) - 1].gold += 1000

def pirate_generate():
    cross_island = True
    while cross_island:
        x = randint(0, map_width * 384) - map_width // 2 * 384
        y = randint(0, map_height * 128) - map_height // 2 * 128
        if islands_check(x, y, x, y, 32):
            cross_island = False
        if island_intersection(x, y, x, y, -384, -128, 384, 128):
            cross_island = True
    fleet_type = randint(0, 1)
    if fleet_type == 0:
        fleets.append(fleet_object([["barkas", 15, 15, 2, 0.8]], barkas_sail1, barkas_sail0, 300, 70, 0.8,
                                   island_x + x, island_y + y, island_x + x, island_y + y, 0, 2, 500))
        barkas_count = randint(0, 2)
        for j in range(barkas_count):
            fleets[len(fleets) - 1].ships.append(["barkas", 15, 15, 2, 0.8])
            fleets[len(fleets) - 1].gold += 500
    elif fleet_type == 1:
        fleets.append(fleet_object([["pink", 15, 15, 2, 1.2]], pink_sail1, pink_sail0, 350, 90, 1.2,
                                   island_x + x, island_y + y, island_x + x, island_y + y, 0, 2, 500))
        shuna_count = randint(0, 2)
        for j in range(shuna_count):
            fleets[len(fleets) - 1].ships.append(["pink", 15, 15, 2, 0.8, 1.2])
            fleets[len(fleets) - 1].gold += 500

def run_game():
    global scale
    global island_x, island_y
    menu = 0
    game = True
    stop = 0

    for forpost_islands in range(0, 3):
        need_forpost = True
        while need_forpost:
            need_forpost = island_generate(0, True)
    for empty_islands in range(0, 7):
        need_island = True
        k = 0
        while need_island and k < 100:
            need_island = island_generate(0, False)
            k += 1

    fleets.append(fleet_object([["pink", 15, 15, 2, 1.2]], pink_sail1, pink_sail0, 375, 75, 1.2, 0, 0, 0, 0, 0, 0, 5000))
    fleets[0].move = False

    for traders in range(5):
        traders_generate()
    for pirates in range(10):
        pirate_generate()

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((0, 162, 232))

        keys = pygame.key.get_pressed()
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
        # if keys[pygame.K_z]:
        #     if scale < 8:
        #         scale *= 2
        # elif keys[pygame.K_x]:
        #     if scale > 2:
        #         scale //= 2

        image_1 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1.png'), (400 / scale, 240 / scale))
        image_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1ne.png'), (400 / scale, 240 / scale))
        image_1ns = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1ns.png'), (400 / scale, 240 / scale))
        image_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nse.png'), (400 / scale, 240 / scale))
        image_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nsw.png'), (400 / scale, 240 / scale))
        image_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nswe.png'), (400 / scale, 240 / scale))
        image_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nw.png'), (400 / scale, 240 / scale))
        image_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nwe.png'), (400 / scale, 240 / scale))
        image_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1se.png'), (400 / scale, 240 / scale))
        image_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1sw.png'), (400 / scale, 240 / scale))
        image_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1swe.png'), (400 / scale, 240 / scale))
        image_1we = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1we.png'),  (400 / scale, 240 / scale))

        image_forpost1 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost1.png'), (400 / scale, 240 / scale))
        image_forpost_zone = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost_zone.png'), (400 / scale, 240 / scale))

        image_palm = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\palm.png'), (128 / scale, 256 / scale))

########################################################movement########################################################

        for fleet in fleets:
            if fleet != fleets[0]:
                if fleet.type == 1:
                    gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                    if gip < 192:
                        k = randint(0, len(forposts) - 1)
                        fleet.target_x = forposts[k][0] - 192
                        fleet.target_y = forposts[k][1] + 64
                elif fleet.type == 2:
                    mingip = 1000
                    for other_fleet in fleets:
                        if other_fleet.type != 2:
                            gip = ((fleet.x - other_fleet.x) ** 2 + 6.25 * (fleet.y - other_fleet.y) ** 2) ** 0.5
                            if gip < mingip:
                                fleet.target_x = -island_x + other_fleet.x
                                fleet.target_y = -island_y + other_fleet.y
                                mingip = gip
                    if mingip >= 1000:
                        gip = ((fleet.target_x + island_x - fleet.x) ** 2 + 6.25 * (fleet.target_y + island_y - fleet.y) ** 2) ** 0.5
                        if gip < 320:
                            cross_island = True
                            while cross_island:
                                cross_island = False
                                fleet.target_x = island_x + randint(0, 24 * 384) - 12 * 384
                                fleet.target_y = island_y + randint(0, 56 * 128) - 28 * 128
                                for i in islands:
                                    ax = island_x + i[0] - fleet.deck_size
                                    ay = island_y + i[1] - fleet.deck_size / 2.5
                                    dx = island_x + i[0] + i[2] * 384 + fleet.deck_size
                                    dy = island_y + i[1] + i[3] * 128 + fleet.deck_size / 2.5
                                    if game_display.dot_in_rect(fleet.target_x, fleet.target_y, ax, ay, ax, dy, dx, ay, dx, dy):
                                        cross_island = True

        for fleet in fleets:
            if fleet != fleets[0]:
                cross_island = False
                island_angles = []
                fx = fleet.x - island_x
                fy = fleet.y - island_y
                for i in islands:
                    ax = i[0] - 80
                    ay = i[1] - 32
                    dx = i[0] + i[2] * 384 + 80
                    dy = i[1] + i[3] * 128 + 32
                    if island_intersection(fx, fy, fleet.target_x, fleet.target_y, ax, ay, dx, dy):
                        cross_island = True
                        if islands_check(fx, fy, ax, ay, 16):
                            island_angles.append([ax, ay, ((ax - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5])
                        if islands_check(fx, fy, ax, dy, 16):
                            island_angles.append([ax, dy, ((ax - fleet.target_x) ** 2 + (dy - fleet.target_y) ** 2) ** 0.5])
                        if islands_check(fx, fy, dx, ay, 16):
                            island_angles.append([dx, ay, ((dx - fleet.target_x) ** 2 + (ay - fleet.target_y) ** 2) ** 0.5])
                        if islands_check(fx, fy, dx, dy, 16):
                            island_angles.append([dx, dy, ((dx - fleet.target_x) ** 2 + (dy - fleet.target_y) ** 2) ** 0.5])
                if cross_island and len(island_angles) > 0:
                    island_angles.sort(key=ways_key)
                    rotate_to_target(fleet, island_x + island_angles[0][0], island_y + island_angles[0][1])
                else:
                    rotate_to_target(fleet, island_x + fleet.target_x, island_y + fleet.target_y)

        for fleet in fleets:
            if fleet.move == True:
                if fleet == fleets[0]:
                    fleet_move(fleet, fleet.angle, fleet.speed * 5)
                    if islands_check(fleet.x - island_x, fleet.y - island_y, fleet.x - island_x, fleet.y - island_y, 40):
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

########################################################painting########################################################

        for island in islands:
            ax = island[0]
            ay = island[1]
            w = island[2]
            h = island[3]
            for i in range(1, w + 1):
                for j in range(1, h + 1):
                    if i == 1 and j == 1:
                        rect = image_1se.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1se, rect, 0)
                    elif i == w and j == 1:
                        rect = image_1sw.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1sw, rect, 0)
                    elif i == 1 and j == h:
                        rect = image_1ne.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1ne, rect, 0)
                    elif i == w and j == h:
                        rect = image_1nw.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1nw, rect, 0)
                    elif i == 1 and j != 1 and j != h:
                        rect = image_1nse.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1nse, rect, 0)
                    elif i == w and j != 1 and j != h:
                        rect = image_1nsw.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1nsw, rect, 0)
                    elif i != 1 and i != w and j == 1:
                        rect = image_1swe.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1swe, rect, 0)
                    elif i != 1 and i != w and j == h:
                        rect = image_1nwe.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1nwe, rect, 0)
                    else:
                        rect = image_1nswe.get_rect(center=(center_x + (island_x + ax + 384 * i - 192) / scale, center_y + (island_y + ay + 128 * j - 64) / scale))
                        surf, r = rot_center(image_1nswe, rect, 0)
                    display.blit(surf, r)

        for forpost in forposts:
            fx = forpost[0]
            fy = forpost[1]
            rect = image_forpost1.get_rect(center=(center_x + (island_x + fx - 192) / scale, center_y + (island_y + fy - 64) / scale))
            surf, r = rot_center(image_forpost1, rect, 0)
            display.blit(surf, r)
            rect = image_forpost_zone.get_rect(center=(center_x + (island_x + fx - 192) / scale, center_y + (island_y + fy + 64) / scale))
            surf, r = rot_center(image_forpost_zone, rect, 0)
            display.blit(surf, r)

        for palm in palms:
            rect = image_palm.get_rect(center=(center_x + (island_x + palm[0]) / scale, center_y + (island_y + palm[1]) / scale))
            surf, r = rot_center(image_palm, rect, 0)
            display.blit(surf, r)

        for fleet in fleets:
            if fleet.move == True:
                image = pygame.transform.smoothscale(fleet.ms_sail1[fleet.angle], (fleet.pic_size / scale, fleet.pic_size / scale))
            else:
                image = pygame.transform.smoothscale(fleet.ms_sail0[fleet.angle], (fleet.pic_size / scale, fleet.pic_size / scale))
            rect = image.get_rect(center=(center_x + fleet.x / scale, center_y + fleet.y / scale))
            surf, r = rot_center(image, rect, 0)
            display.blit(surf, r)

##########################################################info##########################################################

        for fleet in fleets:
            if fleet.type == 0:
                f = pygame.font.Font(None, 48 // scale)
                info = f.render('PLAYER', True, (0, 255, 0))
                display.blit(info, (center_x + (fleet.x - 50) / scale, center_y + (fleet.y - 48) / scale))
            elif fleet.type == 1:
                f = pygame.font.Font(None, 48 // scale)
                info = f.render('TRADERS', True, (0, 0, 255))
                display.blit(info, (center_x + (fleet.x - 70) / scale, center_y + (fleet.y - 48) / scale))
            elif fleet.type == 2:
                f = pygame.font.Font(None, 48 // scale)
                info = f.render('PIRATES', True, (128, 128, 128))
                display.blit(info, (center_x + (fleet.x - 60) / scale, center_y + (fleet.y - 48) / scale))
            k = 0
            for ship in fleet.ships:
                f = pygame.font.Font(None, 32 // scale)
                info = f.render(ship[0] + ' ' + str(ship[1]) + '/' + str(ship[2]), True, (0, 0, 0))
                display.blit(info, (center_x + (fleet.x - 50) / scale, center_y + (fleet.y + k) / scale))
                k += 32

        f = pygame.font.Font(None, 36)
        coord = f.render('GOLD: ' + str(fleets[0].gold), True, (255, 255, 0))
        display.blit(coord, (1050, 10))

        for forpost in forposts:
            fx = forpost[0] - 192
            fy = forpost[1] + 64
            gip = ((fx + island_x) ** 2 + 6.25 * (fy + island_y) ** 2) ** 0.5
            if gip < 192:
                if keys[pygame.K_r]:
                    menu = 0
                elif keys[pygame.K_b]:
                    menu = 1
                if stop > 0:
                    stop -= 1
                if menu == 0:
                    step = 0
                    for ship in fleets[0].ships:
                        f = pygame.font.Font(None, 30)
                        b = f.render("repair " + str(ship[0]) + " - " + str((ship[2] - ship[1]) * 50) + " gold " + str(step + 1), True, (255, 0, 0))
                        display.blit(b, (480, 400 + 30 * step))
                        step += 1
                    b6 = f.render("buy ship - (b)   repair - (r)", True, (0, 0, 0))
                    display.blit(b6, (480, 550))
                    b7 = f.render("sold ship - (s)", True, (0, 0, 0))
                    display.blit(b7, (480, 580))
                    keys = pygame.key.get_pressed()
                    if (stop == 0) and (len(fleets[0].ships) <= 5):
                        if keys[pygame.K_1]:
                            while fleets[0].gold > 0 and fleets[0].ships[0][2] > fleets[0].ships[0][1]:
                                fleets[0].ships[0][1] += 1
                                fleets[0].gold -= 50
                            if fleets[0].gold < 0:
                                fleets[0].ships[0][1] -= 1
                                fleets[0].gold += 50
                        elif keys[pygame.K_2]:
                            if len(fleets[0].ships) >= 2:
                                while fleets[0].gold > 0 and fleets[0].ships[1][2] > fleets[0].ships[1][1]:
                                    fleets[0].ships[1][1] += 1
                                    fleets[0].gold -= 50
                                if fleets[0].gold < 0:
                                    fleets[0].ships[1][1] -= 1
                                    fleets[0].gold += 50
                        elif keys[pygame.K_3]:
                            if len(fleets[0].ships) >= 3:
                                while fleets[0].gold > 0 and fleets[0].ships[2][2] > fleets[0].ships[2][1]:
                                    fleets[0].ships[2][1] += 1
                                    fleets[0].gold -= 50
                                if fleets[0].gold < 0:
                                    fleets[0].ships[2][1] -= 1
                                    fleets[0].gold += 50
                        elif keys[pygame.K_4]:
                            if len(fleets[0].ships) >= 4:
                                while fleets[0].gold > 0 and fleets[0].ships[3][2] > fleets[0].ships[3][1]:
                                    fleets[0].ships[3][1] += 1
                                    fleets[0].gold -= 50
                                if fleets[0].gold < 0:
                                    fleets[0].ships[3][1] -= 1
                                    fleets[0].gold += 50
                        elif keys[pygame.K_5]:
                            if len(fleets[0].ships) >= 5:
                                while fleets[0].gold > 0 and fleets[0].ships[4][2] > fleets[0].ships[4][1]:
                                    fleets[0].ships[4][1] += 1
                                    fleets[0].gold -= 50
                                if fleets[0].gold < 0:
                                    fleets[0].ships[4][1] -= 1
                                    fleets[0].gold += 50
                elif menu == 1:
                    f = pygame.font.Font(None, 30)
                    b1 = f.render("buy barkas - 800 gold - (1)", True, (255, 0, 0))
                    display.blit(b1, (480, 400))
                    b2 = f.render("buy pink - 1000 gold - (2)", True, (255, 0, 0))
                    display.blit(b2, (480, 430))
                    b3 = f.render("buy ladya - 1200 gold - (3)", True, (255, 0, 0))
                    display.blit(b3, (480, 460))
                    b4 = f.render("buy shuna - 1500 gold - (4)", True, (255, 0, 0))
                    display.blit(b4, (480, 490))
                    b5 = f.render("buy lugger - 2500 gold - (5)", True, (255, 0, 0))
                    display.blit(b5, (480, 520))
                    b6 = f.render("buy ship - (b)   repair - (r)", True, (0, 0, 0))
                    display.blit(b6, (480, 550))
                    b7 = f.render("sold ship - (s)", True, (0, 0, 0))
                    display.blit(b7, (480, 580))
                    keys = pygame.key.get_pressed()
                    if (stop == 0) and (len(fleets[0].ships) < 5):
                        if keys[pygame.K_1] and fleets[0].gold >= 800:
                            fleets[0].gold -= 800
                            fleets[0].ships.append(["barkas", 15, 15, 2])
                            stop = 10
                            if 0.8 < fleets[0].speed:
                                fleets[0].speed = 0.8
                        elif keys[pygame.K_2] and fleets[0].gold >= 1000:
                            fleets[0].gold -= 1000
                            fleets[0].ships.append(["pink", 15, 15, 2])
                            stop = 10
                            if 1.2 < fleets[0].speed:
                                fleets[0].speed = 1.2
                        elif keys[pygame.K_3] and fleets[0].gold >= 1200:
                            fleets[0].gold -= 1200
                            fleets[0].ships.append(["ladya", 20, 20, 2])
                            stop = 10
                            if 1.2 < fleets[0].speed:
                                fleets[0].speed = 1.2
                        elif keys[pygame.K_4] and fleets[0].gold >= 1500:
                            fleets[0].gold -= 1500
                            fleets[0].ships.append(["shuna", 20, 20, 3])
                            stop = 10
                            if 1.2 < fleets[0].speed:
                                fleets[0].speed = 1.2
                        fleets[0].ships.sort(key=ships_rank_key)
                        fleets[0].ms_sail1 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][0]
                        fleets[0].ms_sail0 = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][1]
                        fleets[0].pic_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][2]
                        fleets[0].deck_size = ships_dict[fleets[0].ships[len(fleets[0].ships) - 1][0]][3]

########################################################battle##########################################################

        if keys[pygame.K_m]:
            display.fill((0, 162, 232))
            image_1 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1.png'),(400 / 16, 240 / 16))
            image_1ne = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1ne.png'),(400 / 16, 240 / 16))
            image_1ns = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1ns.png'),(400 / 16, 240 / 16))
            image_1nse = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nse.png'),(400 / 16, 240 / 16))
            image_1nsw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nsw.png'),(400 / 16, 240 / 16))
            image_1nswe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nswe.png'),(400 / 16, 240 / 16))
            image_1nw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nw.png'),(400 / 16, 240 / 16))
            image_1nwe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1nwe.png'),(400 / 16, 240 / 16))
            image_1se = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1se.png'),(400 / 16, 240 / 16))
            image_1sw = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1sw.png'),(400 / 16, 240 / 16))
            image_1swe = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1swe.png'),(400 / 16, 240 / 16))
            image_1we = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\1we.png'),(400 / 16, 240 / 16))
            image_forpost1 = pygame.transform.smoothscale(pygame.image.load('global\\island_sprite\\forpost1.png'),(400 / 16, 240 / 16))

            for island in islands:
                ax = island[0]
                ay = island[1]
                w = island[2]
                h = island[3]
                for i in range(1, w + 1):
                    for j in range(1, h + 1):
                        if i == 1 and j == 1:
                            rect = image_1se.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                              center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1se, rect, 0)
                        elif i == w and j == 1:
                            rect = image_1sw.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                              center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1sw, rect, 0)
                        elif i == 1 and j == h:
                            rect = image_1ne.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                              center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1ne, rect, 0)
                        elif i == w and j == h:
                            rect = image_1nw.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                              center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1nw, rect, 0)
                        elif i == 1 and j != 1 and j != h:
                            rect = image_1nse.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                               center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1nse, rect, 0)
                        elif i == w and j != 1 and j != h:
                            rect = image_1nsw.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                               center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1nsw, rect, 0)
                        elif i != 1 and i != w and j == 1:
                            rect = image_1swe.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                               center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1swe, rect, 0)
                        elif i != 1 and i != w and j == h:
                            rect = image_1nwe.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                               center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1nwe, rect, 0)
                        else:
                            rect = image_1nswe.get_rect(center=(center_x + (ax + 384 * i - 192) / 16,
                                                                center_y + (ay + 128 * j - 64) / 16))
                            surf, r = rot_center(image_1nswe, rect, 0)
                        display.blit(surf, r)
            for forpost in forposts:
                fx = forpost[0]
                fy = forpost[1]
                rect = image_forpost1.get_rect(center=(center_x + (fx - 192) / 16, center_y + (fy - 64) / 16))
                surf, r = rot_center(image_forpost1, rect, 0)
                display.blit(surf, r)
            for fleet in fleets:
                if (math.fabs(fleet.x) < display_width) and (math.fabs(fleet.y) < display_height):
                    if fleet.move == True:
                        image = pygame.transform.smoothscale(fleet.ms_sail1[fleet.angle], (fleet.pic_size / 16, fleet.pic_size / 16))
                    else:
                        image = pygame.transform.smoothscale(fleet.ms_sail0[fleet.angle], (fleet.pic_size / 16, fleet.pic_size / 16))
                    rect = image.get_rect(center=(center_x + (fleet.x - island_x) / 16, center_y + (fleet.y - island_y) / 16))
                    surf, r = rot_center(image, rect, 0)
                    display.blit(surf, r)

        for fleet in fleets:
            if fleet.type == 2:
                for other_fleet in fleets:
                    if (other_fleet.type != 2):
                        gip = ((other_fleet.x - fleet.x) ** 2 + 6.25 * (other_fleet.y - fleet.y) ** 2) ** 0.5
                        if gip < other_fleet.deck_size + fleet.deck_size:
                            if other_fleet == fleets[0]:
                                fleets[0].ships = game_display.battle(fleets[0].ships, fleet.ships)
                                if len(fleets[0].ships) > 0:
                                    fleets[0].gold += fleet.gold
                                    fleets.remove(fleet)
                                else:
                                    game = 0
                            elif other_fleet.type == 1:
                                if (len(other_fleet.ships) > 0) and (len(fleet.ships) > 0):
                                    r1 = randint(0, len(fleet.ships) - 1)
                                    r2 = randint(0, len(other_fleet.ships) - 1)
                                    rt1 = randint(0, len(fleet.ships) - 1)
                                    rt2 = randint(0, len(other_fleet.ships) - 1)
                                    fleet.ships[rt1][1] -= randint(0, other_fleet.ships[r2][3])
                                    other_fleet.ships[rt2][1] -= randint(0, fleet.ships[r1][3])
                                    if fleet.ships[rt1][1] < 0:
                                        fleet.ships.remove(fleet.ships[rt1])
                                        fleet.ships.sort(key=ships_speed_key)
                                        if (len(fleet.ships) > 0):
                                            fleet.speed = fleet.ships[0][4]
                                        fleet.ships.sort(key=ships_rank_key)
                                        if (len(fleet.ships) > 0):
                                            fleet.ms_sail1 = ships_dict[fleet.ships[0][0]][0]
                                            fleet.ms_sail0 = ships_dict[fleet.ships[0][0]][1]
                                            fleet.pic_size = ships_dict[fleet.ships[0][0]][2]
                                            fleet.deck_size = ships_dict[fleet.ships[0][0]][3]
                                    if other_fleet.ships[rt2][1] < 0:
                                        other_fleet.ships.remove(other_fleet.ships[rt2])
                                        other_fleet.ships.sort(key=ships_speed_key)
                                        if (len(other_fleet.ships) > 0):
                                            other_fleet.speed = other_fleet.ships[0][4]
                                        other_fleet.ships.sort(key=ships_rank_key)
                                        if (len(other_fleet.ships) > 0):
                                            other_fleet.ms_sail1 = ships_dict[other_fleet.ships[0][0]][0]
                                            other_fleet.ms_sail0 = ships_dict[other_fleet.ships[0][0]][1]
                                            other_fleet.pic_size = ships_dict[other_fleet.ships[0][0]][2]
                                            other_fleet.deck_size = ships_dict[other_fleet.ships[0][0]][3]
                                elif (len(other_fleet.ships) > 0) and (len(fleet.ships) == 0):
                                    other_fleet.gold += fleet.gold
                                    fleets.remove(fleet)
                                    pirate_generate()
                                elif (len(other_fleet.ships) == 0) and (len(fleet.ships) > 0):
                                    fleet.gold += other_fleet.gold
                                    fleets.remove(other_fleet)
                                    traders_generate()
                                else:
                                    fleets.remove(fleet)
                                    fleets.remove(other_fleet)
                                    pirate_generate()
                                    traders_generate()

        pygame.display.update()

        clock.tick(10)

run_game()