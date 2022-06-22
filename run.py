import random


def quit_out():
    """Thank the player for playing and 
    then quits the application"""
    print('Thanks for playing Star Traveller!')
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
          'captain, the name of your ship and choose a collection of useful '
          'items to hold in your cargo.\nYou will then have to navigate a '
          'series of scenarios, choosing to burn precious fuel,\nuse up your '
          'item collection or take increasingly dangerous risks to progress. '
          '\nIf you fail a scenario, you will get a game over.\nThe game is '
          'played by inputting numbers or letters or strings of text when '
          'prompted by the text on screen.')


def introduction():
    """Introduces the user to the game if 
    they have chosen to play"""
    print('\n\nWelcome to Star Traveller!')
    print('You are a captain of the Star Republic Navy.')
    print('You have been tasked with delivering a superweapon from Sector A '
          'to Sector E.')
    print('This will allow the Star Republic to defeat the Robo-Empire.')
    print('You will face many perils on your way there, but the Star Republic '
          'is relying on you!')
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
            print('Sorry, that choice is not available.')
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
        if len(name) > 15 or len(name) < 4 or not(name.isalnum()):
            print(f'{name_in_question.capitalize()} must be between 4 and 15 '
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
    j = 1
    while j < 4:
        print('\nHere are the list of items you can still take:\n')
        for potential_cargo_item, i in zip(potential_cargo_items, 
                                           range(len(potential_cargo_items))):
            print(f'{i + 1}) {potential_cargo_item}')
        cargo_choice = validate_initial_cargo_choices(potential_cargo_items) 
        cargo.append(potential_cargo_items[cargo_choice])
        potential_cargo_items.remove(potential_cargo_items[cargo_choice])
        j += 1

    return cargo


def scenario_conclusion(player_object, scenario, conclusion_number):
    """Function which takes in argument for which 
    scenario is playing and how the player concluded it. Also takes
    in argument for player object.
    Prints flavour text to give the player some idea of what happened
    as a result of that scenario."""
    if scenario == 1:
        if conclusion_number == 1:
            print('\n')
            print(f'{player_object.name} uses extra fuel to accelerate '
                  f'{player_object.ship_name} out of the way\nbefore the '
                  f'asteroid storm hits.\n{player_object.name} makes the '
                  'hyperspace jump to Sector B.')
        elif conclusion_number == 2:
            raise IndexError('This shouldn\'t be possible in the first '
                             'scenario as the player\'s fuel can\'t decrease '
                             'this low in the first scenario.')
        elif conclusion_number == 3:
            print('\n')
            print(f'Captain {player_object.name} masterfully pilots '
                  f'{player_object.ship_name} through the asteroid storm,\n'
                  'performing incredibly risky maneuvers that push their '
                  'skills to the limit.\nHaving survived this, '
                  f'Captain {player_object.name} makes the hyperspace jump to '
                  'Sector B.')
        elif conclusion_number == 4:
            print('\n')
            print(f'Captain {player_object.name} activates the Temporary Force'
                  ' Shield they took in the cargo.\nA kinetic barrier '
                  f'envelops {player_object.ship_name}, allowing it to '
                  'safely traverse the asteroid storm.\nFeeling rather lucky; '
                  f'Captain {player_object.name} makes the hyperspace jump to '
                  'Sector B.')
        elif conclusion_number == 5:
            print('\n')
            print('One after another, asteroids crash into the side of '
                  f'{player_object.ship_name}.\nThe hull is eventually '
                  f'breached and Captain {player_object.name} is left to the '
                  'mercy of cold space.')
    elif scenario == 2:
        if conclusion_number == 1:
            print('\n')
            print(f'Switching on {player_object.ship_name}\'s afterburners,\n'
                  f'Captain {player_object.name} burns some of the additional '
                  'fuel to make sure they aren\'t\npulled into the black '
                  f'hole\'s event horizon.\nBreathing a sigh of relief, '
                  f'Captain {player_object.name} makes the hyperspace jump to '
                  'Sector C.')
        elif conclusion_number == 2:
            raise IndexError('This shouldn\'t be possible in the first '
                             'scenario as the player\'s fuel can\'t decrease '
                             'this lowin the second scenario.')
        elif conclusion_number == 3:
            print('\n')
            print(f'Captain {player_object.name} directs '
                  f'{player_object.ship_name} on a course\nso that it will '
                  'approach the black hole\'s orbit at a '
                  'tangent,\ncatapulting '
                  f'the ship out of the black hole\'s gravity well.\n'
                  f'{player_object.ship_name} is launched across the solar '
                  f'system\nbut Captain {player_object.name}\'s quick '
                  f'thinking has saved them.\nCaptain {player_object.name} '
                  'makes the hyperspace jump to Sector C.')
        elif conclusion_number == 4:
            print('\n')
            print(f'Captain {player_object.name} switches on the Anti-Gravity '
                  f'Device in {player_object.ship_name}\'s cargo.\nThis '
                  'causes '
                  f'{player_object.ship_name} to be propelled away from the '
                  f'black hole instead of towards it.\nCaptain '
                  f'{player_object.name} makes the hyperspace jump to '
                  'Sector C.')
        elif conclusion_number == 5:
            print('\n')
            print(f'Captain {player_object.name} fails to stop '
                  f'{player_object.ship_name} from being pulled into the '
                  f'black hole.\nAs they pass the event horizon, '
                  f'{player_object.name} notices time start to slow and\n'
                  'gravity begin to get continually heavier and heavier...')
    elif scenario == 3:
        if conclusion_number == 1:
            print('\n')
            print(f'Captain {player_object.name} uses '
                  f'{player_object.ship_name}\'s fuel reserves,\nflying it '
                  'out '
                  f'of range of the aliens\' antiquated weapon systems.\n'
                  f'Captain {player_object.name} makes a safe hyperspace jump '
                  'to Sector D.')
        elif conclusion_number == 2:
            print('\n')
            print(f'Captain {player_object.name} tries to use '
                  f'{player_object.ship_name}\'s fuel reserves\nto fly out of '
                  f'range of the alien\' weapon systems,\nbut they find there '
                  f'is no more reserve.\n"If only I\'d taken more fuel" is '
                  'the '
                  f'last thought to pass\ninto {player_object.name}\'s head '
                  f'before {player_object.ship_name} explodes.')
        elif conclusion_number == 3:
            print('\n')
            print(f'Captain {player_object.name} realises '
                  f'{player_object.ship_name} is\nfar superior to the '
                  'aliens\' '
                  f'ships.\nCaptain {player_object.name} powers up '
                  f'{player_object.ship_name}\'s weapon systems\nand fires '
                  f'before the aliens have a chance to power up their own,'
                  f'destroying the aliens.\nCaptain {player_object.name} '
                  f'makes the hyperspace jump to Sector D.')
        elif conclusion_number == 4:
            print('\n')
            print(f'Turning on the Galactic Translator, Captain '
                  f'{player_object.name} speaks with the aliens.\nIt turns '
                  'out '
                  f'they are the Bug People from Sector X, and have mistaken '
                  f'you for an agent of the Robo-Empire.\nAfter clearing up '
                  f'the misunderstanding, {player_object.name} makes a quick '
                  f'hyperspace jump to Sector D.')
        elif conclusion_number == 5:
            print('\n')
            print(f'Captain {player_object.name} attempts to answer the '
                  f'transmission in all the space languages they know,\nbut '
                  'no '
                  f'answer comes back.\nThe aliens power up their weapon '
                  f'systems and their turbo lasers destroy '
                  f'{player_object.ship_name}.')
    elif scenario == 4:
        if conclusion_number == 1:
            print('\n')
            print(f'Just in time, Captain {player_object.name} uses the fuel '
                  f'reserves to\nboost and hide {player_object.ship_name} '
                  f'behind a planet\'s rings, evading the blockade\'s '
                  f'sensors.\nCaptain {player_object.name} waits for '
                  'the blockade to move before making the hyperspace '
                  'jump to Sector E.')
        elif conclusion_number == 2:
            print('\n')
            print(f'Captain {player_object.name} attempts to move quickly to '
                  f'hide from the blockade behind a planet\'s rings,\nbut '
                  'just '
                  f'when they want to tap into the fuel reserves, they '
                  f'realise there are none left.\n{player_object.ship_name} '
                  f'drifts into view of the blockade after several minutes,\n'
                  'and is destroyed by the incoming missiles.')
        elif conclusion_number == 3:
            print('\n')
            print(f'Captain {player_object.name} realises that they can\'t '
                  f'defeat the entire blockade by themselves,\nbut comes up  '
                  f'with a cunning plan.\nThey wait to be targetted by the ' 
                  f'blockade\'s missiles, only to fly '
                  f'{player_object.ship_name} close to the blockade,\ncausing '
                  'the missiles to '
                  f'destroy the blockade itself!\nCaptain '
                  f'{player_object.name} '
                  f'passes the destroyed blockade and hyperspace jumps '
                  f'to Sector E.')
        elif conclusion_number == 4:
            print('\n')
            print(f'Thinking quickly, Captain {player_object.name} activates '
                  f'the Cloaking Device in the cargo hold.\n'
                  f'{player_object.ship_name} {player_object.ship_name} '
                  'becomes invisible to the naked '
                  f'eye and to sensors.\nCaptain {player_object.name} '
                  f'moves the ship carefully past the blockade\nand '
                  'hyperspace jumps to Sector E when out of their range.')
        elif conclusion_number == 5:
            print('\n')
            print(f'A barrage of homing missiles fly towards '
                  f'{player_object.ship_name}.\n{player_object.name}\'s pilot '
                  f'skills are no match for the missiles\'s '
                  f'ability to turn on a whim,\n'
                  f'and {player_object.ship_name} is destroyed in '
                  f'a massive explosion.')
    elif scenario == 5:
        if conclusion_number == 1:
            print(f'Using the last of {player_object.ship_name}\'s fuel '
                  f'reserve,\nCaptain {player_object.name} causes the force '
                  'of '
                  f'the ship to overpower the Robo-Annihilator\'s tractor '
                  f'beam;\nescaping from the Robo-Annihilator.\nCaptain '
                  f'{player_object.name} delivers the superweapon to the Star '
                  f'Republic Navy,\nand after the war is '
                  f'won becomes Admiral {player_object.name}.')
        elif conclusion_number == 2:
            print(f'Captain {player_object.name} attempts to use the fuel '
                  f'reserve to escape the tractor beam\'s pull,\nbut realises '
                  f'there is no more reserve!\nThey are captured,  '
                  f'the superweapon is lost,\nand so is the last hope of the '
                  'Star Republic.')
        elif conclusion_number == 3:
            print(f'Captain {player_object.name} allows themselves to be '
                  f'taken aboard theRobo-Annihilator.\nInside, they pull out '
                  'a concealed '
                  f'laser pistol and kill the Robo-Guards,\nrunning through '
                  f'the ship before activating its self-destruct button.\n'
                  f'Captain {player_object.name} '
                  f'boards {player_object.ship_name} just in time to escape '
                  f'the exploding Robo-Annihilator.\nAfterwards, they deliver '
                  f'the superweapon to the Star Republic Navy,\nbecoming '
                  f'Admiral {player_object.name} and winning the war against '
                  f'the Robo-Empire.')
        elif conclusion_number == 4:
            print(f'As {player_object.ship_name} is pulled by the tractor '
                  f'beam.\nCaptain {player_object.name} releases the Nuclear '
                  f'Mines from the cargo hold.\nThe mines are pulled into the '
                  f'hold of the Robo-Annihilator, causing the dreadnought '
                  f'to explode in a mushroom cloud.'
                  f'\n{player_object.ship_name} just escapes the destruction '
                  'and after'
                  f'delivering the superweapon to the Star Republic Navy,\n'
                  f'Captain {player_object.name} became '
                  f'known as the hero \'{player_object.name} the Daring\'\n'
                  f'for their exploits in destroying the Robo-Annihilator.')
        elif conclusion_number == 5:
            print(f'Captain {player_object.name} is imprisoned aboard the '
                  f'Robo-Annihilator.\nThe superweapon is taken and the last '
                  f'thing {player_object.name} sees before they are executed\n'
                  f'is the capital world of the Star Republic being destroyed '
                  f'by the superweapon.')
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
    i = 1
    for cargo_item in player_object.cargo:
        print(f'{i}) Use {cargo_item}.')
        i += 1
    print(f'{i}) Burn fuel to escape situation. [Fuel = {player_object.fuel}]')
    i += 1
    print(f'{i}) Perform a risky maneuver.')


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
              'a supermassive black hole!\n'
              'What do you do?\n')
    elif number == 3:
        print('\n\nAbout halfway through Sector C.\nA garbled alien '
              'transmission comes through from a spaceship on your radar.\n'
              'You have no idea what they want, but their heat signatures '
              'suggest they are powering up their weapons.\nWhat do you do?\n')
    elif number == 4:
        print('\n\nAs you enter Sector D, you notice a blockade of '
              'Robo-Empire ships.\nThere`s no way you could fight them all.\n'
              'What do you do?\n')
    elif number == 5:
        print('\n\nUpon arrival in Sector E you see your destination appear '
              'after typing in your encrypted password.\nThe end '
              'of your journey seems so close now.\n'
              'But out of nowhere their capital ship, the Robo-Annihilator,\n'
              'appears and starts to pull you in with its '
              'tractor beam.\nWhat do you do?\n')
    elif number == 6:
        victory(player_object)


def move_on():
    """Function that pauses the game, waits for 
    any input then continues when that input is delivered."""
    input('\nPress any button to continue.\n')
    return


def scenario_call(player_object, scenario_number, risk_factor, WINNING_CARGO):
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
                          2, WINNING_CARGO) 
        else:
            scenario_conclusion(player_object, scenario_number, 2)
            game_over(player_object)
    elif number_choice == len(player_object.cargo) + 2:
        if player_object.take_chance(risk_factor):
            scenario_conclusion(player_object, scenario_number, 3)
            move_on()
            scenario_call(player_object, scenario_number + 1, risk_factor + 
                          2, WINNING_CARGO) 
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
                          2, WINNING_CARGO)
        else:
            scenario_conclusion(player_object, scenario_number, 5)
            game_over(player_object)
    

class Player:
    """Creates an instance of the player 
    from what the player has inputted as name,
    ship name and cargp"""
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
        choice = input(f'\nYour {question}: {details}.\nIs this correct? '
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
    WINNING_CARGO = ['Temporary Force Shield', 'Anti-Gravity Device', 
                     'Galactic Translator', 'Cloaking Device', 'Nuclear Mines']
    scenario_call(main_player, int(1), int(1), WINNING_CARGO)
    

main()
