import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clolck = pygame.time.Clock()
        self.settings = Settings()
        pygame.display.set_caption('Spacial Neighbour Visiting')

        # Set background color
        self.bg_color =  (230, 230, 230)


        # Set fullscreen mode.
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Load and scale the background image
        self.background_image = pygame.image.load('images/background1.png')
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (self.settings.screen_width,
                                                        self.settings.screen_height))

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clolck.tick(60)
            self.ship.update()


    def _check_events(self):
        """Respond to keypresses and mouse events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key ==pygame.K_LEFT:
            self.ship.moving_left = False



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Draw the background image at the top-left corner of the screen
        self.screen.blit(self.background_image, (0,0))

        # Draw the ship
        self.ship.blitme()

        #Update the full display surface to the screen
        pygame.display.flip()


if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()