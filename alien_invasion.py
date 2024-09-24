import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # Configura la pantalla del juego
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # Inicializa el color de fondo y la nave
        self.bg_color = (230, 230, 230)  
        self.ship = Ship(self)

    def run_game(self):
        # Bucle principal del juego
        while True:
            self._check_events()  # Revisa los eventos del usuario
            self._update_screen() #actualiza la pantalla
            self.ship.update()  # Actualiza la posición de la nave 

    def _check_events(self):
        """Responde a eventos del teclado y ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Mueve la nave a la derecha
                    self.ship.moving_right = True
                    # se mueve a la dcha
                    self.ship.rect.x +=1
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Actualiza la pantalla con nuevas imágenes y cambia el buffer de pantalla."""
        # Rellena la pantalla con el color de fondo
        self.screen.fill(self.bg_color)
        # Dibuja la nave
        self.ship.blitme()
        # Actualiza la pantalla
        pygame.display.flip()
        # Controla la velocidad del juego a 60 FPS
        self.clock.tick(60)

if __name__ == '__main__':
    # Inicia el juego
    ai = AlienInvasion()
    ai.run_game()




    