import pygame
from typing import Tuple, Callable, Optional

from .interface_object import InterfaceObject

Vector2 = Tuple[int, int]
Color = Tuple[int, int, int]


class Line(InterfaceObject):
    _start_position: Tuple[int, int] = (0, 0)
    _end_position: Tuple[int, int] = (0, 0)
    _color: Tuple[int, int, int] = (0, 0, 0)
    _width: int = 1
    _function: Callable[[], None] = lambda: None

    def __init__(self,
                 start_position: Vector2 | None = None,
                 end_position: Vector2 | None = None,
                 color: Color | None = None,
                 width: int | None = None,
                 func: Optional[Callable] = None):

        super().__init__()

        if start_position:
            self.set_start_position(start_position)
        if end_position:
            self.set_end_position(end_position)
        if color:
            self.set_color(color)
        if width:
            self.set_width(width)
        if func:
            self.set_function(func)

    def set_start_position(self, start_position: Tuple[int, int]):
        self._start_position = start_position

    def set_end_position(self, end_position: Tuple[int, int]):
        self._end_position = end_position

    def set_color(self, color: Tuple[int, int, int]):
        self._color = color

    def set_function(self, func: Callable[[], None]):
        self._function = func

    def set_width(self, width: int):
        self._width = width

    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, self._color, self._start_position, self._end_position, self._width)

    '''def handle_click(self, event: pygame.event.Event):
        if not event.type == pygame.MOUSEBUTTONDOWN:
            return
        if not self._position[0] <= event.pos[0] <= self._position[0] + self._scale[0]:
            return
        if not self._position[1] <= event.pos[1] <= self._position[1] + self._scale[1]:
            return

        self._function()'''