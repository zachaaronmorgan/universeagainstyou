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
        
        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        
        self.ship_speed = 1.5
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        
        if self.moving_left:
            self.rect.x -= 1
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)