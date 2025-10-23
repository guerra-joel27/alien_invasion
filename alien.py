import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """a class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens exact horizontal position
        # we track the horizontal speed precisely
        self.x = float(self.rect.x)

    def check_edges(self):
        """returns true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """move the alien to the right or the left depending on the movement direction"""
        # use float to keep track of movement for more precision
        # 1 and -1 values of the fleet_direction will determing in which direction
        # the alien will move, left or right
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
