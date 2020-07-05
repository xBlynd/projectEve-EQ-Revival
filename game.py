from random import randint


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



# this keeps the game running while the code below continues
while game_running:

    #counter.  Counts the rounds .
    counter = 0
    # at the end of the game this starts a new round.  1st Round Loop
    new_round = True
    #disctionary
    player = {
        'name': 'Eve',
        'attack': 13,
        'heal': 16,
        'health': 100
    }
    monster = {
        'name': 'Drakus',
        'attack_min': 10,
        'attack_max': 20,
        'health': 100
    }

    #added to help with the error on function before variable.  IDK why this works....
    print(calculate_monster_attack(monster['attack_min'], monster['attack_max']))


    # Player name input.  Should find a way to add this before the game starts.  Follow suit with stats page
    print('---' * 8)
    print('Enter player name')
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

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
            monster['health'] -=  player['attack']
            if monster['health'] <= 0:
                player_won = True
            # 
            else:
                player['health'] -= calculate_monster_attack(monster['attack_min'], monster['attack_max'])
                if player['health'] <= 0:
                    monster_won = True


        # the elif is if player input picks option 2.  This initates the heal.
        elif player_choice == '2':
            player['health'] += player['heal']

            # Radommize added to attack
            monster_attack = randint(monster['attack_min'], monster['attack_max'])
            player['health'] -= calculate_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
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

        if player_won == False and monster_won == False:
            print('###' * 8)
            print(f'{player["name"]} has {player["health"]} left')
            print(f'{monster["name"]} has {monster["health"]} left')
            print('###' * 8)
        

        #functions for the winner announements from above.  Game ending conditions
        elif player_won:
            game_ends(player['name'])
            # captures the game results for stat board
            round_result = {'name': player['name'], 'health': player['health'],'round': counter}
            game_results.append(round_result)
            new_round = False

        elif monster_won:
            game_ends(monster['name'])
            # captures the game results for stat board
            round_result = {'name': monster['name'], 'health': monster['health'], 'round': counter}
            game_results.append(round_result)

            new_round = False

         #New Round function from above
        if player_won == True or monster_won == True:
            new_round = False

