# Importations
import pygame


class Button:
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
        self.enabled = False

        # Fonction à exécuter au clic du bouton
        self.callback = callback

    def draw(self, surface):
        # Dessine le bouton
        pygame.draw.rect(
            surface, self.bg_color, self.rect, border_radius=self.border_radius
        )

        # Dessine le texte centré sur le bouton
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def click(self, pos):
        """Méthode vérifiant si le bouton est cliquable"""
        if self.enabled and self.rect.collidepoint(
            pos
        ):  # Si enabled True et la souris est sur le bouton
            if self.callback:  # Si callback True
                self.callback()
            return True
        return False
