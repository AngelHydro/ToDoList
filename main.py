# Importations
import pygame

from ui.interface import Interface

pygame.init()

pygame.display.set_caption("Gestionnaire de tâches")
screen = pygame.display.set_mode((1080, 720))
interface = Interface(screen)
running = True

while running:  # boucle principale
    interface.start()
    screen.blit(interface.text_item.txt_task, pos_task)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
