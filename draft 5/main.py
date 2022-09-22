import pygame
from pygame.locals import *
from sys import exit

from variables import *
from drawing_functions import draw_shop, draw_bank, draw_well, \
                              draw_trade, draw_health, draw_map, \
                              draw_carpenter, draw_inventory, draw_guide_lines

pygame.mixer.init()
pygame.mixer.music.load(sound_dir + "theme.wav")
pygame.mixer.music.play(-1)

player_x, player_y = int(visible_width_window / 2) - 1, int(visible_height_window / 2) - 1

while run:
    my_screen.fill((0, 0, 0))

    pre_player_x = player_x
    pre_player_y = player_y

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_RIGHT] and player_x < map_width - 2:
        player_x += 1
        player_direction = "right"

    elif pressed_keys[K_LEFT] and player_x > 0:
        player_x -= 1
        player_direction = "left"

    elif pressed_keys[K_UP] and player_y > 0:
        player_y -= 1
        player_direction = "up"

    elif pressed_keys[K_DOWN] and player_y < map_height - 2:
        player_y += 1
        player_direction = "down"

    if pressed_keys[K_RIGHT] or pressed_keys[K_LEFT] \
            or pressed_keys[K_UP] or pressed_keys[K_DOWN]:
        if player_scene == 0:
            player_scene = 1

    if pressed_keys[K_SPACE]:
        if objects_map[player_y][player_x] != "":
            if objects_map[player_y][player_x] in objects_cod_dic:
                selected_inventory_item = inventory_decod_dic[objects_cod_dic[objects_map[player_y][player_x]]]
            else:
                selected_inventory_item = inventory_decod_dic["nut"]
                nuts.remove(objects_map[player_y][player_x])
            if selected_inventory_item not in [inventory_decod_dic["pear"], inventory_decod_dic["meat"]]:
                inventory[inventory_cod_dic[selected_inventory_item]][1] += 1
                objects_map[player_y][player_x] = ""
            else:
                if health < 100:
                    health += 10
                else:
                    inventory[inventory_cod_dic[selected_inventory_item]][1] += 1
                objects_map[player_y][player_x] = ""
        if animal_map[player_y][player_x] != "":
            inventory_keys = list(inventory.keys())
            index = 0
            while inventory_keys[index] != animal_map[player_y][player_x].animal:
                index += 1
            selected_inventory_item = index
            inventory[animal_map[player_y][player_x].animal][1] += 1
            animal_map[player_y][player_x] = ""

        elif building_map[player_y][player_x] != "":
            for building in building_code_dic:
                if building == building_map[player_y][player_x]:
                    current_storage = building_code_dic[building]
                    in_shop = True

                    if current_storage == "farm":
                        season_type += 1
                        if season_type == 3:
                            season_type = 0

                        if season_type == 0:
                            tree_type = "norm_tree"
                            block_type = "grass"
                        elif season_type == 1:
                            tree_type = "autumn_tree"
                            block_type = "ground"
                        elif season_type == 2:
                            tree_type = "snow_tree"
                            block_type = "snow"

                        for y in range(0, map_height - 1):
                            for x in range(0, map_width - 1):
                                if blocks_map[y][x] != "":
                                    blocks_map[y][x] = blocks_decod_dic[block_type]
                                if scenery_map[y][x] != "":
                                    scenery_map[y][x] = scenery_decod_dic[tree_type]

                        player_images = {
                            "left": ["left0.png", "left1.png", "left2.png", "left3.png", "left4.png"],
                            "right": ["right0.png", "right1.png", "right2.png", "right3.png", "right4.png"],
                            "up": ["back0.png", "back1.png", "back2.png", "back3.png", "back4.png"],
                            "down": ["front0.png", "front1.png", "front2.png", "front3.png", "front4.png"]}

                        for direction in player_images:
                            index = 0
                            for stage in player_images[direction]:
                                player_images[direction][index] = str(season_type + 1) + \
                                                                  player_images[direction][index]
                                index += 1

                        health = 100
                        health_timer = 80

    if pressed_keys[K_BACKSPACE] and in_shop is True:
        current_storage = building_code_dic[building_map[player_y][player_x]]

        if current_storage == "shop":
            selected_shop_item += 1
            if selected_shop_item == len(shop):
                selected_shop_item = 0
        elif current_storage == "carpenter":
            selected_shop_item += 1
            if selected_shop_item >= len(carpenter):
                selected_shop_item = 0
        elif current_storage == "bank":
            pass
        elif current_storage == "trade":
            selected_shop_item += 1
            if selected_shop_item >= len(trade):
                selected_shop_item = 0
        elif current_storage == "well":
            pass

    if pressed_keys[K_TAB]:
        current_storage = "inventory"
        selected_inventory_item += 1
        if selected_inventory_item == len(inventory):
            selected_inventory_item = 0

    if pressed_keys[K_BACKSLASH] \
            and inventory[inventory_cod_dic[selected_inventory_item]][1] > 0 \
            and (objects_map[player_y][player_x] == "" or objects_map[player_y][player_x] in nuts) \
            and animal_map[player_y][player_x] == "":
        if objects_map[player_y][player_x] in nuts and inventory_cod_dic[selected_inventory_item] == "wateringcan":
            objects_map[player_y][player_x].grow()
            inventory[inventory_cod_dic[selected_inventory_item]][1] -= 1
        else:
            if objects_map[player_y][player_x] == "":
                inventory[inventory_cod_dic[selected_inventory_item]][1] -= 1
                if inventory_cod_dic[selected_inventory_item] in ["goat", "chick", "pig", "sheep"]:
                    animal_map[player_y][player_x] = Animal(player_x, player_y, animal_decod_dic[
                        inventory_cod_dic[selected_inventory_item]])
                else:
                    objects_map[player_y][player_x] = objects_decod_dic[
                        inventory_cod_dic[selected_inventory_item]]
                    if inventory_cod_dic[selected_inventory_item] == "nut":
                        objects_map[player_y][player_x] = Nut(player_x, player_y)
                        nuts.append(objects_map[player_y][player_x])

    if pressed_keys[K_RETURN]:
        if current_storage == "inventory" and \
                inventory[inventory_cod_dic[selected_inventory_item]][1] > 0 \
                and inventory_cod_dic[selected_inventory_item] in ["pear", "meat", "axe"]:
            if selected_inventory_item not in [inventory_decod_dic["pear"], inventory_decod_dic["meat"]]:
                inventory[inventory_cod_dic[selected_inventory_item]][2] = True
                inventory[inventory_cod_dic[selected_inventory_item]][1] -= 1
            else:
                if health < 100:
                    inventory[inventory_cod_dic[selected_inventory_item]][2] = True
                    inventory[inventory_cod_dic[selected_inventory_item]][1] -= 1
        elif current_storage == "shop" and in_shop is True:
            if shop[shop_cod_dic[selected_shop_item]][0] <= inventory["coin"][1]:
                inventory[shop_cod_dic[selected_shop_item]][1] += 1
                inventory["coin"][1] -= shop[shop_cod_dic[selected_shop_item]][0]

        elif current_storage == "carpenter" and in_shop is True:
            if carpenter[carpenter_cod_dic[selected_shop_item]][0] <= inventory["coin"][1] \
                    and carpenter[carpenter_cod_dic[selected_shop_item]][1] <= inventory["log"][1]:
                inventory["coin"][1] -= carpenter[carpenter_cod_dic[selected_shop_item]][0]
                inventory["log"][1] -= carpenter[carpenter_cod_dic[selected_shop_item]][1]
                inventory[carpenter_cod_dic[selected_shop_item]][1] += 1

        elif current_storage == "bank" and in_shop is True:
            selected_shop_item = 0
            inventory["coin"][1] += money_owed
            money_owed = 0
            money_timer = 100

        elif current_storage == "trade" and in_shop is True:
            if inventory[trade_cod_dic[selected_shop_item]][1] > 0:
                inventory["coin"][1] += trade[trade_cod_dic[selected_shop_item]][0]
                inventory[trade_cod_dic[selected_shop_item]][1] -= 1

        elif current_storage == "well" and in_shop is True:
            if inventory["coin"][1] > 0:
                selected_shop_item = 0
                inventory["wateringcan"][1] += 1
                inventory["coin"][1] -= 1

        elif current_storage == "farm" and in_shop is True:
            pass

    if blocks_map[player_y][player_x] == blocks_decod_dic["water"] \
            or scenery_map[player_y][player_x] != "":
        move_player_back = True

        if scenery_map[player_y][player_x] != "":
            if scenery_cod_dic[scenery_map[player_y][player_x]] == tree_type \
                    and inventory["axe"][2] is True:
                scenery_map[player_y][player_x] = ""
                objects_map[player_y][player_x] = objects_decod_dic["log"]
                chances = random.randint(1, 3)
                if chances == 2:
                    inventory["nut"][1] += 1

                if hammer_death == 0:
                    hammer_death = 3
                else:
                    hammer_death -= 1

                move_player_back = False

        if move_player_back == True:
            player_x = pre_player_x
            player_y = pre_player_y

    if player_x - pre_player_x > 0:
        if visible_width_index < map_width - visible_width_window:
            visible_width_index += 1
    if player_x - pre_player_x < 0:
        if visible_width_index > 0:
            visible_width_index -= 1
    if player_y - pre_player_y > 0:
        if visible_height_index < map_height - visible_height_window:
            visible_height_index += 1
    if player_y - pre_player_y < 0:
        if visible_height_index > 0:
            visible_height_index -= 1

    if (player_x, player_y) != (pre_player_x, pre_player_y) \
            and in_shop is True:
        in_shop = False
        current_storage = "inventory"

    if player_scene != 0:
        player_scene += 1
    if player_scene == len(player_images[player_direction]) - 1:
        player_scene = 0

    for item in inventory:
        if inventory[item][2] is True:
            if item == "axe":
                if hammer_death == 0:
                    inventory[item][2] = False
                    hammer_death = 3
            if item in ["pear", "meat"]:
                inventory[item][2] = False
                health += 10

    draw_map()
    draw_guide_lines()
    draw_inventory()
    draw_health()

    if in_shop is True:
        if current_storage == "shop":
            draw_shop()
        elif current_storage == "carpenter":
            draw_carpenter()
        elif current_storage == "bank":
            draw_bank()
        elif current_storage == "trade":
            draw_trade()
        elif current_storage == "well":
            draw_well()

    for y in range(0, len(animal_map)):
        for x in range(0, len(animal_map[0])):
            if animal_map[y][x] != "":
                animal_map[y][x].update()

    health_timer -= 1
    if health_timer == 0:
        health_timer = 80
        health -= 10

    if health <= 0:
        pygame.quit()
        exit()

    money_timer -= 1
    if money_timer == 0:
        money_owed += 1
        money_timer = 75

    if in_shop is False \
            and selected_shop_item > 0:
        selected_shop_item = 0

    print(player_x, player_y, visible_width_index, visible_height_index, "+", "0")

    pygame.time.delay(50)
    pygame.display.update()
