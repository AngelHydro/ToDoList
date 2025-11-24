# Importations
import pygame

import config
from ui.interface import Interface

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Gestionnaire de tâches")
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
interface = Interface(screen)
running = True

interface.start()
while running:  # boucle principale
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            interface.interaction_button(event.pos)

    clock.tick(30)
