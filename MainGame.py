from Live import load_game, welcome
from Utils import screen_cleaner
from Utils import run_flask
# import Utils

screen_cleaner()
print(welcome("Ziv"))
load_game()
run_flask()  # Rise web server to show game scores