import cleverbot


server_running = True


while server_running:

    print('---' * 8)
    print('Please select action')
    print('---' * 8)
    print('1) Talk to Eve')
    print('2) Close')
    # input method from options above
    player_choice = input()


    if player_choice == '1':

        
        cb = cleverbot.Cleverbot('CC93bQ-1QHpWqDm3IsobA6BprYw', timeout=60)

        while True:
            text = input("Say to Eve: ")
            if text == '':
                break
            try:
                reply = cb.say(text)
            except cleverbot.CleverbotError as error:
                print(error)
            else:
                print(reply)


    elif player_choice == '2':
        server_running = False
        print('---' * 8)
        print('See you soon dick.. Bye!')