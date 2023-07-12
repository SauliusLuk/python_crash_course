import sys
import pygame
from keys_settings import Settings
from pygame.locals import *

class EmptyScreen:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('EmptyScreen')
        self.bg_color = (self.settings.bg_color)

        self.font = pygame.font.Font(None, 24) # Set the font and size for the messages
        self.message_right = self.font.render("Right arrow key press detected", True, (255, 255, 255))
        self.message_left = self.font.render("Left arrow key press detected", True, (255, 255, 255))

        self.keydown_detected = False

    def run_screen(self):
        while True:
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            if self.keydown_detected:
                self._blit_messages() # Blit messages onto the screen
            pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("Right arrow key press detected")
                    self.keydown_detected = True
                elif event.key == pygame.K_LEFT:
                    print("Left arrow key press detected")
                    self.keydown_detected = True

    def _blit_messages(self):
        message_right_rect = self.message_right.get_rect()
        message_left_rect = self.message_left.get_rect()

        message_right_rect.center = (
            self.settings.screen_width // 2, self.settings.screen_height // 2 - message_right_rect.height)
        message_left_rect = (
            self.settings.screen_width // 2, self.settings.screen_height // 2 + message_left_rect.height)

        self.screen.blit(self.message_right, message_right_rect) # Blit the messages onto the screen at desired positions
        self.screen.blit(self.message_left, message_left_rect)

if __name__ == '__main__':
    es = EmptyScreen()
    es.run_screen()