import xml.etree.ElementTree as ET
import tkinter as tk

# Fonction pour ajouter un livre dans la base de données XML
def ajouter_livre(titre, ISBN, mots_cles, auteurs, status_label):
    # Charger la base de données XML
    tree = ET.parse('bib.xml')
    root = tree.getroot()

    # Crée un nouvel élément XML appelé "livre" en utilisant la méthode Element du module ElementTree, avec la chaîne de caractères       
    #'livre'comme nom d'élément
    livre = ET.Element('livre')
    # Crée un sous-élément "titre" à l'intérieur de l'élément "livre" en utilisant la méthode SubElement 
    titre_element = ET.SubElement(livre, 'titre')
    #Attribue la valeur de la variable "titre" au texte du sous-élément "titre" en utilisant la propriété "text" de l'élément "titre_element".
    titre_element.text = titre
    etude_element = ET.SubElement(livre, 'ISBN')
    etude_element.text = ISBN

    mots_cles_element = ET.SubElement(livre, 'mots_cle')
    # Séparer les mots-clés par une virgule et les stocker dans l'élément "mots_cles"
    mots_cles_list = mots_cles.split(',')
    for mot in mots_cles_list:
        mot_element = ET.SubElement(mots_cles_element, 'mot_cle')
        mot_element.text = mot.strip() # enlever les espaces en début et fin de mot

    auteurs_element = ET.SubElement(livre, 'auteurs')
    # Séparer les auteurs par une virgule et les stocker dans l'élément "auteurs"
    auteurs_list = auteurs.split(',')
    for auteur in auteurs_list:
        auteur_element = ET.SubElement(auteurs_element, 'auteur')
        auteur_element.text = auteur.strip() # enlever les espaces en début et fin de mot

    # Ajouter le nouvel élément "livre" à la liste des livres
    livres_element = root.find('livres')
    livres_element.append(livre)

    # Enregistrer les modifications dans la base de données XML
    tree.write('bib.xml')

    # Mettre à jour l'étiquette pour indiquer que l'ajout a été effectué avec succès
    status_label.config(text='Ajout effectué avec succès !', fg='green')


# Fonction pour gérer l'événement de clic sur le bouton "Ajouter"
def ajouter_click():
    titre = titre_entry.get()
    ISBN = ISBN_entry.get()
    auteurs = auteurs_entry.get()
    mots_cles = mots_cles_entry.get()

    ajouter_livre(titre, ISBN, mots_cles, auteurs, status_label)


# Créer l'interface utilisateur
root = tk.Tk()
#Définit le titre de la fenêtre principale comme "Ajout livre"
root.title('Ajout livre')
# Créer une frame pour la mise en page
frame = tk.Frame(root, padx=20, pady=20)
#Place le cadre dans la fenêtre principale en utilisant le gestionnaire de géométrie pack()
frame.pack()
#titre_label, ISBN_label, auteurs_label, mots_cles_label: Créent des étiquettes avec les noms "Titre", "ISBN", "Auteurs" et "Mots-clés" respectivement.
#Créent des champs de saisie (Entry) pour permettre à l'utilisateur de saisir les informations du livre.
titre_label = tk.Label(frame, text='Titre', font=('Helvetica', 12))
titre_label.grid(row=0, column=0, sticky='e')
titre_entry = tk.Entry(frame, font=('Helvetica', 12))
titre_entry.grid(row=0, column=1)

ISBN_label = tk.Label(frame, text='ISBN', font=('Helvetica', 12))
ISBN_label.grid(row=1, column=0, sticky='e')
ISBN_entry = tk.Entry(frame, font=('Helvetica', 12))
ISBN_entry.grid(row=1, column=1)

auteurs_label = tk.Label(frame, text='Auteurs', font=('Helvetica', 12))
auteurs_label.grid(row=2, column=0, sticky='e')
auteurs_entry = tk.Entry(frame, font=('Helvetica', 12))
auteurs_entry.grid(row=2, column=1)

mots_cles_label = tk.Label(frame, text='Mots-clés', font=('Helvetica', 12))
mots_cles_label.grid(row=3, column=0, sticky='e')
mots_cles_entry = tk.Entry(frame, font=('Helvetica', 12))
mots_cles_entry.grid(row=3, column=1)
#Crée un bouton avec le texte "Ajouter", une couleur de fond (#3C8DBC), une couleur de texte (blanc) et une fonction de rappel (command) définie comme ajouter_click qui sera appelée lorsque le bouton est cliqué.
ajouter_button = tk.Button(frame, text='Ajouter', bg="#3C8DBC", fg="white",font=('Helvetica', 12), command=ajouter_click)
ajouter_button.grid(row=6, column=1, columnspan=2)
#status_label: Crée une étiquette vide pour afficher les messages d'état.
status_label = tk.Label(frame, text='', fg='red', font=('Helvetica', 12))
status_label.grid(row=7, column=1, columnspan=3)

root.mainloop()

