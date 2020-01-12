import pygame

class StarImage():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/star.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Positions the star in the middle of the screen
        self.rect.x = self.screen_rect.left
        self.rect.y = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)
