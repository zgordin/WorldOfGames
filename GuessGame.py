import random
# import score

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return  secret_number

def play(difficulty):
    random_number = generate_number(difficulty)
    print(random_number)