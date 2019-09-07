import random
# import score

# Generate number that will return a random number between 1 to difficulty
def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return  secret_number

# Ask the user to guess a number
def get_guess_from_user(difficulty):
    guess = int(input("Please guess the number between 1 and",difficulty," :"))
    while guess > difficulty or guess < 1:
        print("Input should be a number between 1 - ",difficulty," \n")
        guess = int(input("Please guess the number: \n"))
    return guess

# Compare the secret generated number to the one prompted
def compare_results(generate_number, get_guess_from_user):
    if generate_number == get_guess_from_user:
        return True
    else:
        return False


def play(difficulty):
    random_number = generate_number(difficulty)
    user_input = get_guess_from_user()

    print(random_number , user_input)
    if compare_results(random_number,user_input) == True:
        print("True")
        # score.add_score(difficulty)
    else:
        print("False")
