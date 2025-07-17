import random
target=random.randint(1,100)
lives=0

print("Welcome to the Number Guessing Game!\n")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

if difficulty=='hard':
    print("You have 5 attempts remaining to guess the number.")
    lives=5
elif difficulty=='easy':
    print("You have 10 attempts remaining to guess the number.")
    lives=10
    
while lives!=0:
    num=int(input("Make a guess:"))
    print(f"You have {lives} attempts remaining to guess the number.")
    if num<target:
        print("Too Low")
    elif num>target:
        print("Too High")
    elif num==target:
        print(f"You got it! The answer was {target}")    
    lives-=1
    if lives==0:
        print("You lose")
        