import pygame

class Ship:
    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/User/PycharmProjects/python_crash_course/12_pygame/12-6 Sideways Shooter/images/ship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's y value, not the rect.
        if self.moving_up and self.rect.topleft > self.screen_rect.topleft:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottomleft < self.screen_rect.bottomleft:
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)