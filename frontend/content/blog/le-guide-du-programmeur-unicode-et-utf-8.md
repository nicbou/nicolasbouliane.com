---
title: Le guide du programmeur: Unicode et UTF-8
description: Vous êtes-vous demandé ce que signifie ASCII? UTF-8? ISO 8859-1? Voici comment ça fonctionne.
date_created: 2015-04-30
---

Cet article est le tout premier d'une série sur la programmation. Il est adressé aux programmeurs débutants et intermédiaires qui cherchent à approfondir leur compréhension de l'informatique.

Vous êtes-vous demandé ce que signifie ASCII? UTF-8? ISO 8859-1? Si vous travaillez avec des données textuelles, ils vous sont sans doute familiers, et vous avez probablement une idée nébuleuse de leur signification. Il s'agit de termes reliés à l'*encodage* de caractères. Si vous avez à traiter des données textuelles: chaînes de caractères, bases de données ou fichiers HTML, une bonne compréhension des différentes méthodes d'encodage vous sera primordiale.

## Tout commence avec ASCII

La table de caractère ASCII, avec laquelle vous êtes possiblement familiers, contient les caractères principaux de l'alphabet latin de base: les 26 lettres de l'alphabet, les chiffres et quelques symboles de base. Au total, on y compte 128 caractères numérotés de 0 à 127. Le caractère #65, un 'a' majuscule, peut être représenté en binaire comme suit: 01000001. Comme il y a seulement 128 caractères, il est donc possible de représenter chaque caractère avec 7 bits, soit moins d'un octet.

Ainsi, les lettres du mot 'bonjour' étaient encodées de la façon suivante:

`01100010` `01101111` `01101110` `01101010` `01101111` `01110101` `01110010`

## Les choses se gâtent

Toutefois, il manque des caractères à cette table: les caractères accentués (éàÊöÙ) et les caractères cyrilliques (тро́йка), parmi tant d'autres, doivent aussi être représentés. Comme les 127 caractères ASCII utilisent seulement 7 bits, il reste de l'espace pour 128 caractères dans notre octet:

`0000 0000` à `0111 1111`: les 128 caractères ASCII de base

`1000 0000` à `1111 1111`: 128 caractères spéciaux

Selon la palette de caractères sélectionnée, ces 128 derniers caractères pouvaient être des caractères cyrilliques, des symboles, des lettres grecques etc.,

Ce système fort audacieux frappait un mur lorsqu'un Français envoyait un message à un ami Russe: l'*étrange péripétie* de Jacques devenait une *йtrange pйripйtie* pour Sasha, parce que le caractère #233 était un 'é' dans la table latine, et un 'й' dans la table cyrillique. C'était encore pire pour les pays asiatiques qui utilisent plusieurs milliers de caractères - beaucoup trop pour entrer dans un seul octet. Dans un contexte mondial, cette solution n'était que temporaire.

## Entre Unicode

La solution à ce problème arrive en deux parties. D'abord, parlons d'Unicode. Contrairement à ASCII qui dicte comment encoder chaque lettre de son alphabet limité, Unicode est seulement une table de caractères.

Comme la table Unicode comporte quelques 110 000 caractères, glyphes et symboles, il est impossible de représenter la majorité des caractères à l'intérieur de deux ou trois octets. UCS-2, une méthode d'encodage maintenant obsolète, utilisait deux octets pour chaque caractère, et pouvait donc représenter plus de 65 000 caractères. Il fallait cependant deux fois plus d'espace qu'avec ASCII pour stocker la même longueur de texte. Heureusement, il existe une ingénieuse méthode d'encodage beaucoup plus compacte pour les caractères Unicode: **UTF-8**.

## UTF-8: l'encodage compact

Contrairement à son prédécesseur, UTF-8 n'utilise que l'espace dont il a besoin pour un caractère. Cela signifie donc que certains caractères n'utilisent qu'un seul octet, et d'autres deux, trois et même quatre. UTF-8 utilise les mêmes codes qu'ASCII pour les 127 premiers caractères, et se sert d'octets additionnels pour représenter des caractères spéciaux comme 'É', '¤' ou '¢'.

Par exemple, le caractère Z serait représenté de la même façon qu'en ASCII: `01011010`

Toutefois, le caractère ¢ devra être représenté en deux octets, car il ne fait pas partie des 127 caractères originaux: `11000010 10100010`

L'encodage d'un caractère multi-octet se fait comme suit:

1. Les premiers bits identifient le nombre d'octets à utiliser. `110xxxxx` signifie que le caractère fait deux octets de long, `1110xxxx` signifie trois octets, `11110xxx` quatre octets, etc. S'il fait un seul octet, il sera plus petit que 127, et commencera inévitablement par un 0.
2. Les premiers bits des octets subséquents de ce caractère commencent par `10xxxxxx` pour identifier qu'ils ne sont pas des caractères individuels.
3. Les bits restants sont utilisés pour représenter le numéro du caractère.

Dans l'exemple suivant, on représente le caractère #8364, '€'.

1. Nous aurons besoin de trois octets, donc notre premier octet commencera par `1110`: `1110xxxx 10xxxxxx 10xxxxxxx`
2. La représentation binaire de 8364 (notre caractère) est **`00100000 10101100`**
3. Nous entrons ce code à l'intérieur de nos trois octets. Le code binaire représentant 8364 est en gras: 1110<span><strong>0010</strong></span> 10<span><strong>000010</strong></span> 10<span><strong>101100</strong></span>.

Nous pouvons ainsi représenter un nombre infini de caractères en utilisant des octets additionnels, mais le véritable avantage d'UTF-8 reste qu'il utilise un minimum de bytes pour représenter chaque caractère, limitant ainsi l'espace nécessaire pour les stocker.

## De ASCII à UTF-8 et vis-versa

Un autre avantage d'UTF-8 est qu'il est rétrocompatible avec ASCII, car il utilise les mêmes codes pour les 127 premiers caractères. Ainsi, un document écrit en ASCII peut être ouvert en UTF-8. Toutefois, s'il y a des caractères spéciaux dans le document, ils seront remplacés par un �, car il n'y a pas de caractère Unicode aux adresses 128 à 255, qui sont utilisées pour les caractères spéciaux en ASCII. Inversement, si on convertit un caractère UTF-8 en ASCII, vous aurez un résultat comme 'Ã¤', car le caractère 'ä', représenté en UTF-8 par `11000011 10100100`, fait plusieurs octets de long, et qu'ASCII essaie de décoder chaque octet comme un caractère individuel.

Pour un guide plus complet sur Unicode, je recommande [le livre O'Reilly sur Unicode](http://amzn.to/2fCgLB2). N'hésitez pas à poser des questions dans les commentaires.

