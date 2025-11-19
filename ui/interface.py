import pygame

from ui.button import Button

# from input_field import *
from ui.task_item import TaskItem


class Interface:
    def __init__(self, surface):
        self.surface = surface
        self.task_item = TaskItem(self.surface)

    def start(self):
        self.task_item.afficher_task()
        self.largeur_taches = self.task_item.width_tasks()
        self.hauteur_taches = self.task_item.height_tasks()
        self.button_ajouter = Button(
            self.surface.get_width() // 3,
            self.hauteur_taches,
            20,
            20,
            "+",
            (0, 128, 0),
            (0, 0, 0),
            2,
            False,
        )
        self.button_ajouter.draw(self.surface)
        # self.button_complement = Button()
        # self.button_supprimer = Button()
        # self.button_modifier = Button()
