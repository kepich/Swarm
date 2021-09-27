from math import sqrt

import pygame
import random

from Display import Display


class Bug(pygame.sprite.Sprite):
    SIZE = 15
    MOVEMENT_SPEED = 1.5
    HEAR_RANGE = 50

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        # Drawing
        self.image = pygame.Surface([self.SIZE, self.SIZE])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))

        pygame.draw.circle(self.image, (0, 0, 255), (self.SIZE // 2, self.SIZE // 2), self.SIZE // 2)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Position
        self.x_pos = x  # Float values of position
        self.y_pos = y
        self.move_vector = []
        self.set_movement([random.randint(-2000, 2000), random.randint(-2000, 2000)])

        # Counters
        self.target_food = 300
        self.target_queen = 300
        self.target = 1

    def set_movement(self, vector):
        vector_len = sqrt(vector[0] * vector[0] + vector[1] * vector[1])
        self.move_vector = [self.MOVEMENT_SPEED * vector[0] / vector_len, self.MOVEMENT_SPEED * vector[1] / vector_len]

    def update(self, *action, **kwargs) -> None:
        if action[0] == "move":
            if self.x_pos + self.move_vector[0] > Display.WINDOW_WIDTH - self.SIZE or self.x_pos + self.move_vector[
                0] < 0 or \
                    self.y_pos + self.move_vector[1] > Display.WINDOW_HEIGHT - self.SIZE or self.y_pos + \
                    self.move_vector[1] < 0:

                self.set_movement([random.randint(-2000, 2000), random.randint(-2000, 2000)])
            else:
                self.move(action[1], action[2])
        elif action[0] == "hear":
            hearable_bugs = list(filter(lambda sprite: sqrt(
                (self.rect.x - sprite.rect.x) ** 2 + (self.rect.y - sprite.rect.y) ** 2) < self.HEAR_RANGE and sprite != self,
                                        self.groups()[0].sprites()))

            if len(hearable_bugs) > 0:
                if self.target == 1:
                    best_bug = min(hearable_bugs, key=lambda bug: bug.target_food)

                    if self.target_food > best_bug.target_food:
                        self.move_vector = [best_bug.move_vector[0] - self.move_vector[0],
                                            best_bug.move_vector[1] - self.move_vector[1]]

                else:
                    best_bug = min(hearable_bugs, key=lambda bug: bug.target_queen)

                    if self.target_queen > best_bug.target_queen:
                        self.move_vector = [best_bug.move_vector[0] - self.move_vector[0],
                                            best_bug.move_vector[1] - self.move_vector[1]]

    def move(self, food, queens):
        if self.target == 1:    # target - food
            collisions = pygame.sprite.spritecollide(self, food, False)
            if len(collisions) > 0:
                self.turn_around()
        else:                   # target - queen
            collisions = pygame.sprite.spritecollide(self, queens, False)
            if len(collisions) > 0:
                self.turn_around()

        self.x_pos += self.move_vector[0]
        self.y_pos += self.move_vector[1]

        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

    def inc_counters(self):
        self.target_food += 1
        self.target_queen += 1

    def turn_around(self):
        self.target *= -1
        self.move_vector[0] = -self.move_vector[0]
        self.move_vector[1] = -self.move_vector[1]
