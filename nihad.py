import time
def result(word):
  for i in word:
    print(i,end="") 
    time.sleep(1)
print(result("Hello World"))