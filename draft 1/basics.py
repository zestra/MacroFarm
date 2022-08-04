import pygame
from pygame.locals import *


def draw_image(img, x, y, my_dir, my_screen, alter=0):
    if alter == 0:
        image = pygame.image.load(my_dir + img).convert()
    else:
        image = pygame.image.load(my_dir + img).convert_alpha()
    image_x = x - image.get_width()/2
    image_y = y - image.get_height()/2
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