import random

def spin_row ():
     symbols=['🍒','🌸','💛','🧿']

     return[random.choice(symbols)for _ in range(3)]


print("*************************")
print("welcome to slotty machine")
print("symbols:🍒🌸💛🧿")
print("*************************")
balance=100
while balance>0:
    print(f"your balance is {balance} ")
    bet=input("enter the bet you wanna place ")
    
    while not bet.isdigit():
        bet=(input("enter valid digits")).strip()
    
    while int(bet)>balance:
         bet=int(input("bet should not be greater than balance"))
         
    while int(bet)<=0:
         bet=int(input("bet must not be less than or equal to 0"))
         
    balance=balance-int(bet)
    row=spin_row()
    print(row) 
         
          
    
