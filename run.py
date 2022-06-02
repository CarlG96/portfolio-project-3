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


def main():
    """Main function"""
    introduction()
    print(f'Hello, {get_name("name")}.')
    print(f'Your ship is called {get_name("ship name")}.')
    
    cargo_items = decide_on_items()
    print(cargo_items)
    

def validate_name(name):
    [str(character) for character in name]
    print(f'{name}')
    

main()
