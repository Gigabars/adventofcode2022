#First, A = rock, B = paper, C = scissors
#Sec, Y = Paper, Rock = X, Scissors = Z
#The score is 6 if you win, 3 if you draw, 0 if you lose.
#1 if you play rock, 2 if you play paper, 3 if you play scissors.
score = 0 # To keep track of the players score.
oppmove = ""
yourmove = ""
oppkey = {"A":"rock", "B":"paper","C":"scissors"}
yourkey = {"X":"rock", "Y":"paper", "Z":"scissors"}
f = open("input.txt", "r")
for line in f:
    oppmove = oppkey.get(line[0]) #Puts the values into a more readable format.
    yourmove = yourkey.get(line[2])
    #The code for getting the value of your play
    if yourmove == "rock":
        score = score + 1
    elif yourmove == "paper":
        score = score + 2
    elif yourmove == "scissors":
        score = score + 3
    #Then we find out if we win, tie or lose
    if yourmove == oppmove:
        score = score + 3
    elif yourmove == "rock" and oppmove == "paper":
        score = score + 0
    elif yourmove == "rock" and oppmove == "scissors":
        score = score + 6   

    elif yourmove == "paper" and oppmove == "rock":
        score = score + 6
    elif yourmove == "paper" and oppmove == "scissors":
        score = score + 0

    elif yourmove == "scissors" and oppmove == "rock":
        score = score + 0
    elif yourmove == "scissors" and oppmove == "paper":
        score = score + 6
print(score)
