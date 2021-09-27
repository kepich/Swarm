import pygame


class Food(pygame.sprite.Sprite):
    SIZE = 50

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([Food.SIZE, Food.SIZE])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))

        pygame.draw.circle(self.image, (0, 255, 0), (Food.SIZE // 2, Food.SIZE // 2), Food.SIZE // 2)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y