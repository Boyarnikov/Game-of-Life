import pygame.draw

from .interface_object import InterfaceObject
import numpy as np
from typing import Tuple, Callable, Optional

Vector2 = Tuple[int, int]
Color = Tuple[int, int, int]


class Engine(InterfaceObject):
    _position: Tuple[int, int] = (0, 0)
    _cell_scale: Tuple[int, int] = (5, 5)
    _field = None
    _alive_color: Color
    _dead_color: Color
    __skip_steps = 30
    __current_step = 0

    def __init__(self, position: Vector2, scale: Vector2, cell_scale: Vector2, alive_color: Color, dead_color: Color):
        self._field = np.zeros(scale, dtype=int)
        self._position = position
        self._cell_scale = cell_scale
        self._alive_color = alive_color
        self._dead_color = dead_color
        super().__init__()

    def set_position(self, position: Tuple[int, int]):
        self._position = position

    def set_scale(self, scale: Vector2):
        self._field = np.zeros(scale, dtype=int)

    def randomize(self):
        self._field = np.random.randint(0, 2, self._field.shape)

    def get_scale(self):
        return self._field.shape

    def get_size(self):
        return self._field.shape[0] * self._cell_scale[0], self._field.shape[1] * self._cell_scale[1]

    def iterate(self):
        new_field = np.zeros(self._field.shape, dtype=int)
        for y in range(self._field.shape[1]):
            for x in range(self._field.shape[0]):
                total = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == dy == 0:
                            continue
                        total += self._field[(x+dx) % self._field.shape[0], (y+dy) % self._field.shape[1]]
                if self._field[x, y] == 1 and 2 <= total <= 3:
                    new_field[x, y] = 1
                elif self._field[x, y] == 0 and total == 3:
                    new_field[x, y] = 1
        self._field = new_field

    def draw(self, screen: pygame.Surface):
        self.__current_step += 1
        if self.__current_step >= self.__skip_steps:
            self.__current_step = 0
            self.iterate()


        for y in range(self._field.shape[1]):
            for x in range(self._field.shape[0]):
                color = self._alive_color
                if self._field[x, y] == 0:
                    color = self._dead_color

                pygame.draw.rect(screen, color,
                                 (self._position[0] + self._cell_scale[0] * x,
                                  self._position[1] + self._cell_scale[1] * y,
                                  *self._cell_scale)
                                 )
