import pygame
from typing import Tuple, Callable, Optional

from .interface_object import InterfaceObject

Vector2 = Tuple[int, int]
Color = Tuple[int, int, int]


class Button(InterfaceObject):
    _position: Tuple[int, int] = (0, 0)
    _scale: Tuple[int, int] = (30, 10)
    _color: Tuple[int, int, int] | "Color" = (0, 0, 0)
    _function: Callable[[], None] = lambda self: None

    def __init__(self,
                 position: Vector2 | None = None,
                 scale: Vector2 | None = None,
                 color: Color | None = None,
                 func: Optional[Callable] = None):

        super().__init__()

        if position:
            self.set_position(position)
        if scale:
            self.set_scale(scale)
        if color:
            self.set_color(color)
        if func:
            self.set_function(func)

    def set_position(self, position: Tuple[int, int]):
        self._position = position

    def set_scale(self, scale: Tuple[int, int]):
        self._scale = scale

    def set_color(self, color: Tuple[int, int, int]):
        self._color = color

    def set_function(self, func: Callable[[], None]):
        self._function = func

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self._color, pygame.Rect(*self._position, *self._scale))

    def handle_click(self, event: pygame.event.Event):
        if not event.type == pygame.MOUSEBUTTONDOWN:
            return
        if not self._position[0] <= event.pos[0] <= self._position[0] + self._scale[0]:
            return
        if not self._position[1] <= event.pos[1] <= self._position[1] + self._scale[1]:
            return

        self._function()
