import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize the game and create screen object.
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_with, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
