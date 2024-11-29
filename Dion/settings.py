import pygame
import os

#加载游戏资源
# 设置游戏界面大小，保存每一个类的图像数据

DEAD = pygame.image.load(os.path.join("Images/Dino", "DinoDead.png"))
RUNNING = [pygame.image.load(os.path.join("Images/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Images/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Images/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Images/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Images/Dino", "DinoDuck2.png"))]
SMALL_CACTUS =  [pygame.image.load(os.path.join("Images/Cactus", "SmallCactus1.png")),
                    pygame.image.load(os.path.join("Images/Cactus", "SmallCactus2.png")),
                    pygame.image.load(os.path.join("Images/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Images/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Images/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Images/Cactus", "LargeCactus3.png"))]
BIRD = [pygame.image.load(os.path.join("Images/Bird", "Bird1.png")),
           pygame.image.load(os.path.join("Images/Bird", "Bird2.png"))]
CLOUD = pygame.image.load(os.path.join("Images/Other", "Cloud.png"))
GAMEOVER = pygame.image.load(os.path.join("Images/Other", "GameOver.png"))
RESET = pygame.image.load(os.path.join("Images/Other", "Reset.png"))
BG = pygame.image.load(os.path.join("Images/Other", "BackGround.png"))

