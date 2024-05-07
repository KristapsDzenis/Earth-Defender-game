# file for all functions

import pygame
import random
import math
import assets
#import stats

pygame.init()

# health counter
def healthCounter(player_HP):
    health_bar = assets.font.render(str(player_HP), True, (255, 255, 255))
    assets.screen.blit(health_bar, (980, 705))

# ammo counter
def ammoCounter(ammo):
    ammo_bar = assets.font.render(str(ammo), True, (255, 255, 255))
    assets.screen.blit(ammo_bar, (150, 705))

# score counter
def scoreCounter(score):
    score_bar = assets.font.render(str(score), True, (255, 255, 255))
    assets.screen.blit(score_bar, (980, 752))

# missile counter
def missileCounter(missile_ammo):
    missile_bar = assets.font.render(str(missile_ammo), True, (255, 255, 255))
    assets.screen.blit(missile_bar, (150, 752))

#player(no collision)
def player(x, y):
    assets.screen.blit(assets.playerAss, (x, y))

#player(collision)
def player2(x, y):
    assets.screen.blit(assets.playerAss2, (x, y))

#fire ammo function
def fire(x, y, i, ammo_list):
    global ammo_state
    assets.screen.blit(ammo_list[i], (x + 24, y + 2))
    assets.screen.blit(ammo_list[i], (x + 24, y + 28))
    ammo_state = "new"

# fire missile function
def missile_fire(x, y):
    global missile_state
    assets.screen.blit(assets.playerMissile, (x + 25, y + 8))
    missile_state = "new"

# boss
def boss(x, y):
    assets.screen.blit(assets.boss_ass, (x, y))

# boss if collision
def boss2(x, y):
    assets.screen.blit(assets.boss_ass_2, (x, y))

# boss fire function (top gun)
def boss_fire(x, y, i, boss_ammo_top):
    assets.screen.blit(boss_ammo_top[i], (x + 100, y + 0))

# boss fire function (bottom gun)
def boss_fire_2(x, y, i, boss_ammo_bottom):
    assets.screen.blit(boss_ammo_bottom[i], (x + 100, y + 150))

# boss fire function for second weapond type (top gun)
def boss_laser(x, y, i, boss_ammo_top):
    assets.screen.blit(boss_ammo_top[i], (x + 80, y + 45))

# boss fire function for second weapond type (bottom gun)
def boss_laser_2(x, y, i, boss_ammo_bottom):
    assets.screen.blit(boss_ammo_bottom[i], (x + 80, y + 105))

# enemy
def enemy(x, y, i, alien_list):
    assets.screen.blit(alien_list[i], (x, y))

# enemy fire function
def enemy_fire(x, y, i, alien_ammo):
    assets.screen.blit(alien_ammo[i], (x + 15, y + 15))

# extra life spawn function
def HP_drop(x, y, i, HP_drop_list):
    assets.screen.blit(HP_drop_list[i], (x, y))

# extra ammunation spawn function
def ammo_drop(x, y, i, ammo_drop_list):
    assets.screen.blit(ammo_drop_list[i], (x, y))

#extra missile spawn function
def missile_drop(x, y, i, missile_drop_list):
    assets.screen.blit(missile_drop_list[i], (x, y))

