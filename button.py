import pygame.font


class Button:
    """a class to build buttons for the game"""

    def __init__(self, ai_game, msg):
        """initialize the burron attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build the buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # we set our rect so that our buttons center matches the center
        # of the screen, which will set the x and y accordingly
        self.rect.center = self.screen_rect.center

        # the button message needs to be prepped once
        self._prep_message(msg)

    def _prep_message(self, msg):
        """turn msg into a rendered image and center text on the button.
        this way will make it so where we can just use the same button and just
        have to call this method to change the words on it. Better in the long run
        to not have to create a whole new button each time we want to change the words.
        """

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
