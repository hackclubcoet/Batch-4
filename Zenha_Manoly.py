import random

#zenhaManoly-Batch4-Number guessing
number = random.randrange(1,10)
#generate random numbers
guess = int(input("Guess a number between 1 and 10 :"))
#ask users the number
while guess!= number:
  if guess<number:
    print("GUESS HIGHER NUMBER")
    guess = int(input("Guess a number between 1 and 10 :"))
  else:
    print("GUESS LOWER NUMBER")
    guess = int(input("Guess a number between 1and 10 :"))
#conditions applied   
    print("RIGHT GUESS!")
#display right guess  


 
  





