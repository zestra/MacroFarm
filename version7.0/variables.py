from basics import *

## Map Information

map_width = 30
map_height = 30

visible_width_window = 19

visible_height_window = 15

player_x, player_y = int(map_width / 2) - 1, int(map_height / 2) - 1

visible_width_index = int(player_x / 2)
visible_height_index = int(player_y / 2)

## Resource Directory Information

main_dir = "/Users/czeslawtracz/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/MacroFarm/"
img_dir = "/Users/czeslawtracz/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/MacroFarm/images/"
sound_dir = "/Users/czeslawtracz/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/MacroFarm/sounds/"

## Initiating Pygame

WIDTH, HEIGHT = 1200

pygame.init()
my_window = pygame.display.set_mode((0, 0), FULLSCREEN)

WIDTH, HEIGHT = pygame.display.get_window_size()

## Graphic Coordination Information

TILE = 40

mid_x_coord = (WIDTH / 2) - 9 * TILE
mid_y_coord = (HEIGHT / 2) - 7.5 * TILE

## Scene Variables

in_action = False  # This tells us whether the player is playing or reading the guide.

health = 100  # This tracks the player's health.
health_timer = 80  # Every 80s, the player's health will go down by 10.

hammer_death = 3
# This tracks how many trees the active hammer can cut
# down. Once it cuts down 3 trees, it is used up.

money_owed = 10  # As the player works as a farmer, he earns money.
money_timer = 75  # Every 75s, the player will earn one more coin,
# which he can collect at the bank.

season_type = 0  # This tracks the scene.
# If it is 0, the scene is a forest.
# If it is 1, the scene is a desert.
# If it is 2, the scene is an arctic

tree_type = "norm_tree"  # This changes the tree type to match the season.
block_type = "grass"  # This also changes the block type to match the season.

run = True  # This checks if the game is still running.

## Specific Image Directories

# Animals

animal_images = {0: {"down": "chick_front.png",
                     "up": "chick_back.png",
                     "right": "chick_right.png",
                     "left": "chick_left.png"},

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
                     "left": "sheep_left.png"},

                 4: {"down": "snail_front.png",
                     "up": "snail_back.png",
                     "right": "snail_right.png",
                     "left": "snail_left.png"}}

animal_cod_dic = {0: "chick",
                  1: "goat",
                  2: "pig",
                  3: "sheep",
                  4: "snail"}

animal_decod_dic = reverse_dic(animal_cod_dic)

# Player

player_images = {"left": ["left0.png", "left1.png", "left2.png", "left3.png", "left4.png"],
                 "right": ["right0.png", "right1.png", "right2.png", "right3.png", "right4.png"],
                 "up": ["back0.png", "back1.png", "back2.png", "back3.png", "back4.png"],
                 "down": ["front0.png", "front1.png", "front2.png", "front3.png", "front4.png"]}

# This paragraph of code below edits each of the elements in the directory above, such that
# the images match with the scene. For example, if the scene is a forest, code 0, then the
# images all have 1 added on the front, to show that the image should represent a farmer in
# the forest. If the code were instead 1, then each image would have a 2 in front, representing
# a farmer in the desert.
for direction in player_images:
    index = 0
    for stage in player_images[direction]:
        player_images[direction][index] = str(season_type + 1) + player_images[direction][index]
        index += 1

player_direction = "down"
player_scene = 0

# Block Elements

blocks_img_dic = {0: "dirt.png",
                  1: "grass.png",
                  2: "stone.png",
                  3: "water.png",
                  4: "snow.png",
                  5: "ground.png"}

blocks_cod_dic = {0: "dirt",
                  1: "grass",
                  2: "stone",
                  3: "water",
                  4: "snow",
                  5: "ground"}

blocks_decod_dic = reverse_dic(blocks_cod_dic)

# Scenery / Trees

scenery_img_dic = {0: "norm_tree.png",
                   1: "snow_tree.png",
                   2: "autumn_tree.png",
                   3: "cherry_tree.png"}
scenery_cod_dic = {0: "norm_tree",
                   1: "snow_tree",
                   2: "autumn_tree",
                   3: "cherry_tree"}
scenery_decod_dic = reverse_dic(scenery_cod_dic)

# Objects / Items

