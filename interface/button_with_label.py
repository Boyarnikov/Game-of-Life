import pygame
from typing import Tuple, Callable, Optional

from .interface_object import InterfaceObject
from .button import Button
from .label import Label

Vector2 = Tuple[int, int]
Color = Tuple[int, int, int]


class ButtonWithLabel(InterfaceObject):
    _button: Button = None
    _label: Label = None

    def __init__(self,
                 position: Vector2 | None = None,
                 scale: Vector2 | None = None,
                 color: Color | None = None,
                 label_color: Color | None = None,
                 func: Optional[Callable] = None,
                 text: str = ""):
        super().__init__()
        self._button = Button(position, scale, color, func)
        self._label = Label(position, label_color, text)
