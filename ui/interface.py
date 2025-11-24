import os
import sys

# On ajoute le dossier parent au chemin Python
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Maintenant l'import fonctionne
import config
from ui.button import Button, Coche

# from input_field import *
from ui.task_item import TaskItem


class Interface(object):
    def __init__(self, surface):
        """Contructeur"""
        self.surface = surface
        self.task_item = TaskItem(self.surface)
        self.liste_buttons_coche = []  # la liste des boutons coches
        self.liste_buttons_complement = []
        self.liste_coche = []

    def start(self):
        """Méthode Start pour lancer l'interface dans main.py"""
        print("début")
        self.task_item.afficher_task()
        self.largeur_taches = (
            self.task_item.x + self.task_item.width
        )  # retourne la largeur prise sur l'écran par les tâches (utile pour placer les coches)
        self.hauteur_taches = (
            self.task_item.y + 75
        )  # retourne la hauteur prise sur l'écran par les tâches (utile pour placer le bouton ajouter)
        self.coche_y = 0  # position y de départ de la coche
        for cle in self.task_item.liste_tasks.liste.keys():
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
                cle,
                (0, 0, 66),
                (),
                2,
                False,
            )
            self.liste_buttons_coche.append(self.button_coche)
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
            self.liste_buttons_complement.append(self.button_complement)
            self.button_coche.draw(self.surface)
            self.button_complement.draw(self.surface)
            self.coche = Coche(
                self.largeur_taches + 13,
                self.coche_y + 13,
                50,
                50,
                "✓",
                config.GREEN,
                config.WHITE,
                2,
            )  # créer une instance de la classe Coche
            self.liste_coche.append(self.coche)

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

    def interaction_button(self, pos):
        for i in range(len(self.liste_buttons_coche)):
            if self.liste_buttons_coche[i].rect.collidepoint(pos):
                if self.liste_buttons_coche[i].enabled:  # pour le bouton coche
                    self.task_item.liste_tasks.cocher_decocher(
                        self.liste_buttons_coche[i].text
                    )
                    self.liste_coche[i].cocher(self.surface)
        for element in self.liste_buttons_complement:  # pour le bouton complément
            if element.rect.collidepoint(pos):
                if element.enabled:
                    pass
        if self.button_ajouter.enabled:  # pour le bouton ajouter
            pass
        """les futurs boutons à ajouter :
            - supprimer
            - annuler
            - modifier
            - valider"""
