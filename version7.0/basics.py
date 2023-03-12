import pygame
from pygame.locals import *

import math, random

def write(my_window, 
          passage, 
          my_size=25, my_colour="white", 
          my_font="Arial"):
    
    """This function draws given text passages onto the screen.
        It is more quick, efficient, neat, and compact 
        than drawing each sentence of the text individually."""

    pos_x = 0
    pos_y = 0

    for sentence in passage:
        for attribute in sentence:
            if attribute == "text":
                text = sentence["text"]
            if attribute == "size":
                my_size = sentence["size"]
            if attribute == "colour":
                my_colour = sentence["colour"]
            if attribute == "font":
                my_font = sentence["font"]
            if attribute == "code":
                for component in sentence["code"]:
                    if component[0:3] == "pos":
                        position = component[3:len(component)]
                        pos_x, pos_y = position.split(',')
                        pos_x, pos_y = float(pos_x), float(pos_y)
                    if component[0:3] == "par":
                        pos_y += 10

        draw_text(my_window, text, pos_x, pos_y, my_size, my_colour, my_font)
        pos_y += 20

    return pos_y


def draw_surface(my_screen,
               my_surface,
               x, y):

    """This function draws the given surface onto the screen."""

    x = x - (my_surface.get_width()/2)
    y = y - (my_surface.get_height()/2)

    my_screen.blit(my_surface, (x, y))


def draw_image(my_screen, filename, x, y, img_dir, transparent=True):

    """This function draws the given image onto the screen."""

    if transparent is False:
        image = pygame.image.load(img_dir + filename + ".png").convert()
    else:
        image = pygame.image.load(img_dir + filename + ".png").convert_alpha()

    image_x = x - image.get_width()/2
    image_y = y - image.get_height()/2

    my_screen.blit(image, (image_x, image_y))


def draw_text(my_screen, text, x, y, my_size=25, my_colour="white", my_font="Arial", margin="center"):

    """This function draws text, with the given characteristics, onto the screen."""

    my_font = pygame.font.SysFont(my_font, my_size, False, False)
    text_surface = my_font.render(text, True, my_colour)

    if margin == "center":
        text_x = x - text_surface.get_width()/2
    elif margin == "left":
        text_x = x

    my_screen.blit(text_surface, (text_x, y))


def text_to_image(text, img_dir, my_size=25, my_colour="white", my_font="Arial"):

    """This function converts a text, with the given properties, into an image, which can
    be found in the given image directory."""

    surface = text_to_surface(text, my_size, my_colour, my_font)
    pygame.image.save(surface, img_dir + text + ".png")


def text_to_surface(text, my_size=25, my_colour="white", my_font="Arial"):

    """This function converts a text, with the given properties, into a surface."""

    font = pygame.font.SysFont(my_font, my_size)
    surface = font.render(text, True, my_colour)
    return surface


def draw_rect(my_screen, x, y, width, height, color="white", filled_in=True, margin="center"):

    """This function draws a rectangle, with the given parameters, onto the screen."""

    if filled_in:
        filled_in = 0
    else:
        filled_in = 1
    
    if margin == "center":
        x -= width/2
    elif margin == "left":
        pass

    pygame.draw.rect(my_screen, color, Rect((x, y - (height/2)), (width, height)), filled_in)

def set_visibility(surface, percentage):
    surface.set_alpha(255*(percentage/100))

def draw_circle(my_window, x, y, radius, colour="white", filled_in=True):
    
    """This function draws a cicle, with the given parameters, onto the screen."""

    if filled_in:
        filled_in = 0
    else:
        filled_in = 1
    
    pygame.draw.circle(my_window, colour, (x, y), radius, filled_in)


def scale_surface(my_surface, dilated_x, dilated_y):

    """This function scales a given surface, by replacing its
     width and height parameters with the new ones given."""

    scaled_surface = pygame.transform.scale(my_surface, (dilated_x, dilated_y))
    return scaled_surface


def rotate_surface(my_surface, angle):

    """This function rotates a given surface by the given angle, in degrees."""

    rotated_surface = pygame.transform.rotate(my_surface, angle)
    return rotated_surface


def image_to_surface(filename, img_dir,
                     translucent=False):

    """This function converts an image into a surface."""

    if translucent is True:
        image_surface = pygame.image.load(img_dir + filename + ".png").convert_alpha()
    else:
        image_surface = pygame.image.load(img_dir + filename + ".png").convert()
    return image_surface

def surface_to_image(surface, filename, img_dir):
    pygame.image.save(surface, img_dir + filename + ".png")

def image_to_PIXAR_surface(filename, img_dir, transparent=(True, "white")):

    """This function converts an image into a surface without any interferences, 
    such as the image becoming completely blank or invisible, which unfortunately,
    the pygame's image-to-surface converter suffers from. It does so by first 
    finding the image with the given features and then converting it into a surface.
    Then, it creates another seperate surface, called a PIXAR surface, which I named
    myself. Basically, the function projects the colour of every pixel in the image-
    surface onto it's corresponding pixel on the PIXAR surface, hence its unique name.
    And guess what, this hack actually works! Pygame will now treat this image, which 
    is now in the form of a PIXAR surface, just like any other surface, hence eliminating
    any ununsual interferrences."""

    image_surface = image_to_surface(filename, img_dir, transparent[0])  # convert image into surface
    image_width, image_height = image_surface.get_size()

    PIXAR_surface = pygame.Surface((image_width, image_height))  # create new PIXAR surface
    for x in range(0, int(image_width)): # for pixel on image-surface...
        for y in range(0, int(image_height)):
            rgba_code = image_surface.get_at([x, y]) # collect corresponding colour of pixel...
            if rgba_code == (0, 0, 0, 0): # if colour is transparent, use given background colour...
                rgba_code = transparent[1]
            PIXAR_surface.set_at([x, y], rgba_code) # project colours to their corresponding pixels on the PIXAR surface
    
    return PIXAR_surface

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


def find_index(item, set):
    index = 0
    for object in set:
        if object == item:
            return index
        index += 1
    return None

def find_item(index, set):
    list = []
    for object in set:
        list.append(object)
    return list[index]