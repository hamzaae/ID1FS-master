C’est quoi ID1FS ?
ID1FS est un système de fichier distribué permettant de stocker et de récupérer des fichiers en un temps record. Il se compose d'un maître que nous donnerons le nom du « FATHER MASTER » qui contient les métadonnées, et de plusieurs esclaves que nous donnerons le nom du  « CHILDS » qui contient les données réelles du fichier et un client pour l'interaction entre les deux.
Notre système est capable de gérer des milliers de  « childs » sans intervention d’un opérateur. Il permet de bénéficier simultanément des avantages du computing parallèle et du computing distribué. Les fichiers logs pour stocker un historique des événements survenus sur notre serveur. ID1FS fait des réplications des données en cas de panne ou d'erreur matérielle. Pour la communication entre nos composants, on a utilisé RPYC qui est une bibliothèque python transparente pour les appels de procédure à distance symétriques et distribué, tel que les objets distants peuvent être manipulés comme s'ils étaient locaux.


Exigences :

 •  Pour que notre ID1FS soit bien prêt pour vous, vous devez tout simplement lancer le Setup (ID1FS /config/setup.py) puis modifier le fichier config (ID1FS /config/ID1FSconfig.conf)
 •  Ensuite pour que notre ID1FS soit plus sécuriser,  les commandes sensibles «ID1fs put, ID1FS get, ID1FS remove et ID1FS chpass » nécessite un password qui est par default  « id1fs » et après tu peux le changer à partir du commande « ID1FS chpass »
 •  Afin de savoir tous les commandes possibles dans ID1FS vous pouvez taper la commande «  ID1FS help »
 •  Il faut toujours être placé dans le dossier ID1FS pour lancer les commandes. 
