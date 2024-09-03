import sys
import pygame

class AlienDescend():
    """A class to control the overall environment of the game."""
    def __init__(self):
        """Initialize attributes"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = (230, 120, 100)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.screen.blit(self.image, self.rect)

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Ships initialization"""
        self.screen.blit(self.image, self.rect)



    def run_game(self):
        """A function to run the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            self.screen.fill(self.bg_color)
            self.blitme()

al = AlienDescend()
al.run_game()
