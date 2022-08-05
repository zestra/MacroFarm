import pygame
from pygame.locals import *
from sys import exit

from basics import *
from buttons import *
from writer import *
from variables import *


while run:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if quit_button.call():
                pygame.quit()
                exit()
                run = False

            for button in version_buttons:
                if button.call():
                    map = read_map(button, map_dir)

                    print(map, len(map), len(map[0]))

                    map_buttons = []
                    for y in range(height):
                        map_buttons.append([])
                        for x in range(width):
                            image = my_images[map[y][x]]
                            map_buttons[len(map_buttons) - 1].append(
                                Button(image, 75 + x * TILE_SIZE, 85 + y * TILE_SIZE, img_dir, pygame.mouse, main_screen))

                    break

            if print_button.call():
                new_map = []
                for row in map_buttons:
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

                write_map_to_file(file_index, new_map, height, width, map_dir)
                version_buttons = get_versions(upload_text, Button, mid_x, mid_y, main_screen, map_dir, img_dir)

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

            for row in map_buttons:
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
        main_screen.fill("black")

        for row in map_buttons:
            for button in row:
                button.draw()

        for button in version_buttons:
            button.draw()

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

        select_button.draw()
        print_button.draw()
        quit_button.draw()

        draw_image(my_images[index], mid_x + 480, mid_y + 30, img_dir, main_screen, 1)
        draw_image("selection.png", mid_x + 480, mid_y + 30, img_dir, main_screen, 1)
        draw_image("selection.png", mid_x + 315 + index * 55, mid_y + 100, img_dir, main_screen, 1)
        draw_image("upload_text.PNG", mid_x + 400, mid_y - 75, img_dir, main_screen, 1)

        draw_text("MINECRAFT", mid_x + 400, mid_y - 300, main_screen, 65)
        draw_text("THE ACTUAL ORIGINAL", mid_x + 400, mid_y - 225, main_screen, 35, "white", "DIN Condensed")
        draw_text("made by Czeslaw Herbert Zestra Tracz", mid_x + 400, mid_y - 190, main_screen, 15, "white",
                  "Noteworthy")
        draw_text(message, mid_x + 400, mid_y + 10, main_screen, 40)

        pygame.time.delay(100)
        pygame.display.update()
