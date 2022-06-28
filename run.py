"""
Module which runs the game.
"""

# Imported for random integer generation
import random
# Imported to hold dictionaries of strings and one function to access them
import scenariodict

# Global constant list of winning cargo items in order
WINNING_CARGO = ['Temporary Force Shield', 'Anti-Gravity Device',
                 'Galactic Translator', 'Cloaking Device', 'Nuclear Mines']


def quit_out():
    """
    Quits application.

    Thank the player for playing and
    then quits the application.

    Parameters: No parameters.

    Returns: No return values.
    """
    print('\nThanks for playing Star Traveller!')
    quit()


def validate_start_menu_option():
    """
    Validates player choice at start menu.

    Asks the player what they want to do
    at the start menu and then
    validates whether the player wants to
    play Star Traveller, see the instructions for
    playing or quit the game.

    Parameters: No parameters.

    Returns: String which represents a number of 1, 2 or 3.
    """
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
    """
    Sends the player where they want to go.

    Calls the start screen and receives the players
    input then sends them where they want to go.

    Parameters: No parameters.

    Returns: No return values, but does call other functions.
    """
    while True:
        option = validate_start_menu_option()

        if option == '1':
            introduction()
        elif option == '2':
            instructions()
        elif option == '3':
            quit_out()


def instructions():
    """
    Gives the player instructions on how to play the game.

    Parameters: No parameters.
    Returns: No return values. Just prints strings.
    """
    print(scenariodict.OTHER_DICT['instruct'])


def introduction():
    """
    Introduction to the game.

    Introduces the user to the game if
    they have chosen to play and then sends the
    player to create their own Player instance.

    Parameters: No parameters.

    Returns: No return values. Just prints strings
    and then calls function for player to get started on creating
    their own Player instance.
    """
    print(scenariodict.OTHER_DICT['intro'])
    create_player()


def validate_initial_cargo_choices(potential_cargo):
    """
    Validates the initial cargo choices.

    Asks the player to input a number and checks and
    validates if that number for the cargo is available.
    If not it creates a while loop where the player is
    asked to provide a valid number.
    Makes sure there are no value or index errors.

    Parameters:
    potential_cargo (list of str): List of items the player
    can potentially still take.

    Returns:
    number (int): Integer which is used to index the potential
    cargo items list outside the function.
    """
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
    """
    Validates whether player wants to replay game.

    Validates whether the player has chosen either 'Y' or 'N'
    for their choice in the replay function. Creates
    while loop so player must input correctly.

    Parameters: No parameters.

    Returns:
    replay_choice(chr): 'Y' or 'N' so that player can
    replay or quit game.
    """
    while True:
        replay_choice = input('Type Y for yes and N for no:\n').upper()
        if replay_choice not in ['Y', 'N']:
            print('\nSorry, that choice is not available.')
        else:
            return replay_choice


def validate_scenario_choice(player_object):
    """
    Validates the player's scenario choice.

    Validates whether the player has inputted a
    possible scenario choice that is available to them.
    Creates while loop so that player must input
    a valid choice.

    Parameters:
    player_object (Player): Used to work out the length of the
    list of cargo items so that the player's input can be assessed
    against the list of available inputs.

    Returns:
    number (int): Returned so that the game can decide where to proceed.
    Whether the player has progressed to the next scenario, achieved victory
    or recieved a game over and what text is associated with that.
    """
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
    """
    Asks the player to name something in their Player instance.

    Asks the user's name for captain or ship
    depending on argument provided and validates
    whether that is correct by creating a while loop and checking
    that the name is valid.

    Parameters:
    name_in_question (str): Either the name of the player's
    captain or the spaceship's name.

    Returns:
    name (str): Returns a string which is used to develop the Player
    instance. If the argument is the spaceship name then a 'the '
    is added to the front of the string.
    """
    while True:
        name = ((input(f'\nWhat is your {name_in_question}, captain?\n'))
                .strip()).capitalize()
        if len(name) > 10 or len(name) < 4 or not name.isalnum():
            print(f'{name_in_question.capitalize()} must be between 4 and 10 '
                  'alphanumeric characters without spaces.')
        else:
            if name_in_question == 'ship name':
                name = 'the ' + name
            return name


def decide_on_items():
    """
    Asks the player to choose three items out of potential 5.

    Asks player to choose items and presents a shrinking list
    as they pick more. Appends a new list that is used for the
    Player instance.

    Parameters: No parameters.

    Returns:
    cargo (list of str): Returns cargo list which is used to
    instantiate the Player instance for the game.
    """
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
    """
    Function which acts as 'switch' to retrieve conclusion text.

    Parameters:
    player_object (Player): Instance of Player class
    created by player at start of game.
    scenario (int): Integer to identify which scenario is taking
    place currently in the game.
    conclusion_number (int): Integer to identify which conclusion
    has happened based on game logic.

    Returns: Returns nothing.
    """
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
    """
    Function which acts as 'switch' for replaying the game.

    This function calls the validation function for
    the player's replay choice and then calls a function to
    go to the start menu or quit the game (and terminal)
    entirely.

    Parameters: No parameters.

    Returns: Returns nothing.
    """
    print('Would you like to play again?')
    choice = validate_replay_choice()
    if choice == 'Y':
        main()
    elif choice == 'N':
        quit_out()


