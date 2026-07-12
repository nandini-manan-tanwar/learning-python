import random

def spin_row ():
     symbols=['🍒','🌸','💛','🧿']

     return[random.choice(symbols)for _ in range(3)]

def print_row(row):
     print("*******************")
     print("-".join(row))
     print("*******************")

def get_payout(row,bet):
   if row[0]==row[1]==row[2]:
       if row[0]=="🍒":
          return int(bet)*2   
       elif row[0]=="🌸":
          return int(bet)*3
       elif row[0]=="💛":
          return int(bet)*4     
       else :
          return int(bet)*5     
    
   else:
       return 0

  



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
    print("spinning......")
    print_row(row) 

    payout=get_payout(row,bet)
    if int(payout)>0:
        print(f"you won ${payout}")
    else:
        print("sorry you lost this round")
          
    balance+=int(payout)
    answer=input(("do you wanna play again?(Y/N)"))
    if answer.upper()=="N":
        break
    elif answer.upper()=="Y":
        continue
    else:
        answer=input("enter only y or n")

