import pygame
import sys

class Ship:
    def __init__(self, ai_game):
        """Inicializa la nave y su posición inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Intentar cargar la imagen de la nave y manejar errores si no se encuentra
        try:
            self.image = pygame.image.load('images/enemy_1.png')
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom
            self.moving_right = False
            self.moving_left = False

        except pygame.error as e:
            print(f"No se pudo cargar la imagen: {e}")
            sys.exit() 
            
    def update(self):
        """Actualiza la posición de la nave según la dirección."""
        if self.moving_right:
            self.rect.x += 1 # Salir si no se puede cargar la imagen
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)
