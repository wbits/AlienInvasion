import pygame
from settings import Settings


class Ship:
    def __init__(self, ai_settings: Settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image and get the rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start a new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
