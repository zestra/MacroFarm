from basics import *
from variables import *


def draw_map():
    block_y = 0
    for y in range(visible_height_index, visible_height_index + visible_height_window - 1):
        block_x = 0

        for x in range(visible_width_index, visible_width_index + visible_width_window - 1):
            draw_image(blocks_img_dic[blocks_map[y][x]], mid_x_coord + (block_x + 1) * TILE,
                       mid_y_coord + (block_y + 1) * TILE,
                       img_dir, my_screen)

            block_x += 1
        block_y += 1

    block_y = 0
    for y in range(visible_height_index, visible_height_index + visible_height_window - 1):
        block_x = 0

        for x in range(visible_width_index, visible_width_index + visible_width_window - 1):

            if objects_map[y][x] != "":
                if objects_map[y][x] in objects_cod_dic:
                    draw_image(objects_img_dic[objects_map[y][x]], mid_x_coord + (block_x + 1) * TILE,
                               mid_y_coord + (block_y + 1) * TILE, img_dir, my_screen, 1)
                else:
                    draw_image(objects_img_dic[objects_decod_dic["nut"]], mid_x_coord + (block_x + 1) * TILE,
                               mid_y_coord + (block_y + 1) * TILE, img_dir, my_screen, 1)

            if building_map[y][x] != "":
                draw_image(building_img_dic[building_map[y][x]], mid_x_coord + (block_x + 1) * TILE,
                           mid_y_coord + (block_y + 1) * TILE, img_dir, my_screen, 1)

            if scenery_map[y][x] != "":
                draw_image(scenery_img_dic[scenery_map[y][x]], mid_x_coord + (block_x + 1) * TILE,
                           mid_y_coord + (block_y + 1) * TILE, img_dir, my_screen, 1)

            if animal_map[y][x] != "":
                draw_image(animal_images[animal_decod_dic[animal_map[y][x].animal]][animal_map[y][x].direction],
                           mid_x_coord + (block_x + 1) * TILE,
                           mid_y_coord + (block_y + 1) * TILE, img_dir, my_screen, 1)
            block_x += 1

        if y == player_y:
            print(player_x, player_y, visible_width_index, visible_height_index, "+", "1")
            draw_image(player_images[player_direction][player_scene - 1],
                       mid_x_coord + (player_x - visible_width_index + 1) * TILE,
                       mid_y_coord + (player_y - visible_height_index + 1) * TILE, img_dir, my_screen, 1)

        block_y += 1


def draw_guide_lines():
    block_y = 0
    for y in range(visible_height_index, visible_height_index + visible_height_window - 1):
        draw_text(str(y), mid_x_coord - 10, mid_y_coord + (block_y + 0.6) * TILE, my_screen, 25, "green",
                  "Din Condensed")
        block_y += 1

    block_x = 0
    for x in range(visible_width_index, visible_width_index + visible_width_window - 1):
        draw_text(str(x), mid_x_coord + (block_x + 1) * TILE, mid_y_coord + (visible_height_window) * TILE - 10,
                  my_screen, 25, "green", "Din Condensed")
        block_x += 1


def draw_inventory():
    if current_storage == "inventory":
        draw_rect(my_screen, mid_x_coord - 150 + 10 - 25, HEIGHT / 2, 275, 700, (28, 28, 28), 0)

    draw_text("INVENTORY", mid_x_coord - 150 - 25, mid_y_coord, my_screen, 45, "white", "din condensed")

    lower_y = 50
    index_max = 3
    index = 0
    for y in range(0, len(inventory)):
        if inventory[inventory_cod_dic[y]][2] is True:
            draw_image("highlight.png", 2 * TILE - 25 + index * (TILE + 40),
                       mid_y_coord + (y - index) * (TILE + (40 / (index_max ** 2))) + 90 + lower_y, img_dir, my_screen,
                       0, 0)
        draw_image(inventory[inventory_cod_dic[y]][0], 2 * TILE - 10 - 25 + index * (TILE + 40),
                   mid_y_coord + (y - index) * (TILE + (40 / (index_max ** 2))) + 110 + lower_y, img_dir, my_screen,
                   1)
        draw_text(str(inventory[inventory_cod_dic[y]][1]), 2 * TILE + 20 - 25 + index * (TILE + 40),
                  mid_y_coord + (y - index) * (TILE + (40 / (index_max ** 2))) + 70 + lower_y, my_screen, 20, "red",
                  "DIN condensed")
        draw_rect(my_screen, 2 * TILE - 25 + index * (TILE + 40),
                  mid_y_coord + (y - index) * (TILE + (40 / (index_max ** 2))) + 90 + lower_y, 60, 60)
        if y == selected_inventory_item:
            draw_image("selection.png", 2 * TILE - 25 + index * (TILE + 40),
                       mid_y_coord + (y - index) * (TILE + (40 / (index_max ** 2))) + 120 + lower_y, img_dir, my_screen,
                       1, 1)

        index += 1
        if index == index_max:
            index = 0


