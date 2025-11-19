import pygame

from ui.fonctionnalite import Fonctionnalite


class TaskItem:
    """Classe TaskItem qui sert à afficher chaque élément de la liste des tâches"""

    def __init__(self, surface):
        self.surface = surface
        self.liste_tasks = Fonctionnalite()
        self.width = 100
        self.height = 50
        self.x = self.surface.get_width() // 2
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def afficher_task(self):
        self.y = 0
        self.font_task = pygame.font.SysFont("Calibri", 20)
        for cle in self.liste_tasks.liste.keys():
            self.y += 20
            pygame.draw.rect(self.surface, (0, 0, 0), self.rect)
            self.txt_task = self.font_task.render(cle, True, (0, 0, 0))
            self.pos_task = self.txt_task.get_rect()
            self.pos_task.centerx = self.surface.get_rect().centerx
            self.pos_task.centery = 20
