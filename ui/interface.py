import pygame

# from button import Button
# from input_field import *
from ui.task_item import TaskItem


class Interface:
    def __init__(self, surface):
        self.surface = surface
        self.task_item = TaskItem(self.surface)

    def start(self):
        self.task_item.afficher_task()
        self.button_ajouter = Button()
        # self.button_complement = Button()
        # self.button_supprimer = Button()
        # self.button_modifier = Button()
