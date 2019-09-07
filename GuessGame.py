import random
# import score


# Generate number that will return a random number between 1 to difficulty
def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return  secret_number

# Ask the user to guess a number
def get_guess_from_user(difficulty):
    guess = int(input("Please guess the number between 1 and %d :"% difficulty))
    while guess > difficulty or guess < 1:
        print("Input should be a number between 1 - ",difficulty," \n")
        guess = int(input("Please guess the number: \n"))
    return guess

def compare_results(user_input, secret_number):
    if secret_number == user_input:
        return True
    else:
        return False

def play(difficulty):
    random_number = generate_number(difficulty)
    user_input = get_guess_from_user(difficulty)

    print(random_number, user_input)
    #get results comparison
    result=compare_results(user_input,random_number)
    if result==True:
        print("True")
        # score.add_score(difficulty)
    else:
        print("False")
