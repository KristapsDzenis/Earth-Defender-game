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
    run = True
    selected_index = 0
    timer = 0

    # array of 2 button objects
    button_1 = stats.Button(400, 480, 400, 60, "NEW GAME", level_1_intro)
    button_2 = stats.Button(400, 550, 400, 60, "QUIT", pygame.quit)

    buttons = [button_1, button_2]

    while run == True:
        assets.screen.fill((0, 0, 0))

        # game title
        title = assets.font4.render("Earth", True, (255, 215, 0))
        assets.screen.blit(title, (390, 200))
        title = assets.font4.render("Defender", True, (255, 215, 0))
        assets.screen.blit(title, (260, 320))

        # event handler for start menu
        if timer > 200:

            # selection for first button on screen
            buttons[selected_index].set_selected(True)

            # places buttons on screen
            for button in buttons:
                button.draw(assets.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        buttons[selected_index].set_selected(False)
                        selected_index = 1
                        buttons[selected_index].set_selected(True)
                    if event.key == pygame.K_UP:
                        buttons[selected_index].set_selected(False)
                        selected_index = 0
                        buttons[selected_index].set_selected(True)
                    if event.key == pygame.K_RETURN:
                        timer = 0
                        run = False
                        buttons[selected_index].is_clicked()

        # updates display each frame
        timer += 1
        pygame.display.update()
        # limit frames to 100fps / 100 loops per second
        clock.tick(100)

    pygame.quit()


# level 1 intro screen loop
def level_1_intro():
    timer = 0
    run = True
    while run == True:
        assets.screen.fill((0, 0, 0))
        timer += 1
        # level title
        title = assets.font5.render("Level 1", True, (8, 167, 3))
        assets.screen.blit(title, (200, 320))
        title = assets.font5.render("Earth", True, (8, 167, 3))
        assets.screen.blit(title, (600, 320))

        if timer == 300:
            run = False
            level_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # updates display each frame
        pygame.display.update()
        # limit frames to 100fps / 100 loops per second
        clock.tick(100)

    pygame.quit()

# level 2 intro screen loop
def level_2_intro(player):
    timer = 0
    run = True
    while run == True:
        assets.screen.fill((0, 0, 0))
        timer += 1

        # level title
        title = assets.font5.render("Level 2", True, (8, 36, 235))
        assets.screen.blit(title, (200, 320))
        title = assets.font5.render("Moon", True, (8, 36, 235))
        assets.screen.blit(title, (600, 320))

        if timer == 300:
            run = False
            level_2(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # updates display each frame
        pygame.display.update()
        # limit frames to 100fps / 100 loops per second
        clock.tick(100)

    pygame.quit()

# level 3 intro screen loop
def level_3_intro(player):
    timer = 0
    run = True
    while run == True:
        assets.screen.fill((0, 0, 0))
        timer += 1

        # level title
        title = assets.font5.render("Level 3", True, (205, 51, 51))
        assets.screen.blit(title, (200, 320))
        title = assets.font5.render("Mars", True, (205, 51, 51))
        assets.screen.blit(title, (600, 320))

        if timer == 300:
            run = False
            level_3(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # updates display each frame
        pygame.display.update()
        # limit frames to 100fps / 100 loops per second
        clock.tick(100)

    pygame.quit()

# main loop for level 1
def level_1():
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

    timer = 0
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
            drops.ammo_drop_count += 1
            for i in range(drops.ammo_drop_count):
                drops.ammo_drop_list.append(assets.bullet_drop)
                drops.ammo_drop_numbX.append(random.randint(0, 550))
                drops.ammo_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)
            drops.missile_drop_count += 1
            for i in range(drops.missile_drop_count):
                drops.missile_drop_list.append(assets.missile_drop)
                drops.missile_drop_numbX.append(random.randint(0, 550))
                drops.missile_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)

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

                # press enter to progress to next level if boss defeated
                if event.key == pygame.K_RETURN:
                    if boss.boss_HP <= 0:
                        run = False
                        del drops
                        del aliens
                        del explode
                        del boss
                        del wpn1
                        del wpn2
                        level_2_intro(player)

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
            InRange_2 = func.Range(player.y, boss.bossY)
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
                if wpn1.boss_bool_top[i] == "yes":
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
            if boss.boss_HP < 50:
                InRange_2 = func.Range(player.y, boss.bossY)
                numb4 = random.randint(1, 75)
                if InRange_2 and numb4 == 5:

                    # top gun
                    wpn2.boss_ammo_counter_top += 1
                    wpn2.bossY_ammo_numb_2_top = boss.bossY
                    wpn2.bossX_ammo_numb_2_top = boss.bossX
                    # adds new elements at teh end of the list
                    for i in range(1):
                        wpn2.boss_ammo_top.append(assets.boss_laser)
                        wpn2.bossY_ammo_top.append(wpn2.bossY_ammo_numb_2_top)
                        wpn2.bossX_ammo_top.append(wpn2.bossX_ammo_numb_2_top)
                        wpn2.boss_bool_top.append("yes")

                    # bottom gun
                    wpn2.boss_ammo_counter_bottom += 1
                    wpn2.bossY_ammo_numb_bottom = boss.bossY
                    wpn2.bossX_ammo_numb_bottom = boss.bossX
                    # adds new elements at teh end of the list
                    for i in range(1):
                        wpn2.boss_ammo_bottom.append(assets.boss_laser)
                        wpn2.bossY_ammo_bottom.append(wpn2.bossY_ammo_numb_bottom)
                        wpn2.bossX_ammo_bottom.append(wpn2.bossX_ammo_numb_bottom)
                        wpn2.boss_bool_bottom.append("yes")

                # top gun
                # tracks enemy shots on screen
                for i in range(wpn2.boss_ammo_counter_top):
                    if wpn2.boss_bool_top[i] == "yes":
                        func.boss_laser(wpn2.bossX_ammo_top[i], wpn2.bossY_ammo_top[i], i, wpn2.boss_ammo_top)
                        wpn2.bossX_ammo_top[i] -= wpn2.bossX_ammoChange_2
                # removes enemy shots when on edge of window
                for j in range(wpn2.boss_ammo_counter_top - 3):
                    if wpn2.boss_bool_top[j] == "yes":
                        if wpn2.bossX_ammo_top[j] <= -100:
                            del wpn2.boss_ammo_top[j]
                            del wpn2.bossY_ammo_top[j]
                            del wpn2.bossX_ammo_top[j]
                            del wpn2.boss_bool_top[j]
                            wpn2.boss_ammo_counter_top -= 1

                # bottom gun
                # tracks enemy shots on screen
                for i in range(wpn2.boss_ammo_counter_bottom):
                    if wpn2.boss_bool_bottom[i] == "yes":
                        func.boss_laser_2(wpn2.bossX_ammo_bottom[i], wpn2.bossY_ammo_bottom[i], i, wpn2.boss_ammo_bottom)
                        wpn2.bossX_ammo_bottom[i] -= wpn2.bossX_ammoChange_2
                # removes enemy shots when on edge of window
                for j in range(wpn2.boss_ammo_counter_bottom - 3):
                    if wpn2.boss_bool_bottom[j] == "yes":
                        if wpn2.bossX_ammo_bottom[j] <= -100:
                            del wpn2.boss_ammo_bottom[j]
                            del wpn2.bossY_ammo_bottom[j]
                            del wpn2.bossX_ammo_bottom[j]
                            del wpn2.boss_bool_bottom[j]
                            wpn2.boss_ammo_counter_bottom -= 1

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
                collide2 = func.collision(player.x, player.y, aliens.alienX_ammo[i], aliens.alienY_ammo[i])
                if collide2:
                    player.hp -= 1
                    player.bool = "Yes_collision"
                    del aliens.alien_ammo[i]
                    del aliens.alienY_ammo[i]
                    del aliens.alienX_ammo[i]
                    del aliens.alienBool_ammo[i]

        # for what happens if collision happens (player <--> enemy)
        for i in range(enemy_numb):
            collide3 = func.collision(player.x, player.y, aliens.alienX_list[i], aliens.alienY_list[i])
            if collide3:
                player.bool = "Yes_collision"
                aliens.alienHP_list[i] -= 5
                player.hp -= 1
                player.score += 1
                aliens.alien_bool[i] = "Yes_collision"
                aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))

        # for what happens if collision happens (player missile --> enemy)
        for i in range(enemy_numb):
            collide1 = func.collision(aliens.alienX_list[i], aliens.alienY_list[i], player.missile_x, player.missile_y)
            if collide1:
                aliens.alienHP_list[i] -= 25
                aliens.alien_bool[i] = "Yes_collision"
                aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_x = 380

        # for what happens if collision happens (player <--> HP_drop)
        for i in range(drops.HP_drop_count):
            collide4 = func.collision(player.x, player.y, drops.drop_numbX[i], drops.drop_numbY[i])
            if collide4:
                drops.drop_numbX[i] = -100
                drops.drop_numbY[i] = 0
                player.hp += 1

        # for what happens if collision happens (player <--> ammo_drop)
        for i in range(drops.ammo_drop_count):
            collide5 = func.collision(player.x, player.y, drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i])
            if collide5:
                drops.ammo_drop_numbX[i] = -100
                drops.ammo_drop_numbY[i] = 0
                player.ammo += 400

        # for what happens if collision happens (player <--> missile_drop)
        for i in range(drops.missile_drop_count):
            collide13 = func.collision(player.x, player.y, drops.missile_drop_numbX[i], drops.missile_drop_numbY[i])
            if collide13:
                drops.missile_drop_numbX[i] = -100
                drops.missile_drop_numbY[i] = 0
                player.missile_ammo += 1

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
                collide6 = func.collision2(boss.bossX, boss.bossY, player.ammoX_list[j],  player.ammoY_list[j])
                # what happens at single impact
                if collide6:
                    boss.boss_HP -= 1
                    player.score += 1
                    boss.boss_bool = "Yes_collision"
                    player.ammoY_list[j] = 750
                    player.ammoX_list[j] = 1150

            # for what happens if collision happens (player missile --> boss)
            collide7 = func.collision2(boss.bossX, boss.bossY, player.missile_x, player.missile_y)
            if collide7:
                boss.boss_HP -= 25
                boss.boss_bool = "Yes_collision"
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_y = 380

            # for what happens if collision happens (player <--> boss)
            collide8 = func.collision2(player.x, player.y, boss.bossX, boss.bossY)
            if collide8:
                player.bool = "Yes_collision"
                boss.boss_HP -= 1
                player.hp -= 1
                player.score += 1
                boss.boss_bool = "Yes_collision"

        # for what happens if collision happens (player <-- boss shots(first weapon stype))
        if boss.boss_HP > 0:
            for i in range(wpn1.boss_ammo_counter_top):
                if player.hp > 0:
                    collide9 = func.collision3(player.x, player.y, wpn1.bossX_ammo_top[i], wpn1.bossY_ammo_top[i])
                    if collide9:
                        player.hp -= 1
                        player.bool = "Yes_collision"
                        wpn1.bossY_ammo_top[i] = 0
                        wpn1.bossX_ammo_top[i] = -100

            for i in range(wpn1.boss_ammo_counter_bottom):
                if player.hp > 0:
                    collide10 = func.collision4(player.x, player.y, wpn1.bossX_ammo_bottom[i], wpn1.bossY_ammo_bottom[i])
                    if collide10:
                        player.hp -= 1
                        player.bool = "Yes_collision"
                        wpn1.bossY_ammo_bottom[i] = 0
                        wpn1.bossX_ammo_bottom[i] = -100

            # for what happens if collision happens (player <-- boss shots(second weapon stype))
            for i in range(wpn2.boss_ammo_counter_top):
                if player.hp > 0:
                    collide11 = func.collision5(player.x, player.y, wpn2.bossX_ammo_top[i], wpn2.bossY_ammo_top[i])
                    if collide11:
                        player.hp -= 2
                        player.bool = "Yes_collision"
                        wpn2.bossY_ammo_top[i] = 0
                        wpn2.bossX_ammo_top[i] = -100

            for i in range(wpn2.boss_ammo_counter_bottom):
                if player.hp > 0:
                    collide12 = func.collision6(player.x, player.y, wpn2.bossX_ammo_bottom[i], wpn2.bossY_ammo_bottom[i])
                    if collide12:
                        player.hp -= 2
                        player.bool = "Yes_collision"
                        wpn2.bossY_ammo_bottom[i] = 0
                        wpn2.bossX_ammo_bottom[i] = -100

        # visual feedback from collision for enemy
        for i in range(enemy_numb):
            if aliens.alien_bool[i] == "Yes_collision":
                aliens.alien_timer[i] += 1
                if aliens.alien_timer[i] == 25:
                    aliens.alien_list[i] = pygame.transform.rotate((pygame.image.load("assets/alien.png")), 90)
                    aliens.alien_bool[i] = "No_collision"
                    aliens.alien_timer[i] = 0

        # visual feedback from collision for player
        if player.bool == "Yes_collision":
            player.timer += 1
            if player.timer == 25:
                player.bool = "No_collision"
                player.timer = 0

        # visual feedback from collision for boss
        if boss.boss_bool == "Yes_collision":
            boss.boss_timer += 1
            if boss.boss_timer == 25:
                boss.boss_bool = "No_collision"
                boss.boss_timer = 0

        # WINNING CONDITIONS
        if boss.boss_HP <= 0:
            explode.lastX = boss.bossX
            explode.lastY = boss.bossY
            boss.boss_HP = 0
            boss.end_timer += 1

            if boss.end_timer == 1:
                boss.boss_level = False
                boss.start_phase = False
                boss.second_phase = False
                player.score += 100
                explode.cub_numb += 500
                func.place_cubes_boss(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list, explode.cube_list,
                                 explode.cubeX_change, explode.cubeY_change)

                drops.HP_drop_count += 3
                for i in range(drops.HP_drop_count):
                    drops.HP_drop_list.append(assets.HP_drop_i)
                    drops.drop_numbX.append(random.randint(200, 1000))
                    drops.drop_numbY.append(random.randint(0, 640))
                    func.HP_drop(drops.drop_numbX[i], drops.drop_numbY[i], i, drops.HP_drop_list)
                drops.ammo_drop_count += 2
                for i in range(drops.ammo_drop_count):
                    drops.ammo_drop_list.append(assets.bullet_drop)
                    drops.ammo_drop_numbX.append(random.randint(200, 1000))
                    drops.ammo_drop_numbY.append(random.randint(0, 640))
                    func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)
                drops.missile_drop_count += 2
                for i in range(drops.missile_drop_count):
                    drops.missile_drop_list.append(assets.missile_drop)
                    drops.missile_drop_numbX.append(random.randint(200, 1000))
                    drops.missile_drop_numbY.append(random.randint(0, 640))
                    func.ammo_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)

            text = assets.font6.render("Press enter to progress to next level", True, (205, 51, 51))
            assets.screen.blit(text, (200, 640))

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
                func.place_cubes(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list, explode.cube_list,
                                 explode.cubeX_change, explode.cubeY_change)
            if player.end_timer == 300:
                run = False
                game_over(player.score)

        # collision feedback from player
        if player.hp > 0:
            if player.bool == "No_collision":
                func.player(player.x, player.y)
            if player.bool == "Yes_collision":
                func.player2(player.x, player.y)

        # print text on screen
        if 0 <= timer <= 60 or 121 <= timer <= 180 or 241 <= timer <= 300 or 361 <= timer <= 420:
            text = assets.font6.render("Wave 1 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 61 <= timer <= 120 or 181 <= timer <= 240 or 301 <= timer <= 360 or 421 <= timer <= 480:
            text = assets.font6.render("Wave 1 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if 2800 <= timer <= 2860 or 2921 <= timer <= 2980 or 3041 <= timer <= 3100 or 3161 <= timer <= 3220:
            text = assets.font6.render("Wave 2 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 2861 <= timer <= 2920 or 2981 <= timer <= 3040 or 3101 <= timer <= 3160 or 3221 <= timer <= 3280:
            text = assets.font6.render("Wave 2 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if 6800 <= timer <= 6860 or 6921 <= timer <= 6980 or 7041 <= timer <= 7100 or 7161 <= timer <= 7220:
            text = assets.font6.render("Wave 3 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 6861 <= timer <= 6920 or 6981 <= timer <= 7040 or 7101 <= timer <= 7160 or 7221 <= timer <= 7280:
            text = assets.font6.render("Wave 3 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if (10800 <= timer <= 10860 or 10921 <= timer <= 10980 or 11041 <= timer <= 11100 or 11161 <= timer <= 11220
            or 11281 <= timer <= 11340 or 11401 <= timer <= 11460 or 11521 <= timer <= 11580):
            text = assets.font6.render("!!! Boss Incoming !!!", True, (205, 51, 51))
            assets.screen.blit(text, (420, 640))
            assets.screen.blit(text, (420, 10))
        if (10861 <= timer <= 10920 or 10981 <= timer <= 11040 or 11101 <= timer <= 11160 or 11221 <= timer <= 11280
            or 11341 <= timer <= 11400 or 11461 <= timer <= 11520 or 11581 <= timer <= 11640):
            text = assets.font6.render("!!! Boss Incoming !!!", True, (219, 209, 4))
            assets.screen.blit(text, (420, 10))
            assets.screen.blit(text, (420, 640))

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
        for i in range(drops.missile_drop_count):
            func.missile_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)
        pygame.display.update()

        # limit frames to 100fps / 100 loops per second
        clock.tick(100)


# main loop for level 2
def level_2(player):
    # initialise all objects
    drops = stats.Drops()
    aliens = stats.Aliens()
    aliens2 = stats.Aliens_2()
    explode = stats.Explosions()
    boss2 = stats.level2_Boss()
    wpn1 = stats.level1_Boss_Wpn1()
    wpn2 = stats.level1_Boss_Wpn2()
    player.x = 0
    player.y = 380

    # enemy counter start stats
    enemy_numb = 0
    enemy_count = 0
    enemy_numb_2 = 0
    enemy_count_2 = 0
    enemy_wave = False

    timer = 0
    run = True
    while run == True:
        # background ,UI elements
        assets.screen.fill((0, 0, 0))
        assets.screen.blit(assets.background_2, (0, 0))
        assets.screen.blit(assets.UI, (-5, 678))

        # first enemy wave spawn
        if timer == 200:
            enemy_numb = 15
            enemy_count = 15
            enemy_wave = True

        # second enemy wave spawn
        if timer == 3000:
            enemy_numb += 13
            enemy_count = 13
            enemy_numb_2 += 2
            enemy_count_2 = 2
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
            enemy_numb_2 += 4
            enemy_count_2 = 4
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
            boss2.boss_level = True
            drops.ammo_drop_count += 1
            for i in range(drops.ammo_drop_count):
                drops.ammo_drop_list.append(assets.bullet_drop)
                drops.ammo_drop_numbX.append(random.randint(0, 550))
                drops.ammo_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)
            drops.missile_drop_count += 1
            for i in range(drops.missile_drop_count):
                drops.missile_drop_list.append(assets.missile_drop)
                drops.missile_drop_numbX.append(random.randint(0, 550))
                drops.missile_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)

        # supply drop during boss battle
        if boss2.boss2_HP == 200 and boss2.boss_phase_ammo_drop == True:
            boss2.boss_phase_ammo_drop = False
            drops.HP_drop_count += 1
            for i in range(drops.HP_drop_count):
                drops.HP_drop_list.append(assets.HP_drop_i)
                drops.drop_numbX.append(random.randint(0, 550))
                drops.drop_numbY.append(random.randint(0, 640))
                func.HP_drop(drops.drop_numbX[i], drops.drop_numbY[i], i, drops.HP_drop_list)
            drops.ammo_drop_count += 1
            for i in range(drops.ammo_drop_count):
                drops.ammo_drop_list.append(assets.bullet_drop)
                drops.ammo_drop_numbX.append(random.randint(0, 550))
                drops.ammo_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)
            drops.missile_drop_count += 1
            for i in range(drops.missile_drop_count):
                drops.missile_drop_list.append(assets.missile_drop)
                drops.missile_drop_numbX.append(random.randint(0, 550))
                drops.missile_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)

        # place enemies on screen
        if enemy_wave == True:
            # for type 1 enemies
            if enemy_numb > 0:
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
            # for type 2 enemies
            if enemy_numb_2 > 0:
                func.create_enemy_2(enemy_count_2, aliens2.alien_list, aliens2.alienX_list, aliens2.alienY_list, aliens2.alienHP_list,
                                  aliens2.alienY_change, aliens2.alienX_change,aliens2.alien_bool, aliens2.alien_timer, aliens2.alien_ammo,
                                  aliens2.alienBool_ammo, aliens2.alienY_ammo, aliens2.alienX_ammo)
                for i in range(enemy_numb_2):
                    if aliens2.alienY_list[i] >= 640:
                        aliens2.alienY_change[i] = -1
                    if aliens2.alienY_list[i] <= 0:
                        aliens2.alienY_change[i] = 1
                    aliens2.alienX_list[i] -= 2
                    func.enemy(aliens2.alienX_list[i], aliens2.alienY_list[i], i, aliens2.alien_list)
                    if int(i) <= 700:
                        enemy_wave = False

        # place boss on screen
        if boss2.boss_level == True:
            boss2.bossX = 1200
            boss2.bossY = 250
            boss2.bossX_change = 0
            boss2.bossY_change = 0
            # collision feedback from boss
            if boss2.boss2_HP > 0:
                if boss2.boss_bool == "No_collision":
                    func.boss_second(boss2.bossX, boss2.bossY)
                if boss2.boss_bool == "Yes_collision":
                    func.boss2_second(boss2.bossX, boss2.bossY)
            boss2.boss_level = False
            boss2.start_phase = True

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

                # press enter to progress to next level if boss defeated
                if event.key == pygame.K_RETURN:
                    if boss2.boss2_HP <= 0:
                        run = False
                        del drops
                        del aliens
                        del explode
                        del boss2
                        del wpn1
                        del wpn2
                        level_3(player)

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

        # ENEMY LOOP TYPE 1
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

        # ENEMY LOOP TYPE 2
        if enemy_wave == False:
            for i in range(enemy_numb_2):
                # enemy movement
                aliens2.alienY_list[i] += aliens2.alienY_change[i]
                aliens2.alienX_list[i] += aliens2.alienX_change[i]
                # enemy zone of control/collision
                if aliens2.alienY_list[i] >= 640:
                    aliens2.alienY_change[i] = -1
                if aliens2.alienY_list[i] <= 0:
                    aliens2.alienY_change[i] = 1
                if aliens2.alienX_list[i] >= 1180:
                    aliens2.alienX_change[i] = -1
                if aliens2.alienX_list[i] <= 450:
                    aliens2.alienX_change[i] = 1
                # random direction change
                numb = random.randint(1, 500)
                if numb == 1:
                    aliens2.alienX_change[i] = -1
                if numb == 2:
                    aliens2.alienX_change[i] = 1
                if numb == 3:
                    aliens2.alienY_change[i] = -1
                if numb == 4:
                    aliens2.alienY_change[i] = 1

                # enemy fire with enemy behavior, which uses random chance of shot and defined range where to shoot
                InRange = func.Range(player.y, aliens2.alienY_list[i])
                numb2 = random.randint(1, 100)
                if InRange and numb2 == 5 and aliens2.alienBool_ammo[i] == "old":
                    aliens2.alienBool_ammo[i] = "new"
                    aliens2.alienY_ammo[i] = aliens2.alienY_list[i]
                    aliens2.alienX_ammo[i] = aliens2.alienX_list[i]
                    # adds new elements at the end of the list
                    for j in range(1):
                        aliens2.alien_ammo.append(pygame.image.load("assets/laser.jpg"))
                        aliens2.alienY_ammo.append(800)
                        aliens2.alienX_ammo.append(1200)
                        aliens2.alienBool_ammo.append("old")

                # tracks enemy shots on screen
                if aliens2.alienBool_ammo[i] == "new":
                    func.enemy_fire(aliens2.alienX_ammo[i], aliens2.alienY_ammo[i], i, aliens2.alien_ammo)
                    aliens2.alienX_ammo[i] -= aliens2.alienX_ammoChange_2
                # removes enemy shots when on edge of window
                if aliens2.alienBool_ammo[i] == "new":
                    if aliens2.alienX_ammo[i] <= 0:
                        del aliens2.alien_ammo[i]
                        del aliens2.alienY_ammo[i]
                        del aliens2.alienX_ammo[i]
                        del aliens2.alienBool_ammo[i]
                        aliens2.max_enemy_ammo -= 1
                # launch and update enemy
                func.enemy(aliens2.alienX_list[i], aliens2.alienY_list[i], i, aliens2.alien_list)

        # adds new enemy elements to enemy lists in 0 coordinates to avoid error by deleting those on collision
        if enemy_numb_2 <= enemy_numb_2 + 2 and len(aliens2.alien_list) <= enemy_numb_2 + 2:
            aliens2.alien_list.append(pygame.transform.rotate((pygame.image.load("assets/alien_second.png")), 90))
            aliens2.alienX_list.append(1250)
            aliens2.alienY_list.append(640)
            aliens2.alienHP_list.append(15)
            aliens2.alienY_change.append(0)
            aliens2.alienX_change.append(0)

        # what happens if enemy HP is 0 ( enemy replaced by exploision)
        for i in range(enemy_numb_2):
            if aliens2.alienHP_list[i] <= 0:
                explode.lastX = aliens2.alienX_list[i]
                explode.lastY = aliens2.alienY_list[i]
                del aliens2.alien_list[i]
                del aliens2.alienX_list[i]
                del aliens2.alienY_list[i]
                del aliens2.alienHP_list[i]
                del aliens2.alienY_change[i]
                del aliens2.alienX_change[i]
                del aliens2.alien_timer[i]
                del aliens2.alien_bool[i]
                player.score += 10
                enemy_numb_2 -= 1
                # place explosion debris on screen
                explode.cub_numb += 70
                func.place_cubes(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list,
                                 explode.cube_list, explode.cubeX_change,
                                 explode.cubeY_change)

        # BOSS LOOPS
        # boss intro
        if boss2.boss_level == False and boss2.start_phase == True:
            # static intro movement
            boss2.bossY += boss2.bossY_change
            boss2.bossX += boss2.bossX_change
            boss2.bossX_change = -0.5
            # collision feedback from boss
            if boss2.boss2_HP > 0:
                if boss2.boss_bool == "No_collision":
                    func.boss_second(boss2.bossX, boss2.bossY)
                if boss2.boss_bool == "Yes_collision":
                    func.boss2_second(boss2.bossX, boss2.bossY)
            if boss2.bossX == 600:
                boss2.second_phase = True
                boss2.start_phase = False
        # battle phase
        if boss2.boss_level == False and boss2.start_phase == False and boss2.second_phase == True:
            # boss movement
            boss2.bossY += boss2.bossY_change
            boss2.bossX += boss2.bossX_change
            func.boss_second(boss2.bossX, boss2.bossY)
            if boss2.bossY >= 520:
                boss2.bossY_change = -1
            if boss2.bossY <= 0:
                boss2.bossY_change = 1
            if boss2.bossX >= 1000:
                boss2.bossX_change = -1
            if boss2.bossX <= 600:
                boss2.bossX_change = 1
            # random direction change
            numb = random.randint(1, 450)
            if numb == 1:
                boss2.bossX_change = -1
            if numb == 2:
                boss2.bossX_change = 1
            if numb == 3:
                boss2.bossY_change = -1
            if numb == 4:
                boss2.bossY_change = 1

            # boss fire with boss behavior, which uses random chance of shot and defined range where to shoot
            # first weapon type
            InRange_2 = func.Range(player.y, boss2.bossY)
            numb3 = random.randint(1, 50)
            if InRange_2 and numb3 == 5:
                # top gun
                wpn1.boss_ammo_counter_top += 1
                wpn1.bossY_ammo_numb_top = boss2.bossY
                wpn1.bossX_ammo_numb_top = boss2.bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    wpn1.boss_ammo_top.append(assets.boss_ammo)
                    wpn1.bossY_ammo_top.append(wpn1.bossY_ammo_numb_top)
                    wpn1.bossX_ammo_top.append(wpn1.bossX_ammo_numb_top)
                    wpn1.boss_bool_top.append("yes")

                # bottom gun
                wpn1.boss_ammo_counter_bottom += 1
                wpn1.bossY_ammo_numb_bottom = boss2.bossY
                wpn1.bossX_ammo_numb_bottom = boss2.bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    wpn1.boss_ammo_bottom.append(assets.boss_ammo)
                    wpn1.bossY_ammo_bottom.append(wpn1.bossY_ammo_numb_bottom)
                    wpn1.bossX_ammo_bottom.append(wpn1.bossX_ammo_numb_bottom)
                    wpn1.boss_bool_bottom.append("yes")

            #top gun
            # tracks enemy shots on screen
            for i in range(wpn1.boss_ammo_counter_top):
                if wpn1.boss_bool_top[i] == "yes":
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
            if boss2.boss2_HP < 200:
                InRange_2 = func.Range(player.y, boss2.bossY)
                numb4 = random.randint(1, 75)
                if InRange_2 and numb4 == 5:

                    # top gun
                    wpn2.boss_ammo_counter_top += 1
                    wpn2.bossY_ammo_numb_2_top = boss2.bossY
                    wpn2.bossX_ammo_numb_2_top = boss2.bossX
                    # adds new elements at teh end of the list
                    for i in range(1):
                        wpn2.boss_ammo_top.append(assets.boss_laser)
                        wpn2.bossY_ammo_top.append(wpn2.bossY_ammo_numb_2_top)
                        wpn2.bossX_ammo_top.append(wpn2.bossX_ammo_numb_2_top)
                        wpn2.boss_bool_top.append("yes")

                    # bottom gun
                    wpn2.boss_ammo_counter_bottom += 1
                    wpn2.bossY_ammo_numb_bottom = boss2.bossY
                    wpn2.bossX_ammo_numb_bottom = boss2.bossX
                    # adds new elements at teh end of the list
                    for i in range(1):
                        wpn2.boss_ammo_bottom.append(assets.boss_laser)
                        wpn2.bossY_ammo_bottom.append(wpn2.bossY_ammo_numb_bottom)
                        wpn2.bossX_ammo_bottom.append(wpn2.bossX_ammo_numb_bottom)
                        wpn2.boss_bool_bottom.append("yes")

                # top gun
                # tracks enemy shots on screen
                for i in range(wpn2.boss_ammo_counter_top):
                    if wpn2.boss_bool_top[i] == "yes":
                        func.boss_laser(wpn2.bossX_ammo_top[i], wpn2.bossY_ammo_top[i], i, wpn2.boss_ammo_top)
                        wpn2.bossX_ammo_top[i] -= wpn2.bossX_ammoChange_2
                # removes enemy shots when on edge of window
                for j in range(wpn2.boss_ammo_counter_top - 3):
                    if wpn2.boss_bool_top[j] == "yes":
                        if wpn2.bossX_ammo_top[j] <= -100:
                            del wpn2.boss_ammo_top[j]
                            del wpn2.bossY_ammo_top[j]
                            del wpn2.bossX_ammo_top[j]
                            del wpn2.boss_bool_top[j]
                            wpn2.boss_ammo_counter_top -= 1

                # bottom gun
                # tracks enemy shots on screen
                for i in range(wpn2.boss_ammo_counter_bottom):
                    if wpn2.boss_bool_bottom[i] == "yes":
                        func.boss_laser_2(wpn2.bossX_ammo_bottom[i], wpn2.bossY_ammo_bottom[i], i, wpn2.boss_ammo_bottom)
                        wpn2.bossX_ammo_bottom[i] -= wpn2.bossX_ammoChange_2
                # removes enemy shots when on edge of window
                for j in range(wpn2.boss_ammo_counter_bottom - 3):
                    if wpn2.boss_bool_bottom[j] == "yes":
                        if wpn2.bossX_ammo_bottom[j] <= -100:
                            del wpn2.boss_ammo_bottom[j]
                            del wpn2.bossY_ammo_bottom[j]
                            del wpn2.bossX_ammo_bottom[j]
                            del wpn2.boss_bool_bottom[j]
                            wpn2.boss_ammo_counter_bottom -= 1

            # death laser weapon type
            if boss2.boss2_HP < 100:
                InRange_3 = func.Range(player.y, boss2.bossY)
                numb4 = random.randint(1, 800)
                # places targeting laser on screen
                if InRange_3 and numb4 == 5 and boss2.tg_laser_active == False and boss2.death_laser_active == False:
                    func.boss_target_sys(boss2.bossX, boss2.bossY)
                    boss2.tg_laser_active = True

                # RELEASE DEATH LASER
                if boss2.tging_timer == 300:
                    boss2.tg_laser_active = False
                    boss2.tging_timer = 0
                    func.boss_death_laser(boss2.bossX, boss2.bossY)
                    boss2.death_laser_active = True

                # turn off death laser
                if boss2.death_laser_timer == 300:
                    boss2.death_laser_active = False
                    boss2.death_laser_timer = 0

            # tracks targeting laser on screen
            if boss2.tg_laser_active == True:
                func.boss_target_sys(boss2.bossX, boss2.bossY)
                boss2.tging_timer += 1 # targeting timer

            # tracks death laser on screeen
            if boss2.death_laser_active == True:
                func.boss_death_laser(boss2.bossX, boss2.bossY)
                boss2.death_laser_timer += 1

            # collision feedback from boss
            if boss2.boss2_HP > 0:
                if boss2.boss_bool == "No_collision":
                    func.boss_second(boss2.bossX, boss2.bossY)
                if boss2.boss_bool == "Yes_collision":
                     func.boss2_second(boss2.bossX, boss2.bossY)

        # COLLISION
        # for what happens if collision happens (player <-- enemy shots(type 1))
        for i in range(enemy_numb):
            if player.hp > 0:
                collide2 = func.collision(player.x, player.y, aliens.alienX_ammo[i], aliens.alienY_ammo[i])
                if collide2:
                    player.hp -= 1
                    player.bool = "Yes_collision"
                    del aliens.alien_ammo[i]
                    del aliens.alienY_ammo[i]
                    del aliens.alienX_ammo[i]
                    del aliens.alienBool_ammo[i]

        # for what happens if collision happens (player <-- enemy shots(type 2))
        for i in range(enemy_numb_2):
            if player.hp > 0:
                collide14 = func.collision(player.x, player.y, aliens2.alienX_ammo[i], aliens2.alienY_ammo[i])
                if collide14:
                    player.hp -= 2
                    player.bool = "Yes_collision"
                    del aliens2.alien_ammo[i]
                    del aliens2.alienY_ammo[i]
                    del aliens2.alienX_ammo[i]
                    del aliens2.alienBool_ammo[i]

        # for what happens if collision happens (player <--> enemy(type 1))
        for i in range(enemy_numb):
            collide3 = func.collision(player.x, player.y, aliens.alienX_list[i], aliens.alienY_list[i])
            if collide3:
                player.bool = "Yes_collision"
                aliens.alienHP_list[i] -= 5
                player.hp -= 1
                player.score += 1
                aliens.alien_bool[i] = "Yes_collision"
                aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))

        # for what happens if collision happens (player <--> enemy(type 2))
        for i in range(enemy_numb_2):
            collide15 = func.collision(player.x, player.y, aliens2.alienX_list[i], aliens2.alienY_list[i])
            if collide15:
                player.bool = "Yes_collision"
                aliens2.alienHP_list[i] -= 5
                player.hp -= 1
                player.score += 1
                aliens2.alien_bool[i] = "Yes_collision"
                aliens2.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien_second2.png")), 90))

        # for what happens if collision happens (player missile --> enemy(type 1))
        for i in range(enemy_numb):
            collide1 = func.collision(aliens.alienX_list[i], aliens.alienY_list[i], player.missile_x, player.missile_y)
            if collide1:
                aliens.alienHP_list[i] -= 25
                aliens.alien_bool[i] = "Yes_collision"
                aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_x = 380

        # for what happens if collision happens (player missile --> enemy(type 2))
        for i in range(enemy_numb_2):
            collide16 = func.collision(aliens2.alienX_list[i], aliens2.alienY_list[i], player.missile_x,
                                      player.missile_y)
            if collide16:
                aliens2.alienHP_list[i] -= 25
                aliens2.alien_bool[i] = "Yes_collision"
                aliens2.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien_second2.png")), 90))
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_x = 380

        # for what happens if collision happens (player <--> HP_drop)
        for i in range(drops.HP_drop_count):
            collide4 = func.collision(player.x, player.y, drops.drop_numbX[i], drops.drop_numbY[i])
            if collide4:
                drops.drop_numbX[i] = -100
                drops.drop_numbY[i] = 0
                player.hp += 1

        # for what happens if collision happens (player <--> ammo_drop)
        for i in range(drops.ammo_drop_count):
            collide5 = func.collision(player.x, player.y, drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i])
            if collide5:
                drops.ammo_drop_numbX[i] = -100
                drops.ammo_drop_numbY[i] = 0
                player.ammo += 400

        # for what happens if collision happens (player <--> missile_drop)
        for i in range(drops.missile_drop_count):
            collide13 = func.collision(player.x, player.y, drops.missile_drop_numbX[i], drops.missile_drop_numbY[i])
            if collide13:
                drops.missile_drop_numbX[i] = -100
                drops.missile_drop_numbY[i] = 0
                player.missile_ammo += 1

        # for what happens if collision happens (player shots --> enemy(type 1 and type 2))
        for j in range(player.max_ammo):
            # for enemy type 1
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
            # for enemy type 2
            for i in range(enemy_numb_2):
                collide17 = func.collision(aliens2.alienX_list[i], aliens2.alienY_list[i], player.ammoX_list[j], player.ammoY_list[j])
                # what happens at single impact
                if collide17:
                    aliens2.alienHP_list[i] -= 1
                    player.score += 1
                    aliens2.alien_bool[i] = "Yes_collision"
                    aliens2.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien_second2.png")), 90))
                    player.ammoY_list[j] = 750
                    player.ammoX_list[j] = 1150

        # colisions for players vs boss
        if boss2.boss_level == False and boss2.start_phase == False and boss2.second_phase == True:
            # for what happens if collision happens (player shots --> boss)
            for j in range(player.max_ammo):
                collide6 = func.collision2(boss2.bossX, boss2.bossY, player.ammoX_list[j],  player.ammoY_list[j])
                # what happens at single impact
                if collide6:
                    boss2.boss2_HP -= 1
                    player.score += 1
                    boss2.boss_bool = "Yes_collision"
                    player.ammoY_list[j] = 750
                    player.ammoX_list[j] = 1150

            # for what happens if collision happens (player missile --> boss)
            collide7 = func.collision2(boss2.bossX, boss2.bossY, player.missile_x, player.missile_y)
            if collide7:
                boss2.boss2_HP -= 25
                boss2.boss_bool = "Yes_collision"
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_y = 380

            # for what happens if collision happens (player <--> boss)
            collide8 = func.collision2(player.x, player.y, boss2.bossX, boss2.bossY)
            if collide8:
                player.bool = "Yes_collision"
                boss2.boss2_HP -= 1
                player.hp -= 1
                player.score += 1
                boss2.boss_bool = "Yes_collision"

        # for what happens if collision happens (player <-- boss shots(first weapon stype))
        if boss2.boss2_HP > 0:
            for i in range(wpn1.boss_ammo_counter_top):
                if player.hp > 0:
                    collide9 = func.collision3(player.x, player.y, wpn1.bossX_ammo_top[i], wpn1.bossY_ammo_top[i])
                    if collide9:
                        player.hp -= 1
                        player.bool = "Yes_collision"
                        wpn1.bossY_ammo_top[i] = 0
                        wpn1.bossX_ammo_top[i] = -100

            for i in range(wpn1.boss_ammo_counter_bottom):
                if player.hp > 0:
                    collide10 = func.collision4(player.x, player.y, wpn1.bossX_ammo_bottom[i], wpn1.bossY_ammo_bottom[i])
                    if collide10:
                        player.hp -= 1
                        player.bool = "Yes_collision"
                        wpn1.bossY_ammo_bottom[i] = 0
                        wpn1.bossX_ammo_bottom[i] = -100

            # for what happens if collision happens (player <-- boss shots(second weapon stype))
            for i in range(wpn2.boss_ammo_counter_top):
                if player.hp > 0:
                    collide11 = func.collision5(player.x, player.y, wpn2.bossX_ammo_top[i], wpn2.bossY_ammo_top[i])
                    if collide11:
                        player.hp -= 2
                        player.bool = "Yes_collision"
                        wpn2.bossY_ammo_top[i] = 0
                        wpn2.bossX_ammo_top[i] = -100

            for i in range(wpn2.boss_ammo_counter_bottom):
                if player.hp > 0:
                    collide12 = func.collision6(player.x, player.y, wpn2.bossX_ammo_bottom[i], wpn2.bossY_ammo_bottom[i])
                    if collide12:
                        player.hp -= 2
                        player.bool = "Yes_collision"
                        wpn2.bossY_ammo_bottom[i] = 0
                        wpn2.bossX_ammo_bottom[i] = -100

        # for what happens if collision happens ( player <-- boss death laser )
        if boss2.death_laser_active == True:
            if player.hp > 0:
                collide18 = func.collision7(player.y, boss2.bossY)
                if collide18:
                    player.hp -= 1
                    player.bool = "Yes_collision"

        # visual feedback from collision for enemy (type 1)
        for i in range(enemy_numb):
            if aliens.alien_bool[i] == "Yes_collision":
                aliens.alien_timer[i] += 1
                if aliens.alien_timer[i] == 25:
                    aliens.alien_list[i] = pygame.transform.rotate((pygame.image.load("assets/alien.png")), 90)
                    aliens.alien_bool[i] = "No_collision"
                    aliens.alien_timer[i] = 0

        # visual feedback from collision for enemy (type 2)
        for i in range(enemy_numb_2):
            if aliens2.alien_bool[i] == "Yes_collision":
                aliens2.alien_timer[i] += 1
                if aliens2.alien_timer[i] == 25:
                    aliens2.alien_list[i] = pygame.transform.rotate((pygame.image.load("assets/alien_second.png")), 90)
                    aliens2.alien_bool[i] = "No_collision"
                    aliens2.alien_timer[i] = 0

        # visual feedback from collision for player
        if player.bool == "Yes_collision":
            player.timer += 1
            if player.timer == 25:
                player.bool = "No_collision"
                player.timer = 0

        # visual feedback from collision for boss
        if boss2.boss_bool == "Yes_collision":
            boss2.boss_timer += 1
            if boss2.boss_timer == 25:
                boss2.boss_bool = "No_collision"
                boss2.boss_timer = 0

        # WINNING CONDITIONS
        if boss2.boss2_HP <= 0:
            explode.lastX = boss2.bossX
            explode.lastY = boss2.bossY
            boss2.boss2_HP = 0
            boss2.end_timer += 1

            if boss2.end_timer == 1:
                boss2.boss_level = False
                boss2.start_phase = False
                boss2.second_phase = False
                player.score += 100
                explode.cub_numb += 500
                func.place_cubes_boss(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list, explode.cube_list,
                                 explode.cubeX_change, explode.cubeY_change)

                drops.HP_drop_count += 3
                for i in range(drops.HP_drop_count):
                    drops.HP_drop_list.append(assets.HP_drop_i)
                    drops.drop_numbX.append(random.randint(200, 1000))
                    drops.drop_numbY.append(random.randint(0, 640))
                    func.HP_drop(drops.drop_numbX[i], drops.drop_numbY[i], i, drops.HP_drop_list)
                drops.ammo_drop_count += 3
                for i in range(drops.ammo_drop_count):
                    drops.ammo_drop_list.append(assets.bullet_drop)
                    drops.ammo_drop_numbX.append(random.randint(200, 1000))
                    drops.ammo_drop_numbY.append(random.randint(0, 640))
                    func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)
                drops.missile_drop_count += 2
                for i in range(drops.missile_drop_count):
                    drops.missile_drop_list.append(assets.missile_drop)
                    drops.missile_drop_numbX.append(random.randint(200, 1000))
                    drops.missile_drop_numbY.append(random.randint(0, 640))
                    func.ammo_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)

            text = assets.font6.render("Press enter to progress to next level", True, (205, 51, 51))
            assets.screen.blit(text, (200, 640))

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
                func.place_cubes(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list, explode.cube_list,
                                 explode.cubeX_change, explode.cubeY_change)
            if player.end_timer == 300:
                run = False
                game_over(player.score)

        # collision feedback from player
        if player.hp > 0:
            if player.bool == "No_collision":
                func.player(player.x, player.y)
            if player.bool == "Yes_collision":
                func.player2(player.x, player.y)

        # print text on screen
        if 0 <= timer <= 60 or 121 <= timer <= 180 or 241 <= timer <= 300 or 361 <= timer <= 420:
            text = assets.font6.render("Wave 1 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 61 <= timer <= 120 or 181 <= timer <= 240 or 301 <= timer <= 360 or 421 <= timer <= 480:
            text = assets.font6.render("Wave 1 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if 2800 <= timer <= 2860 or 2921 <= timer <= 2980 or 3041 <= timer <= 3100 or 3161 <= timer <= 3220:
            text = assets.font6.render("Wave 2 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 2861 <= timer <= 2920 or 2981 <= timer <= 3040 or 3101 <= timer <= 3160 or 3221 <= timer <= 3280:
            text = assets.font6.render("Wave 2 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if 6800 <= timer <= 6860 or 6921 <= timer <= 6980 or 7041 <= timer <= 7100 or 7161 <= timer <= 7220:
            text = assets.font6.render("Wave 3 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 6861 <= timer <= 6920 or 6981 <= timer <= 7040 or 7101 <= timer <= 7160 or 7221 <= timer <= 7280:
            text = assets.font6.render("Wave 3 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if (10800 <= timer <= 10860 or 10921 <= timer <= 10980 or 11041 <= timer <= 11100 or 11161 <= timer <= 11220
            or 11281 <= timer <= 11340 or 11401 <= timer <= 11460 or 11521 <= timer <= 11580):
            text = assets.font6.render("!!! Boss Incoming !!!", True, (205, 51, 51))
            assets.screen.blit(text, (420, 640))
            assets.screen.blit(text, (420, 10))
        if (10861 <= timer <= 10920 or 10981 <= timer <= 11040 or 11101 <= timer <= 11160 or 11221 <= timer <= 11280
            or 11341 <= timer <= 11400 or 11461 <= timer <= 11520 or 11581 <= timer <= 11640):
            text = assets.font6.render("!!! Boss Incoming !!!", True, (219, 209, 4))
            assets.screen.blit(text, (420, 10))
            assets.screen.blit(text, (420, 640))

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
        for i in range(drops.missile_drop_count):
            func.missile_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)
        pygame.display.update()

        # limit frames to 100fps / 100 loops per second
        clock.tick(100)

# main loop for level 3
def level_3(player):
    # initialise all objects
    drops = stats.Drops()
    aliens = stats.Aliens()
    aliens2 = stats.Aliens_2()
    explode = stats.Explosions()
    boss3 = stats.level3_Boss()
    wpn1 = stats.level1_Boss_Wpn1()
    wpn2 = stats.level1_Boss_Wpn2()
    player.x = 0
    player.y = 380

    # enemy counter start stats
    enemy_numb = 0
    enemy_count = 0
    enemy_numb_2 = 0
    enemy_count_2 = 0
    enemy_wave = False

    timer = 0
    run = True
    while run == True:
        # background ,UI elements
        assets.screen.fill((0, 0, 0))
        assets.screen.blit(assets.background_3, (0, 0))
        assets.screen.blit(assets.UI, (-5, 678))

        # first enemy wave spawn
        if timer == 200:
            enemy_numb = 15
            enemy_count = 15
            enemy_numb_2 += 4
            enemy_count_2 = 4
            enemy_wave = True

        # second enemy wave spawn
        if timer == 3000:
            enemy_numb += 15
            enemy_count = 15
            enemy_numb_2 += 4
            enemy_count_2 = 4
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
            enemy_numb_2 += 5
            enemy_count_2 = 5
            enemy_wave = True
            # spawn extra ammunition for player
            drops.ammo_drop_count += 1
            for i in range(drops.ammo_drop_count):
                drops.ammo_drop_list.append(assets.bullet_drop)
                drops.ammo_drop_numbX.append(random.randint(0, 550))
                drops.ammo_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)

        # boss level spawn
        if timer == 12000:
            boss3.boss_level = True
            drops.ammo_drop_count += 1
            for i in range(drops.ammo_drop_count):
                drops.ammo_drop_list.append(assets.bullet_drop)
                drops.ammo_drop_numbX.append(random.randint(0, 550))
                drops.ammo_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)
            drops.missile_drop_count += 1
            for i in range(drops.missile_drop_count):
                drops.missile_drop_list.append(assets.missile_drop)
                drops.missile_drop_numbX.append(random.randint(0, 550))
                drops.missile_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)

        # supply drop during boss battle
        if boss3.boss3_HP == 350 and boss3.boss_phase_ammo_drop == True:
            enemy_numb = 10
            enemy_count = 10
            enemy_wave = True
            boss3.boss_phase_ammo_drop = False
            drops.HP_drop_count += 2
            for i in range(drops.HP_drop_count):
                drops.HP_drop_list.append(assets.HP_drop_i)
                drops.drop_numbX.append(random.randint(0, 550))
                drops.drop_numbY.append(random.randint(0, 640))
                func.HP_drop(drops.drop_numbX[i], drops.drop_numbY[i], i, drops.HP_drop_list)
            drops.ammo_drop_count += 2
            for i in range(drops.ammo_drop_count):
                drops.ammo_drop_list.append(assets.bullet_drop)
                drops.ammo_drop_numbX.append(random.randint(0, 550))
                drops.ammo_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i], i, drops.ammo_drop_list)

        if boss3.boss3_HP == 200 and boss3.last_wave == True:
            enemy_numb = 10
            enemy_count = 10
            enemy_wave = True
            boss3.last_wave = False

        # place enemies on screen
        if enemy_wave == True:
            # for type 1 enemies
            if enemy_numb > 0:
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
            # for type 2 enemies
            if enemy_numb_2 > 0:
                func.create_enemy_2(enemy_count_2, aliens2.alien_list, aliens2.alienX_list, aliens2.alienY_list, aliens2.alienHP_list,
                                  aliens2.alienY_change, aliens2.alienX_change,aliens2.alien_bool, aliens2.alien_timer, aliens2.alien_ammo,
                                  aliens2.alienBool_ammo, aliens2.alienY_ammo, aliens2.alienX_ammo)
                for i in range(enemy_numb_2):
                    if aliens2.alienY_list[i] >= 640:
                        aliens2.alienY_change[i] = -1
                    if aliens2.alienY_list[i] <= 0:
                        aliens2.alienY_change[i] = 1
                    aliens2.alienX_list[i] -= 2
                    func.enemy(aliens2.alienX_list[i], aliens2.alienY_list[i], i, aliens2.alien_list)
                    if int(i) <= 700:
                        enemy_wave = False

        # place boss on screen
        if boss3.boss_level == True:
            boss3.bossX = 1200
            boss3.bossY = 250
            boss3.bossX_change = 0
            boss3.bossY_change = 0
            # collision feedback from boss
            if boss3.boss2_HP > 0:
                if boss3.boss_bool == "No_collision":
                    func.mothership(boss3.bossX, boss3.bossY)
                if boss3.boss_bool == "Yes_collision":
                    func.mothership(boss3.bossX, boss3.bossY)
            boss3.boss_level = False
            boss3.start_phase = True

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
                # press enter to progress to next level if boss defeated
                if event.key == pygame.K_RETURN:
                    if boss3.boss3_HP <= 0:
                        run = False
                        del drops
                        del aliens
                        del explode
                        del boss3
                        del wpn1
                        del wpn2
                        game_win(player.score)

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

        # ENEMY LOOP TYPE 1
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

        # ENEMY LOOP TYPE 2
        if enemy_wave == False:
            for i in range(enemy_numb_2):
                # enemy movement
                aliens2.alienY_list[i] += aliens2.alienY_change[i]
                aliens2.alienX_list[i] += aliens2.alienX_change[i]
                # enemy zone of control/collision
                if aliens2.alienY_list[i] >= 640:
                    aliens2.alienY_change[i] = -1
                if aliens2.alienY_list[i] <= 0:
                    aliens2.alienY_change[i] = 1
                if aliens2.alienX_list[i] >= 1180:
                    aliens2.alienX_change[i] = -1
                if aliens2.alienX_list[i] <= 450:
                    aliens2.alienX_change[i] = 1
                # random direction change
                numb = random.randint(1, 500)
                if numb == 1:
                    aliens2.alienX_change[i] = -1
                if numb == 2:
                    aliens2.alienX_change[i] = 1
                if numb == 3:
                    aliens2.alienY_change[i] = -1
                if numb == 4:
                    aliens2.alienY_change[i] = 1

                # enemy fire with enemy behavior, which uses random chance of shot and defined range where to shoot
                InRange = func.Range(player.y, aliens2.alienY_list[i])
                numb2 = random.randint(1, 100)
                if InRange and numb2 == 5 and aliens2.alienBool_ammo[i] == "old":
                    aliens2.alienBool_ammo[i] = "new"
                    aliens2.alienY_ammo[i] = aliens2.alienY_list[i]
                    aliens2.alienX_ammo[i] = aliens2.alienX_list[i]
                    # adds new elements at the end of the list
                    for j in range(1):
                        aliens2.alien_ammo.append(pygame.image.load("assets/laser.jpg"))
                        aliens2.alienY_ammo.append(800)
                        aliens2.alienX_ammo.append(1200)
                        aliens2.alienBool_ammo.append("old")

                # tracks enemy shots on screen
                if aliens2.alienBool_ammo[i] == "new":
                    func.enemy_fire(aliens2.alienX_ammo[i], aliens2.alienY_ammo[i], i, aliens2.alien_ammo)
                    aliens2.alienX_ammo[i] -= aliens2.alienX_ammoChange_2
                # removes enemy shots when on edge of window
                if aliens2.alienBool_ammo[i] == "new":
                    if aliens2.alienX_ammo[i] <= 0:
                        del aliens2.alien_ammo[i]
                        del aliens2.alienY_ammo[i]
                        del aliens2.alienX_ammo[i]
                        del aliens2.alienBool_ammo[i]
                        aliens2.max_enemy_ammo -= 1
                # launch and update enemy
                func.enemy(aliens2.alienX_list[i], aliens2.alienY_list[i], i, aliens2.alien_list)

        # adds new enemy elements to enemy lists in 0 coordinates to avoid error by deleting those on collision
        if enemy_numb_2 <= enemy_numb_2 + 2 and len(aliens2.alien_list) <= enemy_numb_2 + 2:
            aliens2.alien_list.append(pygame.transform.rotate((pygame.image.load("assets/alien_second.png")), 90))
            aliens2.alienX_list.append(1250)
            aliens2.alienY_list.append(640)
            aliens2.alienHP_list.append(15)
            aliens2.alienY_change.append(0)
            aliens2.alienX_change.append(0)

        # what happens if enemy HP is 0 ( enemy replaced by exploision)
        for i in range(enemy_numb_2):
            if aliens2.alienHP_list[i] <= 0:
                explode.lastX = aliens2.alienX_list[i]
                explode.lastY = aliens2.alienY_list[i]
                del aliens2.alien_list[i]
                del aliens2.alienX_list[i]
                del aliens2.alienY_list[i]
                del aliens2.alienHP_list[i]
                del aliens2.alienY_change[i]
                del aliens2.alienX_change[i]
                del aliens2.alien_timer[i]
                del aliens2.alien_bool[i]
                player.score += 10
                enemy_numb_2 -= 1
                # place explosion debris on screen
                explode.cub_numb += 70
                func.place_cubes(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list,
                                 explode.cube_list, explode.cubeX_change,
                                 explode.cubeY_change)

        # BOSS LOOPS
        # boss intro
        if boss3.boss_level == False and boss3.start_phase == True:
            # static intro movement
            boss3.bossY += boss3.bossY_change
            boss3.bossX += boss3.bossX_change
            boss3.bossX_change = -0.5
            # collision feedback from boss
            if boss3.boss3_HP > 0:
                if boss3.boss_bool == "No_collision":
                    func.mothership(boss3.bossX, boss3.bossY)
                if boss3.boss_bool == "Yes_collision":
                    func.mothership(boss3.bossX, boss3.bossY)
            if boss3.bossX == 600:
                boss3.second_phase = True
                boss3.start_phase = False
        # battle phase
        if boss3.boss_level == False and boss3.start_phase == False and boss3.second_phase == True:
            # boss movement
            boss3.bossY += boss3.bossY_change
            boss3.bossX += boss3.bossX_change
            func.mothership(boss3.bossX, boss3.bossY)
            if boss3.bossY >= 400:
                boss3.bossY_change = -0.5
            if boss3.bossY <= 0:
                boss3.bossY_change = 0.5
            if boss3.bossX >= 1000:
                boss3.bossX_change = -0.5
            if boss3.bossX <= 600:
                boss3.bossX_change = 0.5
            # random direction change
            numb = random.randint(1, 450)
            if numb == 1:
                boss3.bossX_change = -0.5
            if numb == 2:
                boss3.bossX_change = 0.5
            if numb == 3:
                boss3.bossY_change = -0.5
            if numb == 4:
                boss3.bossY_change = 0.5

            # boss fire with boss behavior, which uses random chance of shot and defined range where to shoot
            # first weapon type
            if boss3.boss3_HP > 350:
                InRange_2 = func.Range(player.y, boss3.bossY)
                numb3 = random.randint(1, 50)
                if InRange_2 and numb3 == 5:
                    # top gun
                    wpn1.boss_ammo_counter_top += 1
                    wpn1.bossY_ammo_numb_top = boss3.bossY
                    wpn1.bossX_ammo_numb_top = boss3.bossX
                    # adds new elements at teh end of the list
                    for i in range(1):
                        wpn1.boss_ammo_top.append(assets.boss_ammo)
                        wpn1.bossY_ammo_top.append(wpn1.bossY_ammo_numb_top)
                        wpn1.bossX_ammo_top.append(wpn1.bossX_ammo_numb_top)
                        wpn1.boss_bool_top.append("yes")

                    # bottom gun
                    wpn1.boss_ammo_counter_bottom += 1
                    wpn1.bossY_ammo_numb_bottom = boss3.bossY
                    wpn1.bossX_ammo_numb_bottom = boss3.bossX
                    # adds new elements at teh end of the list
                    for i in range(1):
                        wpn1.boss_ammo_bottom.append(assets.boss_ammo)
                        wpn1.bossY_ammo_bottom.append(wpn1.bossY_ammo_numb_bottom)
                        wpn1.bossX_ammo_bottom.append(wpn1.bossX_ammo_numb_bottom)
                        wpn1.boss_bool_bottom.append("yes")

            #top gun
            # tracks enemy shots on screen
            for i in range(wpn1.boss_ammo_counter_top):
                if wpn1.boss_bool_top[i] == "yes":
                    func.final_boss_fire(wpn1.bossX_ammo_top[i], wpn1.bossY_ammo_top[i], i, wpn1.boss_ammo_top)
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
                    func.final_boss_fire_2(wpn1.bossX_ammo_bottom[i], wpn1.bossY_ammo_bottom[i], i, wpn1.boss_ammo_bottom)
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
            if boss3.boss3_HP < 350 and boss3.boss3_HP > 200:
                InRange_2 = func.Range(player.y, boss3.bossY)
                numb4 = random.randint(1, 50)
                if InRange_2 and numb4 == 5:

                    # top gun
                    wpn2.boss_ammo_counter_top += 1
                    wpn2.bossY_ammo_numb_2_top = boss3.bossY
                    wpn2.bossX_ammo_numb_2_top = boss3.bossX
                    # adds new elements at teh end of the list
                    for i in range(1):
                        wpn2.boss_ammo_top.append(assets.boss_laser)
                        wpn2.bossY_ammo_top.append(wpn2.bossY_ammo_numb_2_top)
                        wpn2.bossX_ammo_top.append(wpn2.bossX_ammo_numb_2_top)
                        wpn2.boss_bool_top.append("yes")

                    # bottom gun
                    wpn2.boss_ammo_counter_bottom += 1
                    wpn2.bossY_ammo_numb_bottom = boss3.bossY
                    wpn2.bossX_ammo_numb_bottom = boss3.bossX
                    # adds new elements at teh end of the list
                    for i in range(1):
                        wpn2.boss_ammo_bottom.append(assets.boss_laser)
                        wpn2.bossY_ammo_bottom.append(wpn2.bossY_ammo_numb_bottom)
                        wpn2.bossX_ammo_bottom.append(wpn2.bossX_ammo_numb_bottom)
                        wpn2.boss_bool_bottom.append("yes")

            # top gun
            # tracks enemy shots on screen
            for i in range(wpn2.boss_ammo_counter_top):
                if wpn2.boss_bool_top[i] == "yes":
                    func.final_boss_laser(wpn2.bossX_ammo_top[i], wpn2.bossY_ammo_top[i], i, wpn2.boss_ammo_top)
                    wpn2.bossX_ammo_top[i] -= wpn2.bossX_ammoChange_2
            # removes enemy shots when on edge of window
            for j in range(wpn2.boss_ammo_counter_top - 3):
                if wpn2.boss_bool_top[j] == "yes":
                    if wpn2.bossX_ammo_top[j] <= -100:
                        del wpn2.boss_ammo_top[j]
                        del wpn2.bossY_ammo_top[j]
                        del wpn2.bossX_ammo_top[j]
                        del wpn2.boss_bool_top[j]
                        wpn2.boss_ammo_counter_top -= 1

            # bottom gun
            # tracks enemy shots on screen
            for i in range(wpn2.boss_ammo_counter_bottom):
                if wpn2.boss_bool_bottom[i] == "yes":
                    func.final_boss_laser_2(wpn2.bossX_ammo_bottom[i], wpn2.bossY_ammo_bottom[i], i, wpn2.boss_ammo_bottom)
                    wpn2.bossX_ammo_bottom[i] -= wpn2.bossX_ammoChange_2
            # removes enemy shots when on edge of window
            for j in range(wpn2.boss_ammo_counter_bottom - 3):
                if wpn2.boss_bool_bottom[j] == "yes":
                    if wpn2.bossX_ammo_bottom[j] <= -100:
                        del wpn2.boss_ammo_bottom[j]
                        del wpn2.bossY_ammo_bottom[j]
                        del wpn2.bossX_ammo_bottom[j]
                        del wpn2.boss_bool_bottom[j]
                        wpn2.boss_ammo_counter_bottom -= 1

            # death laser weapon type
            if boss3.boss3_HP < 200:
                InRange_3 = func.Range(player.y, boss3.bossY)
                numb4 = random.randint(1, 400)
                # places targeting laser on screen
                if InRange_3 and numb4 == 5 and boss3.tg_laser_active == False and boss3.death_laser_active == False:
                    func.final_boss_target_sys(boss3.bossX, boss3.bossY)
                    boss3.tg_laser_active = True

                # RELEASE DEATH LASER
                if boss3.tging_timer == 300:
                    boss3.tg_laser_active = False
                    boss3.tging_timer = 0
                    func.final_boss_death_laser(boss3.bossX, boss3.bossY)
                    boss3.death_laser_active = True

                # turn off death laser
                if boss3.death_laser_timer == 300:
                    boss3.death_laser_active = False
                    boss3.death_laser_timer = 0

            # tracks targeting laser on screen
            if boss3.tg_laser_active == True:
                func.final_boss_target_sys(boss3.bossX, boss3.bossY)
                boss3.tging_timer += 1 # targeting timer

            # tracks death laser on screeen
            if boss3.death_laser_active == True:
                func.final_boss_death_laser(boss3.bossX, boss3.bossY)
                boss3.death_laser_timer += 1

            # collision feedback from boss
            if boss3.boss3_HP > 0:
                if boss3.boss_bool == "No_collision":
                    func.mothership(boss3.bossX, boss3.bossY)
                if boss3.boss_bool == "Yes_collision":
                     func.mothership_2(boss3.bossX, boss3.bossY)

        # COLLISION
        # for what happens if collision happens (player <-- enemy shots(type 1))
        for i in range(enemy_numb):
            if player.hp > 0:
                collide2 = func.collision(player.x, player.y, aliens.alienX_ammo[i], aliens.alienY_ammo[i])
                if collide2:
                    player.hp -= 1
                    player.bool = "Yes_collision"
                    del aliens.alien_ammo[i]
                    del aliens.alienY_ammo[i]
                    del aliens.alienX_ammo[i]
                    del aliens.alienBool_ammo[i]

        # for what happens if collision happens (player <-- enemy shots(type 2))
        for i in range(enemy_numb_2):
            if player.hp > 0:
                collide14 = func.collision(player.x, player.y, aliens2.alienX_ammo[i], aliens2.alienY_ammo[i])
                if collide14:
                    player.hp -= 2
                    player.bool = "Yes_collision"
                    del aliens2.alien_ammo[i]
                    del aliens2.alienY_ammo[i]
                    del aliens2.alienX_ammo[i]
                    del aliens2.alienBool_ammo[i]

        # for what happens if collision happens (player <--> enemy(type 1))
        for i in range(enemy_numb):
            collide3 = func.collision(player.x, player.y, aliens.alienX_list[i], aliens.alienY_list[i])
            if collide3:
                player.bool = "Yes_collision"
                aliens.alienHP_list[i] -= 5
                player.hp -= 1
                player.score += 1
                aliens.alien_bool[i] = "Yes_collision"
                aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))

        # for what happens if collision happens (player <--> enemy(type 2))
        for i in range(enemy_numb_2):
            collide15 = func.collision(player.x, player.y, aliens2.alienX_list[i], aliens2.alienY_list[i])
            if collide15:
                player.bool = "Yes_collision"
                aliens2.alienHP_list[i] -= 5
                player.hp -= 1
                player.score += 1
                aliens2.alien_bool[i] = "Yes_collision"
                aliens2.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien_second2.png")), 90))

        # for what happens if collision happens (player missile --> enemy(type 1))
        for i in range(enemy_numb):
            collide1 = func.collision(aliens.alienX_list[i], aliens.alienY_list[i], player.missile_x, player.missile_y)
            if collide1:
                aliens.alienHP_list[i] -= 25
                aliens.alien_bool[i] = "Yes_collision"
                aliens.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_x = 380

        # for what happens if collision happens (player missile --> enemy(type 2))
        for i in range(enemy_numb_2):
            collide16 = func.collision(aliens2.alienX_list[i], aliens2.alienY_list[i], player.missile_x,
                                      player.missile_y)
            if collide16:
                aliens2.alienHP_list[i] -= 25
                aliens2.alien_bool[i] = "Yes_collision"
                aliens2.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien_second2.png")), 90))
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_x = 380

        # for what happens if collision happens (player <--> HP_drop)
        for i in range(drops.HP_drop_count):
            collide4 = func.collision(player.x, player.y, drops.drop_numbX[i], drops.drop_numbY[i])
            if collide4:
                drops.drop_numbX[i] = -100
                drops.drop_numbY[i] = 0
                player.hp += 1

        # for what happens if collision happens (player <--> ammo_drop)
        for i in range(drops.ammo_drop_count):
            collide5 = func.collision(player.x, player.y, drops.ammo_drop_numbX[i], drops.ammo_drop_numbY[i])
            if collide5:
                drops.ammo_drop_numbX[i] = -100
                drops.ammo_drop_numbY[i] = 0
                player.ammo += 400

        # for what happens if collision happens (player <--> missile_drop)
        for i in range(drops.missile_drop_count):
            collide13 = func.collision(player.x, player.y, drops.missile_drop_numbX[i], drops.missile_drop_numbY[i])
            if collide13:
                drops.missile_drop_numbX[i] = -100
                drops.missile_drop_numbY[i] = 0
                player.missile_ammo += 1

        # for what happens if collision happens (player shots --> enemy(type 1 and type 2))
        for j in range(player.max_ammo):
            # for enemy type 1
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
            # for enemy type 2
            for i in range(enemy_numb_2):
                collide17 = func.collision(aliens2.alienX_list[i], aliens2.alienY_list[i], player.ammoX_list[j], player.ammoY_list[j])
                # what happens at single impact
                if collide17:
                    aliens2.alienHP_list[i] -= 1
                    player.score += 1
                    aliens2.alien_bool[i] = "Yes_collision"
                    aliens2.alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien_second2.png")), 90))
                    player.ammoY_list[j] = 750
                    player.ammoX_list[j] = 1150

        # colisions for players vs boss
        if boss3.boss_level == False and boss3.start_phase == False and boss3.second_phase == True:
            # for what happens if collision happens (player shots --> boss)
            for j in range(player.max_ammo):
                collide6 = func.collision8(boss3.bossX, boss3.bossY, player.ammoX_list[j],  player.ammoY_list[j])
                # what happens at single impact
                if collide6:
                    boss3.boss3_HP -= 1
                    player.score += 1
                    boss3.boss_bool = "Yes_collision"
                    player.ammoY_list[j] = 750
                    player.ammoX_list[j] = 1150

            # for what happens if collision happens (player missile --> boss)
            collide7 = func.collision8(boss3.bossX, boss3.bossY, player.missile_x, player.missile_y)
            if collide7:
                boss3.boss3_HP -= 25
                boss3.boss_bool = "Yes_collision"
                player.missile_state = "old"
                player.missile_x = 0
                player.missile_y = 380

            # for what happens if collision happens (player <--> boss)
            collide8 = func.collision9(player.x, player.y, boss3.bossX, boss3.bossY)
            if collide8:
                player.bool = "Yes_collision"
                boss3.boss3_HP -= 1
                player.hp -= 1
                player.score += 1
                boss3.boss_bool = "Yes_collision"

        # for what happens if collision happens (player <-- final boss shots(first weapon stype))
        if boss3.boss3_HP > 0:
            for i in range(wpn1.boss_ammo_counter_top):
                if player.hp > 0:
                    collide9 = func.collision10(player.x, player.y, wpn1.bossX_ammo_top[i], wpn1.bossY_ammo_top[i])
                    if collide9:
                        player.hp -= 1
                        player.bool = "Yes_collision"
                        wpn1.bossY_ammo_top[i] = 0
                        wpn1.bossX_ammo_top[i] = -100

            for i in range(wpn1.boss_ammo_counter_bottom):
                if player.hp > 0:
                    collide10 = func.collision11(player.x, player.y, wpn1.bossX_ammo_bottom[i], wpn1.bossY_ammo_bottom[i])
                    if collide10:
                        player.hp -= 1
                        player.bool = "Yes_collision"
                        wpn1.bossY_ammo_bottom[i] = 0
                        wpn1.bossX_ammo_bottom[i] = -100

            # for what happens if collision happens (player <-- boss shots(second weapon stype))
            for i in range(wpn2.boss_ammo_counter_top):
                if player.hp > 0:
                    collide11 = func.collision12(player.x, player.y, wpn2.bossX_ammo_top[i], wpn2.bossY_ammo_top[i])
                    if collide11:
                        player.hp -= 2
                        player.bool = "Yes_collision"
                        wpn2.bossY_ammo_top[i] = 0
                        wpn2.bossX_ammo_top[i] = -100

            for i in range(wpn2.boss_ammo_counter_bottom):
                if player.hp > 0:
                    collide12 = func.collision13(player.x, player.y, wpn2.bossX_ammo_bottom[i], wpn2.bossY_ammo_bottom[i])
                    if collide12:
                        player.hp -= 2
                        player.bool = "Yes_collision"
                        wpn2.bossY_ammo_bottom[i] = 0
                        wpn2.bossX_ammo_bottom[i] = -100

        # for what happens if collision happens ( player <-- final boss death laser )
        if boss3.death_laser_active == True:
            if player.hp > 0:
                collide18 = func.collision14(player.y, boss3.bossY)
                if collide18:
                    player.hp -= 1
                    player.bool = "Yes_collision"

        # visual feedback from collision for enemy (type 1)
        for i in range(enemy_numb):
            if aliens.alien_bool[i] == "Yes_collision":
                aliens.alien_timer[i] += 1
                if aliens.alien_timer[i] == 25:
                    aliens.alien_list[i] = pygame.transform.rotate((pygame.image.load("assets/alien.png")), 90)
                    aliens.alien_bool[i] = "No_collision"
                    aliens.alien_timer[i] = 0

        # visual feedback from collision for enemy (type 2)
        for i in range(enemy_numb_2):
            if aliens2.alien_bool[i] == "Yes_collision":
                aliens2.alien_timer[i] += 1
                if aliens2.alien_timer[i] == 25:
                    aliens2.alien_list[i] = pygame.transform.rotate((pygame.image.load("assets/alien_second.png")), 90)
                    aliens2.alien_bool[i] = "No_collision"
                    aliens2.alien_timer[i] = 0

        # visual feedback from collision for player
        if player.bool == "Yes_collision":
            player.timer += 1
            if player.timer == 25:
                player.bool = "No_collision"
                player.timer = 0

        # visual feedback from collision for boss
        if boss3.boss_bool == "Yes_collision":
            boss3.boss_timer += 1
            if boss3.boss_timer == 25:
                boss3.boss_bool = "No_collision"
                boss3.boss_timer = 0

        # WINNING CONDITIONS
        if boss3.boss3_HP <= 0:
            explode.lastX = boss3.bossX
            explode.lastY = boss3.bossY
            boss3.boss3_HP = 0
            boss3.end_timer += 1

            if boss3.end_timer == 1:
                boss3.boss_level = False
                boss3.start_phase = False
                boss3.second_phase = False
                player.score += 100
                explode.cub_numb += 500
                func.place_cubes_boss(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list, explode.cube_list,
                                 explode.cubeX_change, explode.cubeY_change)

            text = assets.font6.render("Press enter to finish game", True, (205, 51, 51))
            assets.screen.blit(text, (330, 640))

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
                func.place_cubes(explode.lastX, explode.lastY, explode.cubeX_list, explode.cubeY_list, explode.cube_list,
                                 explode.cubeX_change, explode.cubeY_change)
            if player.end_timer == 300:
                run = False
                game_over(player.score)

        # collision feedback from player
        if player.hp > 0:
            if player.bool == "No_collision":
                func.player(player.x, player.y)
            if player.bool == "Yes_collision":
                func.player2(player.x, player.y)

        # print text on screen
        if 0 <= timer <= 60 or 121 <= timer <= 180 or 241 <= timer <= 300 or 361 <= timer <= 420:
            text = assets.font6.render("Wave 1 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 61 <= timer <= 120 or 181 <= timer <= 240 or 301 <= timer <= 360 or 421 <= timer <= 480:
            text = assets.font6.render("Wave 1 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if 2800 <= timer <= 2860 or 2921 <= timer <= 2980 or 3041 <= timer <= 3100 or 3161 <= timer <= 3220:
            text = assets.font6.render("Wave 2 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 2861 <= timer <= 2920 or 2981 <= timer <= 3040 or 3101 <= timer <= 3160 or 3221 <= timer <= 3280:
            text = assets.font6.render("Wave 2 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if 6800 <= timer <= 6860 or 6921 <= timer <= 6980 or 7041 <= timer <= 7100 or 7161 <= timer <= 7220:
            text = assets.font6.render("Wave 3 Incoming", True, (205, 51, 51))
            assets.screen.blit(text, (450, 10))
        if 6861 <= timer <= 6920 or 6981 <= timer <= 7040 or 7101 <= timer <= 7160 or 7221 <= timer <= 7280:
            text = assets.font6.render("Wave 3 Incoming", True, (95, 9, 9))
            assets.screen.blit(text, (450, 10))

        if (11800 <= timer <= 11860 or 12921 <= timer <= 11980 or 12141 <= timer <= 12100 or 12161 <= timer <= 12220
            or 12281 <= timer <= 12340 or 12401 <= timer <= 12460 or 12521 <= timer <= 12580):
            text = assets.font6.render("!!! Mothership Incoming !!!", True, (205, 51, 51))
            assets.screen.blit(text, (360, 640))
            assets.screen.blit(text, (360, 10))
        if (11861 <= timer <= 11920 or 11981 <= timer <= 12040 or 12101 <= timer <= 12160 or 12221 <= timer <= 12280
            or 12341 <= timer <= 12400 or 12461 <= timer <= 12520 or 12581 <= timer <= 12640):
            text = assets.font6.render("!!! Mothership Incoming !!!", True, (219, 209, 4))
            assets.screen.blit(text, (360, 10))
            assets.screen.blit(text, (360, 640))

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
        for i in range(drops.missile_drop_count):
            func.missile_drop(drops.missile_drop_numbX[i], drops.missile_drop_numbY[i], i, drops.missile_drop_list)
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    run = False
                    start()

        # updates display each frame
        pygame.display.update()
        # limit frames to 100fps / 100 loops per second
        clock.tick(100)

# game over screen loop
def game_win(score):
    run = True
    while run == True:
        assets.screen.fill((0, 0, 0))

        # all text on the screen
        gameWin = assets.font2.render("You Win", True, (255, 215, 0))
        assets.screen.blit(gameWin, (330, 200))
        text = assets.font3.render("Alien Invasion is defeated! Earth is Saved", True, (255, 255, 255))
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    run = False
                    start()

        # updates display each frame
        pygame.display.update()
        # limit frames to 100fps / 100 loops per second
        clock.tick(100)


# launch start
start()
