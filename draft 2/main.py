import pygame
from pygame.locals import *
from sys import exit

import math
import random

from basics import *
from buttons import *
from variables import *
from complex import *
from animals import *
from game_state import *


# Non-Constant Variables

player_images = {"left": "wiz_left.png",
              "right": "wiz_right.png",
              "up": "wiz_back.png",
              "down": "wiz_front.png"}

inventory = {  # name: [image, no., activated?]
    "boat": [objects_images[objects_dic["boat"]], 2, False],
    "coin": [objects_images[objects_dic["coin"]], 20, False],
    "hammer": [objects_images[objects_dic["hammer"]], 4, False],
    "log": [objects_images[objects_dic["log"]], 12, False],
    "meat": [objects_images[objects_dic["meat"]], 8, False],
    "pear": [objects_images[objects_dic["pear"]], 14, False],
    "portal": [objects_images[objects_dic["portal"]], 0, False],
    "treasure": [objects_images[objects_dic["treasure"]], 0, False]}

selected_inventory_item = 0

shop = {  # item: [no., deal 1 (in coins), deal 2 (in logs), image]
    "boat": [-13, 30, 15, objects_images[objects_dic["boat"]]],
    "coin": [20, "", 1, objects_images[objects_dic["coin"]]],
    "hammer": [15, 3, 2, objects_images[objects_dic["hammer"]]],
    "log": [10, 2, "", objects_images[objects_dic["log"]]],
    "meat": [30, 4, "", objects_images[objects_dic["meat"]]],
    "pear": [50, 2, "", objects_images[objects_dic["pear"]]],
    "portal": [7, 50, "", objects_images[objects_dic["portal"]]],
    "treasure": [20, 20, 10, objects_images[objects_dic["treasure"]]]}

selected_shop_item = 0
selected_shop_deal = 2

player_direction, player_x, player_y, shop, blocks_map, objects_map, scenery_map, health, hammer_death, life_counter, run, pre_blocks, animal_map = initialize(shop)

current_storage = "inventory"

my_game_state = State(["start", "play", "end"])

# Play theme Sound

pygame.mixer.init()
pygame.mixer.music.load(sound_dir + "theme.wav")
pygame.mixer.music.play(-1)

while run:
    my_screen.fill((0, 0, 0))

    if my_game_state.current == "start":
        draw_rect(my_screen, WIDTH/2, HEIGHT/2 - 90, 500, 5, "dark green", 0)
        draw_text("DEEP FOREST", WIDTH/2, HEIGHT/2 - 50, my_screen, 100, "dark green", "DIN Condensed")
        draw_text("press SPACE to start", WIDTH/2, HEIGHT/2 + 40, my_screen, 30, "dark green", "DIN Condensed")
        draw_rect(my_screen, WIDTH/2, HEIGHT/2 + 100, 500, 5, "dark green", 0)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    my_game_state.update()

    elif my_game_state.current == "play":
        pre_player_x = player_x
        pre_player_y = player_y

        # Update all Events

        inventory, selected_inventory_item, \
        shop, selected_shop_item, selected_shop_deal, \
        current_storage, \
        player_direction, player_x, player_y, pre_player_x, pre_player_y, \
        blocks_map, objects_map, animal_map, scenery_map, \
        hammer_death, life_counter, run, pre_blocks, health  = update_window(inventory, selected_inventory_item,
                                                                          shop, selected_shop_item, selected_shop_deal,
                                                                          current_storage,
                                                                          player_direction, player_y, player_x, pre_player_x, pre_player_y,
                                                                          animal_map, scenery_map, blocks_map, objects_map,
                                                                          hammer_death, life_counter, run, pre_blocks, health)

        # Draw entire Window

        player_images = draw_window(inventory, selected_inventory_item,
                                    shop, selected_shop_deal, selected_shop_item,
                                    current_storage,
                                    player_images, player_direction, player_x, player_y,
                                    blocks_map, objects_map, scenery_map, animal_map,
                                    health)

        # other...

        life_counter += 1
        if life_counter == 180:
            health -= 10
            life_counter = 0

        if health <= 0:
            run = False

    pygame.time.delay(100)
    pygame.display.update()