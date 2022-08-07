import pygame
from pygame.locals import *
import random

# IMAGES

# image sources

# WINDOW VARIABLES

WIDTH = 1280
HEIGHT = 700

TILE = 40

mid_x_coord = (WIDTH/2) - 9*TILE
mid_y_coord = (HEIGHT/2) - 6.5*TILE

# MAKE SCREEN

pygame.init()
my_screen = pygame.display.set_mode((WIDTH, HEIGHT), NOFRAME)


main_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 2/"
img_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 2/images/"
sound_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 2/sounds/"

block_images = {0: "dirt_pixel.png",
                1: "grass_pixel.png",
                2: "stone_pixel.png",
                3: "water_pixel.png"}

objects_images = {0: "boat.png",
                  1: "coin.png",
                  2: "hammer.png",
                  3: "log.png",
                  4: "meat.png",
                  5: "pear.png",
                  6: "portal.png",
                  7: "treasure.png"}

objects_dic = {"boat": 0,
               "coin": 1,
               "hammer": 2,
               "log": 3,
               "meat": 4,
               "pear": 5,
               "portal": 6,
               "treasure": 7}

objects_dic2 = {0: "boat",
               1: "coin",
               2: "hammer",
               3: "log",
               4: "meat",
               5: "pear",
               6: "portal",
               7: "treasure"}

scenery_images = {0: "tree.png"} #
