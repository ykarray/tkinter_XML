import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk

# Fonction pour créer la liste de livres
def create_book_list():
    # Charger le fichier XML et obtenir la racine de l'arbre
    tree = ET.parse('bib.xml')
    root = tree.getroot()

    # Créer une liste vide pour stocker les informations des livres
    books = []

    # Parcourir tous les éléments 'livre' sous l'élément racine
    for book in root.findall('./livres/livre'):
        # Obtenir le titre, l'auteur, l'ISBN et les mots-clés du livre en utilisant la méthode find() pour chercher les éléments spécifiques
        title = book.find('titre').text
        author = book.find('./auteurs/auteur').text
        isbn = book.find('ISBN').text
        # Utiliser une compréhension de liste pour obtenir les mots-clés en utilisant la méthode findall() pour chercher tous les éléments 'mot_cle' et la méthode text pour obtenir leur texte
        keywords = ", ".join([keyword.text for keyword in book.findall('./mots_cle/mot_cle')])
        # Ajouter les informations du livre à la liste books sous forme de tuple (titre, auteur, ISBN, mots-clés)
        books.append((title, author, isbn, keywords))

    # Retourner la liste des livres
    return books

# Fonction pour rechercher les livres par titre, ISBN, auteur ou mot-clé
def search_books():
    # Obtenir le terme de recherche depuis l'entrée de recherche et le convertir en minuscules
    search_term = search_entry.get().lower()

    # Effacer les résultats de recherche précédents dans la liste des résultats de recherche
    search_results.delete(*search_results.get_children())

    # Parcourir la liste des livres (book_list) pour rechercher les livres correspondant au terme de recherche
    for book in book_list:
        # Vérifier si le terme de recherche se trouve dans le titre, l'auteur, l'ISBN ou les mots-clés du livre, en ignorant la casse
        if search_term in book[0].lower() or search_term in book[1].lower() or search_term in book[2].lower() or search_term in book[3].lower():
            # Insérer les informations du livre correspondant dans la liste des résultats de recherche sous forme de valeurs dans une nouvelle ligne
            search_results.insert('', tk.END, values=book)


# Création de la fenêtre
root = tk.Tk()
root.title("Liste des livres")
# Création de la liste de livres
book_list = create_book_list()

# Création de la zone de recherche
search_label = tk.Label(root, text="Rechercher:", font=('Helvetica', 12))
search_label.grid(row=0, column=0, padx=5, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = tk.Button(root, text="Rechercher",  bg="#3C8DBC", fg="white",font=('Helvetica', 12),command=search_books)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Création du tableau de résultats
columns = ('Titre', 'Auteur', 'ISBN', 'Mots-clés')
#Le Treeview est utilisé pour afficher des données sous forme d'un arbre hiérarchique avec des colonnes.

#Les colonnes sont définies dans la variable 'columns', qui doit être une liste contenant les noms des colonnes à afficher dans le Treeview. #Les en-têtes des colonnes seront affichés grâce à l'argument 'show' défini sur 'headings'.


search_results = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    search_results.heading(col, text=col)
search_results.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

# Affichage de tous les livres dans le tableau
for book in book_list:
    search_results.insert('', tk.END, values=book)

root.mainloop()

