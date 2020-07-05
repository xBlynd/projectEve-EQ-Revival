

# this turns the game persistant.  
game_running = True

# this keeps the game running while the code below continues
while game_running == True:

    # at the end of the game this starts a new round.  
    new_round = True
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
    print('---' * 8)
    print('Enter player name')
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    # keeps the game running while the conditions below are running
    while new_round == True:
            
        player_won = False
        monster_won = False

        #prints input options.  Has to be a better way to do this.
        print('---' * 8)
        print('Please select action')
        print('---' * 8)
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('---' * 8)


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
            # print('---' * 8)
            # print('You attacked', monster['name'], monster['health'], ' HP left.')
            # print(monster['name'], 'attacked you ', player['health'], ' HP left.')

        # the elif is if player input picks option 2.  This initates the heal.
        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            print('---' * 8)
            print('Healed')
            print(player['health'])

        elif player_choice == '3':
            new_round = False
            game_running = False
            print('---' * 8)
            print('See you soon dick.. Bye!')
        
        # if the user inputs a invalid options.  This will return a message
        else:
            print('not a option try again.')

        if player_won == False and monster_won == False:
            print('###' * 8)
            print(player['name'] + ' has ' + str(player['health']) + ' eft')
            print(monster['name'] + ' has ' + str(monster['health']) +  ' left' )
            print('###' * 8)
            
        elif player_won:
            print('###' * 8)
            print(player['name'] + ' won')
            new_round = False

        elif monster_won:
            print('###' * 8)
            print('You fucking lost')
            new_round = False

         #if player won or lost round.  run new_round
        if player_won == True or monster_won == True:
            new_round = False

