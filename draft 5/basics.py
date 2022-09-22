import pygame
from pygame.locals import *


def draw_image(img, x, y, my_dir, my_screen, alter=0, alter2=0):
    if alter == 0:
        image = pygame.image.load(my_dir + img).convert()
    else:
        image = pygame.image.load(my_dir + img).convert_alpha()

    if alter == 0:
        image_x = x - image.get_width()/2
        image_y = y - image.get_height()/2
        my_screen.blit(image, (image_x, image_y))
    else:
        image_x = x - image.get_width()/2
        image_y = y - image.get_height()
        my_screen.blit(image, (image_x, image_y))


def draw_text(text, x, y, my_screen, my_size=25, my_color="white", my_font="Arial"):
    my_font = pygame.font.SysFont(my_font, my_size, False, False)
    text_surface = my_font.render(text, True, my_color)
    text_x = x - text_surface.get_width()/2
    my_screen.blit(text_surface, (text_x, y))


def upload_text(text, img_dir, my_size=25, my_color="white", my_font="Arial"):
    font = pygame.font.SysFont(my_font, my_size)
    surface = font.render(text, True, my_color)
    pygame.image.save(surface, img_dir + text + ".png")


def draw_rect(my_screen, x, y, width, height, color="white", fill=1, alter=1):
    if alter > 0:
        pygame.draw.rect(my_screen, color, Rect((x - (width/2), y - (height/2)), (width, height)), fill)
    else:
        pygame.draw.rect(my_screen, color, Rect((x, y), (width, height)), fill)

def keys_dic(dic):
    key_dic = {}
    index = 0
    for key in dic:
        key_dic[index] = key
        index += 1
    return key_dic


def reverse_dic(dic):
    reversed_dic = {}

    index = 0

    for value in dic.values():
        reversed_dic[value] = index
        index += 1
    return reversed_dic
