import json
import os
from random import choice

import aiml

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
# k.learn("test.aiml")

if os.path.isfile("bot_brain.brn"):
    k.bootstrap(brainFile="bot_brain.brn", learnFiles='test.aiml')

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
# k.respond("load aiml b")

# with open('interlocutori.json', 'r') as f:
#     iloc_list = json.load(f)
#     print('Avatare disponibile')
#     print('-------------------')
#     for iloc in iloc_list:
#         print(iloc['nume'], str(iloc['varsta'])+' ani', iloc['ocupatie'])
#     ales = False
#     names = [iloc['nume'] for iloc in iloc_list]
#     avatar = input('Nume: ').strip()
#     if avatar in names:
# while not ales:
#     print()
#     avatar = input('Alege: ')
#     if avatar in names:
#         ales = True

######  INITIATIVA - TO DO  ###########
######  RECUNOASTERE - TO DO ##########
######  SALVARE INFO - TO DO ##########


avatar = input('Nume: ').strip()
nume = k.getPredicate('nume',avatar)
k.setPredicate('nume',nume,avatar)
topics = ['varsta','ocupatie']

if nume: k.setPredicate('topic',choice(topics),avatar)
else: k.setPredicate('topic',choice(topics.append('nume')),avatar)

# varsta = k.getPredicate('varsta',avatar)
# ocupatie = k.getPredicate('ocupatie',avatar)
varsta = ''
ocupatie = ''
# Loop forever, reading user input from the command
# line and printing responses.
# TO STOP: Ctrl-D on Win
while True:
    try:
        res = input(avatar + " (tu): ")

        varsta = k.getPredicate('varsta',avatar)
        cat_varsta = k.getPredicate('catvarsta',avatar)

        if varsta and not cat_varsta:
            varsta = int(varsta)
            if 3 <= varsta <= 17: cat_varsta = 'copil'
            elif 18 <= varsta <= 40: cat_varsta = 'tanar'
            else: cat_varsta = 'pensionar'
            k.setPredicate('catvarsta',cat_varsta,avatar)

        ocupatie = k.getPredicate('ocupatie',avatar)
        # if varsta and nume and not ocupatie:
        # if ocupatie: pass
        nume = k.getPredicate('nume',avatar)

        topics = [nume, varsta, ocupatie]
        # daca avem datele min necesare incheiem dialogul
        if all(topics): print('Robi (bot): '+'ok ne-auzim :D'); break

        print('Robi (bot): ' + k.respond(res, avatar))
    except EOFError:
        k.saveBrain('bot_brain.brn')
        break
