import pygame
import random

from Display import Display

from Bug import Bug
from Food import Food
from Queen import Queen

pygame.init()


def init_objects(objects):
    bugs = pygame.sprite.Group()
    for i in range(30):
        bugs.add(Bug(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                     random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD)))

    objects["bugs"] = bugs

    queens = pygame.sprite.Group()
    queens.add(Queen(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                     random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD)))

    objects["queens"] = queens

    food = pygame.sprite.Group()
    for i in range(1):
        food.add(Food(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                      random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD)))

    objects["food"] = food


def update(objects):
    objects["bugs"].update("move", objects["food"], objects["queens"])
    objects["bugs"].update("hear")


def run():
    display = Display()
    objects = {}

    init_objects(objects)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update(objects)
        display.render(objects)

    pygame.quit()


if __name__ == '__main__':
    run()
