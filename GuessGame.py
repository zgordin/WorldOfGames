import random
# import score

#Generate number that will return a random number between 1 to difficulty
def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return  secret_number

def play(difficulty):
    random_number = generate_number(difficulty)
    print(random_number)
