alphabet=input("enter alphabet")
symbol=input("enter symbol")
number=int(input("enter number"))
if alphabet>="A" and alphabet<="z":
    print("move forward")
else:
    print("try alphabet")
if symbol=="#" or symbol=="@"  or symbol=="_":
    print("move further")
else:  
    print("choose wisely") 
if number>1 and number>100:
    print("strong number")  
    print(alphabet+symbol+str(number))    
else:
    print("try again")       
