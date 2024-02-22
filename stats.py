# file for all variables and lists

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