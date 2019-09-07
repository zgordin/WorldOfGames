from Utils import SCORES_FILE_NAME

def add_score(points):
    try:
        scores_file = open(SCORES_FILE_NAME, "r+")
        current_score = int(scores_file.read())
        scores_file.close()
        try:  # If succeeded to read, sum up new value with old one and write to the file
            scores_file = open(SCORES_FILE_NAME, "w")
            scores_file.write(str(current_score + points))
            print("number of points: %d"%(current_score + points))
            scores_file.close()
        except:  # If not succeeded to write the sum to the file, raise exception
            raise Exception('Could not write to Scores.txt')
    except IOError:
        #if file does not exist, create it
        print('Could not open Scores.txt. Creating new one.')
        try:  # if not succeeded to open and read scores file, try to open new file and write current score
            scores_file= open(SCORES_FILE_NAME, 'w')
            scores_file.write(str(points))
            print("number of points: %d"%points)
            scores_file.close()
        except:  # If not succeeded to write to the file the new score, raise exception
            raise Exception('Could not write to  Scores.txt')




