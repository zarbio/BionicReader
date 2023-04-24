# Ouvrir le fichier d'entrée
import easygui
import re
import aspose.words as aw
textToAdd = ""
filename1 = easygui.fileopenbox()
substring = re.split(r'(\b\.\b)(?!.*\1)', filename1)
if substring[2] == 'txt':
    with open(filename1, 'r',encoding='utf-8') as f:
        # Lire le contenu du fichier dans une variable de chaîne
        text = f.readlines()
else:
    doc = aw.Document(filename1)
    doc.save("doc-to-text.txt")
    with open("doc-to-text.txt", 'r',encoding='utf-8') as f:
        # Lire le contenu du fichier dans une variable de chaîne
        text = f.readlines()
        for i in range(2,len(text)- 1,1):
            textToAdd+= text[i]
        text = textToAdd.split("\n")
        
# Séparer la chaîne en mots en utilisant l'espace comme séparateur
bold_text = ""
bold_text+= '<p>'
for line in text :
    words = line.split()
    # Initialiser une variable pour stocker le texte mis en gras
    

    # Boucler à travers la liste de mots
    for word in words:
        # Ajouter une balise HTML de début et de fin pour mettre en gras le mot
        #bold_text += "<b>" + word + "</b> "
        i = 0
        for letter in word:
            i+=1
            if(i <= len(word)/2 or len(word) == 1):
                bold_text+= "<b>" + letter + "</b>"
            else:
                bold_text+= letter
        bold_text+=" "
    bold_text+= '<br>'
    
bold_text+= '</p>'
       
substringFile = re.split(r'(\b\.\b)(?!.*\1).*',filename1)
# Écrire la chaîne résultante dans un nouveau fichier de sortie
with open(substringFile[0] + 'copy.html', 'w') as f:
    f.write(bold_text)
