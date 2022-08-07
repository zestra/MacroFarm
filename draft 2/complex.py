from variables import *
from basics import *


def draw_shop(current_storage, shop, selected_shop_item, selected_shop_deal):
    if current_storage == "shop":
        draw_rect(my_screen, WIDTH - mid_x_coord + 150 + 10, HEIGHT / 2, 250, 700, (28, 28, 28), 0)

    draw_text("SHOP", WIDTH - mid_x_coord + 150, mid_y_coord, my_screen, 45, "white", "din condensed")

    for _ in range(0, len(shop)):
        if _ == objects_dic["portal"]:
            continue
        else:
            draw_image(shop[objects_dic2[_]][3], WIDTH - 200 - 10, mid_y_coord + _ * (TILE + 40) + 120, img_dir,
                       my_screen, 1)
        draw_rect(my_screen, WIDTH - 240, mid_y_coord + _ * (TILE + 40) + 70, 240, 60, "white", 1, 0)
        draw_rect(my_screen, WIDTH - 240, mid_y_coord + _ * (TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(shop[objects_dic2[_]][0]), WIDTH - 240 + 60 + 30, mid_y_coord + _ * (TILE + 40) + 70 + 20,
                  my_screen, 25, "red", "DIN condensed")
        draw_rect(my_screen, WIDTH - 240 + 60, mid_y_coord + _ * (TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(shop[objects_dic2[_]][1]), WIDTH - 240 + 60 + 60 + 30, mid_y_coord + _ * (TILE + 40) + 70 + 20,
                  my_screen, 25, "red", "DIN condensed")
        draw_rect(my_screen, WIDTH - 240 + 60 + 60, mid_y_coord + _ * (TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(shop[objects_dic2[_]][2]), WIDTH - 240 + 60 + 60 + 60 + 30,
                  mid_y_coord + _ * (TILE + 40) + 70 + 20, my_screen, 25, "red", "DIN condensed")

    draw_image("selection.png", WIDTH - 210 + 60 * selected_shop_deal,
               mid_y_coord + selected_shop_item * (TILE + 40) + 130, img_dir, my_screen, 1)


def draw_inventory_store(current_storage, inventory, selected_inventory_item):
    if current_storage == "inventory":
        draw_rect(my_screen, mid_x_coord - 150 + 10, HEIGHT/2, 275, 700, (28, 28, 28), 0)

    draw_text("INVENTORY", mid_x_coord - 150, mid_y_coord, my_screen, 45, "white", "din condensed")

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


def draw_health(health, player_images):
    if health <= 30:
        player_images = {"left": "wiz_left2.png",
                         "right": "wiz_right2.png",
                         "up": "wiz_back2.png",
                         "down": "wiz_front2.png"}
    else:
        player_images = {"left": "wiz_left.png",
                         "right": "wiz_right.png",
                         "up": "wiz_back.png",
                         "down": "wiz_front.png"}

    lower_y = 60
    further_x = 20

    draw_text("health bar", mid_x_coord - 200 + further_x, mid_y_coord + lower_y, my_screen, 20, "white", "arial")
    draw_rect(my_screen, mid_x_coord - 140 + further_x, mid_y_coord + lower_y, 100, 20, "white", 0, 0)
    if health > 30:
        draw_rect(my_screen, mid_x_coord - 140 + further_x, mid_y_coord + lower_y, health, 20, "green", 0, 0)
    else:
        draw_rect(my_screen, mid_x_coord - 140 + further_x, mid_y_coord + lower_y, health, 20, "red", 0, 0)
    draw_text(str(health) + "%", mid_x_coord - 120 + further_x, mid_y_coord + 5 + lower_y, my_screen, 10, "black", "arial")

    return player_images


def draw_inventory(current_storage, inventory, selected_inventory_item, health, player_images):
    draw_inventory_store(current_storage, inventory, selected_inventory_item)
    player_images = draw_health(health, player_images)

    return player_images


def manage_activated_items(inventory, health, player_direction, player_x, player_y, shop, blocks_map, objects_map, scenery_map, hammer_death, life_counter, run, pre_blocks, pre_player_x, pre_player_y, initialize):
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

        elif item == "treasure":
            if inventory[item][2] is True:
                benefit = random.choice([True, False])
                if benefit is True:
                    major = random.choice([True, False])
                    if major is False:
                        for item2 in inventory:
                            if item2 not in ["boat", "portal", "treasure"]:
                                inventory[item2][1] += 5
                            currency = random.choice(["coin", "log"])
                            inventory[currency][1] += 10
                    elif major is True:
                        item2 = random.choice(["boat", "treasure", "portal"])
                        if item2 != "treasure":
                            inventory[item2][1] += 1
                        else:
                            inventory[item2][1] += random.randint(0, 3)
                elif benefit is False:
                    major = random.choice([True, False])
                    if major is False:
                        for item2 in inventory:
                            if item2 not in ["boat", "portal", "treasure"]\
                                    and inventory[item2][1] > 5:
                                inventory[item2][1] -= 5
                            currency = random.choice(["coin", "log"])
                            if inventory[currency][1] > 10:
                                inventory[currency][1] -= 10
                            else:
                                inventory[currency][1] = 0
                    elif major is True:
                        dehealth = random.randint(10, 25)
                        if health > dehealth:
                            health -= dehealth
                        else:
                            health = 0

                        deboat = random.randint(1, 3)

                        if inventory["boat"][1] > deboat:
                            inventory["boat"][1] -= deboat
                        else:
                            inventory["boat"][1] = 0

                        if inventory["portal"][1] > 0:
                            inventory["portal"][1] = 0
            inventory[item][2] = False

    return inventory, health, player_direction, player_x, player_y, shop, blocks_map, objects_map, scenery_map, hammer_death, life_counter, run, pre_blocks


def draw_map(blocks_map, objects_map, scenery_map, player_images, player_direction, player_x, player_y):
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
