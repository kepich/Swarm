import pygame
import random

from Display import Display

from Bug import Bug
from Food import Food
from Queen import Queen

pygame.init()

NUMBER_OF_FOOD = 1
NUMBER_OF_QUEENS = 1
NUMBER_OF_BUGS = 200


def init_objects(objects):
    bugs = pygame.sprite.Group()
    for i in range(NUMBER_OF_BUGS):
        bugs.add(Bug(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                     random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD)))

    objects["bugs"] = bugs

    queens = pygame.sprite.Group()
    for i in range(NUMBER_OF_QUEENS):
        queens.add(Queen(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                         random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD)))

    objects["queens"] = queens

    food = pygame.sprite.Group()
    for i in range(NUMBER_OF_FOOD):
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Bug.MOVEMENT_SPEED += 0.5
                if event.key == pygame.K_DOWN:
                    Bug.MOVEMENT_SPEED -= 0.5

                display.set_caption("Speed: " + str(Bug.MOVEMENT_SPEED))

        update(objects)
        display.render(objects)

    pygame.quit()


if __name__ == '__main__':
    run()