# collision detection (standard)
def collision(x, y, z, i):
    distance = math.sqrt((math.pow(x - z, 2)) + (math.pow(y - i, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player/ player shots --> boss)
def collision2(x, y, z, i):
    distance = math.sqrt((math.pow(x - z, 2)) + (math.pow((y+100) - i, 2)))
    if distance < 50:
        return True
    else:
        return False

# collision detection (player <-- boss shots(first weapon type(top))
def collision3(x, y, z, i):
    distance = math.sqrt((math.pow(x - z - 100, 2)) + (math.pow(y - i, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <-- boss shots(first weapon type(bottom))
def collision4(x, y, z, i):
    distance = math.sqrt((math.pow(x - z - 100, 2)) + (math.pow(y - i - 150, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <-- boss shots(second weapon type(top))
def collision5(x, y, z, i):
    distance = math.sqrt((math.pow(x - z - 80, 2)) + (math.pow(y - i - 45, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <-- boss shots(second weapon type(bottom))
def collision6(x, y, z, i):
    distance = math.sqrt((math.pow(x - z - 80, 2)) + (math.pow(y - i - 105, 2)))
    if distance < 27:
        return True
    else:
        return False

# in range for shot detection for enemies/ boss
def Range(x, y):
    distance = (x + 10) - y
    distance2 = (x - 10) - y
    if 0 < distance < 300 and -11 < distance2 < 300:
        return True
    else:
        return False

# function to create debris elements from explosion
def place_cubes(lastX, lastY, cubeX_list, cubeY_list, cube_list, cubeX_change, cubeY_change):
    for i in range(70):
        cube_list.append(assets.cube)
        numb5 = random.randint(-50, 50)
        numb6 = random.randint(-50, 50)
        numb7 = random.uniform(1, 0.05)
        numb8 = random.uniform(1, 0.05)
        numb9 = random.uniform(- 1, - 0.05)
        numb10 = random.uniform(- 1, - 0.05)
        numb1 = random.randint(1, 2)
        numb2 = random.randint(1, 2)

        cubeX_list.append(lastX + numb5)
        cubeY_list.append(lastY + numb6)

        if numb1 == 1:
            cubeX_change.append(numb7)
        if numb2 == 1:
            cubeY_change.append(numb8)
        if numb1 == 2:
            cubeX_change.append(numb9)
        if numb2 == 2:
            cubeY_change.append(numb10)

# function to create debris elements from explosion for  level 1 boss
def place_cubes_boss(lastX, lastY, cubeX_list, cubeY_list, cube_list, cubeX_change, cubeY_change):
    for i in range(500):
        cube_list.append(assets.cube)
        numb5 = random.randint(-80, 80)
        numb6 = random.randint(-50, 50)
        numb7 = random.uniform(1, 0.05)
        numb8 = random.uniform(1, 0.05)
        numb9 = random.uniform(- 1, - 0.05)
        numb10 = random.uniform(- 1, - 0.05)
        numb1 = random.randint(1, 2)
        numb2 = random.randint(1, 2)

        cubeX_list.append(lastX + numb5)
        cubeY_list.append(lastY + numb6)

        if numb1 == 1:
            cubeX_change.append(numb7)
        if numb2 == 1:
            cubeY_change.append(numb8)
        if numb1 == 2:
            cubeX_change.append(numb9)
        if numb2 == 2:
            cubeY_change.append(numb10)

# explosion
def explosion(x, y, i, cube_list):
    assets.screen.blit(cube_list[i], (x, y))

# create enemies type 1 function
def create_enemy(enemy_count,  alien_list, alienX_list, alienY_list, alienHP_list, alienY_change, alienX_change, alien_bool,
                 alien_timer, alien_ammo, alienBool_ammo, alienY_ammo, alienX_ammo):
    for i in range(enemy_count):
        alien_list.append(pygame.transform.rotate((pygame.image.load("assets/alien.png")), 90))
        alienX_list.append(random.randint(1200, 1400))
        alienY_list.append(random.randint(0, 640))
        alienHP_list.append(15)
        # ENEMY SPEED
        alienY_change.append(0)
        alienX_change.append(1)
        alien_bool.append("No_collision")
        alien_timer.append(0)
        alien_ammo.append(pygame.image.load("assets/alien_shot.png"))
        alienBool_ammo.append("old")
    for i in range(enemy_count):
        alienY_ammo.append(alienY_list[i])
        alienX_ammo.append(alienX_list[i])

# create enemies type 2 function
def create_enemy_2(enemy_count_2,  alien_list, alienX_list, alienY_list, alienHP_list, alienY_change, alienX_change, alien_bool,
                 alien_timer, alien_ammo, alienBool_ammo, alienY_ammo, alienX_ammo):
    for i in range(enemy_count_2):
        alien_list.append(pygame.transform.rotate((pygame.image.load("assets/alien_second.png")), 90))
        alienX_list.append(random.randint(1200, 1400))
        alienY_list.append(random.randint(0, 640))
        alienHP_list.append(30)
        # ENEMY SPEED
        alienY_change.append(0)
        alienX_change.append(1)
        alien_bool.append("No_collision")
        alien_timer.append(0)
        alien_ammo.append(pygame.image.load("assets/alien_shot.png"))
        alienBool_ammo.append("old")
    for i in range(enemy_count_2):
        alienY_ammo.append(alienY_list[i])
        alienX_ammo.append(alienX_list[i])
