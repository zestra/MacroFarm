import pygame


def write_map_to_file(no, new_map, height, width, map_dir):
    file = open(map_dir + "Print out.txt", "a")

    for y in range(height):
        sentence = ""
        for x in range(width):
            sentence += f"{new_map[y][x]} "
        file.write(sentence + "\n")
    file.write("\n")
    file.close()


def read_map(button, map_dir):
    wanted_version = button.code
    begin_copying = False
    map = [[]]

    file = open(map_dir + "Print out.txt", "r")

    index = 0
    for line in file:
        if line == "\n" and begin_copying is False:
            index += 1

        if line == "\n" and begin_copying is True:
            begin_copying = False
            break

        if index == wanted_version:
            begin_copying = True

        if begin_copying:
            for character in line:
                if character == "\n":
                    map.append([])
                elif character != " ":
                    map[len(map) - 1].append(int(character))

    map.remove([])
    file.close()

    return map


def get_versions(upload_text, Button, mid_x, mid_y, my_screen, map_dir, img_dir):
    file = open(map_dir + "Print out.txt", "r")

    file_index = 0
    for line in file:
        if line == "\n":
            file_index += 1

    file.close()

    version_buttons = []
    for i in range(0, file_index):
        upload_text(f"Map {i}", img_dir, 25, "white", "Din Condensed")
        version_buttons.append(Button(f"Map {i}.png", mid_x + 245 + i * 60, mid_y - 35, img_dir, pygame.mouse, my_screen, 10, 1))
        version_buttons[len(version_buttons) - 1].code = i

    return version_buttons
