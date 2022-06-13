import random

def quit_out():
    print('Thanks for playing Star Traveller!')
    quit()

def validate_start_menu_option():
    """Validates whether the player wants to
    play Star Traveller, see the instructions for
    it, check the leaderboard or quit the game.
    Returns number."""
    while True:
        print('1) Play Star Traveller')
        print('2) Instructions for Star Traveller')
        print('3) Quit Star Traveller')
        
        number = (input('Choose which option you want by typing the corresponding number. '))
        if number not in ['1','2','3']:
            print('Invalid choice option. Please input a number between 1 and 3.')
        else:
            return number
        

def start_menu():
    """Gives the player the options of playing the game, 
    reading the instructions for how the game is 
    played, checking the 'leaderboard' or quitting the game.
    """
    while True:
        option = validate_start_menu_option()

        if option == '1':
            return
        elif option == '2':
            instructions()
        elif option == '3':
            quit_out()


def instructions():
    """Gives the player instructions on how 
    to play the game. Returns nothing."""
    print('In Star Traveller, you must choose the name of your '
    'captain, the name of your ship and choose a collection of useful '
    'items to hold in your cargo. You will then have to navigate a series '
    'scenarios, choosing to burn precious fuel, use up your item collection '
    'or take increasingly dangerous risks to progress. If you fail '
    'a scenario, you will get a game over. The game is played by inputting '
    'numbers or letters or strings of text when prompted by the text on screen.')


def introduction():
    """Introduces the user to the game."""
    print('\n\nWelcome to Star Traveller!')
    print('You are a captain of the Star Republic Navy.')
    print('You have been tasked with delivering a superweapon from Sector A to Sector E.')
    print('This will allow the Star Republic to defeat the Robo-Empire.')
    print('You will face many perils on your way there, but the Star Republic is relying on you!')
    print('\n\n\n')
            

def validate_initial_cargo_choices(potential_cargo):
    """Validates the initial cargo choices.
    Makess sure they are not value or index errors.
    Returns choice."""
    while True:
        try:
            number = int(input('Choose which item you want by typing in the number: ')) -1
            if number > len(potential_cargo) or number < 0:
                raise IndexError()
            return number
        except ValueError:
            print('Please type your option as an available number.')
        except IndexError: 
            print(f'Please choose options between 1 and {len(potential_cargo)}.')

def validate_replay_choice():
    """Validates whether the player has chosen either 'Y' or 'N' 
    for their choice in the replay function. Returns the player's
    choice."""
    while True:
        replay_choice = input('Type Y for yes and N for no: ').upper()
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
            number = int(input('\nPlease choose an option using the numbers provided: '))
            if number > len(player_object.cargo) + 2 or number < 1:
                raise IndexError()
            return number
        except ValueError:
            print('Please type your option as an available number.')
        except IndexError: 
            print(f'Please choose options between 1 and {len(player_object.cargo) +2}.')



def get_name(name_in_question):
    """Validates the user's name for captain and ship and returns the name"""
    while True:
        try:
            name = ((input(f'What is your {name_in_question}, captain? ')).strip()).capitalize()
            if len(name) > 15 or len(name) < 4:
                raise ValueError()
            if name_in_question == 'ship name':
                name = 'the ' + name
            return name
        except ValueError:
            print(f'{name_in_question} must be between 4 and 15 characters including spaces.')


def decide_on_items():
    """User chooses 3 of 5 items. Function returns a list of these three items."""
    print('\nOn your journey you will need to take some items for perilous situations.')
    potential_cargo_items = ['Temporary Force Shield', 'Anti-Gravity Device', 'Galactic Translator', 'Cloaking Device', 'Nuclear Mines']
    cargo = []
    j = 1
    while j < 4:
        print('\nHere are the list of items you can still take: ')
        for potential_cargo_item, i in zip(potential_cargo_items, range(len(potential_cargo_items))):
            print(f'{i + 1}) {potential_cargo_item}')
        cargo_choice = validate_initial_cargo_choices(potential_cargo_items) 
        cargo.append(potential_cargo_items[cargo_choice])
        potential_cargo_items.remove(potential_cargo_items[cargo_choice])
        j += 1

    print('You have these items: ')
    k = 1
    for carg in cargo:
        print(f'{k}) {carg}')
        k += 1
    return cargo

