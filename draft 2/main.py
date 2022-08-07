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


def initialize():
    player_direction = "down"

    for item in shop:
        if item not in ["portal", "treasure"]:
            shop[item][0] += 20

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

        while objects_dic2[item] in ["boat", "portal", "treasure", "pear"]:
            item = random.randint(0, len(objects_images) - 1)

        objects_map[random_y][random_x] = item

    random_y = random.randint(0, 13)
    random_x = random.randint(0, 17)

    while (blocks_map[random_y][random_x] == 3):
        random_y = random.randint(0, 13)
        random_x = random.randint(0, 17)

    objects_map[random_y][random_x] = objects_dic["portal"]

    random_y = random.randint(0, 13)
    random_x = random.randint(0, 17)

    while (blocks_map[random_y][random_x] == 3):
        random_y = random.randint(0, 13)
        random_x = random.randint(0, 17)

    objects_map[random_y][random_x] = objects_dic["treasure"]

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

    animal_map = []
    for y in range(14):
        animal_map.append([])
        for x in range(18):
            animal_map[len(animal_map) - 1].append("")

    for _ in range(random.choice([random.randint(7, 15)])):
        random_x = random.randint(1, 17)
        random_y = random.randint(1, 13)

        while (blocks_map[random_y][random_x] == 3)\
                or (objects_map[random_y][random_x] != "")\
                or (scenery_map[random_y][random_x] != ""):
            random_x = random.randint(1, 17)
            random_y = random.randint(1, 13)

        animal_map[random_y][random_x] = Animal(random_x, random_y, random.randint(1, 2))

    return player_direction, player_x, player_y, \
           shop, inventory,\
           blocks_map, objects_map, scenery_map, \
           health, hammer_death, life_counter, run, pre_blocks, \
           animal_map


player_direction, player_x, player_y, shop, inventory, blocks_map, objects_map, scenery_map, health, hammer_death, life_counter, run, pre_blocks, animal_map = initialize()

current_storage = "inventory"

animala_timer = 0

pygame.mixer.init()
pygame.mixer.music.load(sound_dir + "theme.wav")
pygame.mixer.music.play(-1)

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
                current_storage = "shop"
                selected_shop_item += 1
                if selected_shop_item == 6:
                    selected_shop_item = 0
                    selected_shop_deal += 1
                    if selected_shop_deal > 3:
                        selected_shop_deal = 2

            if event.key == K_TAB:
                current_storage = "inventory"
                selected_inventory_item += 1
                if selected_inventory_item == len(objects_dic):
                    selected_inventory_item = 0

            if event.key == K_RETURN:
                if current_storage == "inventory":
                    if inventory[objects_dic2[selected_inventory_item]][1] > 0:
                        if objects_dic2[selected_inventory_item] in ["boat", "hammer", "portal", "treasure"]:
                            inventory[objects_dic2[selected_inventory_item]][2] = True
                            inventory[objects_dic2[selected_inventory_item]][1] -= 1
                        if objects_dic2[selected_inventory_item] in ["meat", "pear"] and health < 100:
                            inventory[objects_dic2[selected_inventory_item]][2] = True
                            inventory[objects_dic2[selected_inventory_item]][1] -= 1
                elif current_storage == "shop":
                    if shop[objects_dic2[selected_shop_item]][0] > 0:
                        if selected_shop_deal - 1 == 1 and shop[objects_dic2[selected_shop_item]][
                            selected_shop_deal - 1] != "":
                            if shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1] <= inventory["coin"][1]:
                                shop[objects_dic2[selected_shop_item]][0] -= 1
                                inventory[shop[objects_dic2[selected_shop_item]][3][
                                          0: len(shop[objects_dic2[selected_shop_item]][3]) - 4]][1] += 1
                                inventory["coin"][1] -= shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1]

                        elif selected_shop_deal - 1 == 2 and shop[objects_dic2[selected_shop_item]][
                            selected_shop_deal - 1] != "":
                            if shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1] <= inventory["log"][1]:
                                shop[objects_dic2[selected_shop_item]][0] -= 1
                                inventory[shop[objects_dic2[selected_shop_item]][3][
                                          0: len(shop[objects_dic2[selected_shop_item]][3]) - 4]][1] += 1
                                inventory["log"][1] -= shop[objects_dic2[selected_shop_item]][selected_shop_deal - 1]

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

            if inventory["hammer"][2] is False and animal_map[player_y][player_x] != "":
                health -= 10

            elif inventory["hammer"][2] is True and animal_map[player_y][player_x] != "":
                animal_map[player_y][player_x] = ""
                inventory["meat"][1] += 1

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

            if event.key == K_SPACE\
                and objects_map[player_y][player_x] != "":
                if objects_dic2[objects_map[player_y][player_x]] in ["meat", "pear"] and health < 100:
                    health += 10
                else:
                    inventory[objects_dic2[objects_map[player_y][player_x]]][1] += 1
                objects_map[player_y][player_x] = ""

            if event.key == K_BACKSLASH\
                and inventory[objects_dic2[selected_inventory_item]][1] > 0\
                and objects_map[player_y][player_x] == "":
                inventory[objects_dic2[selected_inventory_item]][1] -= 1
                objects_map[player_y][player_x] = selected_inventory_item

    for y in range(0, 13):
        for x in range(0, 17):
            animal = animal_map[y][x]
            if animal != "":
                animal.update(blocks_map, objects_map, scenery_map, animal_map)

    # DRAWING MAP

    draw_map(blocks_map, objects_map, scenery_map, player_images, player_direction, player_x, player_y, animal_map)

    # MANAGING INVENTORY

    inventory, health, player_direction, player_x, player_y, shop, blocks_map, objects_map, scenery_map, hammer_death, life_counter, run, pre_blocks, animal_map = manage_activated_items(inventory, health, player_direction, player_x, player_y, shop, blocks_map, objects_map, scenery_map, hammer_death, life_counter, run, pre_blocks, pre_player_x, pre_player_y, animal_map, initialize)

    player_images = draw_inventory(current_storage, inventory, selected_inventory_item, health, player_images)

    # DRAWING SHOP

    draw_shop(current_storage, shop, selected_shop_item, selected_shop_deal)

    # MANAGING LIFE EVENTS

    life_counter += 1
    if life_counter == 180:
        health -= 10
        life_counter = 0

    if health <= 0:
        run = False

    pygame.time.delay(100)
    pygame.display.update()