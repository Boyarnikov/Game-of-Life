import pygame
from typing import Tuple, Callable, Optional, List

from .interface_object import InterfaceObject

Vector2 = Tuple[int, int]
Color = Tuple[int, int, int]


class Polygon(InterfaceObject):
    _pointlist: List
    _color: Tuple[int, int, int] = (0, 0, 0)
    _width: int = 0
    _function: Callable[[], None] = lambda: None

    def __init__(self,
                 pointlist: List | None = None,
                 color: Color | None = None,
                 width: int | None = None,
                 func: Optional[Callable] = None):

        super().__init__()

        if pointlist:
            self.set_pointlist(pointlist)
        if color:
            self.set_color(color)
        if width:
            self.set_width(width)
        if func:
            self.set_function(func)

    def set_pointlist(self, pointlist: List):
        self._pointlist = pointlist

    def set_color(self, color: Tuple[int, int, int]):
        self._color = color

    def set_width(self, width: int):
        self._width = width

    def set_function(self, func: Callable[[], None]):
        self._function = func

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, self._color, self._pointlist, self._width)

