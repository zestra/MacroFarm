import pygame
from pygame.locals import *
from sys import exit

main_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 1/"
img_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 1/images/"
map_dir = "/Users/zestra/PycharmProjects/Zestras-MineCraft/draft 1/your maps/"

from basics import *
from buttons import *

WIDTH = 1280
HEIGHT = 700

TILE_SIZE = 40

mid_x = WIDTH/2
mid_y = HEIGHT/2

pygame.init()
my_screen = pygame.display.set_mode((WIDTH, HEIGHT), NOFRAME)

select_button = Button("selection.png", mid_x, mid_y, img_dir, pygame.mouse, my_screen, 10, 1)
select_button.selected_button = None
print_button = Button("SAVE MAP.PNG", mid_x + 400, mid_y + 200, img_dir, pygame.mouse, my_screen, 10, 1)
upload_button = Button("upload_text.PNG", mid_x + 400, mid_y - 75, img_dir, pygame.mouse, my_screen, 10, 1)
quit_button = Button("QUIT.PNG", mid_x + 400, mid_y + 260, img_dir, pygame.mouse, my_screen, 10, 1)

my_images = {0: "dirt_pixel.PNG",
             1: "grass_pixel.PNG",
             2: "stone_pixel.PNG",
             3: "water_pixel.PNG"}

block_buttons = []
for i in range(0, len(my_images)):
    block_buttons.append(Button(my_images[i], mid_x + 315 + i * 55, mid_y + 100, img_dir, pygame.mouse, my_screen, 10))

height = 14
width = 18

map = []
for y in range(height):
    map.append([])
    for x in range(width):
        map[len(map) - 1].append(0)

buttons = []
for y in range(height):
    buttons.append([])
    for x in range(width):
        image = my_images[map[y][x]]
        buttons[len(buttons) - 1].append(Button(image, 75 + x * TILE_SIZE, 85 + y * TILE_SIZE, img_dir, pygame.mouse, my_screen))
select_button.selected_button = buttons[0][0]
select_button.x, select_button.y = select_button.selected_button.x, select_button.selected_button.y

map_buttons = []

message = "dirt"

run = True
while run:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if quit_button.call():
                pygame.quit()
                exit()
                run = False

            for button in map_buttons:
                if button.call():
                    wanted_version = button.text
                    begin_copying = False
                    map = [[]]

                    file = open(map_dir + "Print out.txt", "r")

                    for line in file:
                        if begin_copying and line == "\n":
                            begin_copying = False
                            break

                        elif begin_copying:
                            for character in line:
                                if character == "\n":
                                    map.append([])
                                elif character != " ":
                                    map[len(map) - 1].append(int(character))

                        if str(line) == str(wanted_version):
                            begin_copying = True


                    map.remove([])
                    file.close()

                    buttons = []
                    for y in range(height):
                        buttons.append([])
                        for x in range(width):
                            image = my_images[map[y][x]]
                            buttons[len(buttons) - 1].append(
                                Button(image, 75 + x * TILE_SIZE, 85 + y * TILE_SIZE, img_dir, pygame.mouse, my_screen))


            if upload_button.call():
                file = open(map_dir + "Print out.txt", "r")

                file_index = 0
                for line in file:
                    if line == "\n":
                        file_index += 1

                file.close()

                map_buttons = []
                for i in range(0, file_index):
                    upload_text(f"Map {i}", img_dir, 25, "white", "Din Condensed")
                    map_buttons.append(Button(f"Map {i}.png", mid_x + 245 + i*60, mid_y - 35, img_dir, pygame.mouse, my_screen, 10, 1))
                    map_buttons[len(map_buttons) - 1].text = f"Map {i} \n"

            if print_button.call():
                new_map = []
                for row in buttons:
                    new_map.append([])
                    for button in row:
                        for index in my_images:
                            if my_images[index] == button.img:
                                new_map[len(new_map) - 1].append(index)
                                break

                file = open(map_dir + "Print out.txt", "r")

                file_index = 0
                for line in file:
                    if line == "\n":
                        file_index += 1

                file.close()

                file = open(map_dir + "Print out.txt", "a")

                file.write(f"Map {file_index} \n")

                for y in range(height):
                    sentence = ""
                    for x in range(width):
                        sentence += f" {new_map[y][x]} "
                    file.write(sentence + "\n")
                file.write("\n")
                file.close()

            for button in block_buttons:
                if button.call():
                    select_button.selected_button.img = button.img

                    for index in my_images:
                        if my_images[index] == button.img:
                            if index == 0:
                                message = "dirt"
                            elif index == 1:
                                message = "grass"
                            elif index == 2:
                                message = "stone"
                            elif index == 3:
                                message = "water"

            for row in buttons:
                for button in row:
                    if button.call():
                        select_button.x, select_button.y = button.x, button.y
                        for index in my_images:
                            if my_images[index] == button.img:
                                select_button.selected_button = button
                                if index == 0:
                                    message = "dirt"
                                elif index == 1:
                                    message = "grass"
                                elif index == 2:
                                    message = "stone"
                                elif index == 3:
                                    message = "water"
                        break

    if run:
        my_screen.fill("black")

        draw_text("MINECRAFT", mid_x + 400, mid_y - 300, my_screen, 65)
        draw_text("THE ACTUAL ORIGINAL", mid_x + 400, mid_y - 225, my_screen, 35, "white", "DIN Condensed")
        draw_text("made by Czeslaw Herbert Zestra Tracz", mid_x + 400, mid_y - 190, my_screen, 15, "white", "Noteworthy")

        for row in buttons:
            for button in row:
                button.draw()

        for button in map_buttons:
            button.draw()

        select_button.draw()
        print_button.draw()
        upload_button.draw()
        quit_button.draw()

        draw_text(message, mid_x + 400, mid_y + 10, my_screen, 40)

        for button in block_buttons:
            button.draw()

        if message == "dirt":
            index = 0
        elif message == "grass":
            index = 1
        elif message == "stone":
            index = 2
        elif message == "water":
            index = 3

        draw_image(my_images[index], mid_x + 480, mid_y + 30, img_dir, my_screen, 1)
        draw_image("selection.png", mid_x + 480, mid_y + 30, img_dir, my_screen, 1)
        draw_image("selection.png", mid_x + 315 + index*55, mid_y + 100, img_dir, my_screen, 1)

        pygame.time.delay(100)
        pygame.display.update()