from math import sqrt

import pygame
import random

from Display import Display


class Bug(pygame.sprite.Sprite):
    SIZE = 5
    MOVEMENT_SPEED = 2
    HEAR_RANGE = 50

    FOOD_TARGET = 1
    QUEEN_TARGET = -1

    def __init__(self, x, y, speed_offset):
        pygame.sprite.Sprite.__init__(self)
        # self.myfont = pygame.font.SysFont("monospace", 6)
        self.speed_offset = speed_offset
        # Drawing
        self.image = pygame.Surface([self.SIZE, self.SIZE])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))

        pygame.draw.circle(self.image, (0, 255, 0), (self.SIZE // 2, self.SIZE // 2), self.SIZE // 2)
        self.mask = pygame.mask.from_surface(self.image)
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
        self.target = self.FOOD_TARGET

    def set_movement(self, vector):
        vector_len = sqrt(vector[0] * vector[0] + vector[1] * vector[1])

        if vector_len > 10:
            self.move_vector = [(self.MOVEMENT_SPEED + self.speed_offset) * vector[0] / vector_len, (self.MOVEMENT_SPEED + self.speed_offset) * vector[1] / vector_len]

    def update(self, *action, **kwargs) -> None:
        if action[0] == "move":
            self.move_action(action)
        elif action[0] == "hear":
            self.hear_action()

    def move_action(self, action):
        if self.x_pos + self.move_vector[0] > Display.WINDOW_WIDTH - self.SIZE or self.x_pos + self.move_vector[0] < 0 \
                or self.y_pos + self.move_vector[1] > Display.WINDOW_HEIGHT - self.SIZE or self.y_pos + self.move_vector[1] < 0:

            self.set_movement([random.randint(-2000, 2000), random.randint(-2000, 2000)])
        else:
            self.move(action[1], action[2], action[3])

    def hear_action(self):
        hearable_bugs = list(filter(lambda sprite: sqrt(
            (self.x_pos - sprite.x_pos) ** 2 + (
                        self.y_pos - sprite.y_pos) ** 2) < self.HEAR_RANGE and sprite != self,
                                    self.groups()[0].sprites()))
        if len(hearable_bugs) > 0:
            best_bug_food = min(hearable_bugs, key=lambda bug: bug.target_food)
            best_bug_queen = min(hearable_bugs, key=lambda bug: bug.target_queen)

            if self.target_food > (best_bug_food.target_food + self.HEAR_RANGE):
                self.target_food = best_bug_food.target_food + self.HEAR_RANGE
                if self.target == self.FOOD_TARGET:
                    self.set_movement([best_bug_food.x_pos - self.x_pos, best_bug_food.y_pos - self.y_pos])

            if self.target_queen > (best_bug_queen.target_queen + self.HEAR_RANGE):
                self.target_queen = best_bug_queen.target_queen + self.HEAR_RANGE
                if self.target == self.QUEEN_TARGET:
                    self.set_movement([best_bug_queen.x_pos - self.x_pos, best_bug_queen.y_pos - self.y_pos])

    def move(self, food, queens, stone):
        collisions_food = pygame.sprite.spritecollide(self, food, False, pygame.sprite.collide_mask)
        collisions_queens = pygame.sprite.spritecollide(self, queens, False, pygame.sprite.collide_mask)

        if len(collisions_food) > 0:
            self.target_food = 0
            if self.target == self.FOOD_TARGET:     # target - food
                self.turn_around()
            else:
                self.set_movement([random.randint(-2000, 2000), random.randint(-2000, 2000)])
        elif len(collisions_queens) > 0:
            self.target_queen = 0
            if self.target == self.QUEEN_TARGET:  # target - food
                self.turn_around()
            else:
                self.set_movement([random.randint(-2000, 2000), random.randint(-2000, 2000)])

        self.x_pos += self.move_vector[0]
        self.y_pos += self.move_vector[1]

        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

        self.inc_counters(stone)

    def inc_counters(self, stone):
        self.target_food += 1
        self.target_queen += 1

        if len(pygame.sprite.spritecollide(self, stone, False, pygame.sprite.collide_mask)) > 0:
            self.target_food += 20
            self.target_queen += 20

    def turn_around(self):
        self.target *= -1
        self.move_vector[0] = -self.move_vector[0]
        self.move_vector[1] = -self.move_vector[1]

        if self.target == self.FOOD_TARGET:
            pygame.draw.circle(self.image, (0, 255, 0), (self.SIZE // 2, self.SIZE // 2), self.SIZE // 2)
        else:
            pygame.draw.circle(self.image, (255, 0, 0), (self.SIZE // 2, self.SIZE // 2), self.SIZE // 2)
