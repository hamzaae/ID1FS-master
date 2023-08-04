IDFS (Academic project distributed with contribution of "NADI Hanane" & "BENLEMKADEM Zakaria") is a file system built in python and shell based on HDFS architecture
-----------------------------------------------------------------------------------------------------------------------------------------------------------
[ENG]

What is ID1FS? ID1FS is a distributed file system for storing and retrieving files in record time. It consists of a master that we will name the "FATHER MASTER" which contains the metadata, and several slaves that we will name the "CHILDS" which contains the actual data of the file and a client for the interaction between both. Our system is able to manage thousands of “childs” without operator intervention. It makes it possible to simultaneously benefit from the advantages of parallel computing and distributed computing. Log files to store a history of events that have occurred on our server. ID1FS makes data replications in case of failure or hardware error. For the communication between our components, we used RPYC which is a transparent python library for symmetric and distributed remote procedure calls, such that remote objects can be manipulated as if they were local.

Requirements:

• For our ID1FS to be ready for you, you simply need to run Setup (ID1FS /config/setup.py) then modify the config file (ID1FS /config/ID1FSconfig.conf) • Then for our ID1FS to be more secure , the sensitive commands "ID1FS put, ID1FS get, ID1FS remove and ID1FS chpass" require a password which is by default "id1fs" and then you can change it from the command "ID1FS chpass" • In order to know all the possible commands in ID1FS you can type the command “ID1FS help” • You must always be placed in the ID1FS folder to launch the commands.

-----------------------------------------------------------------------------------------------------------------------------------------------------------
[FR]

C’est quoi ID1FS ?
ID1FS est un système de fichier distribué permettant de stocker et de récupérer des fichiers en un temps record. Il se compose d'un maître que nous donnerons le nom du « FATHER MASTER » qui contient les métadonnées, et de plusieurs esclaves que nous donnerons le nom du  « CHILDS » qui contient les données réelles du fichier et un client pour l'interaction entre les deux.
Notre système est capable de gérer des milliers de  « childs » sans intervention d’un opérateur. Il permet de bénéficier simultanément des avantages du computing parallèle et du computing distribué. Les fichiers logs pour stocker un historique des événements survenus sur notre serveur. ID1FS fait des réplications des données en cas de panne ou d'erreur matérielle. Pour la communication entre nos composants, on a utilisé RPYC qui est une bibliothèque python transparente pour les appels de procédure à distance symétriques et distribué, tel que les objets distants peuvent être manipulés comme s'ils étaient locaux.


Exigences :

 •  Pour que notre ID1FS soit bien prêt pour vous, vous devez tout simplement lancer le Setup (ID1FS /config/setup.py) puis modifier le fichier config (ID1FS /config/ID1FSconfig.conf)
 •  Ensuite pour que notre ID1FS soit plus sécuriser,  les commandes sensibles «ID1fs put, ID1FS get, ID1FS remove et ID1FS chpass » nécessite un password qui est par default  « id1fs » et après tu peux le changer à partir du commande « ID1FS chpass »
 •  Afin de savoir tous les commandes possibles dans ID1FS vous pouvez taper la commande «  ID1FS help »
 •  Il faut toujours être placé dans le dossier ID1FS pour lancer les commandes. 
