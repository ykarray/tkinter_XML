import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk

# Fonction pour créer la liste de livres
def create_rapport_list():
    tree = ET.parse('bib.xml')
    root = tree.getroot()
    rapports = []
    for rapport in root.findall('./rappots_pfe/rapport'):
        title = rapport.find('titre').text
        etude = rapport.find('etude').text
        annees = rapport.find('annees').text
        keywords = ", ".join([keyword.text for keyword in rapport.findall('./mots_cles/mot_cle')])
        rapports.append((title, etude, annees, keywords))
    return rapports

# Fonction pour rechercher les livres par titre, ISBN, auteur ou mot-clé
def search_rapports():
    search_term = search_entry.get().lower()
    search_results.delete(*search_results.get_children())
    for rapport in rapport_list:
        if search_term in rapport[0].lower() or search_term in rapport[1].lower() or search_term in rapport[2].lower() or search_term in rapport[3].lower():
            search_results.insert('', tk.END, values=rapport)

# Création de la fenêtre
root = tk.Tk()
root.title("Liste des rapport")

# Création de la liste de livres
rapport_list = create_rapport_list()

# Création de la zone de recherche
search_label = tk.Label(root, text="Rechercher:", font=('Helvetica', 12))
search_label.grid(row=0, column=0, padx=5, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = tk.Button(root, text="Rechercher", bg="#3C8DBC", fg="white",font=('Helvetica', 12), command=search_rapports)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Création du tableau de résultats
columns = ('Titre', 'Ètude','Annees', 'Mots-clés')
search_results = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    search_results.heading(col, text=col)
search_results.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Affichage de tous les livres dans le tableau
for rapport in rapport_list:
    search_results.insert('', tk.END, values=rapport)

root.mainloop()