def scenario_conclusion(player_object, scenario, conclusion_number):
    """Function which takes in argument for which 
    scenario is playing and how the player concluded it. Also takes
    in argument for player object.
    Prints flavour text to give the player some idea of what happened
    as a result of that scenario."""
    if scenario == 1:
        if conclusion_number == 1:
            print(f'{player_object.name} uses extra fuel to accelerate '
            f'{player_object.ship_name} out of the way before the '
            f'asteroid storm hits. {player_object.name} makes the '
            'hyperspace jump to Sector B.')
        elif conclusion_number == 2:
            raise IndexError('This shouldn\'t be possible in the first '
            'scenario as the player\'s fuel can\'t decrease this low '
            'in the first scenario.')
        elif conclusion_number == 3:
            print(f'Captain {player_object.name} masterfully pilots the '
            f'{player_object.ship_name} through the asteroid storm, '
            'performing incredibly risky maneuvers that push their '
            'skills to the limit. Having survived this, '
            f'Captain {player_object.name} makes the hyperspace jump to '
            'Sector B.')
        elif conclusion_number == 4:
            print(f'Captain {player_object.name} activates the Temporary Force '
            'Shield they took in the cargo. A kinetic barrier '
            f'envelops {player_object.ship_name}, allowing it to '
            'safely traverse the asteroid storm. Feeling rather lucky; '
            f'Captain {player_object.name} makes the hyperspace jump to Sector B.')
        elif conclusion_number == 5:
            print('One after another, asteroids crash into the side of '
            f'{player_object.ship_name}. The hull is eventually breached '
            f'and Captain {player_object.name} is left to the mercy of cold space.')
    elif scenario == 2:
        if conclusion_number == 1:
            print(f'Switching on {player_object.ship_name}\'s afterburners, '
            f'Captain {player_object.name} burns some of the additional fuel '
            'to make sure they aren\'t pulled into the black hole\'s '
            f'event horizon. Breathing a sigh of relief, Captain {player_object.name} '
            'makes the hyperspace jump to Sector C.')
        elif conclusion_number == 2:
            raise IndexError('This shouldn\'t be possible in the first '
            'scenario as the player\'s fuel can\'t decrease this low '
            'in the second scenario.')
        elif conclusion_number == 3:
            print(f'Captain {player_object.name} directs {player_object.ship_name} '
            'on a course so that it will approach the black hole\'s orbit at '
            'a tangent, catapulting the ship out of the black hole\'s '
            f'gravity well. {player_object.ship_name} is launched across the '
            f'solar system but Captain {player_object.name}\'s quick thinking '
            f'has saved them. Captain {player_object.name} makes the hyperspace '
            'jump to Sector C.')
        elif conclusion_number == 4:
            print(f'Captain {player_object.name} switches on the Anti-Gravity '
            f'Device in {player_object.ship_name}\'s cargo. This causes '
            f'{player_object.ship_name} to be propelled away from the black '
            f'hole instead of towards it. Captain {player_object.name} makes the hyperspace '
            'jump to Sector C.')
        elif conclusion_number == 5:
            print(f'Captain {player_object.name} fails to stop {player_object.ship_name} '
            f'from being pulled into the black hole. As they pass the event horizon, '
            f'{player_object.name} notices time start to slow and gravity begin to get continually '
            'heavier and heavier...')
    elif scenario == 3:
        if conclusion_number == 1:
            print(f'Captain {player_object.name} uses {player_object.ship_name}\'s fuel '
            f'reserves, flying it out of range of the aliens\' antiquated weapon systems. '
            f'Captain {player_object.name} makes a safe hyperspace jump to Sector D.')
        elif conclusion_number == 2:
            print(f'Captain {player_object.name} tries to use {player_object.ship_name}\'s '
            f'fuel reserves to fly out of range of the alien\' weapon systems, but '
            f'they find there is no more reserve. "If only I\'d taken more fuel" is the last '
            f'thought to pass into {player_object.name}\'s head before {player_object.ship_name} '
            f'explodes.')
        elif conclusion_number == 3:
            print(f'Captain {player_object.name} realises {player_object.ship_name} is far '
            f'superior to the aliens\' ships. Captain {player_object.name} powers up {player_object.ship_name}\'s '
            f'weapon systems and fires before the aliens have a chance to power up their own, destroying '
            f'the aliens. Captain {player_object.name} makes the hyperspace jump to Sector D.')
        elif conclusion_number == 4:
            print(f'Turning on the Galactic Translator, Captain {player_object.name} '
            f'speaks with the aliens. It turns out they are the Bug People from Sector X, '
            f'and have mistaken you for an agent of the Robo-Empire. After clearing up the '
            f'misunderstanding, {player_object.name} makes a quick hyperspace jump to Sector D.')
        elif conclusion_number == 5:
            print(f'Captain {player_object.name} attempts to answer the transmission in all the '
            f'space languages they know, but no answer comes back. The aliens power up their '
            f'weapon systems and their turbo laser destroy {player_object.ship_name}.')
    elif scenario == 4:
        if conclusion_number == 1:
            print(f'Just in time, Captain {player_object.name} uses the fuel reserves '
            f'to boost and hide {player_object.ship_name} behind a planet\'s rings, '
            f'evading the blockade\'s sensors. Captain {player_object.name} waits for '
            f'the blockade to move before making the hyperspace jump to Sector E.')
        elif conclusion_number == 2:
            print(f'Captain {player_object.name} attempts to move quickly to hide from the '
            f'blockade behind a planet\'s rings, but just when they want to tap into the '
            f'fuel reserves, they realise there are none left. {player_object.ship_name} drifts '
            f'into view of the blockade after several minutes, and is destroyed by the '
            f'incoming missiles.' )
        elif conclusion_number == 3:
            print(f'Captain {player_object.name} realises that they can\'t defeat the '
            f'entire blockade by themselves, but comes up with a cunning plan. They wait to '
            f'be targetted by the blockade\'s missiles, only to fly {player_object.ship_name} ' 
            f'close to the blockade, causing the missiles to destroy the blockade itself! '
            f'Captain {player_object.name} passes the destroyed blockade and hyperspace jumps '
            f'to Sector E.')
        elif conclusion_number == 4:
            print(f'Thinking quickly, Captain {player_object.name} activates the Cloaking '
            f'Device in the cargo hold. {player_object.ship_name} becomes invisible to the '
            f'naked eye and to sensors. Captain {player_object.name} moves the ship carefully '
            f'past the blockade and hyperspace jumps to Sector E when out of their range.')
        elif conclusion_number == 5:
            print(f'A barrage of homing missiles fly towards {player_object.ship_name}. '
            f'{player_object.name}\'s pilot skills are no match for the missiles\'s '
            f'ability to turn on a whim, and {player_object.ship_name} is destroyed in '
            f'a massive explosion.')
    elif scenario == 5:
        if conclusion_number == 1:
            print(f'Using the last of {player_object.ship_name}\'s fuel reserve, '
            f'Captain {player_object.name} causes the force of the ship to overpower '
            f'the Robo-Annihilator\'s tractor beam; escaping from the Robo-Annihilator. '
            f'Captain {player_object.name} delivers the superweapon to the Star Republic '
            f'Navy, and after the war is won becomes Admiral {player_object.name}.')
        elif conclusion_number == 2:
            print(f'Captain {player_object.name} attempts to use the fuel reserve '
            f'to escape the tractor beam\'s pull, but realises there is no more reserve! '
            f'They are captured, the superweapon is lost, and so is the last hope of the '
            f'Star Republic.')
        elif conclusion_number == 3:
            print(f'Captain {player_object.name} allows themselves to be taken aboard the '
            f'Robo-Annihilator. Inside, they pull out a concealed laser pistol and kill the '
            f'Robo-Guards, running through the ship before activating its self-destruct button. '
            f'Captain {player_object.name} boards {player_object.ship_name} just in time to escape '
            f'the exploding Robo-Annihilator. Afterwards, they deliver the superweapon to the '
            f'Star Republic Navy, becoming Admiral {player_object.name} and winning the war against '
            f'the Robo-Empire.')
        elif conclusion_number == 4:
            print(f'As {player_object.ship_name} is pulled by the tractor beam. Captain '
            f'{player_object.name} releases the Nuclear Mines from the cargo hold. The '
            f'mines are pulled into the hold of the Robo-Annihilator, causing the dreadnought '
            f'to explode in a mushroom cloud. {player_object.ship_name} just escapes the '
            f'destruction and after delivering the superweapon to the Star Republic Navy, '
            f'Captain {player_object.name} became known as the hero \'{player_object.name} '
            f'the Daring\' for their exploits in destroying the Robo-Annihilator.')
        elif conclusion_number == 5:
            print(f'Captain {player_object.name} is imprisoned aboard the Robo-Annihilator. '
            f'The superweapon is taken and the last thing {player_object.name} sees before they '
            f'are executed is the capital world of the Star Republic being destroyed by the '
            f'superweapon.')
    return

