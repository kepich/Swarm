import pygame


class Display:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 800
    WINDOW_BOARD = 50

    def __init__(self):
        self.screen = pygame.display.set_mode([Display.WINDOW_WIDTH, Display.WINDOW_HEIGHT])

    def render(self, objects):
        self.screen.fill((0, 0, 0))

        for key in objects.keys():
            objects[key].draw(self.screen)

        pygame.display.flip()

    def set_caption(self, text):
        pygame.display.set_caption(text)
