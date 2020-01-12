import sys
import pygame
import settings
import image
from pygame.sprite import Group

def run_game():
    pygame.init()
    star_settings = settings.Settings()
    screen = pygame.display.set_mode((star_settings.window_width,
                                    star_settings.window_height))
    pygame.display.set_caption('Stars')

    star_group = Group()
    star_image = image.StarImage(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    sys.quit
        screen.fill(star_settings.bg_collor)
        star_image.blitme()
        pygame.display.flip()
run_game()
