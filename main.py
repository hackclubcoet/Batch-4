#program for a shopping cart
usrinp='' 
products=["Apple","Banana", "Strawberry","Cucumber","Potato"] 
#to print default items in the cart
print("Default list: ") 
print(*products,sep="\n") 
def MyList(): 
  print("Select the option to add or or remove product from the cart.") 
  print("Add to add a product")
  print("Remove to delete a product") 
  print("Close to exit") 
 
while usrinp!='Close':
  MyList() 
  usrinp=input("Enter your option") 
 #to execute as per customer's choice
  if usrinp=='Add': #to add items in the cart
    item=input("Please enter the product to be added to the cart" ) 
    products.append(item) 
    print("Added your product to the cart!" +str(products)) 
   #to remove items from the cart   
  elif usrinp=='Remove': 
    item=input("Please enter the product to be removed")
    products.remove(item) 
    print("Removed your product from the cart"+str(products)) 
    #if not to add or remove,close the cart
  elif usrinp=='Close': 
      print("Thank you,happy shopping") 
  #if customer entered an invalid option 
  else: 
       print("Oops!invalid option") 
       
    
    
    
    
     
     
  