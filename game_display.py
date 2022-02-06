import pygame
import math

pygame.init()
pygame.font.init()

display_width = 1200
display_height = 900
scale = 2

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ship game')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

####################################################classes#############################################################

class ship:
    def __init__(self, pic_move, pic_stay, deck_width, deck_height, speed, t_speed, hp, x, y, angle, guns_left, guns_right, cd_left = 0, cd_right = 0, move=True, target = -1):
        self.pic_move = pic_move
        self.pic_stay = pic_stay
        self.deck_width = deck_width
        self.deck_height = deck_height
        self.speed = speed
        self.t_speed = t_speed
        self.hp = hp
        self.x = x
        self.y = y
        self.angle = angle
        self.guns_left = guns_left
        self.guns_right = guns_right
        self.cd_left = cd_left
        self.cd_right = cd_right
        self.move = move
        self.target = target
    def get_width(self):
        return self.pic_move.get_width() / scale
    def get_height(self):
        return self.pic_move.get_height() / scale

#################################################create_ships###########################################################

kernel_image = pygame.image.load('kernel.png')
kernel_hit_image = pygame.image.load('kernel_hit.png')
kernel_miss_image = pygame.image.load('kernel_miss.png')
ring_image = pygame.image.load('ring.png')

bark_move = pygame.image.load('bark\\sail_1.png')
bark_stay = pygame.image.load('bark\\sail_0.png')
bark_deck_width = 42/scale
bark_deck_height = 144/scale
bark_guns_left = [(-27/scale, -36/scale), (-27/scale, -12/scale), (-27/scale, 12/scale), (-27/scale, 36/scale)]
bark_guns_right = [(27/scale, -36/scale), (27/scale, -12/scale), (27/scale, 12/scale), (27/scale, 36/scale)]

shuna_move = pygame.image.load('shuna\\sail_1.png')
shuna_stay = pygame.image.load('shuna\\sail_0.png')
shuna_deck_width = 34/scale
shuna_deck_height = 108/scale
shuna_guns_left = [(-23/scale, -30/scale), (-23/scale, -6/scale), (-23/scale, 18/scale)]
shuna_guns_right = [(23/scale, -30/scale), (23/scale, -6/scale), (23/scale, 18/scale)]

player_ship = ship(bark_move, bark_stay, bark_deck_width, bark_deck_height, 0.8, 0.6, 30, 600, 450, 0, bark_guns_left, bark_guns_right)
friendly_ships = [ship(bark_move, bark_stay, bark_deck_width, bark_deck_height, 0.8, 0.6, 30, 700, 450, 0, bark_guns_left, bark_guns_right)]
enemy_ships = [ship(shuna_move, shuna_stay, shuna_deck_width, shuna_deck_height, 0.6, 0.8, 20, 200, 100, 180, shuna_guns_left, shuna_guns_right),
               ship(shuna_move, shuna_stay, shuna_deck_width, shuna_deck_height, 0.6, 0.8, 20, 1100, 100, 180, shuna_guns_left, shuna_guns_right),
               ship(shuna_move, shuna_stay, shuna_deck_width, shuna_deck_height, 0.6, 0.8, 20, 200, 800, 0, shuna_guns_left, shuna_guns_right),
               ship(shuna_move, shuna_stay, shuna_deck_width, shuna_deck_height, 0.6, 0.8, 20, 1100, 800, 0, shuna_guns_left, shuna_guns_right)]

# player_ship = ship(shuna_move, shuna_stay, shuna_deck_width, shuna_deck_height, 0.6, 0.8, 20, 600, 450, 0, shuna_guns_left, shuna_guns_right)
# enemy_ships = [ship(bark_move, bark_stay, bark_deck_width, bark_deck_height, 0.8, 0.6, 30, 200, 100, 180, bark_guns_left, bark_guns_right)]

kernels = []

clock = pygame.time.Clock()

###################################################functions############################################################

def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect

