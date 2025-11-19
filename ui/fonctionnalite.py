# Importations


class Fonctionnalite:
    """Classe Fonctionnalite définissant les méthodes :
    - Ajouter une tâche
    - Supprimer une tâche
    - Cocher une tâche
    - Décocher une tâche"""

    def __init__(self):
        """Constructeur"""
        self.liste = {"Faire la vaisselle": False, "Faire la cuisine": False}

    def __str__(self):
        return f"Voici votre liste de tâches : {self.liste}"

    def ajouter(self, titre):
        """Méthode permettant d'ajouter un titre au dictionnaire
        seulement si ce titre n'existe pas encore"""
        if titre in self.liste:  # Si le titre est déjà dans le dictionnaire
            print(f"La tâche '{titre}' existe déjà dans la liste.")
            return
        self.liste[titre] = False
        print(f"La tâche '{titre}' a été ajoutée.")

    def cocher(self, titre):
        """Méthode permettant de cocher la tâche du dictionnaire
        seulement si ce titre existe encore déjà"""
        if titre in self.liste:  # vérifie si le titre est dans le dictionnaire
            self.liste[titre] = True  # cocher la tâche
            print(f"La tâche '{titre}' a été validée.")
            return
        print(f"La tâche '{titre}' n'existe pas dans la liste.")

    def decocher(self, titre):
        """Méthode permettant de décocher la tâche du dictionnaire
        seulement si ce titre existe encore déjà"""
        if titre in self.liste:  # vérifie si le titre est dans le dictionnaire
            self.liste[titre] = False  # décocher la tâche
            print(f"La tâche '{titre}' a été décochée.")
            return
        print(f"La tâche '{titre}' n'existe pas dans la liste.")

    def supprimer(self, titre):
        """Méthode permettant de supprimer la tâche du dictionnaire grâce au titre de la tâche
        seulement si ce titre existe encore déjà"""
        if titre in self.liste:  # vérifie si le titre est dans le dictionnaire
            del self.liste[titre]  # supprime la tâche
            print(f"La tâche '{titre}' a été supprimé.")
            return
        print(f"La tâche '{titre}' n'existe pas dans la liste.")
