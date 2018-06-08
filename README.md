# MemeProject
Meme Project

Aquest projecte ha estat creat amb la finalitat de donar satisfaccio als requeriments expressats en la primera entrega de l'assignatura Projecte Web. El projecte representa la base per la que ha de ser una web creada amb la finalitat de donar servei a una communitat de creacio i intercanvi de MEMS.

Per tal de llençar adecuadament la aplicacio, hom ha de utilitzar la següent versio de python i els següents paquets:

Versió python 
- Python 3.6

Paquets:
-behave==1.2.6
-Django==2.0.4
-parse==1.8.2
-parse-type==0.4.2
-Pillow==5.0.0
-pytz==2018.4
-selenium==3.12.0
-six==1.11.0
-splinter==0.8.0


Els paquets tambe poden trobar-se en el mateix format en l'arxiu requeriments.

Per tal d'accedir a les funcions d'administrador, hom ha d'accedir a l'url /admin i utilitar:

- usuari: admin
- contrasenya: qwer1234

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
- author (Foreign key, User, null=False)
- tag (Foreign key, Tag, null=True)

L'atribut Title: s'empra per al titol a acompanyar al mem. L'atribut image: s'empra per a guardar el meme en si (Per aixo em fet servir el pck Pillow). L'atribut author s'empra per a associar el mem a un usuari segons la relació 1-to-Many, descrita a Django Docs, es null=False perque un MEME sempre ha d'estar creat per un usuari. L'atribut tag s'empra per a poder saber la categoria a la que recau el mem

# MemeComment
Atributs:
- author (Foreign Key, User, null=False)
- title = (CharType)
- text = (CharType)
- commented_meme (Foreign Key, Meme, null=True)

Aquest model s'utilitza per a poder comentar els mems.
L'atribut author s'empra per a associar el mem a un usuari segons la relació 1-to-Many, descrita a Django Docs, es null=False perque un comentari sempre ha d'estar creat per un usuari. Els atributs title i text son per a conformar el comentari i el seu titol. Commented_meme s'utilitza per a relacionar el comentari a un Mem, amb relacions 1-to-Many. Aquest ultims es null=True perquè un comentari només pot estar associat a un MEM, d'aquesta forma podrem ficar null segons pertoqui. 

# CommentComment
Atributs:
- author (Foreign Key, User, null=False)
- title = (CharType)
- text = (CharType)
- related_comment (Foreign Key, Meme, null=True)

Aquest model és molt similar a MemeComment però comentant comentaris enlloc de mems. 
En aquest cas, related_comment s'utilitza per relacionar el comentari a un altre comentari, amb relacions 1-to-Many ja que un comentari pot estar comentat per molts comentaris, d'igual forma que un mem.


# Vot
Atributs:
- author (Foreign key, User,null=False)
- voted_meme (Foreign key, Meme,null=False)
- value (positive:1,negative:2)

L'atribut author s'empra per a associar el mem a un usuari segons la relació 1-to-Many, es null=False perque un vot sempre ha d'estar creat per un usuari. Voted_meme relaciona el vot amb un mem en concret tambe amb 1-to-Many. Value s'empra per a indicar si el vot es positiu o negatiu utilitzant eines natives de django. 

# Tag
Atributs:
- tags (PositiveIntegerType)

L'atribut tags s'utilitza per a poder relacionar un tag a un mem, amb relació 1-to-Many, ja que un tag pot tenir molts mems associats






# Project: Part 2

En aquesta part s'han afegit noves característiques, tals com Web 2.0 (en el nostre cas, la possibilitat de que els usuaris crein i esborrin mems i comentaris). També la llibertat d'afegir tags als mems, de votar els mems (de forma que un usuari pot tenir com a molt un vot ja sigui positiu o negatiu associat a un mem) i finalment es pot buscar mems gràcies al buscador.

# Projecte: Part 3

En aquesta part del projecte s'ha modificat el template meme.html i s'han utilitzat tags com name, genre, text, etc. Basant-se amb schema.org.

