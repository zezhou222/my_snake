import random
import pygame as pg

from settings import (
    width,
    height,
    lattice_size,
    red_image
)


class Point(object):

    def __init__(self):
        self.point = pg.image.load(red_image)

        self.width = lattice_size
        self.height = lattice_size

        self.x_list = range(0, width + lattice_size-lattice_size, lattice_size)
        self.y_list = range(0, height + lattice_size-lattice_size, lattice_size)

        self.x = self.x_list[random.randint(0, len(self.x_list)-1)]
        self.y = self.y_list[random.randint(0, len(self.y_list)-1)]

    def return_surface(self):
        return self.point

    def init_position(self):
        self.x = self.x_list[random.randint(0, len(self.x_list)-1)]
        self.y = self.y_list[random.randint(0, len(self.y_list)-1)]

    def draw(self, screen):
        rect = pg.draw.rect(screen, (193, 35, 238), [self.x, self.y, self.width, self.height])
        return rect
