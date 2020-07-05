
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

game_running = True

while game_running == True:

    new_round = True

    while new_round == True:
            
        player_won = False
        monster_won = False

        #prints the options
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


            print('You attacked', monster['health'])


        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            print('Healed')
            print(player['health'])
        else:
            print('not a option try again.')

        if player_won == True or monster_won == True:
            new_round = False

