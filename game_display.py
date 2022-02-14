import pygame
import math
from random import randint

pygame.init()
pygame.font.init()

display_width = 1200
display_height = 900
scale = 4
center_x = display_width / 2
center_y = display_height / 2
wave_step = 0

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ship game')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#####################################################class##############################################################

class ship_type:
    def __init__(self, pic_move, pic_stay, deck_width, deck_height, speed, t_speed, hp, gun_distance, guns_left, guns_right):
        self.pic_move = pic_move
        self.pic_stay = pic_stay
        self.deck_width = deck_width
        self.deck_height = deck_height
        self.speed = speed
        self.t_speed = t_speed
        self.hp = hp
        self.gun_distance = gun_distance
        self.guns_left = guns_left
        self.guns_right = guns_right

class ship_object(ship_type):
    def __init__(self, x, y, angle, type, cd_left = 0, cd_right = 0, cd_sail = 0, move=True, target = -1):
        self.x = x
        self.y = y
        self.angle = angle
        self.type = type
        self.ship_type = ship_type
        self.cd_left = cd_left
        self.cd_right = cd_right
        self.cd_sail = cd_sail
        self.move = move
        self.target = target
        if (type == "barkas"):
            super().__init__(barkas_move, barkas_stay, barkas_deck_width, barkas_deck_height, 0.8, 1.0, 15, 30, barkas_guns_left, barkas_guns_right)
        elif (type == "pink"):
            super().__init__(pink_move, pink_stay, pink_deck_width, pink_deck_height, 1.2, 0.6, 15, 30, pink_guns_left, pink_guns_right)
        elif (type == "ladya"):
            super().__init__(ladya_move, ladya_stay, ladya_deck_width, ladya_deck_height, 1.2, 0.4, 20, 30, ladya_guns_left, ladya_guns_right)
        elif (type == "shuna"):
            super().__init__(shuna_move, shuna_stay, shuna_deck_width, shuna_deck_height, 1.2, 0.8, 20, 30, shuna_guns_left, shuna_guns_right)
        elif (type == "lugger"):
            super().__init__(lugger_move, lugger_stay, lugger_deck_width, lugger_deck_height, 1.6, 0.8, 25, 30, lugger_guns_left, lugger_guns_right)
        elif (type == "shlup"):
            super().__init__(shlup_move, shlup_stay, shlup_deck_width, shlup_deck_height, 1.2, 1.0, 30, 40, shlup_guns_left, shlup_guns_right)
        elif (type == "bark"):
            super().__init__(bark_move, bark_stay, bark_deck_width, bark_deck_height, 1.6, 0.6, 35, 40, bark_guns_left, bark_guns_right)
        elif (type == "fleyt"):
            super().__init__(fleyt_move, fleyt_stay, fleyt_deck_width, fleyt_deck_height, 1.6, 0.4, 40, 40, fleyt_guns_left, fleyt_guns_right)
        elif (type == "brig"):
            super().__init__(brig_move, brig_stay, brig_deck_width, brig_deck_height, 2.0, 0.8, 40, 40, brig_guns_left, brig_guns_right)
        elif (type == "karaka"):
            super().__init__(karaka_move, karaka_stay, karaka_deck_width, karaka_deck_height, 2.0, 0.4, 50, 50, karaka_guns_left, karaka_guns_right)
        elif (type == "shebeka"):
            super().__init__(shebeka_move, shebeka_stay, shebeka_deck_width, shebeka_deck_height, 1.6, 1.0, 50, 50, shebeka_guns_left, shebeka_guns_right)
        elif (type == "corvet"):
            super().__init__(corvet_move, corvet_stay, corvet_deck_width, corvet_deck_height, 2.4, 0.6, 60, 50, corvet_guns_left, corvet_guns_right)
        elif (type == "fregat"):
            super().__init__(fregat_move, fregat_stay, fregat_deck_width, fregat_deck_height, 2.0, 0.8, 75, 60, fregat_guns_left, fregat_guns_right)
        elif (type == "warship"):
            super().__init__(warship_move, warship_stay, warship_deck_width, warship_deck_height, 2.4, 0.8, 90, 60, warship_guns_left, warship_guns_right)
    def get_width(self):
        return self.pic_move.get_width() / scale
    def get_height(self):
        return self.pic_move.get_height() / scale

