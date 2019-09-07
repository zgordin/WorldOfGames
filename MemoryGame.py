import random
import time
from Utils import screen_cleaner
#import score


def generate_sequence(difficulty):
    seq_list = list()
    for i in range(difficulty):
        num = random.randint(1, 101)
        seq_list.append(num)
    return seq_list


def get_list_from_user(difficulty):
    usr_seq_list = list()
    for i in range(difficulty):
        num = int(input("Please enter a number between 1-100: "))
        usr_seq_list.append(num)
    return usr_seq_list

def is_list_equal(list_a, list_b):
    if list_a == list_b:
        return True
    else:
        return False


def play(difficulty):
    list_a = generate_sequence(difficulty)
    print(list_a)
    time.sleep(0.7)
    screen_cleaner()
    list_b = get_list_from_user(difficulty)

    if is_list_equal(list_a,list_b) == True:
        print("True")
        #score.add_score(difficulty)
    else:
        print("False")