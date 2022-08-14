import pygame
from pygame.locals import *
from sys import exit

import random

# from animals import *
from basics import *

# from game_state import *

# window info

WIDTH = 1280
HEIGHT = 700

TILE = 40

mid_x_coord = (WIDTH / 2) - 9 * TILE
mid_y_coord = (HEIGHT / 2) - 6.5 * TILE

map_width = 30
map_height = 30

visible_width_index = 0
visible_width_window = 18

visible_height_index = 0
visible_height_window = 14

player_x, player_y = int(visible_width_window / 2) - 1, int(visible_height_window / 2) - 1

# images

main_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 3/"
img_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 3/images/"
sound_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 3/sounds/"

# init pygame

pygame.init()
my_screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.mixer.init()
pygame.mixer.music.load(sound_dir + "theme.wav")
pygame.mixer.music.play(-1)

money_owed = 10
money_timer = 100


# dics

class Animal:
    def __init__(self, x, y, animal):
        self.x = x
        self.y = y

        self.animal = animal_cod_dic[animal]

        self.timer = 0

        self.direction = "down"

    def move(self):
        if self.timer == 0:
            paths = [(self.x, self.y), (self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1),
                     (self.x, self.y + 1)]
            possible_paths = []
            for path in paths:
                if (1 <= path[0] <= map_width - 2) and (1 <= path[1] <= map_height - 2):
                    if (blocks_map[path[1]][path[0]] != 3) \
                            and (objects_map[path[1]][path[0]] == "") \
                            and (scenery_map[path[1]][path[0]] == "") \
                            and (animal_map[path[1]][path[0]] == ""):
                        possible_paths.append(path)

            if len(possible_paths) > 0:
                path_take = random.choice(possible_paths)
                animal = Animal(path_take[0], path_take[1], animal_decod_dic[self.animal])
                animal_map[self.y][self.x] = ""
                animal_map[path_take[1]][path_take[0]] = animal
                if (path_take[0] - self.x) > 0:
                    animal.direction = "right"
                elif path_take[0] - self.x < 0:
                    animal.direction = "left"
                elif path_take[1] - self.y > 0:
                    animal.direction = "down"
                elif path_take[1] - self.y < 0:
                    animal.direction = "up"
                else:
                    animal.direction = "down"

    def draw(self):
        draw_image(animal_images[self.animal][self.direction], mid_x_coord + self.x * TILE + TILE,
                   mid_y_coord + self.y * TILE,
                   img_dir, my_screen, 1)

    def update(self):
        self.timer += 1
        if self.timer == 10:
            self.timer = 0
        self.move()


animal_images = {0: {"down": "chick_front.png",
                     "up": "chick_back.png",
                     "right": "chick_right.png",
                     "left": "chick_right.png"},

                 1: {"down": "goat_front.png",
                     "up": "goat_back.png",
                     "right": "goat_right.png",
                     "left": "goat_left.png"},

                 2: {"down": "pig_front.png",
                     "up": "pig_back.png",
                     "right": "pig_right.png",
                     "left": "pig_left.png"},

                 3: {"down": "sheep_front.png",
                     "up": "sheep_back.png",
                     "right": "sheep_right.png",
                     "left": "sheep_left.png"}
                 }
animal_decod_dic = {"chick": 0,
                    "goat": 1,
                    "pig": 2,
                    "sheep": 3}
animal_cod_dic = {0: "chick",
                  1: "goat",
                  2: "pig",
                  3: "sheep"}

player_images = {"left": ["left_0.png", "left_1.png", "left_2.png", "left_3.png", "left_4.png"],
                 "right": ["right_0.png", "right_1.png", "right_2.png", "right_3.png", "right_4.png"],
                 "up": ["back_0.png", "back_1.png", "back_2.png", "back_3.png", "back_4.png"],
                 "down": ["front_0.png", "front_1.png", "front_2.png", "front_3.png", "front_4.png"]}
# player_images = {"left": ["wiz_left.png", "wiz_left.png"],
#                  "right": ["wiz_right.png", "wiz_right.png"],
#                  "up": ["wiz_back.png", "wiz_back.png"],
#                  "down": ["wiz_front.png", "wiz_front.png"]}
player_direction = "down"
player_scene = 0

blocks_img_dic = {0: "dirt.png",
                  1: "grass.png",
                  2: "stone.png",
                  3: "water.png",
                  4: "snow.png"}

blocks_decod_dic = {"dirt": 0,
                    "grass": 1,
                    "stone": 2,
                    "water": 3,
                    "snow": 4}

blocks_cod_dic = {0: "dirt",
                  1: "grass",
                  2: "stone",
                  3: "water",
                  4: "snow"}

scenery_img_dic = {0: "snow_tree.png"}
scenery_decod_dic = {"snow_tree": 0}
scenery_cod_dic = {0: "snow_tree"}

objects_img_dic = {0: "coin.png",
                   1: "hammer.png",
                   2: "log.png",
                   3: "meat.png",
                   4: "pear.png",
                   5: "fence.png"}

