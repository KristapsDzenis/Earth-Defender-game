# file for main loop for start and Level 1

import pygame
import random
import func
import assets
import stats

pygame.init()

# for frame limiter
clock = pygame.time.Clock()

# start screen loop
def start():
    timer = 0
    timer_bool = "yes"
    run = True
    while run == True:
        assets.screen.fill((0, 0, 0))

        # game title
        title = assets.font4.render("Earth", True, (255, 215, 0))
        assets.screen.blit(title, (390, 200))
        title = assets.font4.render("Defender", True, (255, 215, 0))
        assets.screen.blit(title, (260, 320))

        # blinking text
        if timer_bool == "yes":
            text = assets.font3.render("Press ENTER to start new game", True, (255, 255, 255))
            assets.screen.blit(text, (435, 480))
            timer += 1
        if timer == 100 :
            timer_bool = "no"
        if timer_bool == "no":
            text = assets.font3.render("Press ENTER to start new game", True, (0, 0, 0))
            assets.screen.blit(text, (435, 480))
            timer -= 1
        if timer == 0:
            timer_bool = "yes"

        # start menu event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # press enter to start game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                    main()

        # updates display each frame
        pygame.display.update()
        # limit frames to 100fps / 100 loops per second
        clock.tick(100)

# main loop
def main():
    # initialise all objects
    player = stats.Player()
    drops = stats.Drops()
    aliens = stats.Aliens()
    explode = stats.Explosions()
    boss = stats.level1_Boss()
    wpn1 = stats.level1_Boss_Wpn1()
    wpn2 = stats.level1_Boss_Wpn2()

    # enemy counter start stats
    enemy_numb = 0
    enemy_count = 0
    enemy_wave = False

    timer = 10500
    run = True
    while run == True:
        # background ,UI elements
        assets.screen.fill((0, 0, 0))
        assets.screen.blit(assets.background, (0, 0))
        assets.screen.blit(assets.UI, (-5, 678))

        # first enemy wave spawn
        if timer == 200:
            enemy_numb = 10
            enemy_count = 10
            enemy_wave = True

        # second enemy wave spawn
        if timer == 3000:
            enemy_numb += 15
            enemy_count = 15
            enemy_wave = True
            # spawn extra life for player
            drops.HP_drop_count += 1
            for i in range(drops.HP_drop_count):
                drops.HP_drop_list.append(assets.HP_drop_i)
                drops.drop_numbX.append(random.randint(0, 550))
                drops.drop_numbY.append(random.randint(0, 640))
                func.HP_drop(drops.drop_numbX[i], drops.drop_numbY[i], i, drops.HP_drop_list)

        # third enemy wave spawn
        if timer == 7000:
            enemy_numb += 15
            enemy_count = 15
            enemy_wave = True
            # spawn extra ammunition for player
            drops.ammo_drop_count += 1
            for i in range(drops.ammo_drop_count):
                drops.ammo_drop_list.append(assets.bullet_drop)
                drops.ammo_drop_numbX.append(random.randint(0, 550))
                drops.ammo_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)

        # boss level spawn
        if timer == 11000:
            boss.boss_level = True

        # place enemies on screen
        if enemy_wave == True:
            func.create_enemy(enemy_count, aliens.alien_list, aliens.alienX_list, aliens.alienY_list, aliens.alienHP_list,
                              aliens.alienY_change, aliens.alienX_change,aliens.alien_bool, aliens.alien_timer, aliens.alien_ammo,
                              aliens.alienBool_ammo, aliens.alienY_ammo, aliens.alienX_ammo)
            for i in range(enemy_numb):
                if aliens.alienY_list[i] >= 640:
                    aliens.alienY_change[i] = -1
                if aliens.alienY_list[i] <= 0:
                    aliens.alienY_change[i] = 1
                aliens.alienX_list[i] -= 2
                func.enemy(aliens.alienX_list[i], aliens.alienY_list[i], i, aliens.alien_list)
                if int(i) <= 700:
                    enemy_wave = False

        # place boss on screen
        if boss.boss_level == True:
            boss.bossX = 1200
            boss.bossY = 250
            boss.bossX_change = 0
            boss.bossY_change = 0
            # collision feedback from boss
            if boss.boss_HP > 0:
                if boss.boss_bool == "No_collision":
                    func.boss(boss.bossX, boss.bossY)
                if boss.boss_bool == "Yes_collision":
                    func.boss2(boss.bossX, boss.bossY)
            boss.boss_level = False
            boss.start_phase = True

        # tracks explosion debris on screen
        for i in range(explode.cub_numb):
            func.explosion(explode.cubeX_list[i], explode.cubeY_list[i], i, explode.cube_list)
            explode.cubeX_list[i] += explode.cubeX_change[i]
            explode.cubeY_list[i] += explode.cubeY_change[i]

        # what happens if debris reach edge of the screen
        for i in range(explode.cub_numb):
            if explode.cubeX_list[i] >= 1200 or explode.cubeX_list[i] <= 0:
                explode.cubeX_list[i] = 1200
                explode.cubeY_list[i] = 800
                explode.cubeX_change[i] = 0
                explode.cubeY_change[i] = 0
            if explode.cubeY_list[i] >= 678 or explode.cubeY_list[i] <= 0:
                explode.cubeX_list[i] = 1200
                explode.cubeY_list[i] = 800
                explode.cubeX_change[i] = 0
                explode.cubeY_change[i] = 0

        # deletes off screen debris elements
        if explode.cub_numb > 80:
            for i in range(explode.cub_numb - 80):
                if explode.cubeY_list[i] >= 750:
                    del explode.cube_list[i]
                    del explode.cubeX_list[i]
                    del explode.cubeY_list[i]
                    del explode.cubeX_change[i]
                    del explode.cubeY_change[i]
                    explode.cub_numb -= 1

        # PLAYER LOOP
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # MOVEMENT SPEED
                    player.x_change =- 3.5
                if event.key == pygame.K_RIGHT:
                    player.x_change = 3.5
                if event.key == pygame.K_UP:
                    player.y_change =- 3.5
                if event.key == pygame.K_DOWN:
                    player.y_change = 3.5
                # fire ammo
                if event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(1, 200)
                    if player.hp > 0 and player.ammo > 0:
                        player.max_ammo += 1
                        player.ammo -= 1
                        player.ammo_state = "new"
                        if player.ammo_state == "new":
                            ammoAssX = player.x
                            ammoAssY = player.y
                            # adds new elements at teh end of the list
                            for i in range(1):
                                player.ammo_list.append(assets.ammoAss)
                                player.ammoY_list.append(ammoAssY)
                                player.ammoX_list.append(ammoAssX)
                            # launch fire function when space bar is pressed
                            for i in range(player.max_ammo):
                                func.fire(player.ammoX_list[i], player.ammoY_list[i], i, player.ammo_list)
                # fire missile
                if event.key == pygame.K_q:
                    if player.hp > 0 and player.missile_state == "old" and player.missile_ammo > 0:
                        player.missile_ammo -= 1
                        player.missile_state = "new"
                        player.missile_y = player.y
                        player.missile_x = player.x
                        func.missile_fire(player.missile_x, player.missile_y)
            # for when keys are released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.x_change = 0.0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.y_change = 0.0
                if event.key == pygame.K_SPACE:
                    player.max_ammo += 0

        # tracks player change on screen
        player.x += player.x_change
        player.y += player.y_change

        #edge of screen collision
        if player.x <= 0:
            player.x = 0
        if player.x >= 1130:
            player.x = 1130
        if player.y >= 631:
            player.y = 631
        if player.y <= 0:
            player.y = 0

        # track shots across X Axis
        if player.ammo_state == "new":
            for i in range(player.max_ammo):
                func.fire(player.ammoX_list[i], player.ammoY_list[i], i, player.ammo_list)
                player.ammoX_list[i] += player.ammoX_change
        # removes shots leaving window
        if player.ammo_state == "new":
            for i in range(player.max_ammo - 3):
                if player.ammoX_list[i] >= 1200:
                    del player.ammo_list[i]
                    del player.ammoX_list[i]
                    del player.ammoY_list[i]
                    player.max_ammo -= 1

        # track missile across X axis
        if player.missile_state == "new":
            func.missile_fire(player.missile_x, player.missile_y)
            player.missile_x += player.missileX_change
        # prepares for new missile when old one leaves window
        if player.missile_state == "new" and player.missile_x >= 1200:
            player.missile_state = "old"

        # ENEMY LOOP
        if enemy_wave == False:
            for i in range(enemy_numb):
                # enemy movement
                aliens.alienY_list[i] += aliens.alienY_change[i]
                aliens.alienX_list[i] += aliens.alienX_change[i]
                # enemy zone of control/collision
                if aliens.alienY_list[i] >= 640:
                    aliens.alienY_change[i] = -1
                if aliens.alienY_list[i] <= 0:
                    aliens.alienY_change[i] = 1
                if aliens.alienX_list[i] >= 1180:
                    aliens.alienX_change[i] = -1
                if aliens.alienX_list[i] <= 450:
                    aliens.alienX_change[i] = 1
                # random direction change
                numb = random.randint(1, 500)
                if numb == 1:
                    aliens.alienX_change[i] = -1
                if numb == 2:
                    aliens.alienX_change[i] = 1
                if numb == 3:
                    aliens.alienY_change[i] = -1
                if numb == 4:
                    aliens.alienY_change[i] = 1

                # enemy fire with enemy behavior, which uses random chance of shot and defined range where to shoot
                InRange = func.Range(player.y, aliens.alienY_list[i])
                numb2 = random.randint(1, 200)
                if InRange and numb2 == 5 and aliens.alienBool_ammo[i] == "old":
                    aliens.alienBool_ammo[i] = "new"
                    aliens.alienY_ammo[i] = aliens.alienY_list[i]
                    aliens.alienX_ammo[i] = aliens.alienX_list[i]
                    # adds new elements at the end of the list
                    for j in range(1):
                        aliens.alien_ammo.append(pygame.image.load("assets/alien_shot.png"))
                        aliens.alienY_ammo.append(800)
                        aliens.alienX_ammo.append(1200)
                        aliens.alienBool_ammo.append("old")

                # tracks enemy shots on screen
                if aliens.alienBool_ammo[i] == "new":
                    func.enemy_fire(aliens.alienX_ammo[i], aliens.alienY_ammo[i], i, aliens.alien_ammo)
                    aliens.alienX_ammo[i] -= aliens.alienX_ammoChange
                # removes enemy shots when on edge of window
                if aliens.alienBool_ammo[i] == "new":
                    if aliens.alienX_ammo[i] <= 0:
                        del aliens.alien_ammo[i]
                        del aliens.alienY_ammo[i]
                        del aliens.alienX_ammo[i]
                        del aliens.alienBool_ammo[i]
                        aliens.max_enemy_ammo -= 1
                # launch and update enemy
                func.enemy(aliens.alienX_list[i], aliens.alienY_list[i], i, aliens.alien_list)

        # adds new enemy elements to enemy lists in 0 coordinates to avoid error by deleting those on collision
        if enemy_numb <= enemy_numb + 2 and len(aliens.alien_list) <= enemy_numb + 2:
            aliens.alien_list.append(pygame.transform.rotate((pygame.image.load("assets/alien.png")), 90))
            aliens.alienX_list.append(1250)
            aliens.alienY_list.append(640)
            aliens.alienHP_list.append(15)
            aliens.alienY_change.append(0)
            aliens.alienX_change.append(0)

        # what happens if enemy HP is 0 ( enemy replaced by exploision)
        for i in range(enemy_numb):
            if aliens.alienHP_list[i] <= 0:
                explode.lastX = aliens.alienX_list[i]
                explode.lastY = aliens.alienY_list[i]
                del aliens.alien_list[i]
                del aliens.alienX_list[i]
                del aliens.alienY_list[i]
                del aliens.alienHP_list[i]
                del aliens.alienY_change[i]
                del aliens.alienX_change[i]
                del aliens.alien_timer[i]
                del aliens.alien_bool[i]
                player.score += 10
                enemy_numb -= 1
                # place explosion debris on screen
                explode.cub_numb += 70
                func.place_cubes(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list, explode.cube_list, explode.cubeX_change,
                                 explode.cubeY_change)

        # BOSS LOOPS
        # boss intro
        if boss.boss_level == False and boss.start_phase == True:
            # static intro movement
            boss.bossY += boss.bossY_change
            boss.bossX += boss.bossX_change
            boss.bossX_change = -0.5
            # collision feedback from boss
            if boss.boss_HP > 0:
                if boss.boss_bool == "No_collision":
                    func.boss(boss.bossX, boss.bossY)
                if boss.boss_bool == "Yes_collision":
                    func.boss2(boss.bossX, boss.bossY)
            if boss.bossX == 600:
                boss.second_phase = True
                boss.start_phase = False
        # battle phase
        if boss.boss_level == False and boss.start_phase == False and boss.second_phase == True:
            # boss movement
            boss.bossY += boss.bossY_change
            boss.bossX += boss.bossX_change
            func.boss(boss.bossX, boss.bossY)
            if boss.bossY >= 520:
                boss.bossY_change = -1
            if boss.bossY <= 0:
                boss.bossY_change = 1
            if boss.bossX >= 1000:
                boss.bossX_change = -1
            if boss.bossX <= 600:
                boss.bossX_change = 1
            # random direction change
            numb = random.randint(1, 450)
            if numb == 1:
                boss.bossX_change = -1
            if numb == 2:
                boss.bossX_change = 1
            if numb == 3:
                boss.bossY_change = -1
            if numb == 4:
                boss.bossY_change = 1

            # boss fire with boss behavior, which uses random chance of shot and defined range where to shoot
            # first weapon type
            InRange_2 = func.Range_2(player.y, boss.bossY)
            numb3 = random.randint(1, 50)
            if InRange_2 and numb3 == 5:

                # top gun
                wpn1.boss_ammo_counter_top += 1
                wpn1.bossY_ammo_numb_top = boss.bossY
                wpn1.bossX_ammo_numb_top = boss.bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    wpn1.boss_ammo_top.append(assets.boss_ammo)
                    wpn1.bossY_ammo_top.append(wpn1.bossY_ammo_numb_top)
                    wpn1.bossX_ammo_top.append(wpn1.bossX_ammo_numb_top)
                    wpn1.boss_bool_top.append("yes")

                # bottom gun
                wpn1.boss_ammo_counter_bottom += 1
                wpn1.bossY_ammo_numb_bottom = boss.bossY
                wpn1.bossX_ammo_numb_bottom = boss.bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    wpn1.boss_ammo_bottom.append(assets.boss_ammo)
                    wpn1.bossY_ammo_bottom.append(wpn1.bossY_ammo_numb_bottom)
                    wpn1.bossX_ammo_bottom.append(wpn1.bossX_ammo_numb_bottom)
                    wpn1.boss_bool_bottom.append("yes")

            #top gun
            # tracks enemy shots on screen
            for i in range(wpn1.boss_ammo_counter_top):
                if wpn1.boss_bool_top[i] =="yes":
                    func.boss_fire(wpn1.bossX_ammo_top[i], wpn1.bossY_ammo_top[i], i, wpn1.boss_ammo_top)
                    wpn1.bossX_ammo_top[i] -= wpn1.bossX_ammoChange
            # removes enemy shots when on edge of window
            for j in range(wpn1.boss_ammo_counter_top - 3):
                if wpn1.boss_bool_top[j] == "yes":
                    if wpn1.bossX_ammo_top[j] <= -100:
                        del wpn1.boss_ammo_top[j]
                        del wpn1.bossY_ammo_top[j]
                        del wpn1.bossX_ammo_top[j]
                        del wpn1.boss_bool_top[j]
                        wpn1.boss_ammo_counter_top -= 1

            # bottom gun
            # tracks enemy shots on screen
            for i in range(wpn1.boss_ammo_counter_bottom):
                if wpn1.boss_bool_bottom[i] == "yes":
                    func.boss_fire_2(wpn1.bossX_ammo_bottom[i], wpn1.bossY_ammo_bottom[i], i, wpn1.boss_ammo_bottom)
                    wpn1.bossX_ammo_bottom[i] -= wpn1.bossX_ammoChange
            # removes enemy shots when on edge of window
            for j in range(wpn1.boss_ammo_counter_bottom - 3):
                if wpn1.boss_bool_bottom[j] == "yes":
                    if wpn1.bossX_ammo_bottom[j] <= -100:
                        del wpn1.boss_ammo_bottom[j]
                        del wpn1.bossY_ammo_bottom[j]
                        del wpn1.bossX_ammo_bottom[j]
                        del wpn1.boss_bool_bottom[j]
                        wpn1.boss_ammo_counter_bottom -= 1

            # second weapon type
            InRange_2 = func.Range_2(player.y, boss.bossY)
            numb4 = random.randint(1, 75)
            if InRange_2 and numb4 == 5:

                # top gun
                wpn2.boss_ammo_counter_2_top += 1
                wpn2.bossY_ammo_numb_2_top = boss.bossY
                wpn2.bossX_ammo_numb_2_top = boss.bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    wpn2.boss_ammo_2_top.append(assets.boss_laser)
                    wpn2.bossY_ammo_2_top.append(wpn2.bossY_ammo_numb_2_top)
                    wpn2.bossX_ammo_2_top.append(wpn2.bossX_ammo_numb_2_top)
                    wpn2.boss_bool_2_top.append("yes")

                # bottom gun
                wpn2.boss_ammo_counter_2_bottom += 1
                wpn2.bossY_ammo_numb_2_bottom = boss.bossY
                wpn2.bossX_ammo_numb_2_bottom = boss.bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    wpn2.boss_ammo_2_bottom.append(assets.boss_laser)
                    wpn2.bossY_ammo_2_bottom.append(wpn2.bossY_ammo_numb_2_bottom)
                    wpn2.bossX_ammo_2_bottom.append(wpn2.bossX_ammo_numb_2_bottom)
                    wpn2.boss_bool_2_bottom.append("yes")

            # top gun
            # tracks enemy shots on screen
            for i in range(wpn2.boss_ammo_counter_2_top):
                if wpn2.boss_bool_2_top[i] == "yes":
                    func.boss_laser(wpn2.bossX_ammo_2_top[i], wpn2.bossY_ammo_2_top[i], i, wpn2.boss_ammo_2_top)
                    wpn2.bossX_ammo_2_top[i] -= wpn2.bossX_ammoChange_2
            # removes enemy shots when on edge of window
            for j in range(wpn2.boss_ammo_counter_2_top - 3):
                if wpn2.boss_bool_2_top[j] == "yes":
                    if wpn2.bossX_ammo_2_top[j] <= -100:
                        del wpn2.boss_ammo_2_top[j]
                        del wpn2.bossY_ammo_2_top[j]
                        del wpn2.bossX_ammo_2_top[j]
                        del wpn2.boss_bool_2_top[j]
                        wpn2.boss_ammo_counter_2_top -= 1

            # bottom gun
            # tracks enemy shots on screen
            for i in range(wpn2.boss_ammo_counter_2_bottom):
                if wpn2.boss_bool_2_bottom[i] == "yes":
                    func.boss_laser_2(wpn2.bossX_ammo_2_bottom[i], wpn2.bossY_ammo_2_bottom[i], i, wpn2.boss_ammo_2_bottom)
                    wpn2.bossX_ammo_2_bottom[i] -= wpn2.bossX_ammoChange_2
            # removes enemy shots when on edge of window
            for j in range(wpn2.boss_ammo_counter_2_bottom - 3):
                if wpn2.boss_bool_2_bottom[j] == "yes":
                    if wpn2.bossX_ammo_2_bottom[j] <= -100:
                        del wpn2.boss_ammo_2_bottom[j]
                        del wpn2.bossY_ammo_2_bottom[j]
                        del wpn2.bossX_ammo_2_bottom[j]
                        del wpn2.boss_bool_2_bottom[j]
                        wpn2.boss_ammo_counter_2_bottom -= 1

            # collision feedback from boss
            if boss.boss_HP > 0:
                if boss.boss_bool == "No_collision":
                    func.boss(boss.bossX, boss.bossY)
                if boss.boss_bool == "Yes_collision":
                     func.boss2(boss.bossX, boss.bossY)

        # COLLISION
        # for what happens if collision happens (player <-- enemy shots)
        for i in range(enemy_numb):
            if player.hp > 0:
                collide2 = func.collision2(player.x, player.y, aliens.alienX_ammo[i], aliens.alienY_ammo[i])
                if collide2:
                    player.hp -= 1
                    player.bool = "Yes_collision"
                    del aliens.alien_ammo[i]
                    del aliens.alienY_ammo[i]
                    del aliens.alienX_ammo[i]
                    del aliens.alienBool_ammo[i]

        # for what happens if collision happens (player <--> enemy)
        for i in range(enemy_numb):
            collide3 = func.collision3(player.x, player.y, aliens.alienX_list[i], aliens.alienY_list[i])
            if collide3:
                player.bool = "Yes_collision"
                aliens.alienHP_list[i] -= 5
                player.hp -= 1
                player.score += 1
                aliens.alien_bool[i] = "Yes_collision"
                aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))

        # for what happens if collision happens (player missile --> enemy)
        for i in range(enemy_numb):
            collide1 = func.collision1(aliens.alienX_list[i], aliens.alienY_list[i], player.missile_x, player.missile_y)
            if collide1:
                aliens.alienHP_list[i] -= 25
                aliens.alien_bool[i] = "Yes_collision"
                aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_x = 380

        # for what happens if collision happens (player <--> HP_drop)
        for i in range(drops.HP_drop_count):
            collide4 = func.collision4(player.x, player.y, drops.drop_numbX[i], drops.drop_numbY[i])
            if collide4:
                del drops.HP_drop_list[i]
                del drops.drop_numbX[i]
                del drops.drop_numbY[i]
                drops.HP_drop_count -= 1
                player.hp += 1

        # for what happens if collision happens (player <--> ammo_drop)
        for i in range(drops.ammo_drop_count):
            collide5 = func.collision5(player.x, player.y, drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i])
            if collide5:
                del drops.ammo_drop_list[i]
                del drops.ammo_drop_numbX[i]
                del drops.ammo_drop_numbY[i]
                drops.ammo_drop_count -= 1
                player.ammo += 400

        # for what happens if collision happens (player shots --> enemy)
        for j in range(player.max_ammo):
            for i in range(enemy_numb):
                collide = func.collision(aliens.alienX_list[i], aliens.alienY_list[i], player.ammoX_list[j], player.ammoY_list[j])
                # what happens at single impact
                if collide:
                    aliens.alienHP_list[i] -= 1
                    player.score += 1
                    aliens.alien_bool[i] = "Yes_collision"
                    aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))
                    player.ammoY_list[j] = 750
                    player.ammoX_list[j] = 1150

        # colisions for players vs boss
        if boss.boss_level == False and boss.start_phase == False and boss.second_phase == True:
            # for what happens if collision happens (player shots --> boss)
            for j in range(player.max_ammo):
                collide6 = func.collision6(boss.bossX, boss.bossY, player.ammoX_list[j],  player.ammoY_list[j])
                # what happens at single impact
                if collide6:
                    boss.boss_HP -= 1
                    player.score += 1
                    boss.boss_bool = "Yes_collision"
                    player.ammoY_list[j] = 750
                    player.ammoX_list[j] = 1150

            # for what happens if collision happens (player missile --> boss)
            collide7 = func.collision7(boss.bossX, boss.bossY, player.missile_x, player.missile_y)
            if collide7:
                boss.boss_HP -= 25
                boss.boss_bool = "Yes_collision"
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_y = 380

            # for what happens if collision happens (player <--> boss)
            collide8 = func.collision8(player.x, player.y, boss.bossX, boss.bossY)
            if collide8:
                player.bool = "Yes_collision"
                boss.boss_HP -= 1
                player.hp -= 1
                player.score += 1
                boss.boss_bool = "Yes_collision"

        # for what happens if collision happens (player <-- boss shots)
        for i in range(wpn1.boss_ammo_counter_top):
            if player.hp > 0:
                collide9 = func.collision9(player.x, player.y, wpn1.bossX_ammo_top[i], wpn1.bossY_ammo_top[i])
                if collide9:
                    player.hp -= 1
                    player.bool = "Yes_collision"
                    wpn1.bossY_ammo_top[i] = 0
                    wpn1.bossX_ammo_top[i] = -100


        # visual feedback from collision for enemy
        for i in range(enemy_numb):
            if aliens.alien_bool[i] == "Yes_collision":
                aliens.alien_timer[i] += 1
                if aliens.alien_timer[i] == 25:
                    aliens.alien_list[i] = pygame.transform.rotate((pygame.image.load("assets/alien.png")), 90)
                    aliens.alien_bool[i] = "No_collision"
                    aliens.alien_timer[i] = 0

        # visual feedback from collision for boss
        if boss.boss_bool == "Yes_collision":
            boss.boss_timer += 1
            if boss.boss_timer == 25:
                boss.boss_bool = "No_collision"
                boss.boss_timer = 0

        # visual feedback from collision for player
        if player.bool == "Yes_collision":
            player.timer += 1
            if player.timer == 25:
                player.bool = "No_collision"
                player.timer = 0

        # LAUNCH ALL AND GAME OVER CONDITION
        # if player HP is less than 0 game is over
        if player.hp <= 0:
            explode.lastX = player.x
            explode.lastY = player.y
            player.hp = 0
            player.end_timer += 1
            if player.end_timer == 1:
                # place explosion debris on screen
                explode.cub_numb += 70
                func.place_cubes(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list, explode.cube_list, explode.cubeX_change, explode.cubeY_change)

            if player.end_timer == 300:
                run = False
                game_over(player.score)

        # collision feedback from player
        if player.hp > 0:
            if player.bool == "No_collision":
                func.player(player.x, player.y)
            if player.bool == "Yes_collision":
                func.player2(player.x, player.y)

        # update all
        timer += 1
        func.healthCounter(player.hp)
        func.ammoCounter(player.ammo)
        func.scoreCounter(player.score)
        func.missileCounter(player.missile_ammo)
        for i in range(drops.HP_drop_count):
            func.HP_drop(drops.drop_numbX[i], drops.drop_numbY[i], i, drops.HP_drop_list)
        for i in range(drops.ammo_drop_count):
            func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)
        pygame.display.update()

        # limit frames to 100fps / 100 loops per second
        clock.tick(100)

# game over screen loop
def game_over(score):
    run = True
    while run == True:
        assets.screen.fill((0, 0, 0))

        # all text on the screen
        gameOver = assets.font2.render("game over", True, (205, 51, 51))
        assets.screen.blit(gameOver, (330, 200))
        text = assets.font3.render("You lost all your HP! Better luck next time!", True, (255, 255, 255))
        assets.screen.blit(text, (355, 300))
        text2 = assets.font3.render("Press ENTER to play again!", True, (255, 255, 255))
        assets.screen.blit(text2, (430, 430))
        text3 = assets.font3.render("Your final score is " + str(score), True, (255, 255, 255))
        assets.screen.blit(text3, (450, 340))

        # game over menu event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # press enter to play again
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                    main()

        # updates display each frame
        pygame.display.update()
        # limit frames to 100fps / 100 loops per second
        clock.tick(100)


# launch start
start()
