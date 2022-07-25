import random

def is_inital_pen_amt_valid(inputPen):
    '''
    Checks if the initial pencil number is valid

    :param inputPen: pen number to check
    :return: True or False, depending if it valid or not
    '''
    try:
        inputPen = int(inputPen)
    except ValueError:
        print("The number of pencils should be numeric")
        return False

    if inputPen == 0:
        print("The number of pencils should be positive")
        return False

    return True

def is_pen_amt_valid(currentPen, inputPen):
    '''
    Checks if the pencil amount if valid

    :param currentPen: number of pencils left in game
    :param inputPen: user inputted pencil amount to remove
    :return: True or False, depending if the pencil removal amount if valid
    '''
    if inputPen != "1" and inputPen != "2" and inputPen != "3":
        print("Possible values: '1', '2' or '3'")
        return False

    if int(inputPen) > currentPen:
        print("Too many pencils were taken")
        return False

    return True

def is_name_valid(inputName):
    '''
    Checks if proposed name is valid

    :param inputName: Name the user wants to go first
    :return: True or False, depending if the proposed name is Jack or John
    '''
    if inputName != "John" and inputName != "Jack":
        return False
    return True

def win(currentName):
    '''
    Prints the winner

    :param currentName: the person who won
    :return: none
    '''
    print("%s won!" % currentName)

def bot_turn(currentPen):
    '''
    Plays the bot turn. The bot tries to play the most optimal move

    :param currentPen: amount of pencils currently left
    :return: int, the amount of pencils the bot wants to remove
    '''
    if currentPen == 1:
        return 1
    elif currentPen % 4 == 2:
        return 1
    elif currentPen % 4 == 3:
        return 2
    elif currentPen % 4 == 0:
        return 3
    else:
        return random.randint(1, 3)

def turn(currentPen, currentName):
    '''
    Plays one turn in the game
    1) Prints sticks left
    2) Prints player's turn
    3) Does either a player turn (user input) or bot (automatic)
    4) Updates stick amount based on turn
    5) Checks if there is a winner

    :param currentPen: how many sticks there are left
    :param currentName: the name of the person going
    :return: array, amount of sticks left & the player for next turns
    '''
    print("|" * currentPen)
    print("%s's turn: " % currentName)

    # Player turn (changes current name as well)
    if currentName == "John":
        inputPen = input()
        while not is_pen_amt_valid(currentPen, inputPen):
            inputPen = input()

        inputPen = int(inputPen)
        currentName = "Jack"
    # Bot turn
    elif currentName == "Jack":
        inputPen = bot_turn(currentPen)
        print(inputPen)
        currentName = "John"

    currentPen -= inputPen
    if currentPen <= 0:
        win(currentName)


    return [currentPen, currentName]

#####
# Main code

# Takes input for initial pencil amount
currentPenAmt = input("How many pencils would you like to use:")
while not is_inital_pen_amt_valid(currentPenAmt):
    currentPenAmt = input()
currentPenAmt = int(currentPenAmt)

# Takes input for initial name
name = input("Who will be the first (John, Jack): ")
while not is_name_valid(name):
    name = input("Choose between 'John' and 'Jack'")

# Runs the turns
while currentPenAmt > 0:
    currentPenAmt, name = turn(currentPenAmt, name)


