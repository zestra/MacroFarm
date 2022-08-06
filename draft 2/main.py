import pygame
from pygame.locals import *
from sys import exit

import math
import random

from basics import *
from buttons import *

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
                  6: "portal.png"}

objects_dic = {"boat": 0,
               "coin": 1,
               "hammer": 2,
               "log": 3,
               "meat": 4,
               "pear": 5,
               "portal": 6}

objects_dic2 = {0: "boat",
               1: "coin",
               2: "hammer",
               3: "log",
               4: "meat",
               5: "pear",
               6: "portal"}

scenery_images = {0: "tree.png"}

player_images = {"left": "wiz_left.png",
              "right": "wiz_right.png",
              "up": "wiz_back.png",
              "down": "wiz_front.png"}

inventory = {  # name: [image, no., activated?]
    "boat": [objects_images[objects_dic["boat"]], 0, False],
    "coin": [objects_images[objects_dic["coin"]], 10, False],
    "hammer": [objects_images[objects_dic["hammer"]], 3, False],
    "log": [objects_images[objects_dic["log"]], 7, False],
    "meat": [objects_images[objects_dic["meat"]], 2, False],
    "pear": [objects_images[objects_dic["pear"]], 9, False],
    "portal": [objects_images[objects_dic["portal"]], 0, False]}

selected_inventory_item = 0

shop = {  # item: [no., deal 1 (in coins), deal 2 (in logs), image]
    "boat": [-13, 30, 25, objects_images[objects_dic["boat"]]],
    "coin": [20, "", 1, objects_images[objects_dic["coin"]]],
    "hammer": [15, 3, 2, objects_images[objects_dic["hammer"]]],
    "log": [10, 3, "", objects_images[objects_dic["log"]]],
    "meat": [30, 4, 4, objects_images[objects_dic["meat"]]],
    "pear": [50, 2, 2, objects_images[objects_dic["pear"]]],
    "portal": [7, 40, "", objects_images[objects_dic["portal"]]]}

selected_shop_item = 0
selected_shop_deal = 2

timer = 0


def initialize():
    player_direction = "down"

    for item in shop:
        if item != "portal":
            shop[item][0] += 20

    for item in inventory:
        if item not in ["portal", "boat"]:
            inventory[item][1] += 5

    # MAKE MAP

    blocks_map = []
    for y in range(14):
        blocks_map.append([])
        for x in range(18):
            blocks_map[len(blocks_map) - 1].append(1)

    # make river

    start_x = random.randint(0, 16)
    start_y = random.randint(5, 12)
    for _ in range(start_y):
        blocks_map[_][start_x] = 3
    start_x2 = random.randint(start_x, 16)
    for _ in range(start_x2):
        blocks_map[start_y][_] = 3
    for _ in range(start_y, 14):
        blocks_map[_][start_x2] = 3

    # object mapping

    objects_map = []
    for y in range(14):
        objects_map.append([])
        for x in range(18):
            objects_map[len(objects_map) - 1].append("")
    for _ in range(random.randint(15, 35)):
        random_y = random.randint(0, 13)
        random_x = random.randint(0, 17)

        while (blocks_map[random_y][random_x] == 3):
            random_y = random.randint(0, 13)
            random_x = random.randint(0, 17)

        item = random.randint(0, len(objects_images) - 1)

        while objects_dic2[item] in ["boat", "portal"]:
            item = random.randint(0, len(objects_images) - 1)

        objects_map[random_y][random_x] = item

    random_y = random.randint(0, 13)
    random_x = random.randint(0, 17)

    while (blocks_map[random_y][random_x] == 3):
        random_y = random.randint(0, 13)
        random_x = random.randint(0, 17)

    objects_map[random_y][random_x] = objects_dic["portal"]


    # scenery mapping

    scenery_map = []
    for y in range(14):
        scenery_map.append([])
        for x in range(18):
            scenery_map[len(scenery_map) - 1].append("")
    for _ in range(random.choice([random.randint(65, 109)])):
        random_y = random.randint(0, 13)
        random_x = random.randint(0, 17)

        while (objects_map[random_y][random_x] != "") or (blocks_map[random_y][random_x] == 3):
            random_y = random.randint(0, 13)
            random_x = random.randint(0, 17)

        scenery_map[random_y][random_x] = 0

    # player mapping

    player_x = random.randint(0, 17)
    player_y = random.randint(0, 13)
    while (blocks_map[player_y][player_x] != 3
        and objects_map[player_y][player_x] == ""
        and scenery_map[player_y][player_x] == "") is False:
        player_x = random.randint(0, 17)
        player_y = random.randint(0, 13)

    # variables

    health = 100
    hammer_death = 3

    life_counter = 0

    run = True

    pre_blocks = []

    return player_direction, player_x, player_y, \
           shop, inventory,\
           blocks_map, objects_map, scenery_map, \
           health, hammer_death, life_counter, run, pre_blocks


player_direction, player_x, player_y, shop, inventory, blocks_map, objects_map, scenery_map, health, hammer_death, life_counter, run, pre_blocks = initialize()

