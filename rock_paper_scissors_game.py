#Collect all the components of your program to run it in a for loop
#Import the random library
import random
#Add the code to create a list containing the three actions of the game.
game = ['rock' , 'paper' , 'scissors']
#Add the code to set the scores of players to 0
score1 = 0
score2 = 0
#Add the code to ask the user how many rounds they want to play
round = int(input("How many rounds your want to play? "))
#Write a for loop and put the game inside
for i in range(round):
  #Add the code to print the players choices
  gamer1 = random.choice(game)
  gamer2 = random.choice(game)
  print("1st gamer: ",gamer1)
  print("2nd gamer: ",gamer2)
  #Add the tie condition
  if gamer1 == gamer2 :
    print( "Tie! Both players chose the same action.")
  #Add the remaining condition
  elif gamer1 == 'paper':
    if gamer2 == 'rock':
      print('winner 1st gamer')
      score1 += 1
    if gamer2 == 'scissors':
      print('winner 2st gamer')
      score2 += 1
  elif gamer1 == 'scissors' :
    if gamer2 == 'paper':
      print('winner 1st gamer')
      score1 += 1
    if gamer2 == 'rock':
      print('winner 2st gamer')
      score2 += 1
  elif gamer1 == 'rock' :
    if gamer2 == 'scissors':
      print('winner 1st gamer')
      score1 += 1
    if gamer2 == 'paper':
      print('winner 2st gamer')
      score2 += 1

  #print the score
  print("Score:","1.Gamer =",score1,"2.Gamer =",score2)

if score1 > score2 :
  print("Winner is 1. Gamer!")
elif score2 > score1 :
  print("Winner is 2. Gamer!")
else:
  print("Tie !")

