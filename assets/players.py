player = {
    'name': 'Eve',
    'attack': 20,
    'heal': 16,
    'health': 100
}




    gameData = loadLocalStorage()
    if 'player' not in gameData:
        gameData['player'] = {
            'name': '',
            'attack': 13,
            'heal': 16,
            'heal_min': 14,
            'heal_max': 20,
            'health': 100,
            'stamina': 10,
            'armor': 11
        }

# Need to add randomize on race encounter.  However when a map is built we will move it to area placements.
    if 'warrior' not in gameData:
        gameData['warrior'] = {
            'name': 'warrior',
            'race': ['human', 'barbarian', 'orc', 'troll', 'elf', 'woodelf', 'nightelf', 'dwarf'],
            'attack_min': 10,
            'attack_max': 20,
            'health': 100,
            'stamina': 10,
            'armor': 11
        }

#Will have to eventually seperate animals by type as some are stronger then others.  Need to research the best way to create this as to save time..
    if 'animals' not in gameData:
        gameData['animals'] = {
            'type': '',
            'health_min': 55,
            'health_max': 100,
            'stamina_min': 60,
            'stamina_max': 100,
            'attack_min': 3,
            'attack_max': 20
        }