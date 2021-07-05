#program to find treasure

#Riya Febin V.P-batch4-treasure hunt
print("welcome to treasure island")
print("your mission is to find the treasure")
#ask to enter the choice
choice1=input('where do you want to go?"left" or "right".').lower()
#conditions given in the question

if choice1== "left":
    choice2=input('there is an island."wait" or "swim".').lower()
    if choice2== "wait":  
        choice3=input('which door do you choose?"red" or "blue" or "yellow".').lower()
        
        if choice3== "red": 
            print("burned by fire.game over")
        elif choice3== "blue":
            print("eaten by beasts.game over")
       
    
           
        elif choice3== "yellow": 
            print("you win!!")
        
        else: 
            print("game over")
      
    else:
        print("you got attacked by traut,game over")
else: 
    print("you fell into a hole.game over")
  
    
  
    