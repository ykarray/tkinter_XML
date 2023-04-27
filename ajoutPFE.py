import xml.etree.ElementTree as ET
import tkinter as tk

# Fonction pour ajouter un PFE dans la base de données XML
def ajouter_pfe(titre, niveau_etude, annees, mots_cles, status_label):
    # Charger la base de données XML
    tree = ET.parse('bib.xml')
    root = tree.getroot()

    # Créer un nouvel élément "rapport"
    rapport = ET.Element('rapport')
    titre_element = ET.SubElement(rapport, 'titre')
    titre_element.text = titre
    etude_element = ET.SubElement(rapport, 'etude')
    etude_element.text = niveau_etude
    annees_element = ET.SubElement(rapport, 'annees')
    annees_element.text = annees
    mots_cles_element = ET.SubElement(rapport, 'mots_cles')
    # Séparer les mots-clés par une virgule et les stocker dans l'élément "mots_cles"
    mots_cles_list = mots_cles.split(',')
    for mot in mots_cles_list:
        mot_element = ET.SubElement(mots_cles_element, 'mot_cle')
        mot_element.text = mot.strip() # enlever les espaces en début et fin de mot

    # Ajouter le nouvel élément "rapport" à la liste des rapports PFE
    rappots_pfe_element = root.find('rappots_pfe')
    rappots_pfe_element.append(rapport)

    # Enregistrer les modifications dans la base de données XML
    tree.write('bib.xml')
    
    # Mettre à jour l'étiquette pour indiquer que l'ajout a été effectué avec succès
    status_label.config(text='Ajout effectué avec succès !', fg='green')


# Fonction pour gérer l'événement de clic sur le bouton "Ajouter"
def ajouter_click():
    titre = titre_entry.get()
    niveau_etude = niveau_etude_entry.get()
    annees = annees_entry.get()
    mots_cles = mots_cles_entry.get()

    ajouter_pfe(titre, niveau_etude, annees, mots_cles, status_label)


# Créer l'interface utilisateur
root = tk.Tk()
root.title('Ajout rapport')

# Créer une frame pour la mise en page
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

titre_label = tk.Label(frame, text='Titre', font=('Helvetica', 12))
titre_label.grid(row=0, column=0, sticky='e')
titre_entry = tk.Entry(frame, font=('Helvetica', 12))
titre_entry.grid(row=0, column=1)

niveau_etude_label = tk.Label(frame, text='Niveau d\'étude', font=('Helvetica', 12))
niveau_etude_label.grid(row=1, column=0, sticky='e')
niveau_etude_entry = tk.Entry(frame, font=('Helvetica', 12))
niveau_etude_entry.grid(row=1, column=1)



annees_label = tk.Label(frame, text='années', font=('Helvetica', 12))
annees_label.grid(row=2, column=0, sticky='e')
annees_entry = tk.Entry(frame, font=('Helvetica', 12))
annees_entry.grid(row=2, column=1)

mots_cles_label = tk.Label(frame, text='mots clés', font=('Helvetica', 12))
mots_cles_label.grid(row=3, column=0, sticky='e')
mots_cles_entry = tk.Entry(frame, font=('Helvetica', 12))
mots_cles_entry.grid(row=3, column=1)

ajouter_button = tk.Button(frame, text='Ajouter', bg="#3C8DBC", fg="white",font=('Helvetica', 12), command=ajouter_click)
ajouter_button.grid(row=6, column=1, columnspan=2)

status_label = tk.Label(frame, text='', fg='red', font=('Helvetica', 12))
status_label.grid(row=7, column=1, columnspan=3)
root.mainloop()

