rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)_______
          __________)
          ___________)
         ____________)
---._______________)
'''

scissors = '''
    _______
---'   ____)______
          _________)
       ____________)
      (____)
---.__(___)
'''
import random
hands=[rock,paper,scissors]
player=int((input("choose one Rock=0 paper=1 scissors=2\n")))
print("your hand")
print(hands[player])
if player>=0 and player<=2:
    computer=random.randint(0,2)
    print("computer hand")
    print(hands[computer])
    if player==0 and computer==2:#rock scissor
        print("YOU WIN !!")
    elif player==1 and computer==0:#paper rock
        print("YOU WIN !!")
    elif player==2 and computer==1:#scissor paper
        print("YOU WIN !!")
    elif player==computer:
        print("DRAW !!")
    else:
        print("YOU LOSE")
else:
    print("invalid sign")