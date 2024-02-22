# file for all functions

import pygame
import random
import math
import assets

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

# collision detection (player shots --> enemy)
def collision(alienX_list, alienY_list, ammoX_list, ammoY_list):
    distance = math.sqrt((math.pow(alienX_list - ammoX_list, 2)) + (math.pow(alienY_list - ammoY_list, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player missile --> enemy)
def collision1(alienX_list, alienY_list, missileX, missileY):
    distance = math.sqrt((math.pow(alienX_list - missileX, 2)) + (math.pow(alienY_list - missileY, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <-- enemy shots)
def collision2(playerX, playerY, alienX_ammo, alienY_ammo):
    distance = math.sqrt((math.pow(playerX - alienX_ammo, 2)) + (math.pow(playerY - alienY_ammo, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <--> enemy)
def collision3(playerX, playerY, alienX_list, alienY_list):
    distance = math.sqrt((math.pow(playerX - alienX_list, 2)) + (math.pow(playerY - alienY_list, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <--> HP_drop)
def collision4(playerX, playerY, drop_numbX, drop_numbY):
    distance = math.sqrt((math.pow(playerX - drop_numbX, 2)) + (math.pow(playerY - drop_numbY, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <--> ammo_drop)
def collision5(playerX, playerY, ammo_drop_numbX, ammo_drop_numbY):
    distance = math.sqrt((math.pow(playerX - ammo_drop_numbX, 2)) + (math.pow(playerY - ammo_drop_numbY, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player shots --> boss)
def collision6(bossX, bossY, ammoX_list, ammoY_list):
    distance = math.sqrt((math.pow(bossX - ammoX_list, 2)) + (math.pow((bossY + 70) - ammoY_list, 2)))
    if distance < 50:
        return True
    else:
        return False

# collision detection (player missile --> boss)
def collision7(bossX, bossY, missileX, missileY):
    distance = math.sqrt((math.pow(bossX - missileX, 2)) + (math.pow((bossY + 70) - missileY, 2)))
    if distance < 50:
        return True
    else:
        return False

# collision detection (player <--> boss)
def collision8(playerX, playerY, bossX, bossY):
    distance = math.sqrt((math.pow(playerX - bossX, 2)) + (math.pow(playerY - (bossY + 70), 2)))
    if distance < 50:
        return True
    else:
        return False

# collision detection (player <-- boss shots (top))
def collision9(playerX, playerY, bossX_ammo_top, bossY_ammo_top):
    distance = math.sqrt((math.pow(playerX - bossX_ammo_top, 2)) + (math.pow(playerY - bossY_ammo_top, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <-- boss shots (bottom))
def collision10(playerX, playerY, bossX_ammo_bottom, bossY_ammo_bottom):
    distance = math.sqrt((math.pow(playerX - bossX_ammo_bottom, 2)) + (math.pow(playerY - bossY_ammo_bottom, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <-- boss laser shots(top))
def collision11(playerX, playerY, bossX_ammo_2_top, bossY_ammo_2_top):
    distance = math.sqrt((math.pow(playerX - bossX_ammo_2_top, 2)) + (math.pow(playerY - bossY_ammo_2_top, 2)))
    if distance < 27:
        return True
    else:
        return False

# collision detection (player <-- boss laser shots(bottom))
def collision12(playerX, playerY, bossX_ammo_2_bottom, bossY_ammo_2_bottom):
    distance2 = math.sqrt((math.pow(playerX - bossX_ammo_2_bottom, 2)) + (math.pow(playerY - bossY_ammo_2_bottom, 2)))
    if distance2 < 27:
        return True
    else:
        return False

# in range for shot detection for enemies
def Range(playerY, alienY_list):
    distance = (playerY + 10) - alienY_list
    distance2 = (playerY - 10) - alienY_list
    if 0 < distance < 300 and -11 < distance2 < 300:
        return True
    else:
        return False

# in range for shot detection for boss
def Range_2(playerY, bossY):
    distance = (playerY + 10) - bossY
    distance2 = (playerY - 10) - bossY
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

# explosion
def explosion(x, y, i, cube_list):
    assets.screen.blit(cube_list[i], (x, y))

# create enemies function
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