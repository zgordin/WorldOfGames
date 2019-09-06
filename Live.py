# import MemoryGame
import GuessGame
# import Score
import Utils

# Function to welcome a player. It gets name and prints greeting
def welcome(name) :
    return "\nHello " + name + " and welcome to the world of Games (WoG). \nHere you can find many cool games to play\n"

# Function to get a player to choose which play he will play and what difficulty level it will be.
def load_game():
    exception = False                     # Flag to keep info whether exception was thrown or not
    while exception == False:
        print("Please choose a game to play: \n"
              "\t1. Memory Game - a sequence of  numbers  will appear for 1 second and you have to guess it back \n"
              "\t2. Guess Game - guess a number and see if you  chose like the computer \n")
        try:
             game_choice = int(input(">>>"))
             if game_choice not in range (1,3):
                raise ValueError
             else:
                 exception = True        # The exception was not thrown, so the loop will be finished
        except ValueError as e:
            print(Utils.ERROR_MESSAGE())
    d_exception = False                    # Flag to keep info whether exception was thrown or not
    while d_exception == False:
        print("Please choose game difficulty from 1 to 5:")
        try:
            difficulty_choice = int(input(">>>"))
            if difficulty_choice not in range (1,6):
                raise ValueError
            else:
                d_exception = True         # The exception was not thrown, so the loop will be finished.
        except ValueError as e:
                print(Utils.ERROR_MESSAGE())

    if game_choice == 1:
        MemoryGame.set_difficulty(difficulty_choice)
        result = MemoryGame.play()
    if game_choice == 2:
        GuessGame.play(difficulty_choice)
        # GuessGame.set_difficulty(difficulty_choice)
        # result = GuessGame.play()



    # if result == True:
    #     print("                                     You won")
    #     Score.add_score(difficulty_choice)
    # else:
    #     print("                                     You lost")
    #     Score.create_zero_score()