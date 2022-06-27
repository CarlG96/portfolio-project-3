import random
import scenariodict 


WINNING_CARGO = ['Temporary Force Shield', 'Anti-Gravity Device', 
                 'Galactic Translator', 'Cloaking Device', 'Nuclear Mines']


def quit_out():
    """Thank the player for playing and 
    then quits the application"""
    print('\nThanks for playing Star Traveller!')
    quit()


def validate_start_menu_option():
    """Validates whether the player wants to
    play Star Traveller, see the instructions for
    it or quit the game. Also validates the choice.
    Returns number of the choice."""
    while True:
        print('\nWelcome to Star Traveller!\n')
        print('1) Play Star Traveller')
        print('2) Instructions for Star Traveller')
        print('3) Quit Star Traveller')
        number = (input('\nChoose which option you want by typing the '
                  'corresponding number.\n'))
        if number not in ['1', '2', '3']:
            print('Invalid choice option. Please input a number between 1 and '
                  '3.')
        else:
            return number


def main():
    """Gives the player the options of playing the game,
    reading the instructions for how the game is
    played or quitting the game. First function to be
    called."""
    while True:
        option = validate_start_menu_option()

        if option == '1':
            introduction()
        elif option == '2':
            instructions()
        elif option == '3':
            quit_out()


def instructions():
    """Gives the player instructions on how
    to play the game. Returns nothing."""
    print('\nIn Star Traveller, you must choose the name of your\n'
          'captain, the name of your ship and choose a collection\nof useful '
          'items to hold in your cargo.\nYou will then have to navigate a '
          'series of scenarios,\nchoosing to burn precious fuel,\nuse up your '
          'item collection or take increasingly dangerous risks to progress. '
          '\nIf you fail a scenario,\nyou will get a game over.\nThe game is '
          'played by inputting numbers or letters or\nstrings of text when '
          'prompted by the text on screen.')


def introduction():
    """Introduces the user to the game if 
    they have chosen to play"""
    print('\n\nWelcome to Star Traveller!')
    print('You are a captain of the Star Republic Navy.')
    print('You have been tasked with delivering a superweapon from Sector A '
          'to Sector E.')
    print('This will allow the Star Republic to defeat the Robo-Empire.')
    print('You will face many perils on your way there, but the Star Republic'
          '\nis relying on you!')
    print('\n')
    create_player()


def validate_initial_cargo_choices(potential_cargo):
    """Validates the initial cargo choices.
    Makes sure there are no value or index errors.
    Returns choice as a number."""
    while True:
        try:
            number = int(input('\nChoose which item you want by typing in the '
                               'number:\n')) - 1
            if number not in range(0, len(potential_cargo)):
                print(f'Please choose options between 1 and '
                      f'{len(potential_cargo)}.')
            else:
                return number
        except ValueError:
            print('Please type your option as an available number.')
        

def validate_replay_choice():
    """Validates whether the player has chosen either 'Y' or 'N' 
    for their choice in the replay function. Returns the player's
    choice."""
    while True:
        replay_choice = input('Type Y for yes and N for no:\n').upper()
        if replay_choice not in ['Y', 'N']:
            print('\nSorry, that choice is not available.')
        else:
            return replay_choice


def validate_scenario_choice(player_object):
    """Validates the player's scenario choice.
    Check's for Value or Index Error. Returns
    integer for scenario choice."""
    while True:
        try:
            number = int(input('\nPlease choose an option using the numbers '
                               'provided:\n'))
            if number not in range(1, len(player_object.cargo) + 3):
                print(f'Please choose options between 1 and '
                      f'{len(player_object.cargo) +2}.')
            else:
                return number
        except ValueError:
            print('Please type your option as an available number.')


def get_name(name_in_question):
    """Validates the user's name for captain or ship
    depending on argument provided and returns the name."""
    while True:
        name = ((input(f'\nWhat is your {name_in_question}, captain?\n'))
                .strip()).capitalize()
        if len(name) > 10 or len(name) < 4 or not(name.isalnum()):
            print(f'{name_in_question.capitalize()} must be between 4 and 10 '
                  'alphanumeric characters without spaces.')
        else:
            if name_in_question == 'ship name':
                name = 'the ' + name
            return name


def decide_on_items():
    """User chooses 3 of 5 items. Returns a list of these 
    three items."""
    print('\nOn your journey you will need to take some items for perilous '
          'situations.')
    potential_cargo_items = ['Temporary Force Shield', 'Anti-Gravity Device', 
                             'Galactic Translator', 'Cloaking Device', 
                             'Nuclear Mines']
    cargo = []
    counter = 1
    while counter < 4:
        print('\nHere are the list of items you can still take:\n')
        for potential_cargo_item, i in zip(potential_cargo_items, 
                                           range(len(potential_cargo_items))):
            print(f'{i + 1}) {potential_cargo_item}')
        cargo_choice = validate_initial_cargo_choices(potential_cargo_items) 
        cargo.append(potential_cargo_items[cargo_choice])
        potential_cargo_items.remove(potential_cargo_items[cargo_choice])
        counter += 1

    return cargo


