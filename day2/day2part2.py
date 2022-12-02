#First, A = rock, B = paper, C = scissors
#Sec, Y = Paper, Rock = X, Scissors = Z
#The score is 6 if you win, 3 if you draw, 0 if you lose.
#1 if you play rock, 2 if you play paper, 3 if you play scissors.
score = 0 # To keep track of the players score.
oppmove = ""
yourmove = ""
oppkey = {"A":"rock", "B":"paper","C":"scissors"}
yourkey = {"X":"lose", "Y":"draw", "Z":"win"}
f = open("input.txt", "r")
for line in f:
    oppmove = oppkey.get(line[0]) #Puts the values into a more readable format.
    yourmove = yourkey.get(line[2])

    if yourmove == "lose":
        print(yourmove)
        if oppmove == "rock":
            score += 3
        elif oppmove == "paper":
            score += 1
        elif oppmove == "scissors":
            score += 2

    elif yourmove == "draw":
        score += 3
        print(yourmove)
        if oppmove == "rock":
            score += 1
        elif oppmove == "paper":
            score += 2
        elif oppmove == "scissors":
            score += 3

    elif yourmove == "win":
        score += 6
        print(yourmove)
        if oppmove == "rock":
            score += 2
        elif oppmove == "paper":
            score += 3
        elif oppmove == "scissors":
            score += 1
print(score)