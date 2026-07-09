def show_balance():
    pass

def deposit():
    pass

def withdraw():
    pass


is_running=True
def user_choice (choice):
     match choice:
        case 1:
           show_balance()
        case 2 :
           deposit()
        case 3 :
           withdraw()
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
    

