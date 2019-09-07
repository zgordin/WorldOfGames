import os

SCORES_FILE_NAME = "Scores.txt"  # A string representing a file name. By default “Scores.txt”

def ERROR_MESSAGE():
        print("\tSomething went wrong..\n")


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

# Raise HTPP server to show scores of game
def run_flask():
    os.system("python MainScores.py")
