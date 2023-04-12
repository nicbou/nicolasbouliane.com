---
title: Réglez l'erreur #1046 dans phpMyAdmin
description: L'erreur "#1046: No database selected" qui se produit lors de l'importation d'une base de données dans phpMyAdmin est facile à régler. Voici la solution facile à un problème commun chez les nouveaux utilisateurs de WampServer et de XAMP.
date_created: 2010-11-05
---

Voici la solution simple à l'erreur "#1046: No database selected" pendant une importation dans phpMyAdmin

## Solution #1: Avant l'importation

Dans phpMyAdmin, cliquez sur l'onglet *Export* depuis l'accueil et non quand vous êtes dans la base de données à exporter. Le programme s'assure ainsi de créer la base de données et de la sélectionner avant d'y ajouter les tables. Cette solution ne s'applique pas aux hébergeurs partagés puisqu'ils restreignent les noms possibles pour vos bases de données.

## Solution #2: L'alternative

1. Créez la base de données sur le serveur cible et notez le nom
2. Ouvrez votre fichier .sql avec un éditeur de texte.
3. Insérez la ligne suivante juste avant le premier CREATE TABLE dans le fichier .sql: `USE votrebasededonnees;`
4. Enregistrez votre fichier. Il est désormais prêt à importer sur le nouveau serveur.

