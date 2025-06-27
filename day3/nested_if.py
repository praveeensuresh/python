print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("enter age:"))
    if age <= 12 :
        print("child ticket ")
        bill=5
    elif age <= 18 :
        print("teen ticket")
        bill=12
    else:
        print("adult")
        bill=18
    pic=input("want pic?Y or N")
    if pic=='y':
        bill+=3
    print("bill:",bill)
else:
    print("Sorry you have to grow taller before you can ride.")
