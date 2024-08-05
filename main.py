import pygame
import random
from interface.button import Button
from interface.label import Label
from interface import interface_object

pygame.init()
screen = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

running = True
color = (0, 0, 0)

drawables = []
clickable = []

button1 = Button((10, 10), (100, 40), (255, 100, 100), func=lambda: print("Я ПЕРВАЯ КНОПКА"))
button2 = Button((80, 60), (100, 40), (255, 100, 100))

label = Label(position=(10, 0), text="HELLO WORLD")

def button2_func():
    button2.set_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


button2.set_function(button2_func)

for i in interface_object.InterfaceObject.get_items():
    print(i)

while running:
    events = []
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            interface_object.handle_interface_objects_click(event)

    screen.fill((255, 255, 255))
    interface_object.draw_interface_objects(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
