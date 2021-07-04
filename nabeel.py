# simple programe to  login amd view details of a bank account
# Nabeel-4-atm
username=input ("Enter the user name")
# enter the user name
pin=int(input ("Enter the 6 digit pin"))
# enter the pin
print("\t\t\tWelcome to Canara bank", "\nHi, "+username)
#  display the activities 
print("\n 1 Account details \n 2 View balance\n 3 View transaction ")
# ask to enter the choice
print("Enter your choice ")
ch=int(input())
# input the choice and display the output
if ch==1:
  print("User name: "+username+"\nAccount no: 19GA3456 \nAccount type: Saving \nBranch: Kizhithalli ")
elif ch==2:
  print("Your balnce ₹15000.25")
elif ch==3:
  print("Transaction details\n04-03-2020 transfer to 423YT424\t₹1800-\n₹02-03-2020 transfer to 562HK526\t₹2000+")
else :
  print("Wrong choice")
print("\n\n\t\t\t\tThankyou")
 

 
