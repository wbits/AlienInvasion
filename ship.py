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

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect objects from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
