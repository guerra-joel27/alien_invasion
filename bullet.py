import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class to manage the bullets fired from the ship"""

    def __init__(self, ai_game):
        """create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0, 0) and then set correct position
        # bullet isnt built by image so we have to create from scratch
        # using the pygame.Rect class, take x, y and top-left corner of rect
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        # set the bullet start location to the top-middle of the ship where the gun would be
        # this will make it look like it came from the top of the ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position as a float
        # we use float so we can make finer adjustments
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        # update the exact position of the bullet
        self.y -= self.settings.bullet_speed

        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
