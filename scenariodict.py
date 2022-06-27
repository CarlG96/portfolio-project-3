SCENARIO_DICTIONARY = {'1,1':  
                       'Captain {player_object.name} uses extra fuel to '
                       'accelerate '
                       '{player_object.ship_name} out of the way\nbefore the '
                       'asteroid storm hits.\nCaptain {player_object.name} '
                       'makes the '
                       'hyperspace jump to Sector B.',
                       '1,3':
                       'Captain {player_object.name} masterfully pilots '
                       '{player_object.ship_name} through the asteroid storm,'
                       '\n'
                       'performing incredibly risky maneuvers that push their '
                       'skills to the limit.\nHaving survived this, '
                       'Captain {player_object.name} makes the hyperspace '
                       'jump to '
                       'Sector B.',
                       '1,4': 
                       'Captain {player_object.name} activates the Temporary '
                       'Force'
                       ' Shield they took in the cargo.\nA kinetic barrier '
                       'envelops {player_object.ship_name}, allowing it to\n'
                       'safely traverse the asteroid storm.\nFeeling rather '
                       'lucky; '
                       'Captain {player_object.name} makes the hyperspace jump'
                       ' to Sector B.',
                       '1,5':
                       'One after another, asteroids crash into the side of '
                       '{player_object.ship_name}.\nThe hull is eventually '
                       'breached and Captain {player_object.name} is left\nto '
                       'the mercy of cold space.',
                       '2,1':
                       'Switching on {player_object.ship_name}\'s '
                       'afterburners,\n'
                       'Captain {player_object.name} burns some of the'
                       'additional'
                       '\nfuel to make sure they aren\'t\npulled into the '
                       'black '
                       'hole\'s event horizon.\nBreathing a sigh of relief, '
                       'Captain\n{player_object.name} makes\nthe hyperspace '
                       'jump to Sector C.',
                       '2,3':
                       'Captain {player_object.name} directs '
                       '{player_object.ship_name} on a course\nso that it '
                       'will '
                       'approach the black hole\'s orbit at a '
                       'tangent,\ncatapulting '
                       'the ship out of the black hole\'s gravity well.\n'
                       'With extreme speed, '
                       '{player_object.ship_name} is launched across the '
                       'solar '
                       'system\nbut Captain {player_object.name}\'s quick '
                       'thinking has saved them.\nCaptain '
                       '{player_object.name} '
                       'makes the hyperspace jump to Sector C.'}


def retrieve_scenario_text(player_object, scenario, conclusion_number):
    """Input text to be changed."""
    key = str(scenario) + ',' + str(conclusion_number)
    scenario_text = SCENARIO_DICTIONARY[key].replace('{player_object.name}', 
                                                     player_object.name)
    scenario_text = scenario_text.replace('{player_object.ship_name}', 
                                          player_object.ship_name)
    print(scenario_text)
    return