def kernel_in_ship(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
    p21 = [x2 - x1, y2 - y1]
    p41 = [x4 - x1, y4 - y1]
    p21magnitude_squared = p21[0] ** 2 + p21[1] ** 2
    p41magnitude_squared = p41[0] ** 2 + p41[1] ** 2
    p = (x - x1, y - y1)
    if 0 <= (p[0] * p21[0] + p[1] * p21[1]) <= p21magnitude_squared:
        if 0 <= (p[0] * p41[0] + p[1] * p41[1]) <= p41magnitude_squared:
            return True
        else:
            return False
    else:
        return False

def ships_and_kernels(enemy_ship):
    edw2 = enemy_ship.deck_width / 2
    edh2 = enemy_ship.deck_height / 2
    en_x = enemy_ship.x
    en_y = enemy_ship.y
    eangle = enemy_ship.angle

    gip = (edw2 ** 2 + edh2 ** 2) ** 0.5
    eax = gip * math.cos(math.radians(eangle) + math.asin(edh2 / gip)) + en_x
    eay = -gip * math.sin(math.radians(eangle) + math.asin(edh2 / gip)) + en_y
    ebx = gip * math.cos(math.radians(eangle) - math.asin(edh2 / gip)) + en_x
    eby = -gip * math.sin(math.radians(eangle) - math.asin(edh2 / gip)) + en_y
    ecx = gip * math.cos(math.radians(eangle) + math.pi + math.asin(edh2 / gip)) + en_x
    ecy = -gip * math.sin(math.radians(eangle) + math.pi + math.asin(edh2 / gip)) + en_y
    edx = gip * math.cos(math.radians(eangle) + math.pi - math.asin(edh2 / gip)) + en_x
    edy = -gip * math.sin(math.radians(eangle) + math.pi - math.asin(edh2 / gip)) + en_y

    for kernel in kernels:
        if kernel_in_ship(kernel[0], kernel[1], eax, eay, ebx, eby, ecx, ecy, edx, edy):
            image = pygame.transform.smoothscale(kernel_hit_image, (5, 5))
            display.blit(image, (kernel[0], kernel[1]))
            kernels.remove(kernel)
            enemy_ship.hp -= 1

def swim_to_target(enemy_ship, player_ship):
    en_x = enemy_ship.x
    en_y = enemy_ship.y
    usr_x = player_ship.x
    usr_y = player_ship.y
    eangle = enemy_ship.angle
    eturning_speed = enemy_ship.t_speed
    guns_left = enemy_ship.guns_left
    guns_right = enemy_ship.guns_right

    gip = ((en_x - usr_x) ** 2 + (en_y - usr_y) ** 2) ** 0.5
    if (en_y - usr_y < 0):
        i_angle = math.acos((en_x - usr_x) / gip)
    else:
        i_angle = 2 * math.pi - math.acos((en_x - usr_x) / gip)

    dif = (math.radians(eangle) - i_angle)
    pi = math.pi

    if gip < 200:
        if (-2 * pi < dif < -1.5 * pi) or (-pi < dif < -0.5 * pi) or (0 < dif < 0.5 * pi) or (pi < dif < 1.5 * pi):
            enemy_ship.angle -= eturning_speed
            if enemy_ship.angle <= 0:
                enemy_ship.angle = 360
        else:
            enemy_ship.angle += eturning_speed
            if enemy_ship.angle >= 360:
                enemy_ship.angle = 0
    else:
        if (-1.5 * pi < dif < -0.5 * pi) or (0.5 * pi < dif < 1.5 * pi):
            enemy_ship.angle -= eturning_speed
            if enemy_ship.angle <= 0:
                enemy_ship.angle = 360
        else:
            enemy_ship.angle += eturning_speed
            if enemy_ship.angle >= 360:
                enemy_ship.angle = 0

    if (gip < 200):
        if ((-0.05 * pi < dif < 0.05 * pi) or (1.95 * pi < dif < 2 * pi) or (-2 * pi < dif < -1.95 * pi)) and (
                enemy_ship.cd_left == 0):
            for gun in guns_left:
                gip = (gun[0] ** 2 + gun[1] ** 2) ** 0.5
                arcsin = math.asin(gun[1] / gip)
                kernels.append([gip * math.cos(math.radians(eangle) + math.pi + arcsin) + en_x,
                                -gip * math.sin(math.radians(eangle) + math.pi + arcsin) + en_y, eangle - 90, 40])
                enemy_ship.cd_left = 100
        elif ((-1.05 * pi < dif < -0.95 * pi) or (0.95 * pi < dif < 1.05 * pi)) and (enemy_ship.cd_right == 0):
            for gun in guns_right:
                gip = (gun[0] ** 2 + gun[1] ** 2) ** 0.5
                arcsin = math.asin(gun[1] / gip)
                kernels.append([gip * math.cos(math.radians(eangle) + arcsin) + en_x,
                                -gip * math.sin(math.radians(eangle) + arcsin) + en_y, eangle + 90, 40])
                enemy_ship.cd_right = 100

    if enemy_ship.cd_left > 0:
        enemy_ship.cd_left -= 1
    if enemy_ship.cd_right > 0:
        enemy_ship.cd_right -= 1

def ship_intersection(ship1, ship2):
    x1 = ship1.x
    y1 = ship1.y
    x2 = ship2.x
    y2 = ship2.y
    dh1 = ship1.deck_height
    dw1 = ship1.deck_width
    dh2 = ship2.deck_height
    dw2 = ship2.deck_width
    gip = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    dist = ((dh1 / 2) ** 2 + (dw1 / 2) ** 2 + (dh2 / 2) ** 2 + (dw2 / 2) ** 2) ** 0.5
    if gip <= dist:
        dif = dist - gip
        ship1.x += (x1 - x2) * dif / gip
        ship1.y += (y1 - y2) * dif / gip
        ship2.x -= (x1 - x2) * dif / gip
        ship2.y -= (y1 - y2) * dif / gip

###################################################game_start###########################################################

def run_game():
    player_ship.move = True
    game = True
    ring_x = 650
    ring_y = 450

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((63, 72, 204))

        image = pygame.transform.smoothscale(ring_image, (600, 600))

        rect = image.get_rect(center=(ring_x, ring_y))
        surf, r = rot_center(image, rect, 0)
        display.blit(surf, r)

###################################################controls#############################################################

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_ship.move = True
        elif keys[pygame.K_d]:
            player_ship.angle -= player_ship.t_speed
            if player_ship.angle <= 0:
                player_ship.angle = 360
        elif keys[pygame.K_a]:
            player_ship.angle += player_ship.t_speed
            if player_ship.angle >= 360:
                player_ship.angle = 0
        elif keys[pygame.K_s]:
            player_ship.move = False
        elif keys[pygame.K_q]:
            if player_ship.cd_left == 0:
                x = player_ship.x
                y = player_ship.y
                angle = player_ship.angle
                for gun in player_ship.guns_left:
                    gip = (gun[0] ** 2 + gun[1] ** 2) ** 0.5
                    arcsin = math.asin(gun[1]/gip)
                    kernels.append([gip*math.cos(math.radians(angle)+math.pi+arcsin) + x, -gip*math.sin(math.radians(angle)+math.pi+arcsin) + y, angle - 90, 40])
                player_ship.cd_left = 100
        elif keys[pygame.K_e]:
            if player_ship.cd_right == 0:
                x = player_ship.x
                y = player_ship.y
                angle = player_ship.angle
                for gun in player_ship.guns_right:
                    gip = (gun[0] ** 2 + gun[1] ** 2) ** 0.5
                    arcsin = math.asin(gun[1] / gip)
                    kernels.append([gip * math.cos(math.radians(angle) + arcsin) + x, -gip*math.sin(math.radians(angle) + arcsin) + y, angle + 90, 40])
                player_ship.cd_right = 100

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

        for friendly_ship in friendly_ships:
            friendly_ship.target = 0
            dist_target = (friendly_ship.x-enemy_ships[0].x)**2+(friendly_ship.y-enemy_ships[0].y)**2
            for i in range(len(enemy_ships)):
                dist = (friendly_ship.x-enemy_ships[i].x)**2+(friendly_ship.y-enemy_ships[i].y)**2
                if dist < dist_target:
                    friendly_ship.target = i
                    dist_target = dist
            swim_to_target(friendly_ship, enemy_ships[friendly_ship.target])

########################################################movement########################################################

        if player_ship.move:
            image = pygame.transform.smoothscale(player_ship.pic_move, (player_ship.get_width(), player_ship.get_height()))
            # player_ship.x -= math.sin(math.radians(player_ship.angle)) * player_ship.speed
            # player_ship.y -= math.cos(math.radians(player_ship.angle)) * player_ship.speed
            for enemy_ship in enemy_ships:
                enemy_ship.x += math.sin(math.radians(player_ship.angle)) * player_ship.speed
                enemy_ship.y += math.cos(math.radians(player_ship.angle)) * player_ship.speed
            for friendly_ship in friendly_ships:
                friendly_ship.x += math.sin(math.radians(player_ship.angle)) * player_ship.speed
                friendly_ship.y += math.cos(math.radians(player_ship.angle)) * player_ship.speed
            ring_x += math.sin(math.radians(player_ship.angle)) * player_ship.speed
            ring_y += math.cos(math.radians(player_ship.angle)) * player_ship.speed
        else:
            image = pygame.transform.smoothscale(player_ship.pic_stay, (player_ship.get_width(), player_ship.get_height()))

        rect = image.get_rect(center=(player_ship.x, player_ship.y))
        surf, r = rot_center(image, rect, player_ship.angle)
        display.blit(surf, r)

        for enemy_ship in enemy_ships:
            image = pygame.transform.smoothscale(enemy_ship.pic_move, (enemy_ship.get_width(), enemy_ship.get_height()))

            enemy_ship.x -= math.sin(math.radians(enemy_ship.angle)) * enemy_ship.speed
            enemy_ship.y -= math.cos(math.radians(enemy_ship.angle)) * enemy_ship.speed

            rect = image.get_rect(center=(enemy_ship.x, enemy_ship.y))
            surf, r = rot_center(image, rect, enemy_ship.angle)
            display.blit(surf, r)

        for friendly_ship in friendly_ships:
            image = pygame.transform.smoothscale(friendly_ship.pic_move, (friendly_ship.get_width(), friendly_ship.get_height()))

            friendly_ship.x -= math.sin(math.radians(friendly_ship.angle)) * friendly_ship.speed
            friendly_ship.y -= math.cos(math.radians(friendly_ship.angle)) * friendly_ship.speed

            rect = image.get_rect(center=(friendly_ship.x, friendly_ship.y))
            surf, r = rot_center(image, rect, friendly_ship.angle)
            display.blit(surf, r)

################################################ship_intersection#######################################################

        for enemy_ship in enemy_ships:
            ship_intersection(enemy_ship, player_ship)
            for friendly_ship in friendly_ships:
                ship_intersection(enemy_ship, friendly_ship)
            for other_enemy_ship in enemy_ships:
                if (other_enemy_ship != enemy_ship):
                    ship_intersection(enemy_ship, other_enemy_ship)

        for friendly_ship in friendly_ships:
            ship_intersection(friendly_ship, player_ship)
            for enemy_ship in enemy_ships:
                ship_intersection(friendly_ship, enemy_ship)
            for other_friendly_ship in friendly_ships:
                if (other_friendly_ship != friendly_ship):
                    ship_intersection(friendly_ship, other_friendly_ship)

######################################################kernels###########################################################

        for kernel in kernels:
            kernel[0] += math.sin(math.radians(kernel[2])) * 5
            kernel[1] += math.cos(math.radians(kernel[2])) * 5
            kernel[3] -= 1
            if kernel[3] <= 0:
                image = pygame.transform.smoothscale(kernel_miss_image, (5, 5))
                display.blit(image, (kernel[0], kernel[1]))
                kernels.remove(kernel)
            else:
                image = pygame.transform.smoothscale(kernel_image, (3, 3))
                display.blit(image, (kernel[0], kernel[1]))

        ships_and_kernels(player_ship)
        f = pygame.font.Font(None, 72)
        hp = f.render(str(player_ship.hp), True, (0, 255, 0))
        display.blit(hp, (1130, 10))
        if (player_ship.hp <= 0):
            f = pygame.font.Font(None, 72)
            final = f.render("FINISH HIM!", True, (255, 0, 0))
            display.blit(final, (480, 430))
            game = False

        step = 10
        for enemy_ship in enemy_ships:
            ships_and_kernels(enemy_ship)
            f = pygame.font.Font(None, 72)
            hp = f.render(str(enemy_ship.hp), True, (255, 0, 0))
            display.blit(hp, (10, step))
            if (enemy_ship.hp <= 0):
                enemy_ships.remove(enemy_ship)
            step += 50

        step = 60
        for friendly_ship in friendly_ships:
            ships_and_kernels(friendly_ship)
            f = pygame.font.Font(None, 72)
            hp = f.render(str(friendly_ship.hp), True, (255, 255, 0))
            display.blit(hp, (1130, step))
            if (friendly_ship.hp <= 0):
                friendly_ships.remove(friendly_ship)
            step += 50

        if (len(enemy_ships) == 0):
            f3 = pygame.font.Font(None, 72)
            final = f3.render("FLAWLESS VICTORY!", True, (0, 255, 0))
            display.blit(final, (360, 430))
            game = False

        pygame.display.update()
        clock.tick(30)

    pygame.time.wait(3000)

run_game()