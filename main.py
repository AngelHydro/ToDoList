# Importations
import pygame

import config
from ui.interface import Interface

pygame.init()

pygame.display.set_caption("Gestionnaire de tâches")
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
interface = Interface(screen)
running = True

while running:  # boucle principale
    interface.start()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            interface.interaction_button(event.pos)
