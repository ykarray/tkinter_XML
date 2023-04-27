import tkinter as tk
import os

class Accueil(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(pady=20)  # Ajout d'un espace entre les widgets
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, text="Bienvenue sur la page d'accueil !", font=("Helvetica", 18))  # Changement de la police et de la taille du texte
        self.title.pack()

        self.add_livre_button = tk.Button(self, text="Ajouter un livre", command=self.goto_ajout_livre, bg="#3C8DBC", fg="white", font=("Helvetica", 14))  # Ajout d'une couleur de fond, de couleur de texte et changement de la police et de la taille du texte
        self.add_livre_button.pack(pady=10)  # Ajout d'un espace entre les boutons

        self.add_pfe_button = tk.Button(self, text="Ajouter un rapport", command=self.goto_ajout_pfe, bg="#3C8DBC", fg="white", font=("Helvetica", 14))  # Ajout d'une couleur de fond, de couleur de texte et changement de la police et de la taille du texte
        self.add_pfe_button.pack(pady=10)  # Ajout d'un espace entre les boutons

        self.view_pfe_button = tk.Button(self, text="Voir les rapports", command=self.goto_view_pfe, bg="#3C8DBC", fg="white", font=("Helvetica", 14))  # Ajout d'une couleur de fond, de couleur de texte et changement de la police et de la taille du texte
        self.view_pfe_button.pack(pady=10)  # Ajout d'un espace entre les boutons

        self.view_livre_button = tk.Button(self, text="Voir les livres", command=self.goto_view_livre, bg="#3C8DBC", fg="white", font=("Helvetica", 14))  # Ajout d'une couleur de fond, de couleur de texte et changement de la police et de la taille du texte
        self.view_livre_button.pack(pady=10)  # Ajout d'un espace entre les boutons
        
    def goto_ajout_livre(self):
        os.system("python3 ajoutlivre.py")

    def goto_ajout_pfe(self):
        os.system("python3 ajoutPFE.py")
        
    def goto_view_pfe(self):
        os.system("python3 voirRapport.py")    
        
    def goto_view_livre(self):
        os.system("python3 voirLivre.py")

if __name__ == "__main__":
    root = tk.Tk()  # Création d'une nouvelle fenêtre principale
    root.geometry("500x400")  # Définition de la taille de la fenêtre à 500 pixels de largeur et 400 pixels de hauteur
    root.title("accueil")# Définition du titre de la fenêtre comme "accueil"
    root.configure(bg="#F0F0F0")  # Changer la couleur de fond de la fenêtre  en gris clair (#F0F0F0)
    Accueil(root) # Création d'un objet de la classe Accueil avec la fenêtre principale comme parent
    root.mainloop()# Lancement de la boucle principale de la fenêtre pour démarrer l'interface graphique