def draw_health():
    lower_y = 60
    further_x = 20

    draw_text("health bar", mid_x_coord - 200 - 25 + further_x, mid_y_coord + lower_y, my_screen, 20, "white", "arial")
    draw_rect(my_screen, mid_x_coord - 140 - 25 + further_x, mid_y_coord + lower_y, 100, 20, "white", 0, 0)
    if health > 30:
        draw_rect(my_screen, mid_x_coord - 140 - 25 + further_x, mid_y_coord + lower_y, health, 20, "green", 0, 0)
    else:
        draw_rect(my_screen, mid_x_coord - 140 - 25 + further_x, mid_y_coord + lower_y, health, 20, "red", 0, 0)
    draw_text(str(health) + "%", mid_x_coord - 120 - 25 + further_x, mid_y_coord + 5 + lower_y, my_screen, 10, "black",
              "arial")


def draw_shop():
    if current_storage == "shop":
        draw_rect(my_screen, WIDTH - mid_x_coord + 150 + 10, HEIGHT / 2, 250, 700, (28, 28, 28), 0)

    draw_text("SHOP", WIDTH - mid_x_coord + 150, mid_y_coord, my_screen, 45, "white", "din condensed")

    for _ in range(0, len(shop)):
        draw_image(shop[shop_cod_dic[_]][1], WIDTH - 200 - 10 + 20 + 30, mid_y_coord + _ * (TILE + 40) + 120, img_dir,
                   my_screen, 1)
        draw_rect(my_screen, WIDTH - 240 + 20 + 30, mid_y_coord + _ * (TILE + 40) + 70, 120, 60, "white", 1, 0)
        draw_rect(my_screen, WIDTH - 240 + 20 + 30, mid_y_coord + _ * (TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(shop[shop_cod_dic[_]][0]), WIDTH - 240 + 60 + 30 + 20 + 30,
                  mid_y_coord + _ * (TILE + 40) + 70 + 20,
                  my_screen, 25, "red", "DIN condensed")
    draw_image("selection.png", WIDTH - 210 + 60 + 20 + 30,
               mid_y_coord + selected_shop_item * (TILE + 40) + 130, img_dir, my_screen, 1)


def draw_carpenter():
    if current_storage == "carpenter":
        draw_rect(my_screen, WIDTH - mid_x_coord + 150 + 10, HEIGHT / 2, 250, 700, (28, 28, 28), 0)

    draw_text("CARPENTER", WIDTH - mid_x_coord + 150, mid_y_coord, my_screen, 45, "white", "din condensed")

    draw_rect(my_screen,
              WIDTH - 300 + 120 + 20,
              mid_y_coord + selected_shop_item * (TILE + 40) + 70,
              120, 60,
              "blue", 0, 0)
    draw_rect(my_screen,
              WIDTH - 300 + 120 + 20,
              mid_y_coord + selected_shop_item * (TILE + 40) + 70,
              120, 60,
              "cyan", 3, 0)

    for _ in range(0, len(carpenter)):
        draw_image(carpenter[carpenter_cod_dic[_]][2], WIDTH - 200 - 10 + 20, mid_y_coord + _ * (TILE + 40) + 120,
                   img_dir,
                   my_screen, 1)
        draw_rect(my_screen, WIDTH - 240 + 20, mid_y_coord + _ * (TILE + 40) + 70, 180, 60, "white", 1, 0)
        draw_rect(my_screen, WIDTH - 240 + 20, mid_y_coord + _ * (TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(carpenter[carpenter_cod_dic[_]][0]), WIDTH - 240 + 60 + 30 + 20,
                  mid_y_coord + _ * (TILE + 40) + 70 + 20,
                  my_screen, 25, "red", "DIN condensed")
        draw_rect(my_screen, WIDTH - 240 + 60 + 60 + 20, mid_y_coord + _ * (TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(carpenter[carpenter_cod_dic[_]][1]), WIDTH - 240 + 60 + 60 + 30 + 20,
                  mid_y_coord + _ * (TILE + 40) + 70 + 20, my_screen, 25, "red", "DIN condensed")

    draw_text("in",
              WIDTH - 240 + 20 + 60,
              mid_y_coord + 510 + 45,
              my_screen,
              20, "white", "arial")

    draw_image(objects_img_dic[objects_decod_dic["coin"]],
               WIDTH - 240 + 20 + 30 + 60,
               mid_y_coord + 510 + 70,
               img_dir, my_screen, 1, 0)

    draw_text("in",
              WIDTH - 240 + 20 + 60 + 60 + 20,
              mid_y_coord + 510 + 45,
              my_screen,
              20, "white", "arial")

    draw_image(objects_img_dic[objects_decod_dic["log"]],
               WIDTH - 240 + 20 + 30 + 60 + 60 + 20,
               mid_y_coord + 510 + 70,
               img_dir, my_screen, 1, 0)


def draw_bank():
    if current_storage == "bank":
        draw_rect(my_screen, WIDTH - mid_x_coord + 150 + 10, HEIGHT / 2, 250, 700, (28, 28, 28), 0)

    draw_text("BANK", WIDTH - mid_x_coord + 150, mid_y_coord, my_screen, 45, "white", "din condensed")

    draw_rect(my_screen, WIDTH - mid_x_coord + 150, mid_y_coord + TILE + 75, 175, 80, "blue", 3)
    draw_text("Collect", WIDTH - mid_x_coord + 150, mid_y_coord + TILE + 40, my_screen)
    draw_text("Earned Money", WIDTH - mid_x_coord + 150, mid_y_coord + TILE + 65, my_screen)
    draw_text(str(money_owed), WIDTH - mid_x_coord + 150, mid_y_coord + TILE + 90, my_screen)


def draw_trade():
    if current_storage == "trade":
        draw_rect(my_screen, WIDTH - mid_x_coord + 150 + 10, HEIGHT / 2, 250, 700, (28, 28, 28), 0)

    draw_text("TRADE", WIDTH - mid_x_coord + 150, mid_y_coord, my_screen, 45, "white", "din condensed")

    for _ in range(0, len(trade)):
        draw_image(trade[trade_cod_dic[_]][1], WIDTH - 200 - 10 + 20 + 30, mid_y_coord + _ * (TILE + 40) + 120, img_dir,
                   my_screen, 1)
        draw_rect(my_screen, WIDTH - 240 + 20 + 30, mid_y_coord + _ * (TILE + 40) + 70, 120, 60, "white", 1, 0)
        draw_rect(my_screen, WIDTH - 240 + 20 + 30, mid_y_coord + _ * (TILE + 40) + 70, 60, 60, "white", 1, 0)
        draw_text(str(trade[trade_cod_dic[_]][0]), WIDTH - 240 + 60 + 30 + 20 + 30,
                  mid_y_coord + _ * (TILE + 40) + 70 + 20,
                  my_screen, 25, "red", "DIN condensed")
    draw_image("selection.png", WIDTH - 210 + 60 + 20 + 30,
               mid_y_coord + selected_shop_item * (TILE + 40) + 130, img_dir, my_screen, 1)


def draw_well():
    if current_storage == "well":
        draw_rect(my_screen, WIDTH - mid_x_coord + 150 + 10, HEIGHT / 2, 250, 700, (28, 28, 28), 0)

    draw_text("WELL", WIDTH - mid_x_coord + 150, mid_y_coord, my_screen, 45, "white", "din condensed")

    draw_image(objects_img_dic[objects_decod_dic["wateringcan"]], WIDTH - 200 - 10 + 20 + 30,
               mid_y_coord + 0 * (TILE + 40) + 120, img_dir,
               my_screen, 1)
    draw_rect(my_screen, WIDTH - 240 + 20 + 30, mid_y_coord + 0 * (TILE + 40) + 70, 120, 60, "white", 1, 0)
    draw_rect(my_screen, WIDTH - 240 + 20 + 30, mid_y_coord + 0 * (TILE + 40) + 70, 60, 60, "white", 1, 0)
    draw_text("1", WIDTH - 240 + 60 + 30 + 20 + 30,
              mid_y_coord + 0 * (TILE + 40) + 70 + 20,
              my_screen, 25, "red", "DIN condensed")
    draw_image("selection.png", WIDTH - 210 + 60 + 20 + 30,
               mid_y_coord + selected_shop_item * (TILE + 40) + 130, img_dir, my_screen, 1)
