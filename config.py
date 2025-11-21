# ============================================
# CONFIGURATION DE LA FENÊTRE
# ============================================
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Ma TodoList"
FPS = 60  # Images par seconde

# ============================================
# COULEURS (format RGB)
# ============================================
# Couleurs principales
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BROWN = (139, 69, 19)
PINK = (255, 192, 203)
NAVY = (0, 0, 128)
TEAL = (0, 128, 128)
OLIVE = (128, 128, 0)

# Couleurs de l'interface
BACKGROUND_COLOR = (30, 30, 30)
PRIMARY_COLOR = (0, 150, 255)  # Bleu pour les boutons principaux
SECONDARY_COLOR = (100, 100, 100)  # Gris pour les boutons secondaires
SUCCESS_COLOR = (0, 200, 100)  # Vert pour les validations
DANGER_COLOR = (255, 80, 80)  # Rouge pour les suppressions
HOVER_COLOR = (0, 180, 255)  # Couleur au survol

# Couleurs du texte
TEXT_COLOR = (255, 255, 255)
TEXT_COLOR_DARK = (50, 50, 50)
PLACEHOLDER_COLOR = (150, 150, 150)

# ============================================
# POLICES
# ============================================
FONT_NAME = None  # None = police par défaut de Pygame
FONT_SIZE_SMALL = 16
FONT_SIZE_MEDIUM = 24
FONT_SIZE_LARGE = 32
FONT_SIZE_TITLE = 48

# Importations de polices
""" https://fonts.google.com/ """


# ============================================
# DIMENSIONS DES COMPOSANTS
# ============================================
# Boutons
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 40
BUTTON_BORDER_RADIUS = 8

# Champs de texte
INPUT_WIDTH = 400
INPUT_HEIGHT = 40
INPUT_BORDER_RADIUS = 5

# Tâches
TASK_ITEM_HEIGHT = 60
TASK_ITEM_MARGIN = 10
CHECKBOX_SIZE = 30

# ============================================
# ESPACEMENT ET MARGES
# ============================================
PADDING = 20
MARGIN = 10
HEADER_HEIGHT = 80

# ============================================
# CHEMINS DES FICHIERS
# ============================================
DATA_FILE = "data/tasks.json"
FONT_PATH = "assets/fonts/"
IMAGES_PATH = "assets/images/"
