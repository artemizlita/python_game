import pygame
import math
from random import randint

pygame.init()
pygame.font.init()

# display = pygame.display.set_mode((display_width, display_height))
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display_width = display.get_width()
display_height = display.get_height()
scale = 4
center_x = display_width / 2
center_y = display_height / 2
wave_step = 0

pygame.display.set_caption('Ship game')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#####################################################class##############################################################

class ship_type:
    def __init__(self, pic_move, pic_stay, deck_width, deck_height, speed, t_speed, gun_distance, max_hp, guns_left, guns_right):
        self.pic_move = pic_move
        self.pic_stay = pic_stay
        self.deck_width = deck_width
        self.deck_height = deck_height
        self.speed = speed
        self.t_speed = t_speed
        self.gun_distance = gun_distance
        self.max_hp = max_hp
        self.guns_left = guns_left
        self.guns_right = guns_right

class ship_object(ship_type):
    def __init__(self, x, y, angle, type, hp, cd_left = 0, cd_right = 0, cd_sail = 0, move=True, target = -1):
        self.x = x
        self.y = y
        self.angle = angle
        self.type = type
        self.hp = hp
        self.ship_type = ship_type
        self.cd_left = cd_left
        self.cd_right = cd_right
        self.cd_sail = cd_sail
        self.move = move
        self.target = target
        if (type == "barkas"):
            super().__init__(barkas_move, barkas_stay, barkas_deck_width, barkas_deck_height, 0.8, 1.0, 30, 15, barkas_guns_left, barkas_guns_right)
        elif (type == "pink"):
            super().__init__(pink_move, pink_stay, pink_deck_width, pink_deck_height, 1.2, 0.6, 30, 15, pink_guns_left, pink_guns_right)
        elif (type == "ladya"):
            super().__init__(ladya_move, ladya_stay, ladya_deck_width, ladya_deck_height, 1.2, 0.4, 30, 20, ladya_guns_left, ladya_guns_right)
        elif (type == "shuna"):
            super().__init__(shuna_move, shuna_stay, shuna_deck_width, shuna_deck_height, 1.2, 0.8, 30, 20, shuna_guns_left, shuna_guns_right)
        elif (type == "lugger"):
            super().__init__(lugger_move, lugger_stay, lugger_deck_width, lugger_deck_height, 1.6, 0.8, 30, 25, lugger_guns_left, lugger_guns_right)
        elif (type == "shlup"):
            super().__init__(shlup_move, shlup_stay, shlup_deck_width, shlup_deck_height, 1.2, 1.0, 40, 30, shlup_guns_left, shlup_guns_right)
        elif (type == "bark"):
            super().__init__(bark_move, bark_stay, bark_deck_width, bark_deck_height, 1.6, 0.6, 40, 35, bark_guns_left, bark_guns_right)
        elif (type == "fleyt"):
            super().__init__(fleyt_move, fleyt_stay, fleyt_deck_width, fleyt_deck_height, 1.6, 0.4, 40, 40, fleyt_guns_left, fleyt_guns_right)
        elif (type == "brig"):
            super().__init__(brig_move, brig_stay, brig_deck_width, brig_deck_height, 2.0, 0.8, 40, 40, brig_guns_left, brig_guns_right)
        elif (type == "pinas"):
            super().__init__(pinas_move, pinas_stay, pinas_deck_width, pinas_deck_height, 2.0, 0.4, 50, 60, pinas_guns_left, pinas_guns_right)
        elif (type == "galera"):
            super().__init__(galera_move, galera_stay, galera_deck_width, galera_deck_height, 1.6, 1.0, 50, 50, galera_guns_left, galera_guns_right)
        elif (type == "corvet"):
            super().__init__(corvet_move, corvet_stay, corvet_deck_width, corvet_deck_height, 2.4, 0.6, 50, 60, corvet_guns_left, corvet_guns_right)
        elif (type == "fregat"):
            super().__init__(fregat_move, fregat_stay, fregat_deck_width, fregat_deck_height, 2.0, 0.8, 60, 75, fregat_guns_left, fregat_guns_right)
        elif (type == "tradeship"):
            super().__init__(tradeship_move, tradeship_stay, tradeship_deck_width, tradeship_deck_height, 2.4, 0.4, 60, 90, tradeship_guns_left, tradeship_guns_right)
        elif (type == "warship"):
            super().__init__(warship_move, warship_stay, warship_deck_width, warship_deck_height, 2.4, 0.8, 60, 90, warship_guns_left, warship_guns_right)
    def get_width(self):
        return self.pic_move.get_width() / scale
    def get_height(self):
        return self.pic_move.get_height() / scale

#################################################create_ships###########################################################

kernel_image = pygame.image.load('kernel.png')
kernel_hit_image = pygame.image.load('kernel_hit.png')
kernel_miss_image = pygame.image.load('kernel_miss.png')

wave_step = []
wave_step.append(pygame.image.load('battle\\waves\\1.png'))
wave_step.append(pygame.image.load('battle\\waves\\2.png'))
wave_step.append(pygame.image.load('battle\\waves\\3.png'))
wave_step.append(pygame.image.load('battle\\waves\\4.png'))
wave_step.append(pygame.image.load('battle\\waves\\5.png'))
wave_step.append(pygame.image.load('battle\\waves\\6.png'))

barkas_move = pygame.image.load('battle\\barkas\\sail_1.png')
barkas_stay = pygame.image.load('battle\\barkas\\sail_0.png')
barkas_deck_width = 34
barkas_deck_height = 86
barkas_guns_left = [(-23, -18), (-23, 6)]
barkas_guns_right = [(23, -18), (23, 6)]

