def calculate_love_score(name1,name2):
    name=name1+name2
    name.lower()
    raw=name.replace(" ","")
    Tcount=0
    lcount=0
    for i in raw:
        if i in "true":
            Tcount+=1
        if i in "love":
            lcount+=1
    print(str(Tcount)+str(lcount))
    
print(calculate_love_score("Kanye West", "Kim Kardashian"))

            
    

