import random

def introduction():
    """Introduces the user to the game"""
    print('Welcome to Star Traveller!')
    print('You are a captain of the Star Republic Navy.')
    print('You have been tasked with delivering a superweapon from Sector A to Sector E.')
    print('This will allow the Star Republic to defeat the Robo-Empire.')
    print('You will face many perils on your way there, but the Star Republic is relying on you!')
    print('\n\n\n')


def get_name(name_in_question):
    """Gets the user's name for their captain and returns the name"""
    name = ((input(f'What is your {name_in_question}, captain? ')).strip()).capitalize()
    return name


def decide_on_items():
    """User chooses 3 of 5 items. Function returns a list of these three items."""
    potential_cargo_items = ['Temporary Force Shield', 'Anti-Gravity Device', 'Galactic Translator', 'Cloaking Device', 'Nuclear Mines']
    cargo = []
    j = 1
    while j < 4:
        print('Here are the list of items: ')
        for potential_cargo_item, i in zip(potential_cargo_items, range(len(potential_cargo_items))):
            print(f'{i + 1}) {potential_cargo_item}')
        cargo_choice = int(input('Choose which item you want by typing in the number: ')) - 1
        cargo.append(potential_cargo_items[cargo_choice])
        potential_cargo_items.remove(potential_cargo_items[cargo_choice])
        j += 1

    print('You have these items: ')
    k = 1
    for carg in cargo:
        print(f'{k}) {carg}')
        k += 1
    return cargo

def game_over(player_object):
    """Function which is called when the player loses the
    game. Allows them to quit or play again."""
    print(f'Captain {player_object.name} has died.')
    print('Would you like to try again?')
    #Add path back to main or allow the player to quit game

def victory(player_object):
    """Function which is called when the player wins the game.
    Allows them to quit or play again and will eventually add to a 
    board in a Google Sheet."""
    print(f'Well done Captain {player_object.name}. You have saved the Star Republic!')
    #Add path to play again or allow the player to quit the game


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


def scenario_one(player_object):
    """Function for calling the first scenario 
    for the player."""
    print('As you go to leave Sector A. A large asteroid storm appears! You are about to be caught in the middle of it. What do you do?')
    print(player_object.name)
    # Add call for displaying options function
    # Add if else statement with pass or fail causing call for scenario_two or game_over

def scenario_two(player_object):
    """Function for calling the second scenario 
    for the player."""
    print('As you enter Sector B, your ship starts to be pulled in by a supermassive black hole! What do you do?')
    # Add call for displaying options function
    # Add if else statement with pass or fail causing call for scenario_three or game_over


def scenario_three(player_object):
    """Function for calling the third scenario 
    for the player."""
    print('About halfway through Sector C. A garbled alien transmission comes through from a spaceship on your radar. You have no idea what they want, but their heat signatures suggest they are powering up their weapons. What do you do?')
     # Add call for displaying options function
     # Add if else statement with pass or fail causing call for scenario_four or game_over


def scenario_four(player_object):
    """Function for calling the fourth scenario 
    for the player."""
    print('As you enter Sector D, you notice a blockade of Robo-Empire ships. There’s no way you could fight them all. What do you do?')
     # Add call for displaying options function
     # Add if else statement with pass or fail causing call for scenario_five or game_over

def scenario_five(player_object):
    """Function for calling the fifth scenario 
    for the player."""
    print('Upon arrival in Sector E you see your destination appear after typing in your encrypted password. The end of your journey seems so close now. But out of nowhere the capital ship, the Robo-Annihilator, of the Robo-Empire appears and starts to pull you in with its tractor beam. What do you do?')
    # Add call for displaying options function
    # Add if else statement with pass or fail causing call for victory or game_over

class Player:
    """Creates an instance of the player 
    from what the player has inputted"""
    def __init__(self, name, ship_name, cargo):
        self.name = name
        self.ship_name = ship_name
        self.cargo = cargo
        self.fuel = 3

    def use_fuel(self):
        """Removes one fuel from the 
        ship in order to get past an objective"""
        self.fuel -= 1

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

        

def main():
    """Main function"""
    #introduction()
    #player_name = get_name("name")
    #print(f'Hello, {player_name}.')

    #player_ship_name = get_name("ship name")
    #print(f'Your ship is called {player_ship_name}.')
    
    cargo_items = decide_on_items()
    print(cargo_items)
    
    #main_player = Player(player_name, player_ship_name, cargo_items)
    #scenario_one(main_player)
    

def validate_name(name):
    [str(character) for character in name]
    print(f'{name}')
    

main()