pink_move = pygame.image.load('battle\\pink\\sail_1.png')
pink_stay = pygame.image.load('battle\\pink\\sail_0.png')
pink_deck_width = 34
pink_deck_height = 86
pink_guns_left = [(-23, -18), (-23, 6)]
pink_guns_right = [(23, -18), (23, 6)]

ladya_move = pygame.image.load('battle\\ladya\\sail_1.png')
ladya_stay = pygame.image.load('battle\\ladya\\sail_0.png')
ladya_deck_width = 34
ladya_deck_height = 86
ladya_guns_left = [(-27, -15), (-27, 9)]
ladya_guns_right = [(27, -15), (27, 9)]

shuna_move = pygame.image.load('battle\\shuna\\sail_1.png')
shuna_stay = pygame.image.load('battle\\shuna\\sail_0.png')
shuna_deck_width = 34
shuna_deck_height = 108
shuna_guns_left = [(-23, -30), (-23, -6), (-23, 18)]
shuna_guns_right = [(23, -30), (23, -6), (23, 18)]

lugger_move = pygame.image.load('battle\\lugger\\sail_1.png')
lugger_stay = pygame.image.load('battle\\lugger\\sail_0.png')
lugger_deck_width = 34
lugger_deck_height = 108
lugger_guns_left = [(-23, -24), (-23, 0), (-23, 24)]
lugger_guns_right = [(23, -24), (23, 0), (23, 24)]

shlup_move = pygame.image.load('battle\\shlup\\sail_1.png')
shlup_stay = pygame.image.load('battle\\shlup\\sail_0.png')
shlup_deck_width = 42
shlup_deck_height = 122
shlup_guns_left = [(-27, -24), (-27, -0), (-27, 24)]
shlup_guns_right = [(27, -24), (27, -0), (27, 24)]

bark_move = pygame.image.load('battle\\bark\\sail_1.png')
bark_stay = pygame.image.load('battle\\bark\\sail_0.png')
bark_deck_width = 42
bark_deck_height = 146
bark_guns_left = [(-27, -36), (-27, -12), (-27, 12), (-27, 36)]
bark_guns_right = [(27, -36), (27, -12), (27, 12), (27, 36)]

fleyt_move = pygame.image.load('battle\\fleyt\\sail_1.png')
fleyt_stay = pygame.image.load('battle\\fleyt\\sail_0.png')
fleyt_deck_width = 42
fleyt_deck_height = 146
fleyt_guns_left = [(-27, -24), (-27, -0), (-27, 24)]
fleyt_guns_right = [(27, -24), (27, -0), (27, 24)]

brig_move = pygame.image.load('battle\\brig\\sail_1.png')
brig_stay = pygame.image.load('battle\\brig\\sail_0.png')
brig_deck_width = 42
brig_deck_height = 170
brig_guns_left = [(-27, -48), (-27, -24), (-27, -0), (-27, 24), (-27, 48)]
brig_guns_right = [(27, -48), (27, -24), (27, -0), (27, 24), (27, 48)]

galera_move = pygame.image.load('battle\\galera\\sail_1.png')
galera_stay = pygame.image.load('battle\\galera\\sail_0.png')
galera_deck_width = 58
galera_deck_height = 206
galera_guns_left = [(-35, -60), (-35, -36), (-35, -12), (-35, 12), (-35, 36), (-35, 60)]
galera_guns_right = [(35, -60), (35, -36), (35, -12), (35, 12), (35, 36), (35, 60)]

pinas_move = pygame.image.load('battle\\pinas\\sail_1.png')
pinas_stay = pygame.image.load('battle\\pinas\\sail_0.png')
pinas_deck_width = 58
pinas_deck_height = 230
pinas_guns_left = [(-35, -48), (-35, -24), (-35, 0), (-35, 24), (-35, 48)]
pinas_guns_right = [(35, -48), (35, -24), (35, 0), (35, 24), (35, 48)]

corvet_move = pygame.image.load('battle\\corvet\\sail_1.png')
corvet_stay = pygame.image.load('battle\\corvet\\sail_0.png')
corvet_deck_width = 58
corvet_deck_height = 230
corvet_guns_left = [(-35, -72), (-35, -48), (-35, -24), (-35, 0), (-35, 24), (-35, 48), (-35, 72)]
corvet_guns_right = [(35, -72), (35, -48), (35, -24), (35, 0), (35, 24), (35, 48), (35, 72)]

fregat_move = pygame.image.load('battle\\fregat\\sail_1.png')
fregat_stay = pygame.image.load('battle\\fregat\\sail_0.png')
fregat_deck_width = 74
fregat_deck_height = 308
fregat_guns_left = [(-43, -81), (-43, -57), (-43, -33), (-43, -9), (-43, 15), (-43, 39), (-43, 63), (-43, 87)]
fregat_guns_right = [(43, -81), (43, -57), (43, -33), (43, -9), (43, 15), (43, 39), (43, 63), (43, 87)]

tradeship_move = pygame.image.load('battle\\tradeship\\sail_1.png')
tradeship_stay = pygame.image.load('battle\\tradeship\\sail_0.png')
tradeship_deck_width = 74
tradeship_deck_height = 332
tradeship_guns_left = [(-43, -69), (-43, -45), (-43, -21), (-43, 3), (-43, 27), (-43, 51), (-43, 75)]
tradeship_guns_right = [(43, -69), (43, -45), (43, -21), (43, 3), (43, 27), (43, 51), (43, 75)]