objects_img_dic = {0: "coin.png",
                   1: "axe.png",
                   2: "log.png",
                   3: "meat.png",
                   4: "pear.png",
                   5: "fence.png",
                   6: "nut.png",
                   7: "wateringcan.png",
                   8: "cherry.png",
                   9: "shell.png"}

objects_cod_dic = {0: "coin",
                   1: "axe",
                   2: "log",
                   3: "meat",
                   4: "pear",
                   5: "fence",
                   6: "nut",
                   7: "wateringcan",
                   8: "cherry",
                   9: "shell"}

objects_decod_dic = reverse_dic(objects_cod_dic)

# Buildings

building_img_dic = {0: "farm.png",
                    1: "shop.png",
                    2: "carpenter.png",
                    3: "trade.png",
                    4: "bank.png",
                    5: "well.png",
                    6: "well.png",
                    7: "well.png",
                    8: "exit.png"}

building_code_dic = {0: "farm",
                     1: "shop",
                     2: "carpenter",
                     3: "trade",
                     4: "bank",
                     5: "well",
                     6: "well",
                     7: "well",
                     8: "exit"}

building_decod_dic = reverse_dic(building_code_dic)

## Maps

# Makes floor ground
blocks_map = []
for y in range(0, map_height - 1):
    blocks_map.append([])
    for x in range(0, map_width - 1):
        blocks_map[len(blocks_map) - 1].append(blocks_decod_dic[block_type])

# Inserts Buildings
building_map = []
for y in range(0, map_height - 1):
    building_map.append([])
    for x in range(0, map_width - 1):
        building_map[len(building_map) - 1].append("")

for _ in range(0, len(building_img_dic)):
    random_x, random_y = random.randint(0, map_width - 2), random.randint(0, map_height - 2)
    building_map[random_y][random_x] = _

# Create Trees
scenery_map = []
for y in range(0, map_height - 1):
    scenery_map.append([])
    for x in range(0, map_width - 1):
        # These conditions below make sure a tree doesn't land
        # on the character or inside a building.
        if (x == player_x and y == player_y) or \
                (building_map[y][x] != ""):
            scenery_map[len(scenery_map) - 1].append("")
        else:
            scenery_map[len(scenery_map) - 1].append(
                random.choice([scenery_decod_dic["norm_tree"], scenery_decod_dic["norm_tree"], scenery_decod_dic["norm_tree"], scenery_decod_dic["norm_tree"],
                               scenery_decod_dic["cherry_tree"],
                               "", "", "", "", "", "", "", "", "", "", ""]))

