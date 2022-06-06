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
        i = 1
        for potential_cargo_item in potential_cargo_items:
            print(f'{i}) {potential_cargo_item}')
            i += 1
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
        self.cargo.remove(cargo_item) 
        # Need checking for this function

    def take_chance(self, factor):
        """Takes a factor and returns a True or
        False as to whether the ship survived the
        risky maneuver taken"""

        

def main():
    """Main function"""
    # introduction()
    player_name = get_name("name")
    print(f'Hello, {player_name}.')

    player_ship_name = get_name("ship name")
    print(f'Your ship is called {player_ship_name}.')
    
    cargo_items = decide_on_items()
    print(cargo_items)
    
    main_player = Player(player_name, player_ship_name, cargo_items)
    

def validate_name(name):
    [str(character) for character in name]
    print(f'{name}')
    

main()
