# import only system from os 
import os

from random import randint
import time
import json

# this turns the game persistant.  
game_running = True
# stat manager
game_results = []

# this will be used to calculate the random attack from the monsters.
def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

# Winner annoucement Function
def game_ends(winner_name):
    print(f'{winner_name} won the game')
    print('projectEve is made with ', u"\u2661")

# Loads the local storage into memory
def loadLocalStorage():
    localStorageFilename = 'localstorage.json'
    try:
        with open(localStorageFilename, 'r') as infile:
            return json.load(infile)
    except Exception as e:
        print(f'Error loading: {e}')
        return None

# Saves the local storage back into memory
# Do your code here pliz
def saveLocalStorage(obj):
    saveStorageFilename = 'localstorage.json'
    try:
        # Save here
        with open(saveStorageFilename, 'w') as outfile:
            json.dump(obj, outfile, indent=4)

    except Exception as e:
        print(f'Failed to save file: {e}')

# this keeps the game running while the code below continues
while game_running:

    #counter.  Counts the rounds .
    counter = 0
    # at the end of the game this starts a new round.  1st Round Loop
    new_round = True
    #disctionary

    # Load data and make sure it exists
    # gameData = loadLocalStorage()    //this line has been removed until storage is functioning correctly
    gameData = loadLocalStorage()
    if 'player' not in gameData:
        gameData['player'] = {
            'name': 'Eve',
            'attack': 13,
            'heal': 16,
            'health': 100
        }
    if 'monster' not in gameData:
        gameData['monster'] = {
            'name': 'Drakus',
            'attack_min': 10,
            'attack_max': 20,
            'health': 100
        }

    #added to help with the error on function before variable.  IDK why this works....
    # print(calculate_monster_attack(gameData['monster']['attack_min'], gameData['monster']['attack_max']))


    # Player name input.  Should find a way to add this before the game starts.  Follow suit with stats page

    print('projectEvolved Boss Battle!')
    print('---' * 8)
    gameData['player']['name'] = input('Enter Name: ')

    print(f'{gameData["player"]["name"]} has {gameData["player"]["health"]} health')
    print(f'{gameData["monster"]["name"]} has {gameData["monster"]["health"]} health')

    # keeps the game running while the conditions below are running.  Second (y) round loop
    while new_round:
        
        #counter adds +1 per round.
        counter = counter + 1
        player_won = False
        monster_won = False

        #prints input options.  Has to be a better way to do this.
        print('---' * 8)
        print('Please select action')
        print('---' * 8)
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Show Results')
        print('---' * 8)


        # input method from options above
        player_choice = input()


        #attack this monster
        if player_choice == '1':
            gameData['monster']['health'] -= gameData['player']['attack']
            if gameData['monster']['health'] <= 0:
                player_won = True
            else:
                gameData['player']['health'] -= calculate_monster_attack(gameData['monster']['attack_min'], gameData['monster']['attack_max'])
                if gameData['player']['health'] <= 0:
                    monster_won = True


        # the elif is if player input picks option 2.  This initates the heal.
        elif player_choice == '2':
            gameData['player']['health'] +=gameData['player']['heal']

            # Radommize added to attack
            monster_attack = randint(gameData['monster']['attack_min'], gameData['monster']['attack_max'])
            gameData['player']['health'] -= calculate_monster_attack(gameData['monster']['attack_min'], gameData['monster']['attack_max'])
            if gameData['player']['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False
            print('---' * 8)
            print('See you soon dick.. Bye!')

        # Input option 4 to print the previous game results.  Need to put this before the game starts.  Should be able to see before join game
        elif player_choice == '4':
            for player_stats in game_results:
                print(player_stats)
        
        # if the user inputs a invalid options.  This will return a message
        else:
            print('not a option try again.')

        if (not player_won) and (not monster_won):
            os.system('cls')
            print('###' * 8)
            print(f'{gameData["player"]["name"]} has {gameData["player"]["health"]} left')
            print(f'{gameData["monster"]["name"]} has {gameData["monster"]["health"]} left')
            print('###' * 8)
        

        #functions for the winner announements from above.  Game ending conditions
        elif player_won:
            os.system('cls')
            game_ends(gameData['player']['name'])
            # captures the game results for stat board
            round_result = {'name': gameData['player']['name'], 'health': gameData['player']['health'],'round': counter}
            game_results.append(round_result)
            time.sleep(5)
            new_round = False

        elif monster_won:
            os.system('cls')
            game_ends(gameData['monster']['name'])
            # captures the game results for stat board
            round_result = {'name': gameData['monster']['name'], 'health': gameData['monster']['health'], 'round': counter}
            game_results.append(round_result)
            time.sleep(5)
            new_round = False

         #New Round function from above
        if player_won == True or monster_won == True:
            new_round = False