def game_over(player_object):
    """
    Function which is called when the player loses the game.

    Prints game over text and allows them to
    quit or play again by calling
    replay function.

    Parameters:
    player_object (Player): Uses this to print an fstring
    with the name of the captain inside.

    Returns: Returns nothing.
    """
    print(f'\n\nCaptain {player_object.name} has died.')
    replay()


def victory(player_object):
    """
    Function which is called when the player wins the game.

    Prints victory text and allows them to
    quit or play again by calling
    replay function.

    Parameters:
    player_object (Player): Uses this to print an fstring
    with the name of the captain inside.

    Returns: Returns nothing.
    """
    print(f'\n\nWell done Captain {player_object.name}. You have saved the '
          'Star Republic!')
    replay()


def display_options(player_object):
    """
    Function which displays options for player in scenario.

    Function which is called and displays options to the player based on
    their current cargo. Also displays Player class methods that the player
    can call upon.

    Parameters:
    player_object (Player): Used to display the
    cargo list in the Player instance and to also display the
    fuel attribute.

    Returns: Returns nothing.
    """
    counter = 1
    for cargo_item in player_object.cargo:
        print(f'{counter}) Use {cargo_item}.')
        counter += 1
    print(f'{counter}) Burn fuel to escape the situation. [Fuel = '
          f'{player_object.fuel}]')
    counter += 1
    print(f'{counter}) Perform a risky maneuver.')


def scenario_intro(number, player_object):
    """
    Function which acts as 'switch' for scenario intros.
    Function which decides on which scenario intro text
    is provided to the player depending on how far along the game they
    are. Calls from dictionary.Moves to victory function if player
    has completed all scenarios.

    Parameters:
    number (int): Integer used to decide which intro should
    be called from dictionary.
    player_object (Player): Used to be passed on to the
    victory function if player has passed all scenarios.

    Returns: Returns nothing.
    """
    if number == 1:
        print(scenariodict.INTRO_DICTIONARY['1'])
    elif number == 2:
        print(scenariodict.INTRO_DICTIONARY['2'])
    elif number == 3:
        print(scenariodict.INTRO_DICTIONARY['3'])
    elif number == 4:
        print(scenariodict.INTRO_DICTIONARY['4'])
    elif number == 5:
        print(scenariodict.INTRO_DICTIONARY['5'])
    elif number == 6:
        victory(player_object)


def move_on():
    """
    Function that pauses the game.

    Waits for any input then continues when that input is delivered.

    Parameters: No parameters.

    Returns: Returns nothing.
    """
    input('\nPress enter to continue.\n')
    return


def scenario_call(player_object, scenario_number, risk_factor):
    """Function for calling a scenario for the player.

    Calls itself when a scenario is
    completed successfully or calls game over.
    Does this by validating players scenario choice
    and checking it against things in the Player
    instance.

    Parameters:
    player_object (Player): Used to pass on to
    other functions and to call class methods to see if they
    return True or False.
    scenario_number (int): Used to call other functions and
    decide which scenario is being referred to.
    risk_factor (int): Factor used to be increased when passed
    into next scenario and to test against take_chance method
    in Player instance.

    Returns: Returns nothing.
    """
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
    """
    This is a class that holds data and has methods for the
    player to navigate the game.

    Attributes:
    name (str): The name of the Captain.
    ship_name (str): The name of the spaceship.
    cargo (list of str): Holds cargo items.
    fuel (int): Represents spaceship's fuel reserves.
    """
    def __init__(self, name, ship_name, cargo):
        """
        The constructor for Player class.

        Parameters:
        name (str): The name of the Captain.
        ship_name (str): The name of the spaceship.
        cargo (list of str): Holds cargo items.
        """
        self.name = name
        self.ship_name = ship_name
        self.cargo = cargo
        self.fuel = 2

    def use_fuel(self):
        """
        Function to remove 1 fuel and
        check if player has run out.

        Parameters: No parameters.

        Returns:
        bool: Returns True or False depending on
        whether fuel is greater than or equal to 0.
        This is used to decide whether a player fails or
        passes a scenario.
        """
        self.fuel -= 1
        if self.fuel >= 0:
            return True
        else:
            return False

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
    """
    Function that asks the player if the specific detail is correct.

    Before creating the Player instance in the main function. This function
    returns either True or False to break each while loop in the create_player
    function. Also validates player's answer.

    Parameters:
    question (str): Specific question the player must answer yes
    or no to.
    details (str or list of str): Either name, ship name or cargo
    list player has chosen

    Returns:
    bool: Either True or False to break while loop in
    create_player function.
    """
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
    """
    Provides a series of questions which create the Player
    instance and then calls the scenario.

    Parameters: No parameters.

    Returns: Returns nothing just creates Player instance and
    calls scenario.
    """
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