objects_decod_dic = {"coin": 0,
                     "hammer": 1,
                     "log": 2,
                     "meat": 3,
                     "pear": 4,
                     "fence": 5}

objects_cod_dic = {0: "coin",
                   1: "hammer",
                   2: "log",
                   3: "meat",
                   4: "pear",
                   5: "fence"}

building_img_dic = {0: "farm.png",
                    1: "shop.png",
                    2: "carpenter.png",
                    3: "trade.png",
                    4: "bank.png"}
building_decod_dic = {"farm": 0,
                      "shop": 1,
                      "carpenter": 2,
                      "trade": 3,
                      "bank": 4}
building_code_dic = {0: "farm",
                     1: "shop",
                     2: "carpenter",
                     3: "trade",
                     4: "bank"}

# map

blocks_map = []
for y in range(0, map_height - 1):
    blocks_map.append([])
    for x in range(0, map_width - 1):
        blocks_map[len(blocks_map) - 1].append(blocks_decod_dic["snow"])

building_map = []
for y in range(0, map_height - 1):
    building_map.append([])
    for x in range(0, map_width - 1):
        building_map[len(building_map) - 1].append("")

for _ in range(0, len(building_img_dic)):
    random_x, random_y = random.randint(0, map_width - 2), random.randint(0, map_height - 2)
    building_map[random_y][random_x] = _

scenery_map = []
for y in range(0, map_height - 1):
    scenery_map.append([])
    for x in range(0, map_width - 1):
        if (x == player_x and y == player_y) or \
                (building_map[y][x] != ""):
            scenery_map[len(scenery_map) - 1].append("")
        else:
            scenery_map[len(scenery_map) - 1].append(
                random.choice([scenery_decod_dic["snow_tree"], "", "", "", "", ""]))

objects_map = []
for y in range(0, map_height - 1):
    objects_map.append([])
    for x in range(0, map_width - 1):
        objects_map[len(objects_map) - 1].append(
            random.choice([objects_decod_dic["pear"], objects_decod_dic["pear"], objects_decod_dic["pear"],
                           objects_decod_dic["pear"], objects_decod_dic["pear"],
                           objects_decod_dic["log"], objects_decod_dic["log"],
                           objects_decod_dic["coin"], objects_decod_dic["coin"],
                           objects_decod_dic["hammer"],
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]))

        if (building_map[y][x] != "") \
                or (scenery_map[y][x] != ""):
            objects_map[len(objects_map) - 1].pop()
            objects_map[len(objects_map) - 1].append("")

animal_map = []
for y in range(map_width):
    animal_map.append([])
    for x in range(map_height):
        animal_map[len(animal_map) - 1].append("")

for _ in range(random.choice([random.randint(20, 60)])):
    random_x = random.randint(1, map_width - 2)
    random_y = random.randint(1, map_height - 2)

    while (blocks_map[random_y][random_x] == 3) \
            or (objects_map[random_y][random_x] != "") \
            or (scenery_map[random_y][random_x] != ""):
        random_x = random.randint(1, map_width - 2)
        random_y = random.randint(1, map_height - 2)

    animal_map[random_y][random_x] = Animal(random_x, random_y, random.randint(0, len(animal_images) - 1))

inventory = {  # name: [image, no., activated?]
    "coin": [objects_img_dic[objects_decod_dic["coin"]], 20, False],
    "hammer": [objects_img_dic[objects_decod_dic["hammer"]], 4, False],
    "log": [objects_img_dic[objects_decod_dic["log"]], 12, False],
    "meat": [objects_img_dic[objects_decod_dic["meat"]], 8, False],
    "pear": [objects_img_dic[objects_decod_dic["pear"]], 14, False],
    "fence": [objects_img_dic[objects_decod_dic["fence"]], 10, False],
    "chick": [animal_images[animal_decod_dic["chick"]]["down"], 2, False],
    "goat": [animal_images[animal_decod_dic["goat"]]["down"], 2, False],
    "pig": [animal_images[animal_decod_dic["pig"]]["down"], 2, False],
    "sheep": [animal_images[animal_decod_dic["sheep"]]["down"], 2, False]}
inventory_cod_dic = {0: "coin",
                     1: "hammer",
                     2: "log",
                     3: "meat",
                     4: "pear",
                     5: "fence",
                     6: "chick",
                     7: "goat",
                     8: "pig",
                     9: "sheep"}

inventory_decod_dic = {"coin": 0,
                       "hammer": 1,
                       "log": 2,
                       "meat": 3,
                       "pear": 4,
                       "fence": 5,
                       "chick": 6,
                       "goat": 7,
                       "pig": 8,
                       "sheep": 9}

selected_inventory_item = 0

current_storage = "inventory"

shop = {  # item: [(in coins), image]
    "log": [2, objects_img_dic[objects_decod_dic["log"]]],
    "meat": [2, objects_img_dic[objects_decod_dic["meat"]]],
    "pear": [2, objects_img_dic[objects_decod_dic["pear"]]]}
shop_cod_dic = {0: "log",
                1: "meat",
                2: "pear"}
shop_decod_dic = {"log": 0,
                  "meat": 1,
                  "pear": 2}

