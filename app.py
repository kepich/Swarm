import pygame
import random

from Display import Display

from Bug import Bug
from Food import Food
from Queen import Queen
from Rock import Rock

pygame.init()

NUMBER_OF_FOOD = 1
NUMBER_OF_QUEENS = 1
NUMBER_OF_BUGS = 200
NUMBER_OF_STONE = 0


def init_objects(objects):
    objects["queens"] = init_queens()
    objects["food"] = init_food(objects["queens"])
    objects["rocks"] = init_rocks(objects["queens"], objects["food"])
    objects["bugs"] = init_bugs(objects["queens"], objects["food"], objects["rocks"])


def init_bugs(queens, food, rock):
    print("Init 0 of " + str(NUMBER_OF_BUGS) + " bugs")
    bugs = pygame.sprite.Group()
    for i in range(NUMBER_OF_BUGS):
        while True:
            bug = Bug(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                      random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD),
                      (random.random() - 0.5) / 2)

            if (len(pygame.sprite.spritecollide(bug, food, False, pygame.sprite.collide_mask)) +
                len(pygame.sprite.spritecollide(bug, queens, False, pygame.sprite.collide_mask)) +
                len(pygame.sprite.spritecollide(bug, rock, False, pygame.sprite.collide_mask))) > 0:
                continue
            else:
                print("Init " + str(i + 1) + " of " + str(NUMBER_OF_BUGS) + " bugs")
                bugs.add(bug)
                break

    return bugs


def init_rocks(queens, food):
    print("Init 0 of " + str(NUMBER_OF_STONE) + " rocks")

    rocks = pygame.sprite.Group()
    for i in range(NUMBER_OF_STONE):
        while True:
            entity = Rock(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                          random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD))

            if (len(pygame.sprite.spritecollide(entity, food, False, pygame.sprite.collide_mask)) + len(
                    pygame.sprite.spritecollide(entity, queens, False, pygame.sprite.collide_mask))) > 0:
                continue
            else:
                print("Init " + str(i + 1) + " of " + str(NUMBER_OF_STONE) + " rocks")
                rocks.add(entity)
                break

    return rocks


def init_food(queens):
    print("Init 0 of " + str(NUMBER_OF_FOOD) + " foods")

    food = pygame.sprite.Group()
    for i in range(NUMBER_OF_FOOD):
        while True:
            entity = Food(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                          random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD))

            if (len(pygame.sprite.spritecollide(entity, food, False, pygame.sprite.collide_mask)) + len(
                    pygame.sprite.spritecollide(entity, queens, False, pygame.sprite.collide_mask))) > 0:
                continue
            else:
                print("Init " + str(i + 1) + " of " + str(NUMBER_OF_FOOD) + " food")
                food.add(entity)
                break

    return food


def init_queens():
    print("Init 0 of " + str(NUMBER_OF_QUEENS) + " queens")

    queens = pygame.sprite.Group()
    for i in range(NUMBER_OF_QUEENS):
        while True:
            queen = Queen(random.randint(Display.WINDOW_BOARD, Display.WINDOW_WIDTH - Display.WINDOW_BOARD),
                          random.randint(Display.WINDOW_BOARD, Display.WINDOW_HEIGHT - Display.WINDOW_BOARD))

            if len(pygame.sprite.spritecollide(queen, queens, False, pygame.sprite.collide_mask)) > 0:
                continue
            else:
                print("Init " + str(i + 1) + " of " + str(NUMBER_OF_QUEENS) + " queens")
                queens.add(queen)
                break
    return queens


def update(objects):
    objects["bugs"].update("move", objects["food"], objects["queens"], objects["rocks"])
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