def scenario_conclusion(player_object, scenario, conclusion_number):
    """Function which takes in argument for which 
    scenario is playing and how the player concluded it. Also takes
    in argument for player object.
    Prints flavour text to give the player some idea of what happened
    as a result of that scenario."""
    print('\n')
    if scenario == 1:
        if conclusion_number == 1:
            scenariodict.retrieve_scenario_text(player_object, 1, 1)            
        elif conclusion_number == 2:
            raise IndexError('This shouldn\'t be possible in the first '
                             'scenario as the player\'s fuel can\'t decrease '
                             'this low in the first scenario.')
        elif conclusion_number == 3:
            scenariodict.retrieve_scenario_text(player_object, 1, 3)
        elif conclusion_number == 4:
            scenariodict.retrieve_scenario_text(player_object, 1, 4)
        elif conclusion_number == 5:
            scenariodict.retrieve_scenario_text(player_object, 1, 5)
    elif scenario == 2:
        if conclusion_number == 1:
            scenariodict.retrieve_scenario_text(player_object, 2, 1)
        elif conclusion_number == 2:
            raise IndexError('This shouldn\'t be possible in the first '
                             'scenario as the player\'s fuel can\'t decrease '
                             'this lowin the second scenario.')
        elif conclusion_number == 3:
            scenariodict.retrieve_scenario_text(player_object, 2, 3)
        elif conclusion_number == 4:
            scenariodict.retrieve_scenario_text(player_object, 2, 4)
        elif conclusion_number == 5:
            scenariodict.retrieve_scenario_text(player_object, 2, 5)
    elif scenario == 3:
        if conclusion_number == 1:
            scenariodict.retrieve_scenario_text(player_object, 3, 1)
        elif conclusion_number == 2:
            scenariodict.retrieve_scenario_text(player_object, 3, 2)
        elif conclusion_number == 3:
            scenariodict.retrieve_scenario_text(player_object, 3, 3)
        elif conclusion_number == 4:
            scenariodict.retrieve_scenario_text(player_object, 3, 4)
        elif conclusion_number == 5:
            scenariodict.retrieve_scenario_text(player_object, 3, 5)
    elif scenario == 4:
        if conclusion_number == 1:
            scenariodict.retrieve_scenario_text(player_object, 4, 1)
        elif conclusion_number == 2:
            scenariodict.retrieve_scenario_text(player_object, 4, 2)
        elif conclusion_number == 3:
            scenariodict.retrieve_scenario_text(player_object, 4, 3)
        elif conclusion_number == 4:
            scenariodict.retrieve_scenario_text(player_object, 4, 4)
        elif conclusion_number == 5:
            scenariodict.retrieve_scenario_text(player_object, 4, 5)
    elif scenario == 5:
        if conclusion_number == 1:
            scenariodict.retrieve_scenario_text(player_object, 5, 1)
        elif conclusion_number == 2:
            scenariodict.retrieve_scenario_text(player_object, 5, 2)
        elif conclusion_number == 3:
            scenariodict.retrieve_scenario_text(player_object, 5, 3)
        elif conclusion_number == 4:
            scenariodict.retrieve_scenario_text(player_object, 5, 4)
        elif conclusion_number == 5:
            scenariodict.retrieve_scenario_text(player_object, 5, 5)
    return


def replay():
    """Function which is called and asks the player whether they would like to 
    replay the game."""
    print('Would you like to play again?')
    choice = validate_replay_choice()  
    if choice == 'Y':
        main()
    elif choice == 'N':
        quit_out()


def game_over(player_object):
    """Function which is called when the player loses the
    game. Allows them to quit or play again by calling
    replay function."""
    print(f'\n\nCaptain {player_object.name} has died.')
    replay()


def victory(player_object):
    """Function which is called when the player wins the game.
    Allows them to quit or play again by calling replay 
    function."""
    print(f'\n\nWell done Captain {player_object.name}. You have saved the '
          'Star Republic!')
    replay()
   

def display_options(player_object):
    """Function which is called and displays options to the player based on 
    their current cargo. Also displays class methods that the player
    can call upon."""
    counter = 1
    for cargo_item in player_object.cargo:
        print(f'{counter}) Use {cargo_item}.')
        counter += 1
    print(f'{counter}) Burn fuel to escape the situation. [Fuel = '
          f'{player_object.fuel}]')
    counter += 1
    print(f'{counter}) Perform a risky maneuver.')


