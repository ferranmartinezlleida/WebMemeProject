# MemeProject
Meme Project

Aquest projecte ha estat creat amb la finalitat de donar satisfaccio als requeriments expressats en la primera entrega de l'assignatura Projecte Web. El projecte representa la base per la que ha de ser una web creada amb la finalitat de donar servei a una communitat de creacio i intercanvi de MEMS.

Per tal de llençar adecuadament la aplicacio, hom ha de utilitzar la següent versio de python i els següents paquets:

-Versió python 
Python 3.6

- Paquets:
Django==2.0.4
Pillow==5.0.0
pytz==2018.4

Els paquets tambe poden trobar-se en el mateix format en l'arxiu requeriments.

A continuació descriurem els models emprats en el projecte:

# Models

S'han definit els seguents models:

- Meme
- Comentari
- Vot
- Tag
- Usuari

En relacio al esquema inicial proposat, aquest ha quedat modificat per a adecuarse als requeriments i les esmenes expressades en la correcio de la primera activitat: Pre-assignment.

El esquema final ha estat aquest: 

![](https://github.com/ferranmartinezlleida/WebMemeProject/blob/master/Diagrama%20UML.png)


A continuació s'explica el rol que cadascu empren i els seus atributs, aixi com les relacions que mantenen entre ells a partir de la implementacio de certes opcions natives de django en aquests ultims. 

# Meme
Atributs:
- title (CharType)
- image (Image Type)
- author (Foreign key, User,null=False)

L'atribut Title: s'empra per al titol a acompanyar al mem. L'atribut image: s'empra per a guardar el mem en si (Per aixo em fet servir el pck Pillow). L'atribut author s'empra per a associar el mem a un usuari segons la relació 1-to-Many, descrita a Django Docs, es null=False perque un MEM sempre ha d'estar creat per un usuari. 


# Comentari
- author (Foreign key, User,null=False)
- title (CharType)
- text (CharType)
- commented_meme(Foreign key, Meme,null=True)
- commented_comment(Foreign key, self,null=True)

 L'atribut author s'empra per a associar el mem a un usuari segons la relació 1-to-Many, descrita a Django Docs, es null=False perque un comentari sempre ha d'estar creat per un usuari. Els atributs title i text son per a conformar el comentari i el seu titol. Commented_meme i commented_comment s'utilitzen per a relacionar el comentari o be recursivament amb ell mateix o amb un Mem, amb relacions 1-to-Many. Aquest ultims atributs son null=True perque un comentari nomes pot estar associat o be a un MEM o a un altre comentari, d'aquesta forma podrem ficar null segons pertoqui. 

# Vot
- author (Foreign key, User,null=False)
- voted_meme (Foreign key, Meme,null=False)
- value (positive:1,negative:2)

L'atribut author s'empra per a associar el mem a un usuari segons la relació 1-to-Many, es null=False perque un vot sempre ha d'estar creat per un usuari. Voted_meme relaciona el vot amb un mem en concret tambe amb 1-to-Many. Value s'empra per a indicar si el vot es positiu o negatiu utilitzant eines natives de django. 

# Tag
- name (CharType)
- tagged_memes(Many-to-Many, Meme)

Name s'utilitza per a donar-li un nom al Tag. Tagged_memes utilitza eines natives de Django per a representar una relacio de Many-to-Many amb Mem (Un MEM pot tenir molts tags i un tag pot estar associat a molts MEMS).