def replay():
    """Function which is called and asks the player whether they would like to replay
    the game."""
    print('Would you like to play again?')
    choice = validate_replay_choice()  
    if choice == 'Y':
        main()
    elif choice == 'N':
        quit_out()


def game_over(player_object):
    """Function which is called when the player loses the
    game. Allows them to quit or play again."""
    print(f'\n\nCaptain {player_object.name} has died.')
    replay()


def victory(player_object):
    """Function which is called when the player wins the game.
    Allows them to quit or play again and will eventually add to a 
    board in a Google Sheet."""
    print(f'\n\nWell done Captain {player_object.name}. You have saved the Star Republic!')
    replay()
   


def display_options(player_object):
    """Function which is called and displays options to the player based on 
    their current cargo"""
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
        print('\n\nAs you go to leave Sector A. A large asteroid storm appears! You are about to be caught in the middle of it. What do you do?')
    elif number == 2:
        print('\n\nAs you enter Sector B, your ship starts to be pulled in by a supermassive black hole! What do you do?')
    elif number == 3:
        print('\n\nAbout halfway through Sector C. A garbled alien transmission comes through from a spaceship on your radar. You have no idea what they want, but their heat signatures suggest they are powering up their weapons. What do you do?')
    elif number == 4:
        print('\n\nAs you enter Sector D, you notice a blockade of Robo-Empire ships. There`s no way you could fight them all. What do you do?')
    elif number == 5:
        print('\n\nUpon arrival in Sector E you see your destination appear after typing in your encrypted password. The end of your journey seems so close now. But out of nowhere the capital ship, the Robo-Annihilator, of the Robo-Empire appears and starts to pull you in with its tractor beam. What do you do?')
    elif number == 6:
        victory(player_object)


