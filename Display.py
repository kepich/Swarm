import pygame


class Display:
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    WINDOW_BOARD = 80

    def __init__(self):
        self.screen = pygame.display.set_mode([Display.WINDOW_WIDTH, Display.WINDOW_HEIGHT])

    def render(self, objects):
        self.screen.fill((255, 255, 255))

        for key in objects.keys():
            objects[key].draw(self.screen)

        pygame.display.flip()