warship_move = pygame.image.load('battle\\warship\\sail_1.png')
warship_stay = pygame.image.load('battle\\warship\\sail_0.png')
warship_deck_width = 74
warship_deck_height = 332
warship_guns_left = [(-43, -93), (-43, -69), (-43, -45), (-43, -21), (-43, 3), (-43, 27), (-43, 51), (-43, 75), (-43, 99)]
warship_guns_right = [(43, -93), (43, -69), (43, -45), (43, -21), (43, 3), (43, 27), (43, 51), (43, 75), (43, 99)]

friendly_ships = []
enemy_ships = []

kernels = []

waves = []

clock = pygame.time.Clock()

###################################################functions############################################################

def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

def dot_in_rect(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
    p21 = [x2 - x1, y2 - y1]
    p41 = [x4 - x1, y4 - y1]
    p21magnitude_squared = p21[0] ** 2 + p21[1] ** 2
    p41magnitude_squared = p41[0] ** 2 + p41[1] ** 2
    p = [x - x1, y - y1]
    if 0 <= (p[0] * p21[0] + p[1] * p21[1]) <= p21magnitude_squared:
        if 0 <= (p[0] * p41[0] + p[1] * p41[1]) <= p41magnitude_squared:
            return True
        else:
            return False
    else:
        return False

def ships_and_kernels(ship):
    dw2 = ship.deck_width / 2
    dh2 = ship.deck_height / 2
    x = ship.x
    y = ship.y
    angle = ship.angle

    gip = (dw2 ** 2 + dh2 ** 2) ** 0.5
    ax = gip * math.cos(math.radians(angle) + math.asin(dh2 / gip)) + x
    ay = -gip * math.sin(math.radians(angle) + math.asin(dh2 / gip)) + y
    bx = gip * math.cos(math.radians(angle) - math.asin(dh2 / gip)) + x
    by = -gip * math.sin(math.radians(angle) - math.asin(dh2 / gip)) + y
    cx = gip * math.cos(math.radians(angle) + math.pi + math.asin(dh2 / gip)) + x
    cy = -gip * math.sin(math.radians(angle) + math.pi + math.asin(dh2 / gip)) + y
    dx = gip * math.cos(math.radians(angle) + math.pi - math.asin(dh2 / gip)) + x
    dy = -gip * math.sin(math.radians(angle) + math.pi - math.asin(dh2 / gip)) + y

    if (scale == 1):
        kernel_hit_size = kernel_image.get_width()
    else:
        kernel_hit_size = (kernel_image.get_width() + 1) / scale
    for kernel in kernels:
        if dot_in_rect(kernel[0], kernel[1], ax, ay, bx, by, cx, cy, dx, dy):
            image = pygame.transform.smoothscale(kernel_hit_image, (kernel_hit_size, kernel_hit_size))
            display.blit(image, (center_x + kernel[0] / scale, center_y + kernel[1] / scale))
            kernels.remove(kernel)
            ship.hp -= 1

def swim_to_target(ship, target_ship):
    x1 = ship.x
    y1 = ship.y
    x2 = target_ship.x
    y2 = target_ship.y
    angle = ship.angle
    turning_speed = ship.t_speed

    gip = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    pi = math.pi
    if (x2 - x1 >= 0):
        i_angle = math.acos((y2 - y1) / gip)
    else:
        i_angle = 2 * pi - math.acos((y2 - y1) / gip)

    a = math.radians(angle)

    dif = a - i_angle
    t_a = dif
    mt_a = math.fabs(dif)
    ship_ts = math.radians(turning_speed)
    tship_ts = target_ship.speed / gip

    if gip < ship.gun_distance * 10:
        if ((-2 * pi < t_a < -1.5 * pi) and (ship_ts * (2 * pi - mt_a) / (0.5 * pi) > tship_ts) or (
                0 < t_a < 0.5 * pi) and (ship_ts * mt_a / (0.5 * pi) > tship_ts)) and (ship_ts < math.radians(target_ship.t_speed)):
            if (ship.cd_sail == 0) and (ship.move == True):
                ship.move = False
                ship.cd_sail = 100
        elif ((-0.5 * pi < t_a < 0) and (ship_ts * mt_a / (0.5 * pi) > tship_ts) or (1.5 * pi < t_a < 2 * pi) and (
                ship_ts * (2 * pi - mt_a) / (0.5 * pi) > tship_ts)) and (ship_ts < math.radians(target_ship.t_speed)):
            if (ship.cd_sail == 0) and (ship.move == True):
                ship.move = False
                ship.cd_sail = 100
        else:
            if (ship.cd_sail == 0) and (ship.move == False):
                ship.move = True
                ship.cd_sail = 100

        if (-1.49 * pi < dif <= -pi) or (-0.49 * pi < dif <= 0) or (0.51 * pi < dif <= pi) or (1.51 * pi < dif <= 2 * pi):
            ship.angle -= turning_speed
            if ship.angle < 0:
                ship.angle = 360 - turning_speed
        elif (-2 * pi < dif < -1.51 * pi) or (-pi < dif < -0.51 * pi) or (0 < dif < 0.49 * pi) or (pi < dif < 1.49 * pi):
            ship.angle += turning_speed
            if ship.angle >= 360:
                ship.angle = 0
    else:
        if (ship.cd_sail == 0) and (ship.move == False):
            ship.move = True
            ship.cd_sail = 100

        if (-0.99 * pi < dif < -0.01 * pi) or (1.01 * pi < dif < 1.99 * pi):
            ship.angle -= turning_speed
            if ship.angle < 0:
                ship.angle = 360 - turning_speed
        elif (-1.99 * pi < dif < -1.01 * pi) or (0.01 * pi < dif < 0.99 * pi):
            ship.angle += turning_speed
            if ship.angle >= 360:
                ship.angle = 0

    if ship.cd_left > 0:
        ship.cd_left -= 1
    if ship.cd_right > 0:
        ship.cd_right -= 1
    if ship.cd_sail > 0:
        ship.cd_sail -= 1

def ready_shoot_left(ship, target_ship):
    x1 = ship.x
    y1 = ship.y
    x2 = target_ship.x
    y2 = target_ship.y
    angle = ship.angle

    gip = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if (x2 - x1 > 0):
        i_angle = math.acos((y2 - y1) / gip)
    else:
        i_angle = 2 * math.pi - math.acos((y2 - y1) / gip)

    dif = (math.radians(angle) - i_angle)
    pi = math.pi
    dif_angle = math.atan(math.fabs(ship.guns_left[0][1]) / gip)

    return (0.5 * pi - dif_angle < dif < 0.5 * pi + dif_angle) or (-1.5 * pi - dif_angle < dif < -1.5 * pi + dif_angle)

def shoot_left(ship):
    x = ship.x
    y = ship.y
    angle = ship.angle
    guns_left = ship.guns_left

    for gun in guns_left:
        gun0 = gun[0]
        gun1 = gun[1]
        gip = (gun0 ** 2 + gun1 ** 2) ** 0.5
        arcsin = math.asin(gun1 / gip)
        kernels.append([gip * math.cos(math.radians(angle) + math.pi + arcsin) + x,
                        -gip * math.sin(math.radians(angle) + math.pi + arcsin) + y, angle - 90, ship.gun_distance])
    ship.cd_left = 101

def ready_shoot_right(ship, target_ship):
    x1 = ship.x
    y1 = ship.y
    x2 = target_ship.x
    y2 = target_ship.y
    angle = ship.angle

    gip = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if (x2 - x1 > 0):
        i_angle = math.acos((y2 - y1) / gip)
    else:
        i_angle = 2 * math.pi - math.acos((y2 - y1) / gip)

    dif = (math.radians(angle) - i_angle)
    pi = math.pi
    dif_angle = math.atan(math.fabs(ship.guns_left[0][1]) / gip)

    return (-0.5 * pi - dif_angle < dif < -0.5 * pi + dif_angle) or (1.5 * pi - dif_angle < dif < 1.5 * pi + dif_angle)

def shoot_right(ship):
    x = ship.x
    y = ship.y
    angle = ship.angle
    guns_right = ship.guns_right

    for gun in guns_right:
        gun0 = gun[0]
        gun1 = gun[1]
        gip = (gun0 ** 2 + gun1 ** 2) ** 0.5
        arcsin = math.asin(gun1 / gip)
        kernels.append([gip * math.cos(math.radians(angle) + arcsin) + x,
                        -gip * math.sin(math.radians(angle) + arcsin) + y, angle + 90, ship.gun_distance])
    ship.cd_right = 101

def ship_intersection(ship1, ship2):
    x1 = ship1.x
    y1 = ship1.y
    dh1 = ship1.deck_height / 2
    dw1 = ship1.deck_width / 2
    angle1 = ship1.angle
    ac1 = (dw1 ** 2 + dh1 ** 2) ** 0.5

    ax1 = ac1 * math.cos(math.radians(angle1) + math.asin(dh1 / ac1)) + x1
    ay1 = -ac1 * math.sin(math.radians(angle1) + math.asin(dh1 / ac1)) + y1
    bx1 = ac1 * math.cos(math.radians(angle1) - math.asin(dh1 / ac1)) + x1
    by1 = -ac1 * math.sin(math.radians(angle1) - math.asin(dh1 / ac1)) + y1
    cx1 = ac1 * math.cos(math.radians(angle1) + math.pi + math.asin(dh1 / ac1)) + x1
    cy1 = -ac1 * math.sin(math.radians(angle1) + math.pi + math.asin(dh1 / ac1)) + y1
    dx1 = ac1 * math.cos(math.radians(angle1) + math.pi - math.asin(dh1 / ac1)) + x1
    dy1 = -ac1 * math.sin(math.radians(angle1) + math.pi - math.asin(dh1 / ac1)) + y1

    x2 = ship2.x
    y2 = ship2.y
    dh2 = ship2.deck_height / 2
    dw2 = ship2.deck_width / 2
    angle2 = ship2.angle
    ac2 = (dw2 ** 2 + dh2 ** 2) ** 0.5

    ax2 = ac2 * math.cos(math.radians(angle2) + math.asin(dh2 / ac2)) + x2
    ay2 = -ac2 * math.sin(math.radians(angle2) + math.asin(dh2 / ac2)) + y2
    bx2 = ac2 * math.cos(math.radians(angle2) - math.asin(dh2 / ac2)) + x2
    by2 = -ac2 * math.sin(math.radians(angle2) - math.asin(dh2 / ac2)) + y2
    cx2 = ac2 * math.cos(math.radians(angle2) + math.pi + math.asin(dh2 / ac2)) + x2
    cy2 = -ac2 * math.sin(math.radians(angle2) + math.pi + math.asin(dh2 / ac2)) + y2
    dx2 = ac2 * math.cos(math.radians(angle2) + math.pi - math.asin(dh2 / ac2)) + x2
    dy2 = -ac2 * math.sin(math.radians(angle2) + math.pi - math.asin(dh2 / ac2)) + y2

    if (dot_in_rect(ax1, ay1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)) or (
        dot_in_rect(bx1, by1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)) or (
        dot_in_rect(cx1, cy1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)) or (
        dot_in_rect(dx1, dy1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)) or (
        dot_in_rect(ax2, ay2, ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1)) or (
        dot_in_rect(bx2, by2, ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1)) or (
        dot_in_rect(cx2, cy2, ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1)) or (
        dot_in_rect(dx2, dy2, ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1)):
        gip = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if (ship2 == friendly_ships[0]):
            ship1.x += ship1.speed * (x1 - x2) / gip
            ship1.y += ship1.speed * (y1 - y2) / gip
            for ship in enemy_ships:
                ship.x += ship2.speed * (x1 - x2) / gip
                ship.y += ship2.speed * (y1 - y2) / gip
            for ship in friendly_ships:
                if ship != friendly_ships[0]:
                    ship.x += ship2.speed * (x1 - x2) / gip
                    ship.y += ship2.speed * (y1 - y2) / gip
        else:
            ship1.x += ship1.speed * (x1 - x2) / gip
            ship1.y += ship1.speed * (y1 - y2) / gip
            ship2.x -= ship2.speed * (x1 - x2) / gip
            ship2.y -= ship2.speed * (y1 - y2) / gip

def no_may_shoot_left(ship, target_ship, block_ship):
    x = ship.x
    y = ship.y
    dist = ((ship.x - target_ship.x) ** 2 + (ship.y - target_ship.y) ** 2) ** 0.5
    block_dist = ((ship.x - block_ship.x) ** 2 + (ship.y - block_ship.y) ** 2) ** 0.5

    if (dist > block_dist):
        angle = ship.angle
        gip1 = ((ship.guns_left[0][0]) ** 2 + (ship.guns_left[0][1]) ** 2) ** 0.5
        gip2 = ((ship.guns_left[len(ship.guns_left) - 1][0]) ** 2 + (ship.guns_left[len(ship.guns_left) - 1][1]) ** 2) ** 0.5

        arcsin1 = math.asin(ship.guns_left[0][1] / gip1)
        arcsin2 = math.asin(ship.guns_left[len(ship.guns_left) - 1][1] / gip2)
        ax = gip1 * math.cos(math.radians(angle) + math.pi + arcsin1) + x
        ay = -gip1 * math.sin(math.radians(angle) + math.pi + arcsin1) + y
        bx = gip2 * math.cos(math.radians(angle) + math.pi + arcsin2) + x
        by = -gip2 * math.sin(math.radians(angle) + math.pi + arcsin2) + y
        cx = gip1 * math.cos(math.radians(angle) + math.pi + arcsin1) + x + dist * math.sin(math.radians(angle) - math.pi / 2)
        cy = -gip1 * math.sin(math.radians(angle) + math.pi + arcsin1) + y + dist * math.cos(math.radians(angle) - math.pi / 2)
        dx = gip2 * math.cos(math.radians(angle) + math.pi + arcsin2) + x + dist * math.sin(math.radians(angle) - math.pi / 2)
        dy = -gip2 * math.sin(math.radians(angle) + math.pi + arcsin2) + y + dist * math.cos(math.radians(angle) - math.pi / 2)

        shift = 0
        ret = False
        while (shift < block_ship.deck_height / 2):
            downx = block_ship.x + shift * math.sin(math.radians(block_ship.angle))
            downy = block_ship.y + shift * math.cos(math.radians(block_ship.angle))
            upx = block_ship.x - shift * math.sin(math.radians(block_ship.angle))
            upy = block_ship.y - shift * math.cos(math.radians(block_ship.angle))
            if (dot_in_rect(downx, downy, ax, ay, bx, by, cx, cy, dx, dy)) or (
                    dot_in_rect(upx, upy, ax, ay, bx, by, cx, cy, dx, dy)):
                ret = True
            shift += 23
        return ret
    else:
        return False

def no_may_shoot_right(ship, target_ship, block_ship):
    x = ship.x
    y = ship.y
    dist = ((ship.x - target_ship.x) ** 2 + (ship.y - target_ship.y) ** 2) ** 0.5
    block_dist = ((ship.x - block_ship.x) ** 2 + (ship.y - block_ship.y) ** 2) ** 0.5

    if (dist > block_dist):
        angle = ship.angle
        gip1 = ((ship.guns_left[0][0]) ** 2 + (ship.guns_left[0][1]) ** 2) ** 0.5
        gip2 = ((ship.guns_left[len(ship.guns_left) - 1][0]) ** 2 + (ship.guns_left[len(ship.guns_left) - 1][1]) ** 2) ** 0.5

        arcsin1 = math.asin(ship.guns_right[0][1] / gip1)
        arcsin2 = math.asin(ship.guns_right[len(ship.guns_right) - 1][1] / gip2)
        ax = gip1 * math.cos(math.radians(angle) + arcsin1) + x
        ay = -gip1 * math.sin(math.radians(angle) + arcsin1) + y
        bx = gip2 * math.cos(math.radians(angle) + arcsin2) + x
        by = -gip2 * math.sin(math.radians(angle) + arcsin2) + y
        cx = gip1 * math.cos(math.radians(angle) + arcsin1) + x + dist * math.sin(math.radians(angle) + math.pi / 2)
        cy = -gip1 * math.sin(math.radians(angle) + arcsin1) + y + dist * math.cos(math.radians(angle) + math.pi / 2)
        dx = gip2 * math.cos(math.radians(angle) + arcsin2) + x + dist * math.sin(math.radians(angle) + math.pi / 2)
        dy = -gip2 * math.sin(math.radians(angle) + arcsin2) + y + dist * math.cos(math.radians(angle) + math.pi / 2)

        shift = 0
        ret = False
        while (shift < block_ship.deck_height / 2):
            downx = block_ship.x + shift * math.sin(math.radians(block_ship.angle))
            downy = block_ship.y + shift * math.cos(math.radians(block_ship.angle))
            upx = block_ship.x - shift * math.sin(math.radians(block_ship.angle))
            upy = block_ship.y - shift * math.cos(math.radians(block_ship.angle))
            if (dot_in_rect(downx, downy, ax, ay, bx, by, cx, cy, dx, dy)) or (
                    dot_in_rect(upx, upy, ax, ay, bx, by, cx, cy, dx, dy)):
                ret = True
            shift += 23
        return ret
    else:
        return False

###################################################game_start###########################################################

def battle(friendly_ships_list, enemy_ships_list):

    i = 0
    for ship in friendly_ships_list:
        friendly_ships.append(ship_object(i, 0, 0, ship[0], ship[1]))
        i += 200

    i = -(len(enemy_ships_list) - 1) * 100 + (len(friendly_ships_list) - 1) * 100
    for ship in enemy_ships_list:
        enemy_ships.append(ship_object(i, -1000, 180, ship[0], ship[1]))
        i += 200

    friendly_ships[0].move = True
    game = True
    global scale, center_x, center_y, wave_step
    for i in range(192):
        waves.append([randint(-display_width * 2, display_width * 2), randint(-display_height * 2, display_height * 2), i // 4])

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((0, 162, 232))

        for i in range(4):
            waves.append([randint(-display_width * 2, display_width * 2), randint(-display_height * 2, display_height * 2), 0])

#####################################################player#############################################################

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if friendly_ships[0].cd_sail == 0:
                friendly_ships[0].move = True
                friendly_ships[0].cd_sail = 100
        elif keys[pygame.K_s]:
            if friendly_ships[0].cd_sail == 0:
                friendly_ships[0].move = False
                friendly_ships[0].cd_sail = 100
        if keys[pygame.K_d]:
            friendly_ships[0].angle -= friendly_ships[0].t_speed
            if friendly_ships[0].angle < 0:
                friendly_ships[0].angle = 360 - friendly_ships[0].t_speed
        elif keys[pygame.K_a]:
            friendly_ships[0].angle += friendly_ships[0].t_speed
            if friendly_ships[0].angle >= 360:
                friendly_ships[0].angle = 0
        if keys[pygame.K_q]:
            if friendly_ships[0].cd_left == 0:
                shoot_left(friendly_ships[0])
        if keys[pygame.K_e]:
            if friendly_ships[0].cd_right == 0:
                shoot_right(friendly_ships[0])
        if keys[pygame.K_1]:
            scale = 1
        elif keys[pygame.K_2]:
            scale = 2
        elif keys[pygame.K_3]:
            scale = 4
        if keys[pygame.K_ESCAPE]:
            quit()

        if friendly_ships[0].cd_left > 0:
            friendly_ships[0].cd_left -= 1
        if friendly_ships[0].cd_right > 0:
            friendly_ships[0].cd_right -= 1
        if friendly_ships[0].cd_sail > 0:
            friendly_ships[0].cd_sail -= 1

####################################################control#############################################################

        for enemy_ship in enemy_ships:
            enemy_ship.target = 0
            dist_target = (enemy_ship.x-friendly_ships[0].x)**2+(enemy_ship.y-friendly_ships[0].y)**2
            for i in range(len(friendly_ships)):
                dist = (enemy_ship.x-friendly_ships[i].x)**2+(enemy_ship.y-friendly_ships[i].y)**2
                if dist < dist_target:
                    enemy_ship.target = i
                    dist_target = dist
            swim_to_target(enemy_ship, friendly_ships[enemy_ship.target])

            for friendly_ship in friendly_ships:
                gip = ((enemy_ship.x - friendly_ship.x) ** 2 + (enemy_ship.y - friendly_ship.y) ** 2) ** 0.5
                if (gip < enemy_ship.gun_distance * 10) and (ready_shoot_left(enemy_ship, friendly_ship)) and enemy_ship.cd_left == 0:
                    may_shoot_left = True
                    for no_shoot_enemy_ship in enemy_ships:
                        block_gip = ((enemy_ship.x-no_shoot_enemy_ship.x)**2+(enemy_ship.y-no_shoot_enemy_ship.y)**2)**0.5
                        if (no_shoot_enemy_ship != enemy_ship) and (block_gip < enemy_ship.gun_distance * 10):
                            if no_may_shoot_left(enemy_ship, friendly_ship, no_shoot_enemy_ship):
                                may_shoot_left = False
                    if may_shoot_left:
                        shoot_left(enemy_ship)
                    else:
                        if (enemy_ship.cd_sail == 0):
                            enemy_ship.move = True
                            enemy_ship.cd_sail = 100
                if (gip < enemy_ship.gun_distance * 10
                    ) and (ready_shoot_right(enemy_ship, friendly_ship)) and enemy_ship.cd_right == 0:
                    may_shoot_right = True
                    for no_shoot_enemy_ship in enemy_ships:
                        block_gip = ((enemy_ship.x-no_shoot_enemy_ship.x)**2+(enemy_ship.y-no_shoot_enemy_ship.y)**2)**0.5
                        if (no_shoot_enemy_ship != enemy_ship) and (block_gip < enemy_ship.gun_distance * 10):
                            if no_may_shoot_right(enemy_ship, friendly_ship, no_shoot_enemy_ship):
                                may_shoot_right = False
                    if may_shoot_right:
                        shoot_right(enemy_ship)
                    else:
                        if (enemy_ship.cd_sail == 0):
                            enemy_ship.move = True
                            enemy_ship.cd_sail = 100

        for friendly_ship in friendly_ships:
            if (friendly_ship != friendly_ships[0]):
                friendly_ship.target = 0
                dist_target = (friendly_ship.x-enemy_ships[0].x)**2+(friendly_ship.y-enemy_ships[0].y)**2
                for i in range(len(enemy_ships)):
                    dist = (friendly_ship.x-enemy_ships[i].x)**2+(friendly_ship.y-enemy_ships[i].y)**2
                    if dist < dist_target:
                        friendly_ship.target = i
                        dist_target = dist
                swim_to_target(friendly_ship, enemy_ships[friendly_ship.target])

                for enemy_ship in enemy_ships:
                    gip = ((enemy_ship.x - friendly_ship.x) ** 2 + (enemy_ship.y - friendly_ship.y) ** 2) ** 0.5
                    if (gip < friendly_ship.gun_distance * 10) and (ready_shoot_left(friendly_ship, enemy_ship)) and friendly_ship.cd_left == 0:
                        may_shoot_left = True
                        for no_shoot_friendly_ship in friendly_ships:
                            block_gip = ((friendly_ship.x-no_shoot_friendly_ship.x)**2+(friendly_ship.y-no_shoot_friendly_ship.y)**2)**0.5
                            if (no_shoot_friendly_ship != friendly_ship) and (block_gip < enemy_ship.gun_distance * 10):
                                if no_may_shoot_left(friendly_ship, enemy_ship, no_shoot_friendly_ship):
                                    may_shoot_left = False
                        if may_shoot_left:
                            shoot_left(friendly_ship)
                        else:
                            if (friendly_ship.cd_sail == 0):
                                friendly_ship.move = True
                                friendly_ship.cd_sail = 100
                    if (gip < friendly_ship.gun_distance * 10
                        ) and (ready_shoot_right(friendly_ship, enemy_ship)) and friendly_ship.cd_right == 0:
                        may_shoot_right = True
                        for no_shoot_friendly_ship in friendly_ships:
                            block_gip = ((friendly_ship.x-no_shoot_friendly_ship.x)**2+(friendly_ship.y-no_shoot_friendly_ship.y)**2)**0.5
                            if (no_shoot_friendly_ship != friendly_ship) and (block_gip < enemy_ship.gun_distance * 10):
                                if no_may_shoot_right(friendly_ship, enemy_ship, no_shoot_friendly_ship):
                                    may_shoot_right = False
                        if may_shoot_right:
                            shoot_right(friendly_ship)
                        else:
                            if (friendly_ship.cd_sail == 0):
                                friendly_ship.move = True
                                friendly_ship.cd_sail = 100

################################################ship_intersection#######################################################

        for enemy_ship in enemy_ships:
            for friendly_ship in friendly_ships:
                if (enemy_ship.x-friendly_ship.x)**2+(enemy_ship.y-friendly_ship.y)**2 < (
                    enemy_ship.deck_width/2)**2+(enemy_ship.deck_height/2)**2+(friendly_ship.deck_width/2)**2+(friendly_ship.deck_height/2)**2:
                    ship_intersection(enemy_ship, friendly_ship)
            for other_enemy_ship in enemy_ships:
                if other_enemy_ship != enemy_ship:
                    if (enemy_ship.x-other_enemy_ship.x)**2+(enemy_ship.y-other_enemy_ship.y)**2 < (
                        enemy_ship.deck_width/2)**2+(enemy_ship.deck_height/2)**2+(other_enemy_ship.deck_width/2)**2+(other_enemy_ship.deck_height/2)**2:
                        ship_intersection(enemy_ship, other_enemy_ship)

        for friendly_ship in friendly_ships:
            for other_friendly_ship in friendly_ships:
                if other_friendly_ship != friendly_ship and friendly_ship != friendly_ships[0]:
                    if (other_friendly_ship.x-friendly_ship.x)**2+(other_friendly_ship.y-friendly_ship.y)**2 < (
                        other_friendly_ship.deck_width/2)**2+(other_friendly_ship.deck_height/2)**2+(friendly_ship.deck_width/2)**2+(friendly_ship.deck_height/2)**2:
                        ship_intersection(friendly_ship, other_friendly_ship)

########################################################painting########################################################

        for wave in waves:
            image = pygame.transform.smoothscale(wave_step[wave[2] // 8], (24 / scale, 8 / scale))
            rect = image.get_rect(center=(center_x + wave[0] / scale, center_y + wave[1] / scale))
            surf, r = rot_center(image, rect, 0)
            display.blit(surf, r)
            wave[2] += 1
            if wave[2] >= 48:
                waves.remove(wave)

        if friendly_ships[0].move:
            image = pygame.transform.smoothscale(friendly_ships[0].pic_move, (friendly_ships[0].get_width(), friendly_ships[0].get_height()))
            for enemy_ship in enemy_ships:
                enemy_ship.x += math.sin(math.radians(friendly_ships[0].angle)) * friendly_ships[0].speed
                enemy_ship.y += math.cos(math.radians(friendly_ships[0].angle)) * friendly_ships[0].speed
            for friendly_ship in friendly_ships:
                friendly_ship.x += math.sin(math.radians(friendly_ships[0].angle)) * friendly_ships[0].speed
                friendly_ship.y += math.cos(math.radians(friendly_ships[0].angle)) * friendly_ships[0].speed
            for wave in waves:
                wave[0] += math.sin(math.radians(friendly_ships[0].angle)) * friendly_ships[0].speed
                wave[1] += math.cos(math.radians(friendly_ships[0].angle)) * friendly_ships[0].speed
        else:
            image = pygame.transform.smoothscale(friendly_ships[0].pic_stay, (friendly_ships[0].get_width(), friendly_ships[0].get_height()))

        rect = image.get_rect(center=(center_x, center_y))
        surf, r = rot_center(image, rect, friendly_ships[0].angle)
        display.blit(surf, r)

        for enemy_ship in enemy_ships:

            if enemy_ship.move == 1:
                image = pygame.transform.smoothscale(enemy_ship.pic_move, (enemy_ship.get_width(), enemy_ship.get_height()))
                enemy_ship.x -= math.sin(math.radians(enemy_ship.angle)) * enemy_ship.speed
                enemy_ship.y -= math.cos(math.radians(enemy_ship.angle)) * enemy_ship.speed
            else:
                image = pygame.transform.smoothscale(enemy_ship.pic_stay, (enemy_ship.get_width(), enemy_ship.get_height()))

            rect = image.get_rect(center=(center_x + enemy_ship.x / scale, center_y + enemy_ship.y / scale))
            surf, r = rot_center(image, rect, enemy_ship.angle)
            display.blit(surf, r)
            f = pygame.font.Font(None, 48 // scale)
            typ = f.render(str(enemy_ship.hp), True, (255, 0, 0))
            display.blit(typ, (center_x + enemy_ship.x / scale, center_y + enemy_ship.y / scale))

        for friendly_ship in friendly_ships:

            if friendly_ship.move == 1:
                image = pygame.transform.smoothscale(friendly_ship.pic_move, (friendly_ship.get_width(), friendly_ship.get_height()))
                friendly_ship.x -= math.sin(math.radians(friendly_ship.angle)) * friendly_ship.speed
                friendly_ship.y -= math.cos(math.radians(friendly_ship.angle)) * friendly_ship.speed
            else:
                image = pygame.transform.smoothscale(friendly_ship.pic_stay, (friendly_ship.get_width(), friendly_ship.get_height()))

            rect = image.get_rect(center=(center_x + friendly_ship.x / scale, center_y + friendly_ship.y / scale))
            surf, r = rot_center(image, rect, friendly_ship.angle)
            display.blit(surf, r)
            f = pygame.font.Font(None, 48 // scale)
            typ = f.render(str(friendly_ship.hp), True, (0, 255, 0))
            display.blit(typ, (center_x + friendly_ship.x / scale, center_y + friendly_ship.y / scale))

#######################################################damage###########################################################

        if (scale == 1):
            kernel_size = kernel_image.get_width()
            kernel_miss_size = kernel_image.get_width()
        else:
            kernel_size = (kernel_image.get_width() - 1) / scale
            kernel_miss_size = (kernel_image.get_width() + 1) / scale

        for kernel in kernels:
            kernel[0] += math.sin(math.radians(kernel[2])) * 10
            kernel[1] += math.cos(math.radians(kernel[2])) * 10
            kernel[3] -= 1
            if kernel[3] <= 0:
                image = pygame.transform.smoothscale(kernel_miss_image, (kernel_size, kernel_size))
                display.blit(image, (center_x + kernel[0] / scale, center_y + kernel[1] / scale))
                kernels.remove(kernel)
            else:
                image = pygame.transform.smoothscale(kernel_image, (kernel_miss_size, kernel_miss_size))
                display.blit(image, (center_x + kernel[0] / scale, center_y + kernel[1] / scale))

        step = 5
        for enemy_ship in enemy_ships:
            ships_and_kernels(enemy_ship)
            f = pygame.font.Font(None, 48)
            typ = f.render(enemy_ship.type, True, (255, 255, 0))
            display.blit(typ, (10, step))
            hp = f.render(str(enemy_ship.hp), True, (255, 0, 0))
            display.blit(hp, (150, step))
            if (enemy_ship.hp <= 0):
                enemy_ships.remove(enemy_ship)
            step += 35

        step = 5
        for friendly_ship in friendly_ships:
            ships_and_kernels(friendly_ship)
            f = pygame.font.Font(None, 48)
            typ = f.render(friendly_ship.type, True, (255, 255, 0))
            display.blit(typ, (display_width - 200, step))
            hp = f.render(str(friendly_ship.hp), True, (0, 255, 0))
            display.blit(hp, (display_width - 50, step))
            if (friendly_ships[0].hp <= 0):
                friendly_ships.remove(friendly_ships[0])
                if (len(friendly_ships) == 0):
                    game = False
                else:
                    for ship_shift in friendly_ships:
                        if (ship_shift != friendly_ships[0]):
                            ship_shift.x -= friendly_ships[0].x
                            ship_shift.y -= friendly_ships[0].y
                    for ship_shift in enemy_ships:
                        ship_shift.x -= friendly_ships[0].x
                        ship_shift.y -= friendly_ships[0].y
                    friendly_ships[0].x = 0
                    friendly_ships[0].y = 0
            elif (friendly_ship.hp <= 0):
                friendly_ships.remove(friendly_ship)
            step += 35

        if (len(enemy_ships) == 0):
            game = False

        f = pygame.font.Font(None, 20)
        coord = f.render("(a)/(d) - turn     (w)/(s) - move/stop", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 50))
        f = pygame.font.Font(None, 20)
        coord = f.render("(q)/(e) - shot     (1)/(2)/(3) - scale", True, (0, 0, 0))
        display.blit(coord, (10, display_height - 30))

        pygame.display.update()
        clock.tick(30)

    friendly_ships_list.clear()
    for ship in friendly_ships:
        friendly_ships_list.append([ship.type, ship.hp])
    friendly_ships.clear()
    enemy_ships.clear()
    kernels.clear()
    waves.clear()
    return friendly_ships_list