while run:
    my_screen.fill((0, 0, 0))

    pre_player_x = player_x
    pre_player_y = player_y

    # MANAGING EVENTS

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DELETE:
                pygame.quit()
                exit()

            if event.key == K_BACKSPACE:
                selected_shop_item += 1
                if selected_shop_item == 6:
                    selected_shop_item = 0
                    selected_shop_deal += 1
                    if selected_shop_deal > 3:
                        selected_shop_deal = 2

            if event.key == K_n\
                    and shop[objects_dic2[selected_shop_item]][0] > 0:

                if selected_shop_deal - 1 == 1 and shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1] != "":
                    if shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1] <= inventory["coin"][1]:
                        shop[objects_dic2[selected_shop_item]][0] -= 1
                        inventory[shop[objects_dic2[selected_shop_item]][3][0: len(shop[objects_dic2[selected_shop_item]][3]) - 4]][1] += 1
                        inventory["coin"][1] -= shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1]

                elif selected_shop_deal - 1 == 2 and shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1] != "":
                    if shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1] <= inventory["log"][1]:
                        shop[objects_dic2[selected_shop_item]][0] -= 1
                        inventory[shop[objects_dic2[selected_shop_item]][3][0: len(shop[objects_dic2[selected_shop_item]][3]) - 4]][1] += 1
                        inventory["log"][1] -= shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1]

            if event.key == K_TAB:
                selected_inventory_item += 1
                if selected_inventory_item == len(objects_dic):
                    selected_inventory_item = 0

            if event.key == K_RETURN\
                    and inventory[objects_dic2[selected_inventory_item]][1] > 0:
                if objects_dic2[selected_inventory_item] in ["boat", "hammer", "meat", "pear", "portal"]:
                    inventory[objects_dic2[selected_inventory_item]][2] = True
                    inventory[objects_dic2[selected_inventory_item]][1] -= 1

            if event.key == K_UP\
                    and player_y > 0:
                player_y -= 1
                player_direction = "up"

            if event.key == K_DOWN\
                    and player_y < 13:
                player_y += 1
                player_direction = "down"

            if event.key == K_LEFT\
                    and player_x > 0:
                player_x -= 1
                player_direction = "left"

            if event.key == K_RIGHT\
                    and player_x < 17:
                player_x += 1
                player_direction = "right"

            if scenery_map[player_y][player_x] != "" and inventory["hammer"][2] is True:
                scenery_map[player_y][player_x] = ""
                hammer_death -= 1
                if hammer_death == 0:
                    inventory["hammer"][2] = False
                    inventory["log"][1] += 2
                    hammer_death = 3

            elif scenery_map[player_y][player_x] != ""\
                    or blocks_map[player_y][player_x] == 3\
                    and inventory["boat"][2] is False:
                player_y = pre_player_y
                player_x = pre_player_x

            elif scenery_map[player_y][player_x] != ""\
                    or blocks_map[player_y][player_x] == 3\
                    and inventory["boat"][2] is True:
                pass

            if event.key == K_c\
                and objects_map[player_y][player_x] != "":
                inventory[objects_dic2[objects_map[player_y][player_x]]][1] += 1
                objects_map[player_y][player_x] = ""

            if event.key == K_d\
                and objects_map[player_y][player_x] == ""\
                and inventory[objects_dic2[selected_inventory_item]][1] > 0:
                objects_map[player_y][player_x] = selected_inventory_item
                inventory[objects_dic2[selected_inventory_item]][1] -= 1

    # DRAWING MAP

    y = -1
    for row in blocks_map:
        y += 1
        x = -0
        for block in row:
            x += 1
            if block != "":
                draw_image(block_images[block], mid_x_coord + x*TILE, mid_y_coord + y*TILE, img_dir, my_screen)

    y = -1
    for row in objects_map:
        y += 1
        x = -0
        for object in row:
            x += 1
            if object != "":
                draw_image(objects_images[object], mid_x_coord + x * TILE, mid_y_coord + y * TILE, img_dir, my_screen,
                           1)

    y = -1
    for row in scenery_map:
        y += 1
        x = -0
        for scenery in row:
            x += 1
            if scenery != "":
                draw_image(scenery_images[scenery], mid_x_coord + x*TILE, mid_y_coord + y*TILE, img_dir, my_screen, 1, 1)

        if player_y == y:
            draw_image(player_images[player_direction], mid_x_coord + player_x * TILE + TILE,
                       mid_y_coord + player_y * TILE, img_dir, my_screen, 1)

    # MANAGING INVENTORY

    for item in objects_dic:
        if item in ["pear", "meat"]:
            if inventory[item][2] is True and health < 100:
                health += 10
                inventory[item][2] = False

        elif item == "boat":
            if inventory[item][2] is True:
                if player_y != pre_player_y or player_x != pre_player_x:
                    pre_blocks.append(blocks_map[player_y][player_x])
                if len(pre_blocks) == 2:
                    inventory[item][2] = False
                    pre_blocks = []
        elif item == "portal":
            if inventory[item][2] is True:
                player_direction, player_x, player_y, shop, inventory, blocks_map, objects_map, scenery_map, health, hammer_death, life_counter, run, pre_blocks = initialize()
                inventory[item][2] = False


    # DRAWING INVENTORY

    draw_text("INVENTORY", mid_x_coord - 150, mid_y_coord, my_screen, 45, "white", "din condensed")

    # DRAWING HEALTH BAR
    lower_y = 60
    further_x = 20

    draw_text("health bar", mid_x_coord - 200 + further_x, mid_y_coord + lower_y, my_screen, 20, "white", "arial")
    draw_rect(my_screen, mid_x_coord - 140 + further_x, mid_y_coord + lower_y, 100, 20, "white", 0, 0)
    if health > 30:
        draw_rect(my_screen, mid_x_coord - 140 + further_x, mid_y_coord + lower_y, health, 20, "green", 0, 0)
    else:
        draw_rect(my_screen, mid_x_coord - 140 + further_x, mid_y_coord + lower_y, health, 20, "red", 0, 0)
    draw_text(str(health) + "%", mid_x_coord - 120 + further_x, mid_y_coord + 5 + lower_y, my_screen, 10, "black", "arial")

    # ...

    lower_y = 50
    index_max = 3
    index = 0
    for y in range(0, len(inventory)):
        if inventory[objects_dic2[y]][2] is True:
            draw_image("highlight.png", 2*TILE + index*(TILE + 40), mid_y_coord + (y - index) * (TILE + (40/(index_max**2))) + 90 + lower_y, img_dir, my_screen, 0, 0)
        if y == objects_dic["portal"]:
            draw_image("portal2.png", 2 * TILE - 10 + index*(TILE + 40), mid_y_coord + (y - index) * (TILE + (40/(index_max**2))) + 110 + lower_y, img_dir,
                       my_screen, 1)
        else:
            draw_image(inventory[objects_dic2[y]][0], 2*TILE - 10 + index*(TILE + 40), mid_y_coord + (y - index) * (TILE + (40/(index_max**2))) + 110 + lower_y, img_dir, my_screen, 1)
        draw_text(str(inventory[objects_dic2[y]][1]), 2*TILE + 20 + index*(TILE + 40), mid_y_coord + (y - index) * (TILE + (40/(index_max**2))) + 70 + lower_y, my_screen, 20, "red", "DIN condensed")
        draw_rect(my_screen, 2*TILE + index*(TILE + 40), mid_y_coord + (y - index) * (TILE + (40/(index_max**2))) + 90 + lower_y, 60, 60)
        if y == selected_inventory_item:
            draw_image("selection.png", 2 * TILE + index*(TILE + 40), mid_y_coord + (y - index) * (TILE + (40/(index_max**2))) + 120 + lower_y, img_dir, my_screen, 1, 1)

        index += 1
        if index == index_max:
            index = 0

    # DRAWING SHOP

    draw_text("SHOP", WIDTH - mid_x_coord + 150, mid_y_coord, my_screen, 45, "white", "din condensed")

    for _ in range(0, len(shop)):
        if _ == objects_dic["portal"]:
            draw_image("portal2.png", WIDTH - 200 - 10, mid_y_coord + _ * (TILE + 40) + 120, img_dir,
                       my_screen, 1)
        else:
            draw_image(shop[objects_dic2[_]][3], WIDTH - 200 - 10, mid_y_coord + _*(TILE + 40) + 120, img_dir, my_screen, 1)
        draw_rect(my_screen, WIDTH - 240, mid_y_coord + _*(TILE + 40) + 70, 240, 60, "white", 1, 0)
        draw_rect(my_screen, WIDTH - 240, mid_y_coord + _*(TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(shop[objects_dic2[_]][0]), WIDTH - 240 + 60 + 30, mid_y_coord + _*(TILE + 40) + 70 + 20, my_screen, 25, "red", "DIN condensed")
        draw_rect(my_screen, WIDTH - 240 + 60, mid_y_coord + _*(TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(shop[objects_dic2[_]][1]), WIDTH - 240 + 60 + 60 + 30, mid_y_coord + _*(TILE + 40) + 70 + 20, my_screen, 25, "red", "DIN condensed")
        draw_rect(my_screen, WIDTH - 240 + 60 + 60, mid_y_coord + _*(TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(shop[objects_dic2[_]][2]), WIDTH - 240 + 60 + 60 + 60 + 30, mid_y_coord + _*(TILE + 40) + 70 + 20, my_screen, 25, "red", "DIN condensed")

    draw_image("selection.png", WIDTH - 210 + 60 * selected_shop_deal, mid_y_coord + selected_shop_item * (TILE + 40) + 130, img_dir, my_screen, 1)

    # MANAGING LIFE EVENTS

    life_counter += 1
    if life_counter == 180:
        health -= 10
        life_counter = 0

    if health == 0:
        run = False

    pygame.display.update()