#################################################create_ships###########################################################

kernel_image = pygame.image.load('kernel.png')
kernel_hit_image = pygame.image.load('kernel_hit.png')
kernel_miss_image = pygame.image.load('kernel_miss.png')

wave_step = []
wave_step.append(pygame.image.load('waves\\1.png'))
wave_step.append(pygame.image.load('waves\\2.png'))
wave_step.append(pygame.image.load('waves\\3.png'))
wave_step.append(pygame.image.load('waves\\4.png'))
wave_step.append(pygame.image.load('waves\\5.png'))
wave_step.append(pygame.image.load('waves\\6.png'))

barkas_move = pygame.image.load('barkas\\sail_1.png')
barkas_stay = pygame.image.load('barkas\\sail_0.png')
barkas_deck_width = 34
barkas_deck_height = 86
barkas_guns_left = [(-23, -18), (-23, 6)]
barkas_guns_right = [(23, -18), (23, 6)]

pink_move = pygame.image.load('pink\\sail_1.png')
pink_stay = pygame.image.load('pink\\sail_0.png')
pink_deck_width = 34
pink_deck_height = 86
pink_guns_left = [(-23, -18), (-23, 6)]
pink_guns_right = [(23, -18), (23, 6)]

ladya_move = pygame.image.load('ladya\\sail_1.png')
ladya_stay = pygame.image.load('ladya\\sail_0.png')
ladya_deck_width = 34
ladya_deck_height = 86
ladya_guns_left = [(-27, -15), (-27, 9)]
ladya_guns_right = [(27, -15), (27, 9)]

shuna_move = pygame.image.load('shuna\\sail_1.png')
shuna_stay = pygame.image.load('shuna\\sail_0.png')
shuna_deck_width = 34
shuna_deck_height = 108
shuna_guns_left = [(-23, -30), (-23, -6), (-23, 18)]
shuna_guns_right = [(23, -30), (23, -6), (23, 18)]

lugger_move = pygame.image.load('lugger\\sail_1.png')
lugger_stay = pygame.image.load('lugger\\sail_0.png')
lugger_deck_width = 34
lugger_deck_height = 108
lugger_guns_left = [(-23, -24), (-23, 0), (-23, 24)]
lugger_guns_right = [(23, -24), (23, 0), (23, 24)]

shlup_move = pygame.image.load('shlup\\sail_1.png')
shlup_stay = pygame.image.load('shlup\\sail_0.png')
shlup_deck_width = 42
shlup_deck_height = 122
shlup_guns_left = [(-27, -24), (-27, -0), (-27, 24)]
shlup_guns_right = [(27, -24), (27, -0), (27, 24)]

bark_move = pygame.image.load('bark\\sail_1.png')
bark_stay = pygame.image.load('bark\\sail_0.png')
bark_deck_width = 42
bark_deck_height = 146
bark_guns_left = [(-27, -36), (-27, -12), (-27, 12), (-27, 36)]
bark_guns_right = [(27, -36), (27, -12), (27, 12), (27, 36)]

fleyt_move = pygame.image.load('fleyt\\sail_1.png')
fleyt_stay = pygame.image.load('fleyt\\sail_0.png')
fleyt_deck_width = 42
fleyt_deck_height = 146
fleyt_guns_left = [(-27, -24), (-27, -0), (-27, 24)]
fleyt_guns_right = [(27, -24), (27, -0), (27, 24)]

brig_move = pygame.image.load('brig\\sail_1.png')
brig_stay = pygame.image.load('brig\\sail_0.png')
brig_deck_width = 42
brig_deck_height = 170
brig_guns_left = [(-27, -48), (-27, -24), (-27, -0), (-27, 24), (-27, 48)]
brig_guns_right = [(27, -48), (27, -24), (27, -0), (27, 24), (27, 48)]

