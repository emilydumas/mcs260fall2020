"""
Dice game where players roll two 6-sided dice and have
the total added to their score, unless they sum to the
"knockout" number which ends their turn.  First player
to reach a certain total wins.

MCS 260 Fall 2020 Lecture 20
"""

import dice   # this line will read and execute dice.py

print("This is a two-player game.")
print("What should be the goal?  Reaching this total wins.")

goal = int(input("Goal: "))

print("\nWhat should be the knockout number?  Rolling this ends your turn.")
print("It should be a number between 2 and 12.  If the answer is blank,")
print("the number will be chosen at random.")

s = input("Knockout: ")
if s == "":
    kn = 1 + dice.roll(11)
    print("The knockout number is: {}".format(kn))
else:
    kn = int(s)

# Play
player,other = 0,1  # player is current player; other is the other one
scores = [ 0, 0 ]
#     /---- are all the scores less than the threshold to win
#     |  if so, continue playing.
while all( [ k < goal for k in scores ] ):
    print()
    print("Scores: Player 1: {}  Player 2: {}".format(scores[0],scores[1]))
    print("It is player {}'s turn.  Press Enter to roll.".format(player+1))
    x,y = dice.roll_many(6,2)
    input()
    print("Player {} rolled {} and {} for total of {}.".format(player+1,x,y,x+y))
    if x+y == kn:
        print("Knockout! Your turn ends with no points added to score.")
    else:
        scores[player] = scores[player] + x + y

    # Switch who's up
    player,other = other,player

if scores[0] >= goal:
    winner = 0
else:
    winner = 1

print()
print("Final scores: Player 1: {}  Player 2: {}.".format(scores[0],scores[1]))
print("Player {} wins!".format(winner+1))
