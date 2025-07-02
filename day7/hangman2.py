import random
word_list = ["aardvark", "baboon", "camel"]
guess=input("Guess the letter:\n")
word = random.choice(word_list)
blanks=''
for w in word:
   
   if w==guess:
      blanks+=guess
   else:
      blanks+='_'

print(blanks)