karaka_move = pygame.image.load('karaka\\sail_1.png')
karaka_stay = pygame.image.load('karaka\\sail_0.png')
karaka_deck_width = 58
karaka_deck_height = 206
karaka_guns_left = [(-35, -48), (-35, -24), (-35, 0), (-35, 24), (-35, 48)]
karaka_guns_right = [(35, -48), (35, -24), (35, 0), (35, 24), (35, 48)]

shebeka_move = pygame.image.load('shebeka\\sail_1.png')
shebeka_stay = pygame.image.load('shebeka\\sail_0.png')
shebeka_deck_width = 58
shebeka_deck_height = 206
shebeka_guns_left = [(-35, -60), (-35, -36), (-35, -12), (-35, 12), (-35, 36), (-35, 60)]
shebeka_guns_right = [(35, -60), (35, -36), (35, -12), (35, 12), (35, 36), (35, 60)]

corvet_move = pygame.image.load('corvet\\sail_1.png')
corvet_stay = pygame.image.load('corvet\\sail_0.png')
corvet_deck_width = 58
corvet_deck_height = 230
corvet_guns_left = [(-35, -72), (-35, -48), (-35, -24), (-35, 0), (-35, 24), (-35, 48), (-35, 72)]
corvet_guns_right = [(35, -72), (35, -48), (35, -24), (35, 0), (35, 24), (35, 48), (35, 72)]

fregat_move = pygame.image.load('fregat\\sail_1.png')
fregat_stay = pygame.image.load('fregat\\sail_0.png')
fregat_deck_width = 74
fregat_deck_height = 302
fregat_guns_left = [(-43, -84), (-43, -60), (-43, -36), (-43, -12), (-43, 12), (-43, 36), (-43, 60), (-43, 84)]
fregat_guns_right = [(43, -84), (43, -60), (43, -36), (43, -12), (43, 12), (43, 36), (43, 60), (43, 84)]

warship_move = pygame.image.load('warship\\sail_1.png')
warship_stay = pygame.image.load('warship\\sail_0.png')
warship_deck_width = 74
warship_deck_height = 326
warship_guns_left = [(-43, -96), (-43, -72), (-43, -48), (-43, -24), (-43, 0), (-43, 24), (-43, 48), (-43, 72), (-43, 96)]
warship_guns_right = [(43, -96), (43, -72), (43, -48), (43, -24), (43, 0), (43, 24), (43, 48), (43, 72), (43, 96)]

# player_ship = ship_object(0, 0, 0, "corvet")
# friendly_ships = [ship_object(300, 0, 0, "corvet"),
#                   ship_object(-300, -300, 0, "brig"),
#                   ship_object(0, -300, 0, "brig")]
# enemy_ships = [ship_object(-1000, -1500, 180, "fregat"),
#                ship_object(-500, -1500, 180, "fregat"),
#                ship_object(-500, -2000, 180, "karaka"),
#                ship_object(-1000, -2000, 180, "karaka")]

player_ship = ship_object(0, 0, 0, "warship")
friendly_ships = []
enemy_ships = [ship_object(0, -1000, 180, "corvet"),
               ship_object(200, -1000, 180, "corvet")]

kernels = []

waves = []

clock = pygame.time.Clock()

###################################################functions############################################################

def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

