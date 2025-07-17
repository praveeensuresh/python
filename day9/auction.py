dict1:dict[str,int]={}
max=0
again=True
while again:
   name=input("Name:")
   bid=int(input("Bid:"))
   dict1[name]=bid
   again=input("more bidders?:").lower()
   if again=='no':
      again=False
for bid in dict1.values():
   if max<bid:
      max=bid
for name in dict1.keys():
   if bid==max:
      winner=name
print(f"winner is {winner} with bid:{max}")

