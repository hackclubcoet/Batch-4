from math import sin,cos,pi 

#Vyshakh M-4-calculator 
def add(x, y):
    return x + y       #this function add 2 numbers

def subtract(x, y):    #this function subtract 2 numbers
    return x - y

def multiply(x, y):    #this function multplies 2 numbers
    return x * y

def divide(x, y):      #this function divides 2 numbers
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")     #choices for user to select an option
print("3.Multiply")
print("4.Divide")  
print('5.sin function') 
print('6.cos function')  
print('7.exit')  


choice= int(input("enter choice:"))  #user can enter a output
while  choice != 7:

 if  choice ==1 :
  num1=int(input("enter the first number:"))
  num2=int(input('enterthe second number:') )
  print(num1, "+", num2, "=", add(num1, num2))
 elif choice ==2: 
  num1=int(input("enter the first number:"))
  num2=int(input('enterthe second number:'))
  print(num1, "-", num2, "=", subtract(num1, num2))
 elif choice ==3: 
  num1=int(input("enter the first number:"))
  num2=int(input('enterthe second number:'))
  print(num1, "*", num2, "=", multiply(num1, num2))
 elif choice == 4: 
  num1=int(input("enter the first number:"))
  num2=int(input('enterthe second number:'))
  print(num1, "/", num2, "=", divide(num1, num2))    
 elif choice==5: 
  x=int(input('Enter angle(degree):')) 
  print(sin(x*(pi/180))) 
 elif choice ==6: 
  x=int(input('Enter angle(degree):')) 
  print(cos(x*(pi/180)))
 else: 
   print('inavid output') 
   break





