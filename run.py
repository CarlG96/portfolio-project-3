def main():
    """Main function"""
    print('Hello World!')
    print('Please enter your name.')
    print('Name should be between 5 and 15 characters long.')
    print("Name can't include numbers.")
    name_prototype = input('Input your name:\n')
    name = name_prototype.strip()
    print(name)
    validate_name(name)
    

def validate_name(name):
    [str(character) for character in name]
    print(f'{name}')
    

main()