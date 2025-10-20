import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()  # we create a clock to track time
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Alien Invasion")

        # create a ship variable and pass in the current instance of the game
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:

            self._check_events()
            self.ship.update()
            self._update_screen()

            # set the frame rate to the common 60 FPS
            self.clock.tick(60)

    def _check_events(self):
        """respond to keypresses and mouse events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    # Make an instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
