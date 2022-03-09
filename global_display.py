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

display = game_display.display

clock = pygame.time.Clock()

class fleet_object:
    def __init__(self, ships, ms_sail1, ms_sail0, pic_size, deck_size, speed, x, y, angle, move=True): #, gold, wood1, wood2, iron, cotton):
        self.ships = ships
        self.ms_sail1 = ms_sail1
        self.ms_sail0 = ms_sail0
        self.pic_size = pic_size
        self.deck_size = deck_size
        self.speed = speed
        self.x = x
        self.y = y
        self.angle = angle
        self.move = move
        # self.gold = gold
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

islands = []

forposts = []

palms = []

def palm_key(palm):
    return palm[1]

def island_generate(type, forpost):
    if type == 0:
        width = randint(2, 4)
        height = randint(2, 4)
        ax = (randint(1, 20 - width) - 10) * 384
        ay = (randint(1, 20 - height) - 10) * 128
        w = width * 384
        h = height * 128
        may_be_add = True
        for i in islands:
            if (game_display.dot_in_rect(1, 1, i[0]+1, i[1]+1, i[0] + i[2] * 384+1, i[1]+1, i[0]+1, i[1] + i[3] * 128+1, i[0] + i[2] * 384+1, i[1] + i[3] * 128+1)) or (
                game_display.dot_in_rect(ax - 1, ay - 1, i[0], i[1], i[0] + i[2] * 384, i[1], i[0], i[1] + i[3] * 128, i[0] + i[2] * 384, i[1] + i[3] * 128)) or (
                game_display.dot_in_rect(ax + w + 1, ay - 1, i[0], i[1], i[0] + i[2] * 384, i[1], i[0], i[1] + i[3] * 128, i[0] + i[2] * 384, i[1] + i[3] * 128)) or (
                game_display.dot_in_rect(ax - 1, ay + h + 1, i[0], i[1], i[0] + i[2] * 384, i[1], i[0], i[1] + i[3] * 128, i[0] + i[2] * 384, i[1] + i[3] * 128)) or (
                game_display.dot_in_rect(ax + w + 1, ay + h + 1, i[0], i[1], i[0] + i[2] * 384, i[1], i[0], i[1] + i[3] * 128, i[0] + i[2] * 384, i[1] + i[3] * 128)):
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
                    if not ((ax + i * 384 == fx) and (ay + j * 128 == fy)):
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
        fleet.y += -0.4 * speed
    elif angle == 1:
        fleet.x += 0.6 * speed
        fleet.y += -0.3 * speed
    elif angle == 2:
        fleet.x += 0.9 * speed
        fleet.y += -0.2 * speed
    elif angle == 3:
        fleet.x += 1 * speed
        fleet.y += 0 * speed
    elif angle == 4:
        fleet.x += 0.9 * speed
        fleet.y += 0.2 * speed
    elif angle == 5:
        fleet.x += 0.6 * speed
        fleet.y += 0.3 * speed
    elif angle == 6:
        fleet.x += 0 * speed
        fleet.y += 0.4 * speed
    elif angle == 7:
        fleet.x += -0.6 * speed
        fleet.y += 0.3 * speed
    elif angle == 8:
        fleet.x += -0.9 * speed
        fleet.y += 0.2 * speed
    elif angle == 9:
        fleet.x += -1 * speed
        fleet.y += 0 * speed
    elif angle == 10:
        fleet.x += -0.9 * speed
        fleet.y += -0.2 * speed
    elif angle == 11:
        fleet.x += -0.6 * speed
        fleet.y += -0.3 * speed

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

def rotate_to_target(fleet, target_fleet):
    x1 = fleet.x
    y1 = fleet.y
    x2 = target_fleet.x
    y2 = target_fleet.y
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
        fleet.angle -= 1
        if fleet.angle < 0:
            fleet.angle = 11
        a = angle_to_radian(fleet.angle)
        dif = a - i_angle
        if (-2 * pi < dif < -pi) or (0 < dif < pi):
            fleet.angle += 1
            if fleet.angle >= 12:
                fleet.angle = 0
    elif (-2 * pi < dif < -pi) or (0 < dif < pi):
        fleet.angle += 1
        if fleet.angle >= 12:
            fleet.angle = 0
        a = angle_to_radian(fleet.angle)
        dif = a - i_angle
        if (-pi < dif < 0) or (pi < dif < 2 * pi):
            fleet.angle -= 1
            if fleet.angle < 0:
                fleet.angle = 11

