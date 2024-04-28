# file for main loop for start and Level 1

import pygame
import random
import func
import assets
#import stats

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
    # player starting position, stats
    playerX = 0
    playerY = 380
    playerX_change = 0
    playerY_change = 0
    player_bool = "No_collision"
    player_timer = 0
    player_HP = 10
    ammo = 1000
    missile_ammo = 3
    score = 0
    ammoAssY = 380
    ammoAssX = 0
    missileY = 380
    missileX = 0
    ammoX_change = 4  # BULLET SPEED
    missileX_change = 2.5  # MISSILE SPEED
    ammo_state = "old"
    missile_state = "old"
    ammo_list = []
    ammoY_list = []
    ammoX_list = []
    max_ammo = 0
    end_timer = 0

    # booster drop lists
    HP_drop_count = 0
    HP_drop_list = []
    drop_numbX = []
    drop_numbY = []
    ammo_drop_count = 0
    ammo_drop_list = []
    ammo_drop_numbX = []
    ammo_drop_numbY = []

    # alien lists
    alien_list = []
    alienX_list = []
    alienY_list = []
    alienHP_list = []
    alienY_change = []
    alienX_change = []
    alien_bool = []
    alien_timer = []
    alien_ammo = []
    alienY_ammo = []
    alienX_ammo = []
    alienBool_ammo = []
    alienX_ammoChange = 3.5  # ENEMY BULLET SPEED
    max_enemy_ammo = 0

    # enemy counter start stats
    enemy_numb = 0
    enemy_count = 0
    enemy_wave = False

    # explosions lists
    lastX = 0
    lastY = 0
    cub_numb = 0
    cube_list = []
    cubeX_list = []
    cubeY_list = []
    cubeX_change = []
    cubeY_change = []

    # boss start counters
    boss_level = False
    start_phase = False
    second_phase = False
    bossX = 0
    bossY = 0
    bossX_change = 0
    bossY_change = 0
    boss_HP = 110
    boss_bool = "No_collision"
    boss_timer = 0

    # boss first weapon type stats
    bossX_ammoChange = 3.5

    boss_ammo_counter_top = 0
    bossX_ammo_numb_top = 0
    bossY_ammo_numb_top = 0
    boss_ammo_top = []
    bossX_ammo_top = []
    bossY_ammo_top = []
    boss_bool_top = []

    boss_ammo_counter_bottom = 0
    bossX_ammo_numb_bottom = 0
    bossY_ammo_numb_bottom = 0
    boss_ammo_bottom = []
    bossX_ammo_bottom = []
    bossY_ammo_bottom = []
    boss_bool_bottom = []

    # boss second weapon type stats
    bossX_ammoChange_2 = 5.5

    boss_ammo_counter_2_top = 0
    bossX_ammo_numb_2_top = 0
    bossY_ammo_numb_2_top = 0
    boss_ammo_2_top = []
    bossX_ammo_2_top = []
    bossY_ammo_2_top = []
    boss_bool_2_top = []

    boss_ammo_counter_2_bottom = 0
    bossX_ammo_numb_2_bottom = 0
    bossY_ammo_numb_2_bottom = 0
    boss_ammo_2_bottom = []
    bossX_ammo_2_bottom = []
    bossY_ammo_2_bottom = []
    boss_bool_2_bottom = []

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
            HP_drop_count += 1
            for i in range(HP_drop_count):
                HP_drop_list.append(assets.HP_drop_i)
                drop_numbX.append(random.randint(0, 550))
                drop_numbY.append(random.randint(0, 640))
                func.HP_drop(drop_numbX[i], drop_numbY[i], i, HP_drop_list)

        # third enemy wave spawn
        if timer == 7000:
            enemy_numb += 15
            enemy_count = 15
            enemy_wave = True
            # spawn extra ammunition for player
            ammo_drop_count += 1
            for i in range(ammo_drop_count):
                ammo_drop_list.append(assets.bullet_drop)
                ammo_drop_numbX.append(random.randint(0, 550))
                ammo_drop_numbY.append(random.randint(0, 640))
                func.ammo_drop(ammo_drop_numbX[i], ammo_drop_numbY[i], i, ammo_drop_list)

        # boss level spawn
        if timer == 11000:
            boss_level = True

        # place enemies on screen
        if enemy_wave == True:
            func.create_enemy(enemy_count, alien_list, alienX_list, alienY_list, alienHP_list,alienY_change, alienX_change,
                              alien_bool, alien_timer, alien_ammo, alienBool_ammo, alienY_ammo, alienX_ammo)
            for i in range(enemy_numb):
                if alienY_list[i] >= 640:
                    alienY_change[i] = -1
                if alienY_list[i] <= 0:
                    alienY_change[i] = 1
                alienX_list[i] -= 2
                func.enemy(alienX_list[i], alienY_list[i], i, alien_list)
                if int(i) <= 700:
                    enemy_wave = False

        # place boss on screen
        if boss_level == True:
            bossX = 1200
            bossY = 250
            bossX_change = 0
            bossY_change = 0
            # collision feedback from boss
            if boss_HP > 0:
                if boss_bool == "No_collision":
                    func.boss(bossX, bossY)
                if boss_bool == "Yes_collision":
                    func.boss2(bossX, bossY)
            boss_level = False
            start_phase = True

        # tracks explosion debris on screen
        for i in range(cub_numb):
            func.explosion(cubeX_list[i], cubeY_list[i], i, cube_list)
            cubeX_list[i] += cubeX_change[i]
            cubeY_list[i] += cubeY_change[i]

        # what happens if debris reach edge of the screen
        for i in range(cub_numb):
            if cubeX_list[i] >= 1200 or cubeX_list[i] <= 0:
                cubeX_list[i] = 1200
                cubeY_list[i] = 800
                cubeX_change[i] = 0
                cubeY_change[i] = 0
            if cubeY_list[i] >= 678 or cubeY_list[i] <= 0:
                cubeX_list[i] = 1200
                cubeY_list[i] = 800
                cubeX_change[i] = 0
                cubeY_change[i] = 0

        # deletes off screen debris elements
        if cub_numb > 80:
            for i in range(cub_numb - 80):
                if cubeY_list[i] >= 750:
                    del cube_list[i]
                    del cubeX_list[i]
                    del cubeY_list[i]
                    del cubeX_change[i]
                    del cubeY_change[i]
                    cub_numb -= 1

        # PLAYER LOOP
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # MOVEMENT SPEED
                    playerX_change =- 3.5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 3.5
                if event.key == pygame.K_UP:
                    playerY_change =- 3.5
                if event.key == pygame.K_DOWN:
                    playerY_change = 3.5
                # fire ammo
                if event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(1, 200)
                    if player_HP > 0 and ammo > 0:
                        max_ammo += 1
                        ammo -= 1
                        ammo_state = "new"
                        if ammo_state == "new":
                            ammoAssX = playerX
                            ammoAssY = playerY
                            # adds new elements at teh end of the list
                            for i in range(1):
                                ammo_list.append(assets.ammoAss)
                                ammoY_list.append(ammoAssY)
                                ammoX_list.append(ammoAssX)
                            # launch fire function when space bar is pressed
                            for i in range(max_ammo):
                                func.fire(ammoX_list[i], ammoY_list[i], i, ammo_list)
                # fire missile
                if event.key == pygame.K_q:
                    if player_HP > 0 and missile_state == "old" and missile_ammo > 0:
                        missile_ammo -= 1
                        missile_state = "new"
                        missileY = playerY
                        missileX = playerX
                        func.missile_fire(missileX, missileY)
            # for when keys are released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0.0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0.0
                if event.key == pygame.K_SPACE:
                    max_ammo += 0

        # tracks player change on screen
        playerX += playerX_change
        playerY += playerY_change

        #edge of screen collision
        if playerX <= 0:
            playerX = 0
        if playerX >= 1130:
            playerX = 1130
        if playerY >= 631:
            playerY = 631
        if playerY <= 0:
            playerY = 0

        # track shots across X Axis
        if ammo_state == "new":
            for i in range(max_ammo):
                func.fire(ammoX_list[i], ammoY_list[i], i, ammo_list)
                ammoX_list[i] += ammoX_change
        # removes shots leaving window
        if ammo_state == "new":
            for i in range(max_ammo - 3):
                if ammoX_list[i] >= 1200:
                    del ammo_list[i]
                    del ammoX_list[i]
                    del ammoY_list[i]
                    max_ammo -= 1

        # track missile across X axis
        if missile_state == "new":
            func.missile_fire(missileX, missileY)
            missileX += missileX_change
        # prepares for new missile when old one leaves window
        if missile_state == "new" and missileX >= 1200:
            missile_state = "old"

        # ENEMY LOOP
        if enemy_wave == False:
            for i in range(enemy_numb):
                # enemy movement
                alienY_list[i] += alienY_change[i]
                alienX_list[i] += alienX_change[i]
                # enemy zone of control/collision
                if alienY_list[i] >= 640:
                    alienY_change[i] = -1
                if alienY_list[i] <= 0:
                    alienY_change[i] = 1
                if alienX_list[i] >= 1180:
                    alienX_change[i] = -1
                if alienX_list[i] <= 450:
                    alienX_change[i] = 1
                # random direction change
                numb = random.randint(1, 500)
                if numb == 1:
                    alienX_change[i] = -1
                if numb == 2:
                    alienX_change[i] = 1
                if numb == 3:
                    alienY_change[i] = -1
                if numb == 4:
                    alienY_change[i] = 1

                # enemy fire with enemy behavior, which uses random chance of shot and defined range where to shoot
                InRange = func.Range(playerY, alienY_list[i])
                numb2 = random.randint(1, 200)
                if InRange and numb2 == 5 and alienBool_ammo[i] == "old":
                    alienBool_ammo[i] = "new"
                    alienY_ammo[i] = alienY_list[i]
                    alienX_ammo[i] = alienX_list[i]
                    # adds new elements at the end of the list
                    for j in range(1):
                        alien_ammo.append(pygame.image.load("assets/alien_shot.png"))
                        alienY_ammo.append(800)
                        alienX_ammo.append(1200)
                        alienBool_ammo.append("old")

                # tracks enemy shots on screen
                if alienBool_ammo[i] == "new":
                    func.enemy_fire(alienX_ammo[i], alienY_ammo[i], i, alien_ammo)
                    alienX_ammo[i] -= alienX_ammoChange
                # removes enemy shots when on edge of window
                if alienBool_ammo[i] == "new":
                    if alienX_ammo[i] <= 0:
                        del alien_ammo[i]
                        del alienY_ammo[i]
                        del alienX_ammo[i]
                        del alienBool_ammo[i]
                        max_enemy_ammo -= 1
                # launch and update enemy
                func.enemy(alienX_list[i], alienY_list[i], i, alien_list)

        # adds new enemy elements to enemy lists in 0 coordinates to avoid error by deleting those on collision
        if enemy_numb <= enemy_numb + 2 and len(alien_list) <= enemy_numb + 2:
            alien_list.append(pygame.transform.rotate((pygame.image.load("assets/alien.png")), 90))
            alienX_list.append(1250)
            alienY_list.append(640)
            alienHP_list.append(15)
            alienY_change.append(0)
            alienX_change.append(0)

        # what happens if enemy HP is 0 ( enemy replaced by exploision)
        for i in range(enemy_numb):
            if alienHP_list[i] <= 0:
                lastX = alienX_list[i]
                lastY = alienY_list[i]
                del alien_list[i]
                del alienX_list[i]
                del alienY_list[i]
                del alienHP_list[i]
                del alienY_change[i]
                del alienX_change[i]
                del alien_timer[i]
                del alien_bool[i]
                score += 10
                enemy_numb -= 1
                # place explosion debris on screen
                cub_numb += 70
                func.place_cubes(lastX, lastY, cubeX_list, cubeY_list, cube_list, cubeX_change,
                                 cubeY_change)

        # BOSS LOOPS
        # boss intro
        if boss_level == False and start_phase == True:
            # static intro movement
            bossY += bossY_change
            bossX += bossX_change
            bossX_change = -0.5
            # collision feedback from boss
            if boss_HP > 0:
                if boss_bool == "No_collision":
                    func.boss(bossX, bossY)
                if boss_bool == "Yes_collision":
                    func.boss2(bossX, bossY)
            if bossX == 600:
                second_phase = True
                start_phase = False
        # battle phase
        if boss_level == False and start_phase == False and second_phase == True:
            # boss movement
            bossY += bossY_change
            bossX += bossX_change
            func.boss(bossX, bossY)
            if bossY >= 520:
                bossY_change = -1
            if bossY <= 0:
                bossY_change = 1
            if bossX >= 1000:
                bossX_change = -1
            if bossX <= 600:
                bossX_change = 1
            # random direction change
            numb = random.randint(1, 450)
            if numb == 1:
                bossX_change = -1
            if numb == 2:
                bossX_change = 1
            if numb == 3:
                bossY_change = -1
            if numb == 4:
                bossY_change = 1

            # boss fire with boss behavior, which uses random chance of shot and defined range where to shoot
            # first weapon type
            InRange_2 = func.Range_2(playerY, bossY)
            numb3 = random.randint(1, 50)
            if InRange_2 and numb3 == 5:

                # top gun
                boss_ammo_counter_top += 1
                bossY_ammo_numb_top = bossY
                bossX_ammo_numb_top = bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    boss_ammo_top.append(assets.boss_ammo)
                    bossY_ammo_top.append(bossY_ammo_numb_top)
                    bossX_ammo_top.append(bossX_ammo_numb_top)
                    boss_bool_top.append("yes")

                # bottom gun
                boss_ammo_counter_bottom += 1
                bossY_ammo_numb_bottom = bossY
                bossX_ammo_numb_bottom = bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    boss_ammo_bottom.append(assets.boss_ammo)
                    bossY_ammo_bottom.append(bossY_ammo_numb_bottom)
                    bossX_ammo_bottom.append(bossX_ammo_numb_bottom)
                    boss_bool_bottom.append("yes")

            #top gun
            # tracks enemy shots on screen
            for i in range(boss_ammo_counter_top):
                if boss_bool_top[i] =="yes":
                    func.boss_fire(bossX_ammo_top[i], bossY_ammo_top[i], i, boss_ammo_top)
                    bossX_ammo_top[i] -= bossX_ammoChange
            # removes enemy shots when on edge of window
            for j in range(boss_ammo_counter_top - 3):
                if boss_bool_top[j] == "yes":
                    if bossX_ammo_top[j] <= -100:
                        del boss_ammo_top[j]
                        del bossY_ammo_top[j]
                        del bossX_ammo_top[j]
                        del boss_bool_top[j]
                        boss_ammo_counter_top -= 1

            # bottom gun
            # tracks enemy shots on screen
            for i in range(boss_ammo_counter_bottom):
                if boss_bool_bottom[i] == "yes":
                    func.boss_fire_2(bossX_ammo_bottom[i], bossY_ammo_bottom[i], i, boss_ammo_bottom)
                    bossX_ammo_bottom[i] -= bossX_ammoChange
            # removes enemy shots when on edge of window
            for j in range(boss_ammo_counter_bottom - 3):
                if boss_bool_bottom[j] == "yes":
                    if bossX_ammo_bottom[j] <= -100:
                        del boss_ammo_bottom[j]
                        del bossY_ammo_bottom[j]
                        del bossX_ammo_bottom[j]
                        del boss_bool_bottom[j]
                        boss_ammo_counter_bottom -= 1

            # second weapon type
            InRange_2 = func.Range_2(playerY, bossY)
            numb4 = random.randint(1, 75)
            if InRange_2 and numb4 == 5:

                # top gun
                boss_ammo_counter_2_top += 1
                bossY_ammo_numb_2_top = bossY
                bossX_ammo_numb_2_top = bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    boss_ammo_2_top.append(assets.boss_laser)
                    bossY_ammo_2_top.append(bossY_ammo_numb_2_top)
                    bossX_ammo_2_top.append(bossX_ammo_numb_2_top)
                    boss_bool_2_top.append("yes")

                # bottom gun
                boss_ammo_counter_2_bottom += 1
                bossY_ammo_numb_2_bottom = bossY
                bossX_ammo_numb_2_bottom = bossX
                # adds new elements at teh end of the list
                for i in range(1):
                    boss_ammo_2_bottom.append(assets.boss_laser)
                    bossY_ammo_2_bottom.append(bossY_ammo_numb_2_bottom)
                    bossX_ammo_2_bottom.append(bossX_ammo_numb_2_bottom)
                    boss_bool_2_bottom.append("yes")

            # top gun
            # tracks enemy shots on screen
            for i in range(boss_ammo_counter_2_top):
                if boss_bool_2_top[i] == "yes":
                    func.boss_laser(bossX_ammo_2_top[i], bossY_ammo_2_top[i], i, boss_ammo_2_top)
                    bossX_ammo_2_top[i] -= bossX_ammoChange_2
            # removes enemy shots when on edge of window
            for j in range(boss_ammo_counter_2_top - 3):
                if boss_bool_2_top[j] == "yes":
                    if bossX_ammo_2_top[j] <= -100:
                        del boss_ammo_2_top[j]
                        del bossY_ammo_2_top[j]
                        del bossX_ammo_2_top[j]
                        del boss_bool_2_top[j]
                        boss_ammo_counter_2_top -= 1

            # bottom gun
            # tracks enemy shots on screen
            for i in range(boss_ammo_counter_2_bottom):
                if boss_bool_2_bottom[i] == "yes":
                    func.boss_laser_2(bossX_ammo_2_bottom[i], bossY_ammo_2_bottom[i], i, boss_ammo_2_bottom)
                    bossX_ammo_2_bottom[i] -= bossX_ammoChange_2
            # removes enemy shots when on edge of window
            for j in range(boss_ammo_counter_2_bottom - 3):
                if boss_bool_2_bottom[j] == "yes":
                    if bossX_ammo_2_bottom[j] <= -100:
                        del boss_ammo_2_bottom[j]
                        del bossY_ammo_2_bottom[j]
                        del bossX_ammo_2_bottom[j]
                        del boss_bool_2_bottom[j]
                        boss_ammo_counter_2_bottom -= 1

            # collision feedback from boss
            if boss_HP > 0:
                if boss_bool == "No_collision":
                    func.boss(bossX, bossY)
                if boss_bool == "Yes_collision":
                     func.boss2(bossX, bossY)

        # COLLISION
        # for what happens if collision happens (player <-- enemy shots)
        for i in range(enemy_numb):
            if player_HP > 0:
                collide2 = func.collision2(playerX, playerY, alienX_ammo[i], alienY_ammo[i])
                if collide2:
                    player_HP -= 1
                    player_bool = "Yes_collision"
                    del alien_ammo[i]
                    del alienY_ammo[i]
                    del alienX_ammo[i]
                    del alienBool_ammo[i]

        # for what happens if collision happens (player <--> enemy)
        for i in range(enemy_numb):
            collide3 = func.collision3(playerX, playerY, alienX_list[i], alienY_list[i])
            if collide3:
                player_bool = "Yes_collision"
                alienHP_list[i] -= 5
                player_HP -= 1
                score += 1
                alien_bool[i] = "Yes_collision"
                alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))

        # for what happens if collision happens (player missile --> enemy)
        for i in range(enemy_numb):
            collide1 = func.collision1(alienX_list[i], alienY_list[i], missileX, missileY)
            if collide1:
                alienHP_list[i] -= 25
                alien_bool[i] = "Yes_collision"
                alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))
                missile_state = "old"
                missileX = 0
                missileY = 380

        # for what happens if collision happens (player <--> HP_drop)
        for i in range(HP_drop_count):
            collide4 = func.collision4(playerX, playerY, drop_numbX[i], drop_numbY[i])
            if collide4:
                del HP_drop_list[i]
                del drop_numbX[i]
                del drop_numbY[i]
                HP_drop_count -= 1
                player_HP += 1

        # for what happens if collision happens (player <--> ammo_drop)
        for i in range(ammo_drop_count):
            collide5 = func.collision5(playerX, playerY, ammo_drop_numbX[i], ammo_drop_numbY[i])
            if collide5:
                del ammo_drop_list[i]
                del ammo_drop_numbX[i]
                del ammo_drop_numbY[i]
                ammo_drop_count -= 1
                ammo += 400

        # for what happens if collision happens (player shots --> enemy)
        for j in range(max_ammo):
            for i in range(enemy_numb):
                collide = func.collision(alienX_list[i], alienY_list[i], ammoX_list[j], ammoY_list[j])
                # what happens at single impact
                if collide:
                    alienHP_list[i] -= 1
                    score += 1
                    alien_bool[i] = "Yes_collision"
                    alien_list[i] = (pygame.transform.rotate((pygame.image.load("assets/alien2.png")), 90))
                    ammoY_list[j] = 750
                    ammoX_list[j] = 1150

        # colisions for players vs boss
        if boss_level == False and start_phase == False and second_phase == True:
            # for what happens if collision happens (player shots --> boss)
            for j in range(max_ammo):
                collide6 = func.collision6(bossX, bossY, ammoX_list[j],  ammoY_list[j])
                # what happens at single impact
                if collide6:
                    boss_HP -= 1
                    score += 1
                    boss_bool = "Yes_collision"
                    ammoY_list[j] = 750
                    ammoX_list[j] = 1150

            # for what happens if collision happens (player missile --> boss)
            collide7 = func.collision7(bossX, bossY, missileX, missileY)
            if collide7:
                boss_HP -= 25
                boss_bool = "Yes_collision"
                missile_state = "old"
                missileX = 0
                missileY = 380

            # for what happens if collision happens (player <--> boss)
            collide8 = func.collision8(playerX, playerY, bossX, bossY)
            if collide8:
                player_bool = "Yes_collision"
                boss_HP -= 1
                player_HP -= 1
                score += 1
                boss_bool = "Yes_collision"

        # for what happens if collision happens (player <-- boss shots)
        for i in range(boss_ammo_counter_top):
            if player_HP > 0:
                collide9 = func.collision9(playerX, playerY, bossX_ammo_top[i], bossY_ammo_top[i])
                if collide9:
                    player_HP -= 1
                    player_bool = "Yes_collision"
                    bossY_ammo_top[i] = 0
                    bossX_ammo_top[i] = -100

        # visual feedback from collision for enemy
        for i in range(enemy_numb):
            if alien_bool[i] == "Yes_collision":
                alien_timer[i] += 1
                if alien_timer[i] == 25:
                    alien_list[i] = pygame.transform.rotate((pygame.image.load("assets/alien.png")), 90)
                    alien_bool[i] = "No_collision"
                    alien_timer[i] = 0

        # visual feedback from collision for boss
        if boss_bool == "Yes_collision":
            boss_timer += 1
            if boss_timer == 25:
                boss_bool = "No_collision"
                boss_timer = 0

        # visual feedback from collision for player
        if player_bool == "Yes_collision":
            player_timer += 1
            if player_timer == 25:
                player_bool = "No_collision"
                player_timer = 0

        # LAUNCH ALL AND GAME OVER CONDITION
        # if player HP is less than 0 game is over
        if player_HP <= 0:
            lastX = playerX
            lastY = playerY
            player_HP = 0
            end_timer += 1
            if end_timer == 1:
                # place explosion debris on screen
                cub_numb += 70
                func.place_cubes(lastX, lastY, cubeX_list, cubeY_list, cube_list, cubeX_change, cubeY_change)

            if end_timer == 300:
                run = False
                game_over(score)

        # collision feedback from player
        if player_HP > 0:
            if player_bool == "No_collision":
                func.player(playerX, playerY)
            if player_bool == "Yes_collision":
                func.player2(playerX, playerY)

        # update all
        timer += 1
        func.healthCounter(player_HP)
        func.ammoCounter(ammo)
        func.scoreCounter(score)
        func.missileCounter(missile_ammo)
        for i in range(HP_drop_count):
            func.HP_drop(drop_numbX[i], drop_numbY[i], i, HP_drop_list)
        for i in range(ammo_drop_count):
            func.ammo_drop(ammo_drop_numbX[i], ammo_drop_numbY[i], i, ammo_drop_list)
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