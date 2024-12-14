import pygame
import random
from interface.button import Button
from interface.engine import Engine
from interface.label import Label
from interface.button_with_label import ButtonWithLabel
from interface import interface_object
import config

field = Engine((0, 0), config.FIELD_SIZE, config.CELL_SIZE_PX, config.RED, config.BLUE, True)
random_button = Button()
start_stop_button = Button()


def create_game_layout():
    recalculate_layout()


def recalculate_layout():
    field_width, field_height = field.get_size()

    window_width = max(config.SMALLEST_WINDOW_SIZE[0], config.DEFAULT_BORDER_SIZE_PX * 2 + field_width)
    window_height = max(config.SMALLEST_WINDOW_SIZE[1],
                        config.DEFAULT_BORDER_SIZE_PX * 3 + field_height + config.DEFAULT_BUTTON_SIZE[1])

    pygame.display.set_mode((window_width, window_height))

    field.set_position((window_width / 2 - field_width / 2, config.DEFAULT_BORDER_SIZE_PX))

    random_button.set_position((window_width / 2 - config.DEFAULT_BORDER_SIZE_PX - config.DEFAULT_BUTTON_SIZE[0],
                                field_height + config.DEFAULT_BORDER_SIZE_PX * 2))
    random_button.set_scale(config.DEFAULT_BUTTON_SIZE)

    start_stop_button.set_position(
        (window_width / 2 + config.DEFAULT_BORDER_SIZE_PX, field_height + config.DEFAULT_BORDER_SIZE_PX * 2))
    start_stop_button.set_scale(config.DEFAULT_BUTTON_SIZE)