def run_game():
    global scale

    game = True

    island_x = 0
    island_y = 0

    need_forpost = True
    while need_forpost:
        need_forpost = island_generate(0, True)
    need_forpost = True
    while need_forpost:
        need_forpost = island_generate(0, True)
    for k in range(1, 3):
        island_generate(0, False)

    fleets.append(fleet_object([("barkas", 15), ("barkas", 15)], barkas_sail1, barkas_sail0, 300, 70, 0.8, 0, 0, 0))
    fleets.append(fleet_object([("ladya", 20)], ladya_sail1, ladya_sail0, 300, 75, 1.2, -250, 100, 4))
    fleets.append(fleet_object([("shuna", 20)], shuna_sail1, shuna_sail0, 400, 90, 1.2, 500, 100, 4))

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
        if keys[pygame.K_1]:
            scale = 2
        elif keys[pygame.K_2]:
            scale = 4
        elif keys[pygame.K_3]:
            scale = 8

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
                rotate_to_target(fleet, fleets[0])

        for fleet in fleets:
            if fleet.move == True:
                if fleet == fleets[0]:
                    if fleet.angle == 6:
                        island_x += 0 * fleet.speed * 5
                        island_y += -0.4 * fleet.speed * 5
                    elif fleet.angle == 7:
                        island_x += 0.6 * fleet.speed * 5
                        island_y += -0.3 * fleet.speed * 5
                    elif fleet.angle == 8:
                        island_x += 0.9 * fleet.speed * 5
                        island_y += -0.2 * fleet.speed * 5
                    elif fleet.angle == 9:
                        island_x += 1 * fleet.speed * 5
                        island_y += 0 * fleet.speed * 5
                    elif fleet.angle == 10:
                        island_x += 0.9 * fleet.speed * 5
                        island_y += 0.2 * fleet.speed * 5
                    elif fleet.angle == 11:
                        island_x += 0.6 * fleet.speed * 5
                        island_y += 0.3 * fleet.speed * 5
                    elif fleet.angle == 0:
                        island_x += 0 * fleet.speed * 5
                        island_y += 0.4 * fleet.speed * 5
                    elif fleet.angle == 1:
                        island_x += -0.6 * fleet.speed * 5
                        island_y += 0.3 * fleet.speed * 5
                    elif fleet.angle == 2:
                        island_x += -0.9 * fleet.speed * 5
                        island_y += 0.2 * fleet.speed * 5
                    elif fleet.angle == 3:
                        island_x += -1 * fleet.speed * 5
                        island_y += 0 * fleet.speed * 5
                    elif fleet.angle == 4:
                        island_x += -0.9 * fleet.speed * 5
                        island_y += -0.2 * fleet.speed * 5
                    elif fleet.angle == 5:
                        island_x += -0.6 * fleet.speed * 5
                        island_y += -0.3 * fleet.speed * 5
                    for other_fleet in fleets:
                        if other_fleet != fleets[0]:
                            fleet_move(other_fleet, (fleets[0].angle + 6) % 12, fleets[0].speed * 5)
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
            rect = image_forpost1.get_rect(center=(center_x + (island_x + palm[0]) / scale, center_y + (island_y + palm[1]) / scale))
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

########################################################battle##########################################################

        for fleet in fleets:
            if fleets[0] != fleet:
                gip = ((fleets[0].x - fleet.x) ** 2 + 6.25 * (fleets[0].y - fleet.y) ** 2) ** 0.5
                if gip < fleets[0].deck_size + fleet.deck_size:
                    fleets[0].ships = game_display.battle(fleets[0].ships, fleet.ships)
                    if len(fleets[0].ships) > 0:
                        fleets.remove(fleet)
                    else:
                        game = False

        pygame.display.update()

        clock.tick(5)

run_game()