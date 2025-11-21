import pygame

from ui.fonctionnalite import Fonctionnalite


class TaskItem:
    """Classe TaskItem qui sert à afficher chaque élément de la liste des tâches"""

    def __init__(self, surface):
        """Constructeur"""
        self.surface = surface
        self.liste_tasks = Fonctionnalite()
        self.width = self.surface.get_width() // 3
        self.height = 75
        self.x = self.surface.get_width() // 3
        self.y = 0

    def afficher_task(self):
        """Méthode qui affiche chaque ligne de la tâche"""
        self.y = 0
        self.font_task = pygame.font.SysFont("Calibri", 20)
        for cle in self.liste_tasks.liste.keys():
            self.y += 75
            self.rect_task = pygame.draw.rect(
                self.surface, (66, 0, 0), [self.x, self.y, self.width, self.height], 2
            )
            self.txt_task = self.font_task.render(cle, True, (66, 0, 0))
            self.pos_task = self.txt_task.get_rect(center=self.rect_task.center)
            self.surface.blit(self.txt_task, self.pos_task)
