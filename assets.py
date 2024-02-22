# file for all game assets links

import pygame

pygame.init()

# assets
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Earth Defender")
playerAss = pygame.transform.rotate((pygame.image.load("assets/spaceship.png")), -90)
playerAss2 = pygame.transform.rotate((pygame.image.load("assets/spaceship2.png")), -90)
ammoAss = pygame.transform.rotate((pygame.image.load("assets/bullet.png")), -90)
playerMissile = pygame.transform.rotate((pygame.image.load("assets/missile.png")), -90)
HP_drop_i = pygame.image.load("assets/HP.png")
bullet_drop = pygame.image.load("assets/bullet_drop.png")
missile_drop = pygame.image.load("assets/missile_drop.png")
cube = pygame.image.load("assets/square.jpg")
background = pygame.image.load("assets/earth.jpg")
UI = pygame.image.load("assets/ui.jpg")
font = pygame.font.Font("assets/Basica.ttf", 32)
font2 = pygame.font.Font("assets/pixel.ttf", 102)
font3 = pygame.font.Font("assets/OpenSans.ttf", 22)
font4 = pygame.font.Font("assets/pixel.ttf", 150)
boss_ass = pygame.transform.rotate((pygame.image.load("assets/boss_1.png")), 90)
boss_ass_2 = pygame.transform.rotate((pygame.image.load("assets/boss_1_2.png")), 90)
boss_ammo = pygame.image.load("assets/alien_shot.png")
boss_laser = pygame.image.load("assets/laser.jpg")