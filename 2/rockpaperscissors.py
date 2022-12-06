# for each line if is \n add all the numbers previously
import os
# from depq import DEPQ as queue

# SCORES: (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
# X Y Z 
# X = Scissors, 3 | Y = Paper, 2 | Z = Rock, 1
# X = Paper, 2 | Y = Rock, 1 | Z = Scissors, 3

# A = Rock, B = paper, C = Scissors
# X = Rock, 1 | Y = Paper, 2 | Z = Scissors, 3

# AX = 4, AY = 

def score():
    # q = queue()
    # answer = 0
    total = 0
    dictionary = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    input_file = open("rpc.txt",'r')
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        total += dictionary[line] 
            
            
    return total
        

# print(score())

# A = Rock, B = paper, C = Scissors
# X = lose | Y = draw | Z = win
# X = Rock, 1 | Y = Paper, 2 | Z = Scissors, 3
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)


def wld():
    # q = queue()
    # answer = 0
    total = 0
    dictionary = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
    input_file = open("rpc.txt",'r')
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        total += dictionary[line] 
            
            
    return total

print(wld())
