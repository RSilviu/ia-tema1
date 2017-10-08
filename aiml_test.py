import json

import aiml

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("test.aiml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
# k.respond("load aiml b")

with open('interlocutori.json', 'r') as f:
    iloc_list = json.load(f)
    print('Avatare disponibile')
    print('-------------------')
    for iloc in iloc_list:
        print(iloc['nume'], str(iloc['varsta'])+' ani', iloc['ocupatie'])
    ales = False
    names = [iloc['nume'] for iloc in iloc_list]
    avatar = ''
    while not ales:
        print()
        avatar = input('Alege: ')
        if avatar in names:
            ales = True
    # Loop forever, reading user input from the command
    # line and printing responses.
    while True: print(k.respond(input("> "), avatar))