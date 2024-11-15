import pygame

class Ship:
    def __init__(self, uay_game):
        """Initialize the ship and set its starting position."""
        self.screen = uay_game.screen
        self.settings = uay_game.settings
        self.screen_rect = uay_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for the ship's horizontal position.
        self.x = float(self.rect.x)
        
        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)