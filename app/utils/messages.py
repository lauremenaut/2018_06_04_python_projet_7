#! /usr/bin/env python3
# coding: utf-8

""" Set messages GrandPy randomly uses to answer the user query """

ADDRESS_SUCCESS_MESSAGES = [
    "GrandPy : Hum ... oh oui, je me souviens ! Tu trouveras ça au ",
    "GrandPy : Bien sûr, voici l'adresse : ",
    "GrandPy : Dans mes souvenirs, c'est au ",
    "GrandPy : Aussitôt demandé, aussitôt trouvé ! Ce que tu cherches est au ",
    "GrandPy : Il me semble que ça se trouve au "
    ]

PARSER_FAILURE_MESSAGES = [
    "GrandPy : Dis-moi ça plus clairement s'il te plait !",
    "GrandPy : Je n'ai pas compris ! Que dis-tu ?",
    "GrandPy : Ça ne me dit rien, pourrais-tu être plus clair ?",
    "GrandPy : Pardon ? Je n'ai pas compris !",
    "GrandPy : Répète-moi ça en bon français STP ;-) ?"
    ]

ADDRESS_FAILURE_MESSAGES = [
    "GrandPy : Oh oui, ça me dit vaguement quelque chose, mais impossible de \
me souvenir de l'adresse ...",
    "GrandPy : Je m'excuse, je ne me souviens pas où cela se trouve :-/",
    "GrandPy : Oh, j'ai beau réfléchir, je ne me souviens plus de cette \
adresse ...",
    "GrandPy : Je suis vraiment désolé, j'ai oublié où cela se trouve ...",
    "GrandPy : C'est que je me fais vieux ... impossible de me rappeler de \
cette adresse :-/"
    ]

SUMMARY_SUCCESS_MESSAGES = [
    "GrandPy : En parlant de ça, j'avais une petite chose à te raconter ... ",
    "GrandPy : A ce sujet, savais-tu cela ? ",
    "GrandPy : D'ailleurs, cela me rappelle quelque chose ... ",
    "GrandPy : Au fait, cela me rappelle un souvenir ! ",
    "GrandPy : Maintenant que tu m'y fais penser ... "
    ]

SUMMARY_FAILURE_MESSAGES = [
    "GrandPy : Par contre, c'est bien un des rares endroits au sujet duquel je\
 n'ai rien à raconter ;-) !",
    "GrandPy : Curieusement, ma mémoire me fait défaut, je n'ai pas d'anecdote\
 à raconter à ce sujet ... ",
    "GrandPy : Mais cela fait trop longtemps que je n'y suis pas allé ... j'ai\
 oublié toutes mes petites histoires à ce sujet ! ",
    "GrandPy : Dommage, je n'ai pas d'anecdote concernant cet endroit à \
raconter ...",
    "GrandPy : Pas de chance, aucune histoire ne me revient en tête à ce sujet\
 :-/"
    ]

NEXT_QUESTION_MESSAGES = [
    "GrandPy : As-tu autre chose à me demander ?",
    "GrandPy : Puis-je encore quelque chose pour toi ?",
    "GrandPy : Encore une question ?",
    "GrandPy : N'hésite pas si tu as besoin d'autre chose, je suis là !",
    "GrandPy : As-tu encore besoin de moi ?"
    ]
