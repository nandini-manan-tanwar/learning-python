def show_balance():
    print(f"your balance is : {balance}") 

def deposit():
    
      amount=float(input("enter your amount to be deposited"))
      while amount<0:
             amount=float(input("it is not valid amount"))
      else:
             return amount
   
def withdraw():
    amount=float(input("enter the amount to be withdrawn"))
    if amount > balance:
      amount=float(input("enter the valid  amount to be withdrawn"))
    else:   
      return amount

balance=0
is_running=True
def user_choice (choice):
     global balance
     match choice:
        case 1:
           show_balance()
        case 2 :
          balance += deposit()
          return True
        case 3 :
          balance -= withdraw()
        case 4 :
           return  False
        case _:
           print("enter valid choice please ") 
     
     return True
        
while is_running:
    print("welcome to bob")
    print("----------------------------------")
    print("press 1. for showing balance")
    print("press 2. for deposit")
    print("press 3. for withdraw")
    print("press 4. to exit")
    choice= int(input("enter valid choice"))
    is_running = user_choice(choice) 
    