carpenter = {  # item: [(in coins), (in logs), image]
    "hammer": [1, 3, objects_img_dic[objects_decod_dic["hammer"]]],
    "fence": [1, 2, objects_img_dic[objects_decod_dic["fence"]]],
}
carpenter_cod_dic = {0: "hammer",
                     1: "fence"}
carpenter_decode_dic = {"hammer": 0,
                        "fence": 1}

trade = {  # item: [(in coins), image]
    "chick": [8, animal_images[animal_decod_dic["chick"]]["down"]],
    "sheep": [6, animal_images[animal_decod_dic["sheep"]]["down"]],
    "goat": [6, animal_images[animal_decod_dic["goat"]]["down"]],
    "pig": [10, animal_images[animal_decod_dic["pig"]]["down"]]}

trade_cod_dic = {0: "chick",
                 1: "sheep",
                 2: "goat",
                 3: "pig"}
trade_decod_dic = {"chick": 0,
                   "sheep": 1,
                   "goat": 2,
                   "pig": 3}

selected_shop_item = 0


# classes


# functions


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
                draw_image(objects_img_dic[objects_map[y][x]], mid_x_coord + (block_x + 1) * TILE,
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


run = True
hammer_death = 3
health = 100
health_timer = 80

in_shop = False

while run:
    my_screen.fill((0, 0, 0))

    pre_player_x = player_x
    pre_player_y = player_y

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT and player_x < map_width - 2:
                player_x += 1
                player_scene = 1
                player_direction = "right"

            if event.key == K_LEFT and player_x > 0:
                player_x -= 1
                player_scene = 1
                player_direction = "left"

            if event.key == K_UP and player_y > 0:
                player_y -= 1
                player_scene = 1
                player_direction = "up"

            if event.key == K_DOWN and player_y < map_height - 2:
                player_y += 1
                player_scene = 1
                player_direction = "down"

            if event.key == K_SPACE:
                if objects_map[player_y][player_x] != "":
                    selected_inventory_item = objects_map[player_y][player_x]
                    if selected_inventory_item not in [objects_decod_dic["pear"], objects_decod_dic["meat"]]:
                        inventory[objects_cod_dic[selected_inventory_item]][1] += 1
                        objects_map[player_y][player_x] = ""
                    else:
                        if health < 100:
                            health += 10
                        else:
                            inventory[objects_cod_dic[selected_inventory_item]][1] += 1
                        objects_map[player_y][player_x] = ""
                if animal_map[player_y][player_x] != "":
                    inventory[animal_map[player_y][player_x].animal][1] += 1
                    animal_map[player_y][player_x] = ""

                elif building_map[player_y][player_x] != "":
                    for building in building_code_dic:
                        if building == building_map[player_y][player_x]:
                            current_storage = building_code_dic[building]
                            in_shop = True

            if event.key == K_BACKSPACE and in_shop is True:
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

            if event.key == K_TAB:
                current_storage = "inventory"
                selected_inventory_item += 1
                if selected_inventory_item == len(inventory):
                    selected_inventory_item = 0

            if event.key == K_BACKSLASH \
                    and inventory[inventory_cod_dic[selected_inventory_item]][1] > 0 \
                    and objects_map[player_y][player_x] == "" \
                    and animal_map[player_y][player_x] == "":
                inventory[inventory_cod_dic[selected_inventory_item]][1] -= 1
                if inventory_cod_dic[selected_inventory_item] in ["goat", "chick", "pig", "sheep"]:
                    animal_map[player_y][player_x] = Animal(player_x, player_y, animal_decod_dic[
                        inventory_cod_dic[selected_inventory_item]])
                else:
                    objects_map[player_y][player_x] = selected_inventory_item

            if event.key == K_RETURN:
                if current_storage == "inventory" and \
                        inventory[objects_cod_dic[selected_inventory_item]][1] > 0 \
                        and objects_cod_dic[selected_inventory_item] in ["pear", "meat", "hammer"]:
                    if selected_inventory_item not in [objects_decod_dic["pear"], objects_decod_dic["meat"]]:
                        inventory[objects_cod_dic[selected_inventory_item]][2] = True
                        inventory[objects_cod_dic[selected_inventory_item]][1] -= 1
                    else:
                        if health < 100:
                            inventory[objects_cod_dic[selected_inventory_item]][2] = True
                            inventory[objects_cod_dic[selected_inventory_item]][1] -= 1
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

    if blocks_map[player_y][player_x] == blocks_decod_dic["water"] \
            or scenery_map[player_y][player_x] != "":
        move_player_back = True

        if scenery_map[player_y][player_x] != "":
            if scenery_cod_dic[scenery_map[player_y][player_x]] == "snow_tree" \
                    and inventory["hammer"][2] is True:
                scenery_map[player_y][player_x] = ""
                objects_map[player_y][player_x] = objects_decod_dic["log"]

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
            if item == "hammer":
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
        money_timer = 100

    if in_shop is False\
            and selected_shop_item > 0:
        selected_shop_item = 0


    pygame.time.delay(50)
    pygame.display.update()
