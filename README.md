# AiScores
AiScores est un programme de **calcul**, de **statistiques,** de **conversion**, et de 
**partage** de notes.

# AiGraphs
AiGraphs es un programme de **graphiques** et de **statistiques** sur des notes.

## Comment utiliser?

Tout d'abord, il faut télécharger un programme de gestion des installations, décompilations, et mises à jour automatiques de AiScoires et de ses annexes.
*Il y a deux versions : une qui peut être exécutée de n'importe où, et une autre seulement depuis un IDE installé sur le PC.*

Version exécutable partout [COPIER](https://raw.githubusercontent.com/TechnoSpiritMC/AiXtentions/main/ExtentionsLtrs.py?token=GHSAT0AAAAAACAAMGMDHMCSYYMS65WANRNWZBP25FQ)     *python 3.2 minimum, python 3.10 recommandé, dernière version : 1.0*\
Version exécutable via IDE [COPIER](https://raw.githubusercontent.com/TechnoSpiritMC/AiXtentions/main/ExtentionsArrws.py?token=GHSAT0AAAAAACAAMGMDQ4F2GPXSRL2TEMF4ZBP26BA)     *python 3.2 minimum, python 3.10 recommandé dernière version : 1.0.2*

## Installer l'extension AiScores et/ou AiGraphs

Une fois installé, le programme doit être exécuté. Une fois lancé, il va vous proposer un menu:

    EXTENTIONS INSTALLÉES: 
    Extention de test            :  NON 
    Extention AiScores           :  NON 
    Extention AiTrainer          :  NON 
    Extention AiGraphs.console   :  NON 
    Extention AiGraphs.turtle    :  NON 
    Que voulez vous faire avec ces 0 extention(s)? Les CHARGER (c) les INSTALLER (i) ou UTILISER CELLES DEJA INSTALLÉES (u) 
Ce qui suit les `:` peut varier selon si vous avez déjà installé des extensions. Si vous avez au moins un `NON`, alors, faites `[i]`, puis `[ENTRÉE]`. Le programme va alors aller télécharger les dernières versions des extensions manquantes, et va aussi lors que ce sera fini, vous proposer si vous voulez mettre à jour les extensions déjà installées.

    Action en cours: tentative de téléchargement des 5 extentions absentes 
    100% - __________  
    Opération effectuée en 0.99623 secondes avec succès.

\***

Une fois fait, relancez le programme et vous verrez que le(s) ancien(s) `NON` se sont transformés en `OUI`. Si ce n'est pas le cas, cherchez la résolution du problème dans la partie **Résolution de problèmes.**

    EXTENTIONS INSTALLÉES: 
    Extention de test            :  OUI 
    Extention AiScores           :  OUI 
    Extention AiTrainer          :  OUI 
    Extention AiGraphs.console   :  OUI 
    Extention AiGraphs.turtle    :  OUI 

\***

Maintenant que vous avez installé l'extension AiScores, il faut la dé-compiler. Le programme va s'en charger tout seul, il faut juste faire `[c]` puis `[ENTRÉE]`.

    c
    Action en cours: tentative de chargement des 5 extentions disponnibles 
    100% - __________  Opération effectuée en 0.0 secondes avec succès.
Le temps indiqué (`Opération effectuée en `**0,0**` secondes`) peut changer suivant votre connexion.

Maintenant, cherchez dans vos fichiers, vous devez avoir un fichier qui ressemble à cela: `AiScores.py`

# AiScores

Lancez le programme. Il va vous dire `Faites entrée pour rentrer dans le programme.`, il faut faire entrée sauf si vous voulez avoir des informations complémentaires sur le programme, notamment sur sa version. *Cette fonctionnalité sera ajoutée dans une prochaine mise à jour du programme*.

Commandes:\
`AiScores -i version`           -> savoir la version du programme.\
`AiScores -iL version`         -> savoir la dernière version disponible du programme.\
`AiScores -u <param>`			 -> mettre à jour votre programme manuellement (*"param" doit être remplacé par: soit "official" pour obtenir une version complète, ou alors "snapshot" pour obtenir la dernière version, mais qui peut contenir des erreurs*.

Si vous voulez ignorer cette étape, faites juste `[ENTRÉE]`. Le programme va ensuite vous dire ceci:

    Choisissez une option : ajouter une évaluation, ou entrer et recalculer une note? Écrivez 'entrer' ou 'ajouter'.
    Écrivez 'entrer' ou 'ajouter'. Tout abus sera sanctionné     -> 
## Ajouter un contrôle
Si vous êtes un professeur, et que vous voulez ajouter un contrôle, écrivez sur votre clavier `ajouter`, puis, faites `[ENTRÉE]`. Attention, le mot ajouter n'est **pas** obligé d'avoir l'orthographe exacte. Il **peut** être écrit "ajt". 

Une fois fait, le programme va vous demander:
`Merci d'entrer le nombre sur combien est votre note (Maximum : 2.343700e+08)`. Il faut alors entrer sur combien votre contrôle est. Il ne doit pas dépasser le maximum, dans ce cas, `2.343700e+08`. Pour l'exemple, j'ai mis 25.\
Attention, le maximum est amené à changer entre chaque utilisation, et entre chaque utilisateur\
Attention, même si la note maximum du contrôle **peut** être un nombre à virgules, le nombre sera arrondi lors de l'entée des notes.

\
Puis, le programme va demander votre nom:
`Merci d'entrer votre nom sans le Mr/Mme (Desjardins)`. Il sera utilisé pour être formaté dans l'id du contrôle, et, sera affiché lors de l'ajour d'une note par un élève. Pour l'exemple, j'ai mis "Quelqun". Attention, merci de ne pas mettre dans votre nom les caractères énumérés dans la liste suivante:

 \- Nombres\
 \- Caractères spéciaux\
 \- Espaces\
 \- Traits d'union\
 \- Et tout autre symbole n'étant pas une lettre minuscule ou majuscule.



Puis, le programme va composer l'ID unique pour votre contrôle. Voici un exemple d'ID qui peut être généré:
`Aeovaex-25.0+368`.

### Cas spéciaux:
Il existe des arrangements de lettres qui peuvent former des mots familiers, insultants, et autres mots indésirables. Ces ID sont bloqués automatiquement. Si vous découvrez un ID rentrant dans cette catégorie mais qui n'est **pas** automatiquement bloqué, merci d'adresser un mail à "contactaiscores@gmail.com"

## Entrer une note
Pour entrer une note, lors du démarrage du programme, écrivez sur votre clavier `entrer`, puis, faites `[ENTRÉE]`. Attention, le mot entrer n'est **pas** obligé d'avoir l'orthographe exacte. Il **peut** être écrit "ent". 

Une fois fait, le programme va vous demander:
L'`Id de l'évaluation`. Il vous faut alors entrer l'ID du contrôle, noté (normalement) en haut de votre copie. Il doit ressembler à quelque chose comme ça : `Abcdefg-25.3+349`. Attention, l'ID doit être copié au **symbole près**.

Puis, le programme va demander la note que vos avez eu à ce contrôle:\
`Votre note du contrôle par Mr/Mme Quelqun sur 125 :`\
Attention, le nom et la note sont amenés à changer en fonction du contrôle. Merci de mettre votre vraie note et pas ce que vous auriez aimé avoir.

Une fois votre note rentrée, le programme va automatiquement vous la convertir en note sur 5, sur 10, sur 20, et en pourcentage de réussite. Ici, pour l'exemple, j'ai mis 53 sur 125:

    Avec une note de 53.0 sur 125
                2.12 sur 5
                4.24 sur 10
                8.48 sur 20
                Et vous avez réussi
     : 42.4 % du contrôle 
Attention, votre note **peut** être un nombre à virgule (19.25). Cependant, la virgule doit être remplacée par un point. Mais ne peut pas être une fraction (1925/100).

### Note imporante:
Pour l'instant, AiScores ne marche seulement avec les ID. Les parties 
- moyennes
- statistiques
- parage

ne sont pas disponibles. Seulement la partie calcul l'est.

# AiGraphs
Il existe deux versions de AiGraphs. Une, `AiGraphs.turtle`, qui doit être exécutée sur VSC ou sur tout autre IDE. Et l'autre, `AiGraphs.console`, peut être exécutée de n'importe ou.

Pou l'instant, ce programme est sous "développement intensif", donc indisponible au public.

# Résolution de prolemmes fréquents:

## AiXtentions
### Connexion internet:

    File "E:\AiPrograms\venv\Lib\site-packages\requests\adapters.py", line 565, in send
        raise ConnectionError(e, request=request)
    requests.exceptions.ConnectionError: HTTPSConnectionPool(host='gist.githubusercontent.com', port=443): Max retries exceeded with url: /TechnoSpiritMC/c908c04c284c6a875c04e9c776e4e987/raw/ec27d1dc9184722361bb70fd650bcf5d8cd4560b/AiTrainer_Test.aiext (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000002074873A0D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

Pour pouvoir installer les extensions, AiXtentions a besoin d'une connexion internet. Si l'erreur ci-dessus apparait, accompagnée de plein d'autres, c'est que vos n'êtes pas connectés à internet.

### Connexon internet (très) lente:

    The request timed out while trying to connect to the remote server.  
      
    Requests that produced this error are safe to retry
Pour éviter des erreurs bien rouges, bien pétantes, et bien énervantes, AiXtentions a une fonction "timeout" qui empêche une connexion de trop longue durée avec le serveur distributeur de code. Si vous avez une connexion lente, cette erreur peut arriver de nouveau.

## AiScores
### Une lettre n'est pas un chiffre:

    Traceback (most recent call last):
      File "E:\AiPrograms\AiScores and AiGraphs\AiScores.py", line 130, in <module>
        _NewTestScoreOnBase = float(
                              ^^^^^^
    ValueError: could not convert string to float: 'des letres'
AiScores n'accepte que les nombres et les nombres à virgules. Attention, cette erreur peut arriver si vous mettez un nombre à virgules: dans ce cas, remplacez le virgule par un point.

### Format d'id

    Id de l'évaluation :     dfgs546+5
    Merci de respecter le format obligatoire le l'ID.
    
    Process finished with exit code 3
Cette erreur arrive lors que l'ID ne respecte pas le format obligatoire, mais pour le savoir, analysons d'abord la structure de l'ID: `Abcdefg-123+456`\
`Abcdefg` est le nom du professeur formatté l'ayant créé.\
`-` est le séparateur entre le nom et la note maximale possible du contrôle.\
`123` est la note maximale possible de ce contrôle.\
`+` est le séparateur entre la note maximale possible et l'ID d'ID.\
`456` est l'ID d'ID (utilisé pour que un professeur puisse créer plusieurs contrôles avec la même note maximale).

Si un des séparateurs (`-` et/ou `+`) n'est pas présent, alors le programme va sortir cette erreur.

Si une erreur non listée dans cette catégorie apparait, merci de contacter contactaiscores@gmail.com.





