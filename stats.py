# file for all classes
import pygame
import assets

# Player class containing all attributes for player
class Player:
    def __init__(self):
        self.x = 0
        self.y = 380
        self.x_change = 0
        self.y_change = 0
        self.bool = "No_collision"
        self.timer = 0
        self.hp = 10  #10
        self.ammo = 1000
        self.missile_ammo = 3
        self.score = 0
        self.ammo_y = 380
        self.ammo_x = 0
        self.missile_y = 380
        self.missile_x = 0
        self.ammoX_change = 4
        self.missileX_change = 2.5
        self.ammo_state = "old"
        self.missile_state = "old"
        self.ammo_list = []
        self.ammoY_list = []
        self.ammoX_list = []
        self.max_ammo = 0
        self.end_timer = 0

# class for supply drops attributes
class Drops:
    def __init__(self):
        self.HP_drop_count = 0
        self.HP_drop_list = []
        self.drop_numbX = []
        self.drop_numbY = []
        self.ammo_drop_count = 0
        self.ammo_drop_list = []
        self.ammo_drop_numbX = []
        self.ammo_drop_numbY = []
        self.missile_drop_count = 0
        self.missile_drop_list = []
        self.missile_drop_numbX = []
        self.missile_drop_numbY = []

# class for alien type 1 attributes and lists
class Aliens:
    def __init__(self):
        self.alien_list = []
        self.alienX_list = []
        self.alienY_list = []
        self.alienHP_list = []
        self.alienY_change = []
        self.alienX_change = []
        self.alien_bool = []
        self.alien_timer = []
        self.alien_ammo = []
        self.alienY_ammo = []
        self.alienX_ammo = []
        self.alienBool_ammo = []
        self.alienX_ammoChange = 3.5
        self.max_enemy_ammo = 0

class Aliens_2(Aliens):
    def __init__(self):
        Aliens.__init__(self)
        self.alienX_ammoChange_2 = 5.5

# class for sprites used in explosions
class Explosions:
    def __init__(self):
        self.lastX = 0
        self.lastY = 0
        self.cub_numb = 0
        self.cube_list = []
        self.cubeX_list = []
        self.cubeY_list = []
        self.cubeX_change = []
        self.cubeY_change = []

# Level 1 boss class containing all attributes for boss
class level1_Boss:
    def __init__(self):
        self.boss_level = False
        self.start_phase = False
        self.second_phase = False
        self.bossX = 0
        self.bossY = 0
        self.bossX_change = 0
        self.bossY_change = 0
        self.boss_HP = 110  # 110
        self.boss_bool = "No_collision"
        self.boss_timer = 0
        self.end_timer = 0

# Level 2 boss class containing all attributes for boss, inheriting attributes from Level 1 boss
class level2_Boss(level1_Boss):
    def __init__(self):
        level1_Boss.__init__(self)
        self.boss2_HP = 300  # 300
        self.boss_phase_ammo_drop = True
        self.tg_laser_active = False
        self.death_laser_active = False
        self.tging_timer = 0
        self.death_laser_timer = 0

# Level 3 boss class containing all attributes for boss, inheriting attributes from Level 1 and Level2 boses
class level3_Boss(level2_Boss):
    def __init__(self):
        level2_Boss.__init__(self)
        self.boss3_HP = 500  # 500
        self.last_wave = True

# class for boss's first type weapons
class level1_Boss_Wpn1:
    def __init__(self):
        self.bossX_ammoChange = 3.5
        self.boss_ammo_counter_top = 0
        self.bossX_ammo_numb_top = 0
        self.bossY_ammo_numb_top = 0
        self.boss_ammo_top = []
        self.bossX_ammo_top = []
        self.bossY_ammo_top = []
        self.boss_bool_top = []
        self.boss_ammo_counter_bottom = 0
        self.bossX_ammo_numb_bottom = 0
        self.bossY_ammo_numb_bottom = 0
        self.boss_ammo_bottom = []
        self.bossX_ammo_bottom = []
        self.bossY_ammo_bottom = []
        self.boss_bool_bottom = []

# class for boss's second type weapons, properties inherited from first type
class level1_Boss_Wpn2(level1_Boss_Wpn1):
    def __init__(self):
        level1_Boss_Wpn1.__init__(self)
        self.bossX_ammoChange_2 = 5.5

#class for buttons
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        # all buttons attributes
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (36, 36, 36)
        self.hover_color = (255, 215, 0)
        self.text = text
        self.font = assets.font6
        self.action = action
        self.text_surf = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.selected = False

    # draw buttons on screen
    def draw(self, screen):
        if self.selected:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    # function for triggering function associated to button
    def is_clicked(self):
        if self.action:
            action_to_execute = self.action  # Store the action to execute
            self.action = None  # Remove the action before executing it
            action_to_execute()

    # function for selecting button
    def set_selected(self, selected):
        self.selected = selected
