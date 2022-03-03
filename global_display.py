import pygame
import math
import game_display

pygame.init()
pygame.font.init()

display_width = 1200
display_height = 900
center_x = display_width / 2
center_y = display_height / 2

display = game_display.display

clock = pygame.time.Clock()

class fleet_object:
    def __init__(self, ships, ms_sprites, pic_size, deck_size, speed, x, y, angle): #, gold, wood1, wood2, iron, cotton):
        self.ships = ships
        self.ms_sprites = ms_sprites
        self.pic_size = pic_size
        self.deck_size = deck_size
        self.speed = speed
        self.x = x
        self.y = y
        self.angle = angle
        # self.gold = gold
        # self.wood1 = wood1
        # self.wood2 = wood2
        # self.iron = iron
        # self.cotton = cotton

fleets = []

barkas_sprites = []
for i in range(0, 12):
    barkas_sprites.append(pygame.image.load('global\\barkas\\' + str(i) + '\\sail_1.png'))

ladya_sprites = []
for i in range(0, 12):
    ladya_sprites.append(pygame.image.load('global\\ladya\\' + str(i) + '\\sail_1.png'))

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

    if angle == 0:
        a = 0
    elif angle == 1:
        a = math.atan(6 / 3)
    elif angle == 2:
        a = math.atan(9 / 2)
    elif angle == 3:
        a = 0.5 * pi
    elif angle == 4:
        a = pi - math.atan(9 / 2)
    elif angle == 5:
        a = pi - math.atan(6 / 3)
    elif angle == 6:
        a = pi
    elif angle == 7:
        a = pi + math.atan(6 / 3)
    elif angle == 8:
        a = pi + math.atan(9 / 2)
    elif angle == 9:
        a = 1.5 * pi
    elif angle == 10:
        a = 2 * pi - math.atan(9 / 2)
    elif angle == 11:
        a = 2 * pi - math.atan(6 / 3)

    dif = a - i_angle

    if (-0.99 * pi < dif < -0.01 * pi) or (1.01 * pi < dif < 1.99 * pi):
        fleet.angle -= 1
        if fleet.angle < 0:
            fleet.angle = 11
    elif (-1.99 * pi < dif < -1.01 * pi) or (0.01 * pi < dif < 0.99 * pi):
        fleet.angle += 1
        if fleet.angle >= 12:
            fleet.angle = 0

def run_game():
    scale = 2

    game = True

    fleets.append(fleet_object([("barkas", 15), ("barkas", 15)], barkas_sprites, 200, 70, 0.8, 0, 0, 0))
    fleets.append(fleet_object([("ladya", 20)], ladya_sprites, 200, 75, 1.2, -250, 100, 4))
    fleets.append(fleet_object([("ladya", 20)], ladya_sprites, 200, 75, 1.2, 0, 100, 4))

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((0, 162, 232))

        keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     fleets[0].angle += 1
        # elif keys[pygame.K_s]:
        #     player_angle = 0
        if keys[pygame.K_d]:
            fleets[0].angle += 1
            if fleets[0].angle >= 12:
                fleets[0].angle = 0
        elif keys[pygame.K_a]:
            fleets[0].angle -= 1
            if fleets[0].angle < 0:
                fleets[0].angle = 11
        if keys[pygame.K_1]:
            scale = 1
        elif keys[pygame.K_2]:
            scale = 2
        elif keys[pygame.K_3]:
            scale = 4

        for fleet in fleets:
            if fleet == fleets[0]:
                for other_fleet in fleets:
                    if other_fleet != fleets[0]:
                        fleet_move(other_fleet, (fleets[0].angle + 6) % 12, fleets[0].speed * 5)
            else:
                fleet_move(fleet, fleet.angle, fleet.speed * 5)

        for fleet in fleets:
            if fleet != fleets[0]:
                rotate_to_target(fleet, fleets[0])

        image = pygame.transform.smoothscale(fleets[0].ms_sprites[fleets[0].angle], (fleets[0].pic_size / scale, fleets[0].pic_size / scale))
        rect = image.get_rect(center=(center_x, center_y))
        surf, r = rot_center(image, rect, 0)
        display.blit(surf, r)
        for fleet in fleets:
            if fleet != fleets[0]:
                image = pygame.transform.smoothscale(fleet.ms_sprites[fleet.angle], (fleet.pic_size / scale, fleet.pic_size / scale))
                rect = image.get_rect(center=(center_x + fleet.x / scale, center_y + fleet.y / scale))
                surf, r = rot_center(image, rect, 0)
                display.blit(surf, r)

        for fleet in fleets:
            if fleets[0] != fleet:
                gip = ((fleets[0].x - fleet.x) ** 2 + 6.25 * (fleets[0].y - fleet.y) ** 2) ** 0.5
                if gip < fleets[0].deck_size + fleet.deck_size:
                    fleets[0].ships = game_display.battle(fleets[0].ships, fleet.ships)
                    print(fleets[0].ships)
                    if len(fleets[0].ships) > 0:
                        fleets.remove(fleet)
                    else:
                        game = False

        pygame.display.update()

        clock.tick(10)

run_game()