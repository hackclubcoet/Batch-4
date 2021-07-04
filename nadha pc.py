#program to print quiz 

# nadhapc-43-quiz
# input the answer 
ans ={"1":'1',"2":'1',"3":'60',"4":'25',"5":'217'}
#question 1
i=1 

a=0 
#printing the questions 
print ("cos 60 = ?")
print ("tan 45 = ?") 
print ("360/60 = ?")
print ("5*5 = ?")
print ("200+17 = ?")
while i<6 : 
  n= input() 
  if n == ans[str(i)] : 
    a+=1 
  i+=1  
  # printing the result of quiz  
if a==5:
    print("YOU WIN") 
else: 
    print("YOU LOSE")
  


