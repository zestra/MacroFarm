from variables import *
from basics import *
from animals import *


def draw_shop(shop, selected_shop_item, selected_shop_deal,
              current_storage):
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


def draw_inventory_store(inventory, selected_inventory_item,
                         current_storage):
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


def draw_inventory(inventory, selected_inventory_item,
                   current_storage,
                   player_images, health):
    draw_inventory_store(inventory, selected_inventory_item,
                         current_storage)
    player_images = draw_health(health, player_images)

    return player_images


def manage_activated_items(inventory, shop,
                           player_direction, player_x, player_y, pre_player_x, pre_player_y,
                           blocks_map, objects_map, scenery_map, animal_map,
                           hammer_death, life_counter, run, pre_blocks, health):
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
                player_direction, player_x, player_y, shop, blocks_map, objects_map, scenery_map, health, hammer_death, life_counter, run, pre_blocks, animal_map = initialize(shop)
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
                        inventory[currency][1] += 5
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

    return inventory, shop, \
           player_direction, player_x, player_y, \
           blocks_map, objects_map, scenery_map, animal_map, \
           hammer_death, life_counter, run, pre_blocks, health


def draw_map(player_images, player_direction, player_x, player_y,
             blocks_map, objects_map, scenery_map, animal_map):

    for y in range(0, 14):
        for x in range(0, 18):
            if blocks_map[y][x] != "":
                draw_image(block_images[blocks_map[y][x]], mid_x_coord + (x + 1)*TILE, mid_y_coord + y*TILE, img_dir, my_screen)
            if animal_map[y][x] != "":
                animal_map[y][x].draw()
            if objects_map[y][x] != "":
                draw_image(objects_images[objects_map[y][x]], mid_x_coord + (x + 1) * TILE, mid_y_coord + y * TILE, img_dir, my_screen,
                           1)
            if scenery_map[y][x] != "":
                draw_image(scenery_images[scenery_map[y][x]], mid_x_coord + (x + 1)*TILE, mid_y_coord + y*TILE, img_dir, my_screen, 1, 1)
        if player_y == y:
            draw_image(player_images[player_direction], mid_x_coord + (player_x + 1)* TILE,
                       mid_y_coord + player_y * TILE, img_dir, my_screen, 1)


def update_animals(blocks_map, objects_map, scenery_map, animal_map):
    for y in range(0, 13):
        for x in range(0, 17):
            animal = animal_map[y][x]
            if animal != "":
                animal.update(blocks_map, objects_map, scenery_map, animal_map)


def update_main(inventory, selected_inventory_item,
                shop, selected_shop_item, selected_shop_deal,
                current_storage,
                player_direction, player_y, player_x, pre_player_x, pre_player_y,
                blocks_map, objects_map, scenery_map, animal_map,
                hammer_death, health):

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

    return inventory, selected_inventory_item, \
           shop, selected_shop_item, selected_shop_deal,\
           current_storage, \
           player_direction, player_y, player_x, pre_player_x, pre_player_y, \
           blocks_map, objects_map, scenery_map, animal_map, \
           hammer_death, health


def initialize(shop):
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
           shop, \
           blocks_map, objects_map, scenery_map, \
           health, hammer_death, life_counter, run, pre_blocks, \
           animal_map


def draw_window(inventory, selected_inventory_item,
                shop, selected_shop_deal, selected_shop_item,
                current_storage,
                player_images, player_direction, player_x, player_y,
                blocks_map, objects_map, scenery_map, animal_map,
                health):

    draw_map(player_images, player_direction, player_x, player_y,
             blocks_map, objects_map, scenery_map, animal_map)

    player_images = draw_inventory(inventory, selected_inventory_item,
                                   current_storage,
                                   player_images, health)

    draw_shop(shop, selected_shop_item, selected_shop_deal,
              current_storage)

    return player_images


def update_window(inventory, selected_inventory_item,
                  shop, selected_shop_item, selected_shop_deal,
                  current_storage,
                  player_direction, player_y, player_x, pre_player_x, pre_player_y,
                  animal_map, scenery_map, blocks_map, objects_map,
                  hammer_death, life_counter, run, pre_blocks, health):

    inventory, selected_inventory_item, \
        shop, selected_shop_item, selected_shop_deal, \
        current_storage, \
        player_direction, player_y, player_x, pre_player_x, pre_player_y, \
        blocks_map, objects_map, scenery_map, animal_map, \
        hammer_death, health = update_main(inventory, selected_inventory_item,
                                           shop, selected_shop_item, selected_shop_deal,
                                           current_storage,
                                           player_direction, player_y, player_x, pre_player_x, pre_player_y,
                                           blocks_map, objects_map, scenery_map, animal_map,
                                           hammer_death, health)

    update_animals(blocks_map, objects_map, scenery_map, animal_map)

    inventory, shop, \
        player_direction, player_x, player_y, \
        blocks_map, objects_map, scenery_map, animal_map, \
        hammer_death, life_counter, run, pre_blocks, health = manage_activated_items(inventory, shop,
                                                                                     player_direction, player_x, player_y, pre_player_x, pre_player_y,
                                                                                     blocks_map, objects_map, scenery_map, animal_map,
                                                                                     hammer_death, life_counter, run, pre_blocks, health)
    return inventory, selected_inventory_item, \
           shop, selected_shop_item, selected_shop_deal, \
           current_storage, \
           player_direction, player_x, player_y, pre_player_x, pre_player_y, \
           blocks_map, objects_map, animal_map, scenery_map, \
           hammer_death, life_counter, run, pre_blocks, health