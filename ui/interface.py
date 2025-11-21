import pygame

from ui.button import Button

# from input_field import *
from ui.task_item import TaskItem


class Interface:
    def __init__(self, surface):
        """Contructeur"""
        self.surface = surface
        self.task_item = TaskItem(self.surface)

    def start(self):
        """Méthode Start pour lancer l'interface dans main.py"""
        self.task_item.afficher_task()
<<<<<<< HEAD
        self.largeur_taches = (
            self.task_item.x + self.task_item.width
        )  # retourne la largeur prise sur l'écran par les tâches (utile pour placer les coches)
        self.hauteur_taches = (
            self.task_item.y + 75
        )  # retourne la hauteur prise sur l'écran par les tâches (utile pour placer le bouton ajouter)
        self.coche_y = 0  # position y de départ de la coche
        for _ in self.task_item.liste_tasks.liste.keys():
            """ Boucle pour : à chaque tâche créer et afficher :
                    - Le bouton Coche
                    - Le bouton Complément"""
            # créer le bouton coche
            self.coche_y += 75
            self.button_coche = Button(
                self.largeur_taches + 13,
                self.coche_y + 13,
                50,
                50,
                "",
                (0, 0, 66),
                (),
                2,
                False,
            )
            # créer le bouton complément
            self.button_complement = Button(
                self.largeur_taches - 40,
                self.coche_y + 22,
                20,
                20,
                "...",
                (0, 0, 0),
                (66, 0, 0),
                2,
                False,
            )
            self.button_coche.draw(self.surface)
            self.button_complement.draw(self.surface)

        # Créer le bouton ajouter
        self.button_ajouter = Button(
            self.surface.get_width() // 3,
            self.hauteur_taches + 10,
            40,
            40,
=======
        self.largeur_taches = self.task_item.width_tasks()
        self.hauteur_taches = self.task_item.height_tasks()
        self.button_ajouter = Button(
            self.surface.get_width() // 3,
            self.hauteur_taches,
            20,
            20,
>>>>>>> d2cc93dd2158b9a82622b2d241912959b9b38c47
            "+",
            (0, 128, 0),
            (0, 0, 0),
            2,
            False,
        )
<<<<<<< HEAD
        self.button_ajouter.draw(self.surface)  # afficher bouton ajouter
=======
        self.button_ajouter.draw(self.surface)
        # self.button_complement = Button()
>>>>>>> d2cc93dd2158b9a82622b2d241912959b9b38c47
        # self.button_supprimer = Button()
        # self.button_modifier = Button()