def dot_in_ship(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
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
        if dot_in_ship(kernel[0], kernel[1], ax, ay, bx, by, cx, cy, dx, dy):
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

    if (ship.cd_sail == 0) and (ship.move == False):
        ship.move = True
        ship.cd_sail = 100

    gip = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    pi = math.pi
    if (x2 - x1 > 0):
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
        if (-2 * pi < t_a < -1.5 * pi) and (ship_ts * (2 * pi - mt_a) / (0.5 * pi) > tship_ts) or (
                0 < t_a < 0.5 * pi) and (ship_ts * mt_a / (0.5 * pi) > tship_ts):
            if (ship.cd_sail == 0) and (target_ship.t_speed > ship.t_speed):
                ship.move = False
                ship.cd_sail = 300

        if (-0.5 * pi < t_a < 0) and (ship_ts * mt_a / (0.5 * pi) > tship_ts) or (1.5 * pi < t_a < 2 * pi) and (
                ship_ts * (2 * pi - mt_a) / (0.5 * pi) > tship_ts):
            if (ship.cd_sail == 0) and (target_ship.t_speed > ship.t_speed):
                ship.move = False
                ship.cd_sail = 300

        if (-1.49 * pi < dif <= -pi) or (-0.49 * pi < dif <= 0) or (0.51 * pi < dif <= pi) or (1.51 * pi < dif <= 2 * pi):
            ship.angle -= turning_speed
            if ship.angle < 0:
                ship.angle = 360 - turning_speed
        elif (-2 * pi < dif < -1.51 * pi) or (-pi < dif < -0.51 * pi) or (0 < dif < 0.49 * pi) or (pi < dif < 1.49 * pi):
            ship.angle += turning_speed
            if ship.angle >= 360:
                ship.angle = 0
    else:
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

def shoot_left(ship, target_ship):
    x1 = ship.x
    y1 = ship.y
    x2 = target_ship.x
    y2 = target_ship.y
    angle = ship.angle
    guns_left = ship.guns_left

    gip = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if (x2 - x1 > 0):
        i_angle = math.acos((y2 - y1) / gip)
    else:
        i_angle = 2 * math.pi - math.acos((y2 - y1) / gip)

    dif = (math.radians(angle) - i_angle)
    pi = math.pi
    dif_angle = math.atan(math.fabs(ship.guns_left[0][1])/gip)

    if gip < ship.gun_distance * 10:
        if ((0.5 * pi - dif_angle < dif < 0.5 * pi + dif_angle) or (-1.5 * pi - dif_angle < dif < -1.5 * pi + dif_angle)) and (ship.cd_left == 0):
            for gun in guns_left:
                gun0 = gun[0]
                gun1 = gun[1]
                gip = (gun0 ** 2 + gun1 ** 2) ** 0.5
                arcsin = math.asin(gun1 / gip)
                kernels.append([gip * math.cos(math.radians(angle) + math.pi + arcsin) + x1,
                                -gip * math.sin(math.radians(angle) + math.pi + arcsin) + y1, angle - 90, ship.gun_distance])
                ship.cd_left = 101

def shoot_right(ship, target_ship):
    x1 = ship.x
    y1 = ship.y
    x2 = target_ship.x
    y2 = target_ship.y
    angle = ship.angle
    guns_right = ship.guns_right

    gip = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if (x2 - x1 > 0):
        i_angle = math.acos((y2 - y1) / gip)
    else:
        i_angle = 2 * math.pi - math.acos((y2 - y1) / gip)

    dif = (math.radians(angle) - i_angle)
    pi = math.pi
    dif_angle = math.atan(math.fabs(ship.guns_left[0][1]) / gip)

    if gip < ship.gun_distance * 10:
        if ((-0.5 * pi - dif_angle < dif < -0.5 * pi + dif_angle) or (1.5 * pi - dif_angle < dif < 1.5 * pi + dif_angle)) and (ship.cd_right == 0):
            for gun in guns_right:
                gun0 = gun[0]
                gun1 = gun[1]
                gip = (gun0 ** 2 + gun1 ** 2) ** 0.5
                arcsin = math.asin(gun1 / gip)
                kernels.append([gip * math.cos(math.radians(angle) + arcsin) + x1,
                                -gip * math.sin(math.radians(angle) + arcsin) + y1, angle + 90, ship.gun_distance])
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

    if (dot_in_ship(ax1, ay1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)) or (
        dot_in_ship(bx1, by1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)) or (
        dot_in_ship(cx1, cy1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)) or (
        dot_in_ship(dx1, dy1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)) or (
        dot_in_ship(ax2, ay2, ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1)) or (
        dot_in_ship(bx2, by2, ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1)) or (
        dot_in_ship(cx2, cy2, ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1)) or (
        dot_in_ship(dx2, dy2, ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1)):
        gip = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if (ship2 == player_ship):
            ship1.x += ship1.speed * (x1 - x2) / gip
            ship1.y += ship1.speed * (y1 - y2) / gip
            for ship in enemy_ships:
                ship.x += ship2.speed * (x1 - x2) / gip
                ship.y += ship2.speed * (y1 - y2) / gip
            for ship in friendly_ships:
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
    angle = ship.angle
    dist = ((ship.x - target_ship.x) ** 2 + (ship.y - target_ship.y) ** 2) ** 0.5
    block_dist = ((ship.x - block_ship.x) ** 2 + (ship.y - block_ship.y) ** 2) ** 0.5
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

    downx = block_ship.x + (ship.guns_left[0][1]) * math.sin(math.radians(block_ship.angle))
    downy = block_ship.y + (ship.guns_left[0][1]) * math.cos(math.radians(block_ship.angle))
    upx = block_ship.x + (ship.guns_left[len(ship.guns_left) - 1][1]) * math.sin(math.radians(block_ship.angle))
    upy = block_ship.y + (ship.guns_left[len(ship.guns_left) - 1][1]) * math.cos(math.radians(block_ship.angle))

    if ((dot_in_ship(downx, downy, ax, ay, bx, by, cx, cy, dx, dy)) or (
            dot_in_ship(upx, upy, ax, ay, bx, by, cx, cy, dx, dy))) and (
            dist > block_dist):
        return True
    else:
        return False

def no_may_shoot_right(ship, target_ship, block_ship):
    x = ship.x
    y = ship.y
    angle = ship.angle
    dist = ((ship.x - target_ship.x) ** 2 + (ship.y - target_ship.y) ** 2) ** 0.5
    block_dist = ((ship.x - block_ship.x) ** 2 + (ship.y - block_ship.y) ** 2) ** 0.5
    gip1 = ((ship.guns_left[0][0]) ** 2 + (ship.guns_left[0][1]) ** 2) ** 0.5
    gip2 = ((ship.guns_left[len(ship.guns_left) - 1][0]) ** 2 + (ship.guns_left[len(ship.guns_left) - 1][1]) ** 2)

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

    downx = block_ship.x + (ship.guns_left[0][1]) * math.sin(math.radians(block_ship.angle))
    downy = block_ship.y + (ship.guns_left[0][1]) * math.cos(math.radians(block_ship.angle))
    upx = block_ship.x + (ship.guns_left[len(ship.guns_left) - 1][1]) * math.sin(math.radians(block_ship.angle))
    upy = block_ship.y + (ship.guns_left[len(ship.guns_left) - 1][1]) * math.cos(math.radians(block_ship.angle))

    if ((dot_in_ship(downx, downy, ax, ay, bx, by, cx, cy, dx, dy)) or (
            dot_in_ship(upx, upy, ax, ay, bx, by, cx, cy, dx, dy))) and (
            dist > block_dist):
        return True
    else:
        return False

###################################################game_start###########################################################

def run_game():
    player_ship.move = True
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

####################################################control#############################################################

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_ship.move = True
        elif keys[pygame.K_s]:
            player_ship.move = False
        if keys[pygame.K_d]:
            player_ship.angle -= player_ship.t_speed
            if player_ship.angle < 0:
                player_ship.angle = 360 - player_ship.t_speed
        elif keys[pygame.K_a]:
            player_ship.angle += player_ship.t_speed
            if player_ship.angle >= 360:
                player_ship.angle = 0
        if keys[pygame.K_q]:
            if player_ship.cd_left == 0:
                x = player_ship.x
                y = player_ship.y
                angle = player_ship.angle
                gun_distance = player_ship.gun_distance
                for gun in player_ship.guns_left:
                    gun0 = gun[0]
                    gun1 = gun[1]
                    gip = (gun0 ** 2 + gun1 ** 2) ** 0.5
                    arcsin = math.asin(gun1/gip)
                    kernels.append([gip*math.cos(math.radians(angle)+math.pi+arcsin) + x, -gip*math.sin(math.radians(angle)+math.pi+arcsin) + y, angle - 90, gun_distance])
                player_ship.cd_left = 100
        if keys[pygame.K_e]:
            if player_ship.cd_right == 0:
                x = player_ship.x
                y = player_ship.y
                angle = player_ship.angle
                gun_distance = player_ship.gun_distance
                for gun in player_ship.guns_right:
                    gun0 = gun[0]
                    gun1 = gun[1]
                    gip = (gun0 ** 2 + gun1 ** 2) ** 0.5
                    arcsin = math.asin(gun1 / gip)
                    kernels.append([gip * math.cos(math.radians(angle) + arcsin) + x, -gip*math.sin(math.radians(angle) + arcsin) + y, angle + 90, gun_distance])
                player_ship.cd_right = 100
        if keys[pygame.K_1]:
            scale = 1
        elif keys[pygame.K_2]:
            scale = 2
        elif keys[pygame.K_3]:
            scale = 4

        if player_ship.cd_left > 0:
            player_ship.cd_left -= 1
        if player_ship.cd_right > 0:
            player_ship.cd_right -= 1

        for enemy_ship in enemy_ships:
            enemy_ship.target = -1
            dist_target = (enemy_ship.x-player_ship.x)**2+(enemy_ship.y-player_ship.y)**2
            for i in range(len(friendly_ships)):
                dist = (enemy_ship.x-friendly_ships[i].x)**2+(enemy_ship.y-friendly_ships[i].y)**2
                if dist < dist_target:
                    enemy_ship.target = i
                    dist_target = dist
            if enemy_ship.target == -1:
                swim_to_target(enemy_ship, player_ship)
            else:
                swim_to_target(enemy_ship, friendly_ships[enemy_ship.target])

            may_shoot_left = True
            may_shoot_right = True
            for no_shoot_enemy_ship in enemy_ships:
                if (no_shoot_enemy_ship != enemy_ship):
                    if no_may_shoot_left(enemy_ship, player_ship, no_shoot_enemy_ship):
                        may_shoot_left = False
                    if no_may_shoot_right(enemy_ship, player_ship, no_shoot_enemy_ship):
                        may_shoot_right = False
            if may_shoot_left:
                shoot_left(enemy_ship, player_ship)
            else:
                if (enemy_ship.cd_sail == 0):
                    enemy_ship.move = True
                    enemy_ship.cd_sail = 100
            if may_shoot_right:
                shoot_right(enemy_ship, player_ship)
            else:
                if (enemy_ship.cd_sail == 0):
                    enemy_ship.move = True
                    enemy_ship.cd_sail = 100

            for friendly_ship in friendly_ships:
                may_shoot_left = True
                may_shoot_right = True
                for no_shoot_enemy_ship in enemy_ships:
                    if (no_shoot_enemy_ship != enemy_ship):
                        if no_may_shoot_left(enemy_ship, friendly_ship, no_shoot_enemy_ship):
                            may_shoot_left = False
                        if no_may_shoot_right(enemy_ship, friendly_ship, no_shoot_enemy_ship):
                            may_shoot_right = False
                if may_shoot_left:
                    shoot_left(enemy_ship, friendly_ship)
                else:
                    if (enemy_ship.cd_sail == 0):
                        enemy_ship.move = True
                        enemy_ship.cd_sail = 100
                if may_shoot_right:
                    shoot_right(enemy_ship, friendly_ship)
                else:
                    if (enemy_ship.cd_sail == 0):
                        enemy_ship.move = True
                        enemy_ship.cd_sail = 100

        for friendly_ship in friendly_ships:
            friendly_ship.target = 0
            dist_target = (friendly_ship.x-enemy_ships[0].x)**2+(friendly_ship.y-enemy_ships[0].y)**2
            for i in range(len(enemy_ships)):
                dist = (friendly_ship.x-enemy_ships[i].x)**2+(friendly_ship.y-enemy_ships[i].y)**2
                if dist < dist_target:
                    friendly_ship.target = i
                    dist_target = dist
            swim_to_target(friendly_ship, enemy_ships[friendly_ship.target])

            for enemy_ship in enemy_ships:
                may_shoot_left = True
                may_shoot_right = True
                for no_shoot_friendly_ship in friendly_ships:
                    if (no_shoot_friendly_ship != friendly_ship):
                        if no_may_shoot_left(friendly_ship, enemy_ship, no_shoot_friendly_ship):
                            may_shoot_left = False
                        if no_may_shoot_right(friendly_ship, enemy_ship, no_shoot_friendly_ship):
                            may_shoot_right = False
                if no_may_shoot_left(friendly_ship, enemy_ship, player_ship):
                    may_shoot_left = False
                if no_may_shoot_right(friendly_ship, enemy_ship, player_ship):
                    may_shoot_right = False
                if may_shoot_left:
                    shoot_left(friendly_ship, enemy_ship)
                else:
                    if (friendly_ship.cd_sail == 0):
                        friendly_ship.move = True
                        friendly_ship.cd_sail = 100
                if may_shoot_right:
                    shoot_right(friendly_ship, enemy_ship)
                else:
                    if (friendly_ship.cd_sail == 0):
                        friendly_ship.move = True
                        friendly_ship.cd_sail = 100

################################################ship_intersection#######################################################

        for enemy_ship in enemy_ships:
            ship_intersection(enemy_ship, player_ship)
            for friendly_ship in friendly_ships:
                ship_intersection(enemy_ship, friendly_ship)
            for other_enemy_ship in enemy_ships:
                if other_enemy_ship != enemy_ship:
                    ship_intersection(enemy_ship, other_enemy_ship)

        for friendly_ship in friendly_ships:
            ship_intersection(friendly_ship, player_ship)
            for enemy_ship in enemy_ships:
                ship_intersection(friendly_ship, enemy_ship)
            for other_friendly_ship in friendly_ships:
                if other_friendly_ship != friendly_ship:
                    ship_intersection(friendly_ship, other_friendly_ship)

########################################################movement########################################################

        for wave in waves:
            image = pygame.transform.smoothscale(wave_step[wave[2] // 8], (24 / scale, 8 / scale))
            rect = image.get_rect(center=(center_x + wave[0] / scale, center_y + wave[1] / scale))
            surf, r = rot_center(image, rect, 0)
            display.blit(surf, r)
            wave[2] += 1
            if wave[2] >= 48:
                waves.remove(wave)

        if player_ship.move:
            image = pygame.transform.smoothscale(player_ship.pic_move, (player_ship.get_width(), player_ship.get_height()))
            for enemy_ship in enemy_ships:
                enemy_ship.x += math.sin(math.radians(player_ship.angle)) * player_ship.speed
                enemy_ship.y += math.cos(math.radians(player_ship.angle)) * player_ship.speed
            for friendly_ship in friendly_ships:
                friendly_ship.x += math.sin(math.radians(player_ship.angle)) * player_ship.speed
                friendly_ship.y += math.cos(math.radians(player_ship.angle)) * player_ship.speed
            for wave in waves:
                wave[0] += math.sin(math.radians(player_ship.angle)) * player_ship.speed
                wave[1] += math.cos(math.radians(player_ship.angle)) * player_ship.speed
        else:
            image = pygame.transform.smoothscale(player_ship.pic_stay, (player_ship.get_width(), player_ship.get_height()))

        rect = image.get_rect(center=(center_x, center_y))
        surf, r = rot_center(image, rect, player_ship.angle)
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

        ships_and_kernels(player_ship)
        f = pygame.font.Font(None, 48)
        typ = f.render(player_ship.type, True, (128, 255, 0))
        display.blit(typ, (1000, 5))
        hp = f.render(str(player_ship.hp), True, (0, 255, 0))
        display.blit(hp, (1150, 5))
        if (player_ship.hp <= 0):
            f = pygame.font.Font(None, 72)
            final = f.render("FINISH HIM!", True, (255, 0, 0))
            display.blit(final, (480, 430))
            game = False

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

        step = 40
        for friendly_ship in friendly_ships:
            ships_and_kernels(friendly_ship)
            f = pygame.font.Font(None, 48)
            typ = f.render(friendly_ship.type, True, (255, 255, 0))
            display.blit(typ, (1000, step))
            hp = f.render(str(friendly_ship.hp), True, (0, 255, 0))
            display.blit(hp, (1150, step))
            if (friendly_ship.hp <= 0):
                friendly_ships.remove(friendly_ship)
            step += 35

        if (len(enemy_ships) == 0):
            f3 = pygame.font.Font(None, 72)
            final = f3.render("FLAWLESS VICTORY!", True, (0, 255, 0))
            display.blit(final, (360, 430))
            game = False

        pygame.display.update()
        clock.tick(30)

    pygame.time.wait(3000)

run_game()