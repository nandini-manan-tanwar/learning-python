food=((input("what's your fav food  [enter q to quit]")).strip())

while not food=="q":
    print(f"you like {food}")
    food=((input("what's your fav food  [enter q to quit]")).strip())
  
print("bye")
    
num=int(input("enter number between 1 to 10"))

while num<1 or num> 10 :
    print("enter a valid number")
    num=int(input("enter number between 1 to 10"))

print(f"your number is {num} ")    
