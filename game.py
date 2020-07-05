
#disctionary
player = {
    'name': 'Eve',
    'attack': 20,
    'heal': 16,
    'health': 100
}

monster = {
    'name': 'Drakus',
    'attack': 12,
    'health': 100
}

# this turns the game persistant.  
game_running = True

# this keeps the game running while the code below continues
while game_running == True:

    # at the end of the game this starts a new round.  
    new_round = True

    # keeps the game running while the conditions below are running
    while new_round == True:
            
        player_won = False
        monster_won = False

        #prints input options.  Has to be a better way to do this.
        print('Please select action')
        print('1) Attack')
        print('2) Heal')

        # input method from options above
        player_choice = input()


        #attack this monster
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True

            else:
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0:
                    monster_won = True

            #random print check to test functions.  Remove later
            print('You attacked', monster['health'])

        # the elif is if player input picks option 2.  This initates the heal.
        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            print('Healed')
            print(player['health'])
        
        # if the user inputs a invalid options.  This will return a message
        else:
            print('not a option try again.')

        #if player won or lost round.  run new_round
        if player_won == True or monster_won == True:
            new_round = False

