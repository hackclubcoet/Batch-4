import time

#Muhammad Nihad K V-4-Hello World (animation)
def result(word):
  #this function takes a word and print it character by character with 1 second delay
	for i in word:
		print(i, end="")
		time.sleep(1)
print(result("Hello World"))