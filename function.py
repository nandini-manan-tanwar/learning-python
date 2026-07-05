#repetitive used block of code 
# place () after it to invoke it 

def invoice(user_name,amount,duedate):
    print(f'your name is : {user_name}')
    print(f'your due amount:{amount:.2f} due on {duedate}')

invoice("nandini",49.678,"04/01")