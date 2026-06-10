food=((input("what's your fav food  [enter q to quit]")).strip())

while not food=="q":
    print(f"you like {food}\n")
    food=((input("what's your fav food  [enter q to quit]")).strip())
  
print("bye\n\n\n")
    
num=int(input("enter number between 1 to 10\n\n"))

while num<1 or num> 10 :
    print("enter a valid number")
    num=int(input("enter number between 1 to 10"))

print(f"your number is {num}\n ")    

for x in range(12,33,2):
 print(x)
print("\n\n")
creditcard="1234-5678-910"

for x in creditcard:
 print(f"{x}\n")