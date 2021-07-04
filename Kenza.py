import time
'''We import time module so we can use sleep which delays time.'''
#kenza-4-Hello World(Animation)
def result(word):
  '''returns "Hello world" character by character and there should be a delay of 1 sec between printing each character.'''
  for i in word:
    print(i)
    time.sleep(1)
result("Hello world")
