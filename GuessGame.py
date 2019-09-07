import random
from Score import add_score


# Generate number that will return a random number between 1 to difficulty
def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return  secret_number

# Ask the user to guess a number
def get_guess_from_user(difficulty):
    guess = int(input("Please guess the number between 1 and %d :"% difficulty))
    while guess > difficulty or guess < 1:
        print("Input should be a number between 1 - %d\n"%difficulty)
        guess = int(input("Please guess the number: \n"))
    return guess

def compare_results(user_input, secret_number):
    if secret_number == user_input:
        return True
    else:
        return False

def play(difficulty):
    # Get random number
    random_number = generate_number(difficulty)
    # Get user input
    user_input = get_guess_from_user(difficulty)

    print("random number is %d , your guess is %d"%(random_number, user_input))
    # Get results comparison
    result=compare_results(user_input,random_number)
    # Return True / False if the user lost or won.
    if result==True:
        print("True")
        add_score(difficulty)
    else:
        print("False")
