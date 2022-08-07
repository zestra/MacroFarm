import pygame
from pygame.locals import *

from basics import *

# This is the main code.


class Button:
    def __init__(self, img, x, y, my_dir, my_mouse, my_screen, strictness=0, alter=0):
        self.img = img
        self.x = x
        self.y = y

        self.pre_img = pygame.image.load(my_dir + img).convert()

        self.my_dir = my_dir
        self.my_mouse = my_mouse
        self.my_screen = my_screen

        self.alter = alter
        self.strictness = -strictness

    def call(self):
        my_mouse_x, my_mouse_y = self.my_mouse.get_pos()

        # This checks whether the mouse is within the button.
        if (self.x + self.strictness - self.pre_img.get_width() / 2 < my_mouse_x < self.x - self.strictness + self.pre_img.get_width()) \
                and (self.y + self.strictness - self.pre_img.get_height() / 2 < my_mouse_y < self.y - self.strictness + self.pre_img.get_height()):
            return True  # If the mouse is within the button, it calls the main function.
        else:
            return False

    def draw(self):
        # This draws the button onto the screen.
        draw_image(self.img, self.x, self.y, self.my_dir, self.my_screen, self.alter)
