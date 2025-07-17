def add(n1,n2):
   return n1+n2
def sub(n1,n2):
   return n1-n2
def multi(n1,n2):
   return n1*n2
def div(n1,n2):
   return n1/n2

opdict={
    "+":add,
    "-":sub,
    "*":multi,
    "/":div
    }
again=True
n1=float(input("First Number:"))
while again:
   op=input("operator:")
   n2=float(input("Second Number:"))
   ans=opdict[op](n1,n2)
   print(f"{n1}{op}{n2}={ans}")
   req=input("continue? Y or N:").lower()
   if req=='n':
      again=False
   if req=='y':
       n1=ans
       
