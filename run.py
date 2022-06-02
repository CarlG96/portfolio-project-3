def introduction():
    print('Welcome to Star Traveller!')
    print('You are a captain of the Star Republic Navy.')
    print('You have been tasked with delivering a superweapon from Sector A to Sector E.')
    print('This will allow the Star Republic to defeat the Robo-Empire.')
    print('You will face many perils on your way there, but the Star Republic is relying on you!')
    print('\n\n\n')


def get_name():
    name = (input('What is your name, captain? ')).strip()
    return name


def main():
    """Main function"""
    introduction()
    print(f'Hello, {get_name()}.')
    # print('Hello World!')
    # print('Please enter your name.')
    # print('Name should be between 5 and 15 characters long.')
    # print("Name can't include numbers.")
    # name_prototype = input('Input your name:\n')
    # name = name_prototype.strip()
    # print(name)
    # validate_name(name)
    

def validate_name(name):
    [str(character) for character in name]
    print(f'{name}')
    

main()