def scenario_intro(number, player_object):
    """Function which decides on which scenario intro text
    is provided to the player depending on how far along the game they 
    are. Moves to victory function if player has completed all scenarios."""
    if number == 1:
        print('\n\nAs you go to leave Sector A. A large asteroid storm ' 
              'appears!\nYou are about to be caught in the middle of it.\n'
              'What do you do?\n')
    elif number == 2:
        print('\n\nAs you enter Sector B, your ship starts to be pulled in by '
              'a supermassive\nblack hole!\n'
              'What do you do?\n')
    elif number == 3:
        print('\n\nAbout halfway through Sector C\na garbled alien '
              'transmission comes through from a spaceship on your radar.\n'
              'You have no idea what they want, but their heat signatures\n'
              'suggest they are powering up their weapons.\nWhat do you do?\n')
    elif number == 4:
        print('\n\nAs you enter Sector D, you notice a blockade of '
              'Robo-Empire ships.\nThere`s no way you could fight them all.\n'
              'What do you do?\n')
    elif number == 5:
        print('\n\nUpon arrival in Sector E you see your destination appear '
              'after\ntyping in your encrypted password.\nThe end '
              'of your journey seems so close now.\n'
              'But out of nowhere their capital ship, the Robo-Annihilator,\n'
              'appears and starts to pull you in with its '
              'tractor beam.\nWhat do you do?\n')
    elif number == 6:
        victory(player_object)


def move_on():
    """Function that pauses the game, waits for 
    any input then continues when that input is delivered."""
    input('\nPress enter to continue.\n')
    return


def scenario_call(player_object, scenario_number, risk_factor):
    """Function for calling the first scenario 
    for the player. Also calls itself when a scenario is 
    completed successfully."""
    scenario_intro(int(scenario_number), player_object)
    display_options(player_object)
    number_choice = validate_scenario_choice(player_object) 
    if number_choice == len(player_object.cargo) + 1:
        if player_object.use_fuel():
            scenario_conclusion(player_object, scenario_number, 1)
            move_on()
            scenario_call(player_object, scenario_number + 1, risk_factor + 
                          2) 
        else:
            scenario_conclusion(player_object, scenario_number, 2)
            game_over(player_object)
    elif number_choice == len(player_object.cargo) + 2:
        if player_object.take_chance(risk_factor):
            scenario_conclusion(player_object, scenario_number, 3)
            move_on()
            scenario_call(player_object, scenario_number + 1, risk_factor + 
                          2) 
        else:
            scenario_conclusion(player_object, scenario_number, 5)
            game_over(player_object)
    elif number_choice <= len(player_object.cargo):
        if player_object.cargo[number_choice - 1] == WINNING_CARGO[int
           (scenario_number)-1]:
            player_object.cargo.remove(WINNING_CARGO[int(scenario_number)-1])
            scenario_conclusion(player_object, scenario_number, 4)
            move_on()
            scenario_call(player_object, scenario_number + 1, risk_factor + 
                          2)
        else:
            scenario_conclusion(player_object, scenario_number, 5)
            game_over(player_object)
    

class Player:
    """Creates an instance of the player 
    from what the player has inputted as name,
    ship name and cargo."""
    def __init__(self, name, ship_name, cargo):
        self.name = name
        self.ship_name = ship_name
        self.cargo = cargo
        self.fuel = 2

    def use_fuel(self):
        """Removes one fuel from the 
        ship in order to get past an objective."""
        self.fuel -= 1
        if self.fuel >= 0:
            return True
        else: 
            return False

    def use_cargo(self, cargo_item):
        """Uses a cargo item and removes
        it from the ship's cargo."""
        self.cargo.remove(self.cargo[int(cargo_item)-1]) 

    def take_chance(self, factor):
        """Takes a factor and returns a True or
        False as to whether the ship survived the
        risky maneuver taken."""
        num = random.randint(1, 10)
        if num >= factor:
            return True
        else:
            return False


def confirm_choice(question, details):
    """Function that asks the player if the specific detail
    (name, ship name or cargo items) are correct before creating
    the player object in the main function. This function returns
    either True or False to break each while loop in the main 
    function."""
    while True:
        choice = input(f'\nYour {question}:\n{details}.\nIs this correct? '
                       'Type Y for yes and N for no:\n').upper()
        if choice not in ['Y', 'N']:
            print('Sorry, that choice is not available.')
        elif choice == 'Y':
            return True
        elif choice == 'N':
            return False

        
def create_player():
    """Provides a series of questions which create the Player
    object and then calls the scenario."""
    name_correct = False
    ship_name_correct = False
    cargo_items_correct = False
    while not name_correct:
        player_name = get_name("name")
        name_correct = confirm_choice('Captain\'s name is', player_name)

    while not ship_name_correct:
        player_ship_name = get_name("ship name")
        ship_name_correct = confirm_choice('Ship\'s name is', player_ship_name)
    
    while not cargo_items_correct:
        cargo_items = decide_on_items()
        cargo_items_correct = confirm_choice('Cargo hold contains these items',
                                             cargo_items)
    
    main_player = Player(player_name, player_ship_name, cargo_items)

    scenario_call(main_player, int(1), int(1))
    
    
if __name__ == '__main__':
    main()
