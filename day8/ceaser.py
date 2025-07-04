
# def encode(text,shift):
#     text=text.lower().replace(" ","")
#     cipher=""
#     for letter in text:
#         newi=alpha.index(letter)+shift
#         newi%=len(alpha)
#         cipher+=alpha[newi]
#     print(f"encrypted message:\n{cipher}")
    
# def decode(text,shift):
#     text=text.lower().replace(" ","")
#     cipher=""
#     for letter in text:
#         newi=alpha.index(letter)-shift
#         newi%=len(alpha)
#         cipher+=alpha[newi]
#     print(f"decrypted message:\n{cipher}")
    
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser(text,shift,choice):
    text=text.lower().replace(" ","")
    cipher=""
    if choice=="decode":
        shift*=-1
    for letter in text:
        newi=alpha.index(letter)+shift
        newi%=len(alpha)
        cipher+=alpha[newi]
    print(f"encrypted message:\n{cipher}")
  
again=True
while again:
    req=input("encode or decode\n").lower()
    message=input("enter message:\n")
    shiftno=int(input("enter shift amount:\n"))
    ceaser(message,shiftno,req) 
    continu=input("once again:\n").lower()
    if continu=='no':
        again=False
        
