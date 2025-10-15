import pygame


class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        # this will give us the screen itself
        self.screen = ai_game.screen
        # which we then use to get the position/numbers
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("images/SpaceShipNormal.bmp")
        # we call the get_rect method to get the numbers for the image
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        # basically we set the ships "midbottom" to be the same as the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw the ship at its current location"""
        # we draw the image, at the rect position currently set
        # self.rect will change depending on certain events
        # after starting at the initial midbottom we we set as the default position
        self.screen.blit(self.image, self.rect)
