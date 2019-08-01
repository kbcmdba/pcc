import pygame
from random import randint
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to manage background stars"""

    def __init__(self, ai_settings, screen):
        """Create a star object at a random position."""
        super(Star, self).__init__()
        self.screen = screen

        # Create a star rect
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.color = 0, 0, 0

        # Where do I put it?
        self.rect.x = randint(0, ai_settings.screen_width - 1 - self.rect.width)
        self.rect.y = randint(0, ai_settings.screen_height - 1 - self.rect.height)

        # Store the star's position as a decimal value.
        self.y = float(self.rect.y)


    def draw_star(self):
        """Draw the star to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

