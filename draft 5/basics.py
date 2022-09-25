import pygame
from pygame.locals import *


def draw_surface(window,
               my_surface,
               x, y,
               center_image=True):

    if center_image is True:
        x = x - (my_surface.get_width()/2)
        y = y - (my_surface.get_height()/2)

    window.blit(my_surface, (x, y))


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


def draw_text(text, x, y, my_screen, my_size=25, my_color="white", my_font="Arial", centered=True):
    my_font = pygame.font.SysFont(my_font, my_size, False, False)
    text_surface = my_font.render(text, True, my_color)
    if centered:
        text_x = x - text_surface.get_width()/2
    else:
        text_x = x
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


def scale_surface(my_surface, dilated_x, dilated_y, multiply=True):
    if multiply is True:
        scaled_surface = pygame.transform.scale(my_surface, (dilated_x*my_surface.get_width(), dilated_y*my_surface.get_height()))
    else:
        scaled_surface = pygame.transform.scale(my_surface, (dilated_x+my_surface.get_width(), dilated_y+my_surface.get_height()))
    return scaled_surface


def image_to_surface(image_filename, img_dir,
                     translucent=False):
    if translucent is True:
        image_surface = pygame.image.load(img_dir + image_filename).convert_alpha()
    else:
        image_surface = pygame.image.load(img_dir + image_filename).convert()
    return image_surface


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
