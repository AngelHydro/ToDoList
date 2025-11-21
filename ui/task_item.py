import pygame

from ui.fonctionnalite import Fonctionnalite


class TaskItem:
    """Classe TaskItem qui sert à afficher chaque élément de la liste des tâches"""

    def __init__(self, surface):
        self.surface = surface
        self.liste_tasks = Fonctionnalite()
        self.width = self.surface.get_width() // 3
<<<<<<< HEAD
        self.height = 75
=======
        self.height = 50
>>>>>>> d2cc93dd2158b9a82622b2d241912959b9b38c47
        self.x = self.surface.get_width() // 3
        self.y = 0

    def afficher_task(self):
        self.y = 0
        self.font_task = pygame.font.SysFont("Calibri", 20)
        for cle in self.liste_tasks.liste.keys():
<<<<<<< HEAD
            self.y += 75
=======
            self.y += 50
>>>>>>> d2cc93dd2158b9a82622b2d241912959b9b38c47
            self.rect_task = pygame.draw.rect(
                self.surface, (66, 0, 0), [self.x, self.y, self.width, self.height], 2
            )
            self.txt_task = self.font_task.render(cle, True, (66, 0, 0))
            self.pos_task = self.txt_task.get_rect(center=self.rect_task.center)
            self.surface.blit(self.txt_task, self.pos_task)
<<<<<<< HEAD
=======

    def height_tasks(
        self,
    ):  # retourne la hauteur prise sur l'écran par les tâches (utile pour placer le bouton ajouter)
        return self.y + 50

    def width_tasks(self):
        return (
            self.x + self.width
        )  # retourne la largeur prise sur l'écran par les tâches (utile pour placer les coches)
>>>>>>> d2cc93dd2158b9a82622b2d241912959b9b38c47
