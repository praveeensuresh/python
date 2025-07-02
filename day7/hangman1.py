import random
word_list = ["aardvark", "baboon", "camel"]
guess=input("Guess the letter:\n")
word = random.choice(word_list)
for w in word:
   if w==guess:
      print("right")
   else:
      print("false")