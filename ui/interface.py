import os
import sys

# On ajoute le dossier parent au chemin Python
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Maintenant l'import fonctionne

import config
from ui.button import Button, Coche

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
                "✓",
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
            "+",
            (0, 128, 0),
            (0, 0, 0),
            2,
            False,
        )
        self.button_ajouter.draw(self.surface)  # afficher bouton ajouter
        self.coche = Coche(
            self.largeur_taches + 13,
            self.coche_y + 13,
            50,
            50,
            "",
            config.GREEN,
            config.YELLOW,
            2,
        )  # créer une instance de la classe Coche

    def interaction_button(self, pos):
        if self.button_coche.rect.collidepoint(pos):
            if self.button_coche.enabled:  # pour le bouton coche
                self.coche.cocher(self.surface)
            elif self.button_ajouter.enabled:  # pour le bouton ajouter
                pass
            elif self.button_complement.enabled:  # pour le bouton complément
                pass
            """les futurs boutons à ajouter :
                - supprimer
                - annuler
                - modifier
                - valider"""
