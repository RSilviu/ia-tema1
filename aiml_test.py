import json
import os

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
nume = k.setPredicate('nume',k.getPredicate('nume',avatar),avatar)

# varsta = k.getPredicate('varsta',avatar)
# ocupatie = k.getPredicate('ocupatie',avatar)

# Loop forever, reading user input from the command
# line and printing responses.
# TO STOP: Ctrl-D on Win
while True:
    try:
        res = input(avatar + " (tu): ")
        print('Robi (bot): ' + k.respond(res, avatar))
    except EOFError:
        k.saveBrain('bot_brain.brn')
        break
