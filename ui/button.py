# Importations
import pygame

import config


class Button(object):
    """Classe permettant de créer un bouton"""

    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        bg_color,
        text_color,
        border_radius,
        callback=None,
        font=None,
    ):
        """Constructeur de la  classe"""

        # Position et dimensions du bouton
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Texte et apparence du bouton
        self.text = text
        self.font = font or pygame.font.Font(None, 24)
        self.text_color = text_color
        self.bg_color = bg_color
        self.border_radius = border_radius

        # Etats du bouton
        self.enabled = True  # Le bouton est-il cliquable ? Cliquable par défaut

    def draw(self, surface):
        """Méthode pour dessiner le bouton"""
        pygame.draw.rect(
            surface, self.bg_color, self.rect, border_radius=self.border_radius
        )

        # Dessine le texte centré sur le bouton
        if self.text_color != ():  # vérifie si on n'a pas de couleur pour le texte
            text_surf = self.font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)

    def utilisable(self):
        """Méthode pour vérifier si la coche est cliquable (False ou True)"""
        self.enabled = not self.enabled


class Coche(object):
    """Classe Coche définissant :
    - dessiner la coche validée
    - inverser l'état du coche"""

    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        bg_color,
        text_color,
        border_radius,
        font=None,
    ):
        """Constructeur de la  classe"""

        # Position et dimensions du bouton
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Texte et apparence du bouton
        self.text = text
        self.font = font or pygame.font.Font(config.FONT_NAME, self.width)
        self.text_color = text_color
        self.bg_color = bg_color
        self.border_radius = border_radius

        # Etats de la coche
        self.is_checked = False  # Le coche est-elle cochée ? Non cochée par défaut

    def dessiner_coche(self, surface):
        """Méthode qui dessine une coche validée si la coche is_enabled"""
        # Dessine le fond du bouton
        pygame.draw.rect(
            surface, self.bg_color, self.rect, border_radius=self.border_radius
        )

        # Dessine la coche seulement si is_checked est True
        if self.is_checked:
            checkmark_surf = self.font.render(self.text, True, self.text_color)
            checkmark_rect = checkmark_surf.get_rect(center=self.rect.center)
            surface.blit(checkmark_surf, checkmark_rect)

    def cocher(self, surface):
        """Inverse l'état de la coche (True ou False : coché ou non ?)"""
        self.is_checked = not self.is_checked
        self.dessiner_coche(surface)
