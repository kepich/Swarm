import pygame


class Rock(pygame.sprite.Sprite):
    SIZE = 30

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.SIZE, self.SIZE])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))

        pygame.draw.circle(self.image, (150, 150, 100), (self.SIZE // 2, self.SIZE // 2), self.SIZE // 2)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
