# Ask for two numbers


# Let's play a game! Rock Paper Scissors
# see https://en.wikipedia.org/wiki/Rock_paper_scissors for a refresher on the rules
# this can be solved in various manners and will look chaotic!!!

# Write code that does the following:
# - pick a random number between 1 and 3 for the the AI
# - use if-statements to translate the outcome for the AI. 1 = rock, 2 = paper, 3 = scissors
# - ask the user rock, paper, scissors
# - show the user what the AI picked and what the user pickes
# - show the user the outcome of this (see rules). Use if-statements for this
# tip: first do for instance rock for the user and determine the outcomes if the AI chose scissors or paper 

from random import randint
rps = ["Rock", "Paper", "Scissors"]


computerSelection = rps[randint(0,int(len(rps))-1)]
print("computerSelection")
print("Let's play rock, paper, scissors!")
print(rps)

playerSelection = input("Rock paper scissors?")
playerSelection = rps[int(playerSelection)-1]

print("Your selection:", playerSelection, "Computer:", computerSelection)


# Tie
if playerSelection == computerSelection:
    {
        print("it's a tie!")
    }
# Winning case
elif {playerSelection == rps[0] and computerSelection == rps[1] or rps[2]} or {playerSelection == rps[1] and computerSelection == rps[0]} or {playerSelection == rps[2] and computerSelection == rps[1]}:
    {
        print("Winner winner, chicken dinner!")
    }

else:
    {
        print("Helaas Pindakaas!")
    }







