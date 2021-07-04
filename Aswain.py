import random

# Aswain-4-Number Guessing
number = random.randrange(1,10)
# returns a randomly selected element from the range created by start,stop and step argumemts
guess = int(input("Guess a number between 1 and 10 :"))
#stores the guessed number

while guess!= number: #checks whether guess not to equal to number
  if guess<number:
    print("You need to guess higher.Please try again!")
    guess = int(input("Guess a number between 1 and 10 :"))
  else:
    print("You need to guess lower. Please try again")
    guess = int(input("Guess a number between 1and 10 :"))
    
  #branching statement
    
print("Guessed the correct number!")  
  #prints the guessed number