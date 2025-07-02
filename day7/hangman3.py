hangman=[
   '''
      _______
     |/      |

     |      (_)
     |      \|/
     |       |
     |      | |
     |
    _|___
''',
'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
''',
'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |   
     |
    _|___
''',
'''
      _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___
''',
'''
      _______
     |/      |
     |      
     |     
     |       
     |      
     |
    _|___
'''
]


import random
word_list = ["aardvark", "baboon", "camel"]
chosenword = random.choice(word_list)
placeholder=''
for i in chosenword:
   placeholder+='_'
print(placeholder)

lives=4
corrects=[]
gameover=False

while not gameover:
   blanks=''
   guess=input("guess the letter:\n").lower()
   for letter in chosenword:
      if letter==guess:
         blanks+=letter
         corrects.append(guess)
      elif letter in corrects:
         blanks+=letter
      else:
         blanks+='_'
   print(blanks)

   if "_" not in blanks:
      gameover=True
      print("YOU WIN !!!")
   
   if guess not in chosenword:
      lives-=1
      if lives==0:
         gameover=True
         print("YOU LOSE !!")
   print(hangman[lives])



