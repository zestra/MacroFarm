from buttons import *
from writer import *


# Directories

main_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 1/"
img_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 1/images/"
map_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 1/your maps/"


my_images = {0: "dirt_pixel.PNG",
             1: "grass_pixel.PNG",
             2: "stone_pixel.PNG",
             3: "water_pixel.PNG"}

# Windows information

WIDTH = 1280
HEIGHT = 700

TILE_SIZE = 40

mid_x = WIDTH / 2
mid_y = HEIGHT / 2

height = 14
width = 18

# Maps

map = []
for y in range(height):
    map.append([])
    for x in range(width):
        map[len(map) - 1].append(0)

# Screen Set up

pygame.init()
main_screen = pygame.display.set_mode((WIDTH, HEIGHT), NOFRAME)
current_window = main_screen

# Unique Buttons

select_button = Button("selection.png", mid_x, mid_y, img_dir, pygame.mouse, main_screen, 10, 1)
select_button.selected_button = None
print_button = Button("SAVE MAP.PNG", mid_x + 400, mid_y + 200, img_dir, pygame.mouse, main_screen, 10, 1)
quit_button = Button("QUIT.PNG", mid_x + 400, mid_y + 260, img_dir, pygame.mouse, main_screen, 10, 1)

version_buttons = get_versions(upload_text, Button, mid_x, mid_y, main_screen, map_dir, img_dir)

# Common Buttons

block_buttons = []
for i in range(0, len(my_images)):
    block_buttons.append(Button(my_images[i], mid_x + 315 + i * 55, mid_y + 100, img_dir, pygame.mouse, main_screen, 10))

map_buttons = []
for y in range(height):
    map_buttons.append([])
    for x in range(width):
        image = my_images[map[y][x]]
        map_buttons[len(map_buttons) - 1].append(
            Button(image, 75 + x * TILE_SIZE, 85 + y * TILE_SIZE, img_dir, pygame.mouse, main_screen))
select_button.selected_button = map_buttons[0][0]
select_button.x, select_button.y = select_button.selected_button.x, select_button.selected_button.y

# Other variables

message = "dirt"

run = True