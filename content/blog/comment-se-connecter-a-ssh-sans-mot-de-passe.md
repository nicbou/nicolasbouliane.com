---
title: Comment se connecter à SSH sans mot de passe
description: Un guide qui vous montre comment vous connecter à une machine SSH distante sans mot de passe. Utile pour les tâches planifiées avec cron.
date_created: 2012-04-21
---

Il est possible que vous ayez un jour le besoin de vous connecter sans mot de passe à un ordinateur distant. Par exemple, vous pourriez avoir besoin d'exécuter une tâche cron qui copie des fichiers entre deux machines. Pour se faire, vous devez configurez une connexion SSH sans mot de passe à l'aide de clés publiques.

Dans le scénario suivant, nous auront deux machines: machinelocale et machinedistante. La machine distante est celle à laquelle on veut se connecter sans mot de passe.

## Générer la clé RSA

Dans le terminal de machinelocale, entrez `ssh-keygen -t rsa`.

On vous demandera où placer votre clé et d'entrer une passphrase. Laissez ces champs vides.

## Copier la clé RSA

Vous devez maintenant copier la clé RSA. Utilisez la commande suivante sur machinelocale en remplaçant les informations ci-dessous par l'adresse externe et le nom d'utilisateur de votre machine distante:

`ssh-copy-id -i ~/.ssh/id_rsa.pub <strong>utilisateurdistant</strong>@<strong>machinedistante</strong>`

Vous devrez entrer le mot de passe de votre machine distante, et les clés seront ensuite copiées.

## Tester la connexion

Vous pouvez maintentant tester la connexion à l'aide de cette commande sur machinelocale (n'oubliez pas de changer les noms pour la connexion):

`ssh utilisateurdistant@machinedistante`

Vous devriez être connecté à machinedistante sans avoir à rentrer votre mot de passe. Vous pourrez donc utiliser des commandes comme `scp` sans mot de passe.

## Ça ne fonctionne pas! À l'aide!

Si on vous demande toujours un mot de passe à la connexion, ne paniquez pas. Suivez les étapes suivantes pour trouver votre problème:

1. Vérifiez votre journal d'erreurs d'authentification. Entrez la commande suivante:`tail /var/log/auth.log` sur machinedistante. Recherchez un message du genre *Authentication refused: bad ownership or modes for directory /undossier.* Si vous en avez un, c'est que vous devez corriger les permissions de ce dossier (essayez `chmod 755 <strong>undossier</strong>`). Votre dossier d'utilisateur et votre dossier .ssh ne doivent pas être avoir de permissions d'écriture pour les autres utilisateurs.
2. Vérifiez que l'authentification RSA soit activée sur machinedistante. Entrez `cat /etc/ssh/sshd_config | grep Authentication` sur machinedistante, et recherchez *RSAAuthentication yes* dans ce qui est retourné. S'il est à *no,* vous devrez le changer, enregistrer et redémarrer SSH.
3. Assurez-vous que la clé aie bien été ajoutée au fichier .ssh/authorized_keys dans votre dossier utilisateur.
4. Laissez un commentaire dans l'espoir que je sois passé par là!