# Spreads items
objects_map = []
for y in range(0, map_height - 1):
    objects_map.append([])
    for x in range(0, map_width - 1):
        objects_map[len(objects_map) - 1].append(
            random.choice([objects_decod_dic["pear"], objects_decod_dic["pear"], objects_decod_dic["pear"],
                           objects_decod_dic["pear"], objects_decod_dic["pear"],
                           objects_decod_dic["log"], objects_decod_dic["log"],
                           objects_decod_dic["coin"], objects_decod_dic["coin"],
                           objects_decod_dic["axe"],
                           objects_decod_dic["wateringcan"],
                           objects_decod_dic["nut"],
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                           "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]))
        # Note: "" is an object which represents nothing,
        # and is there as a placeholder so the program doesn't crash.

        # The conditions below make sure that the items
        # do not land inside a building or on a tree.
        if (building_map[y][x] != "") \
                or (scenery_map[y][x] != ""):
            objects_map[len(objects_map) - 1].pop()
            objects_map[len(objects_map) - 1].append("")

nuts = []
# This is a special directory (above). Although nuts are items,
# they also have the special property of growing into a tree when
# given 2 buckets of water. So, they have their own seperate
# class with these features, and a special directory to track
# them.

for y in range(0, map_height - 1):
    for x in range(0, map_width - 1):
        if objects_map[y][x] == objects_decod_dic["nut"]:
            objects_map[y][x] = Nut(x, y)  # This is the special class, Nut.
            nuts.append(objects_map[y][x])

# Produce animals

animal_map = []
for y in range(map_width):
    animal_map.append([])
    for x in range(map_height):
        animal_map[len(animal_map) - 1].append("")

for _ in range(random.choice([random.randint(20, 60)])):
    random_x = random.randint(1, map_width - 2)
    random_y = random.randint(1, map_height - 2)

    # The conditions below, again, make sure that the animal
    # does not land on an item or inside a tree.
    while (objects_map[random_y][random_x] != "") \
            or (scenery_map[random_y][random_x] != ""):
        random_x = random.randint(1, map_width - 2)
        random_y = random.randint(1, map_height - 2)

    species = random.randint(0, len(animal_images) - 1)
    if species == animal_decod_dic["snail"]:
        animal_map[random_y][random_x] = IQ_Animal(random_x, random_y, species)
    else:
        animal_map[random_y][random_x] = Animal(random_x, random_y, species)
    # Animal is another special class. As animals, we have to
    # make them move, and we do this by making them their very
    # own class. This class takes in an animal's location and species.

## Inventory and Stores

current_storage = "inventory"
# This variable tracks which storage the player is
# currently using. For example, if you are active in
# the inventory or the shop.

in_shop = False
# This variable tells us whether we are in a store or
# not.

selected_inventory_item = 0
# This variable tracks what item you are selecting in
# the inventory. For example, are you selecting a
# pear, wateringcan, or goat?

selected_shop_item = 0
# This variable tracks what item you are selecting in
# a store, similar to the variable above.

# Inventory

inventory = {  # name: [image, no., activated?]
    "coin": [objects_img_dic[objects_decod_dic["coin"]], 20, False],
    "log": [objects_img_dic[objects_decod_dic["log"]], 12, False],
    "meat": [objects_img_dic[objects_decod_dic["meat"]], 70, False],
    "pear": [objects_img_dic[objects_decod_dic["pear"]], 14, False],
    "cherry": [objects_img_dic[objects_decod_dic["cherry"]], 10, False],
    "nut": [objects_img_dic[objects_decod_dic["nut"]], 2, False],
    "axe": [objects_img_dic[objects_decod_dic["axe"]], 4, False],
    "wateringcan": [objects_img_dic[objects_decod_dic["wateringcan"]], 6, False],
    "fence": [objects_img_dic[objects_decod_dic["fence"]], 10, False],
    "chick": [animal_images[animal_decod_dic["chick"]]["down"], 2, False],
    "goat": [animal_images[animal_decod_dic["goat"]]["down"], 2, False],
    "pig": [animal_images[animal_decod_dic["pig"]]["down"], 2, False],
    "sheep": [animal_images[animal_decod_dic["sheep"]]["down"], 2, False],
    "snail": [animal_images[animal_decod_dic["snail"]]["down"], 5, False],
    "shell": [objects_img_dic[objects_decod_dic["shell"]], 2, False]}
inventory_cod_dic = keys_dic(inventory)
inventory_decod_dic = reverse_dic(inventory_cod_dic)

# Shop

shop = {  # item: [(in coins), image]
    "log": [2, objects_img_dic[objects_decod_dic["log"]]],
    "meat": [1, objects_img_dic[objects_decod_dic["meat"]]],
    "pear": [2, objects_img_dic[objects_decod_dic["pear"]]],
    "cherry": [3, objects_img_dic[objects_decod_dic["cherry"]]],
    "nut": [2, objects_img_dic[objects_decod_dic["nut"]]]}
shop_cod_dic = keys_dic(shop)
shop_decod_dic = reverse_dic(shop_cod_dic)

# Carpenter

carpenter = {  # item: [(in coins), (in logs), image]
    "axe": [1, 1, objects_img_dic[objects_decod_dic["axe"]]],
    "fence": [1, 2, objects_img_dic[objects_decod_dic["fence"]]],
}
carpenter_cod_dic = keys_dic(carpenter)
carpenter_decode_dic = reverse_dic(carpenter_cod_dic)

# Trade

trade = {  # item: [(in coins), image]
    "chick": [8, animal_images[animal_decod_dic["chick"]]["down"]],
    "sheep": [6, animal_images[animal_decod_dic["sheep"]]["down"]],
    "goat": [6, animal_images[animal_decod_dic["goat"]]["down"]],
    "pig": [10, animal_images[animal_decod_dic["pig"]]["down"]]}

trade_cod_dic = keys_dic(trade)
trade_decod_dic = reverse_dic(trade_cod_dic)