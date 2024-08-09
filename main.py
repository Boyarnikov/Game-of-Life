import pygame
import random
from interface.button import Button
from interface.label import Label
from interface.button_with_label import ButtonWithLabel
from interface import interface_object
import config
import layout

pygame.init()
screen = pygame.display.set_mode((1, 1))
clock = pygame.time.Clock()


def init_window():
    layout.create_game_layout()

    def change_size():
        layout.field.set_scale((random.randint(20, 100), random.randint(20, 100)))
        layout.field.randomize()
        layout.recalculate_layout()

    layout.random_button.set_function(change_size)


if __name__ == "__main__":
    init_window()

    # Главный цикл
    running = True
    while running:
        # обработка событий
        events = []
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                interface_object.handle_interface_objects_click(event)

        # отрисовка
        screen.fill((255, 255, 255))
        interface_object.draw_interface_objects(screen)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()