def scenario_one(player_object, scenario_number, risk_factor, WINNING_CARGO):
    """Function for calling the first scenario 
    for the player."""
    scenario_intro(int(scenario_number), player_object)
    display_options(player_object)
    number_choice = validate_scenario_choice(player_object) 
    if number_choice == len(player_object.cargo) + 1:
        if player_object.use_fuel():
            scenario_conclusion(player_object, scenario_number, 1)
            scenario_one(player_object, scenario_number + 1, risk_factor + 0.2, WINNING_CARGO) 
        else:
            scenario_conclusion(player_object, scenario_number, 2)
            game_over(player_object)
    elif number_choice == len(player_object.cargo) + 2:
        if player_object.take_chance(risk_factor):
            scenario_conclusion(player_object, scenario_number, 3)
            scenario_one(player_object, scenario_number + 1, risk_factor + 0.2, WINNING_CARGO) 
        else:
            scenario_conclusion(player_object, scenario_number, 5)
            game_over(player_object)
    elif number_choice <= len(player_object.cargo):
        if player_object.cargo[number_choice - 1] == WINNING_CARGO[int(scenario_number)-1]:
            player_object.cargo.remove(WINNING_CARGO[int(scenario_number)-1])
            scenario_conclusion(player_object, scenario_number, 4)
            scenario_one(player_object, scenario_number + 1, risk_factor + 0.2, WINNING_CARGO)
        else:
            scenario_conclusion(player_object, scenario_number, 5)
            game_over(player_object)
    

class Player:
    """Creates an instance of the player 
    from what the player has inputted"""
    def __init__(self, name, ship_name, cargo):
        self.name = name
        self.ship_name = ship_name
        self.cargo = cargo
        self.fuel = 2

    def use_fuel(self):
        """Removes one fuel from the 
        ship in order to get past an objective"""
        self.fuel -= 1
        if self.fuel >= 0:
            return True
        else: 
            return False

    def use_cargo(self, cargo_item):
        """Uses a cargo item and removes
        it from the ship's cargo"""
        self.cargo.remove(self.cargo[int(cargo_item)-1]) 
        # Need checking for this function

    def take_chance(self, factor):
        """Takes a factor and returns a True or
        False as to whether the ship survived the
        risky maneuver taken"""
        floating_num = random.random()
        if floating_num >= factor:
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
        choice = input(f'Your {question}: {details}. Is this correct?'
        'Type Y for yes and N for no: ').upper()
        if choice not in ['Y', 'N']:
            print('Sorry, that choice is not available.')
        elif choice == 'Y':
            return True
        elif choice == 'N':
            return False
        
        
def main():
    """Main function"""
    start_menu()
    introduction()
    name_correct = False
    ship_name_correct = False
    cargo_items_correct = False
    while not name_correct:
        player_name = get_name("name")
        print(f'Hello, {player_name}.')
        name_correct = confirm_choice('Captain\'s name is', player_name)

    while not ship_name_correct:
        player_ship_name = get_name("ship name")
        print(f'Your ship is called {player_ship_name}.')
        ship_name_correct = confirm_choice('Ship\'s name is', player_ship_name)
    
    while not cargo_items_correct:
        cargo_items = decide_on_items()
        cargo_items_correct = confirm_choice('Cargo hold contains these items', cargo_items)
    
    main_player = Player(player_name, player_ship_name, cargo_items)
    WINNING_CARGO = ['Temporary Force Shield', 'Anti-Gravity Device', 'Galactic Translator', 'Cloaking Device', 'Nuclear Mines']
    scenario_one(main_player, int(1), float(0.1), WINNING_CARGO)
    

main()
