import pygame

class Ship:
    def __init__(self, uay_game):
        """Initialize the ship and set its starting position."""
        self.screen = uay_game.screen
        self.screen_rect = uay_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image, self.rect)