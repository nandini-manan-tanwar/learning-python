#  types of arguments 
# 1. positional 2. default 3. keyword 4.arbitary
# 1.An argument passed to a function based on its position (order).
# 2.default value of a parameter
# 3. an argument preceded by identifiers 
# 4. varying arguments 

# 1. pos 

def invoice(user_name,amount,duedate):
    print(f'your name is : {user_name}')
    print(f'your due amount:{amount:.2f} due on {duedate}')

invoice("nandini",49.678,"04/01")

# 2. default
def net_price(listedprice,discount=0,tax=0.05):
    return listedprice*(1-discount)*(1+tax)
net_price(450)
# 3. keyword

def net_price(listedprice,discount=0,tax=0.05):
    return listedprice*(1-discount)*(1+tax)
net_price(listedprice=450,discount=0.02)

#  4. arbitary 
# *args= allow you to pass multiple non key word arguments
# **kwargs= pass key word arguments
# *  = (unpacking op)

def multiply(*args):
    total=1
    for arg in args:
     total *= arg
  
    return total

print(multiply(1,2,3))

def print_address(**kwargs):
   for key,value in kwargs.items():
      print(f'{key}:{value}')

print_address(street="40",city="surat",state="gujarat")


def shippy(*args,**kwargs):
   for arg in args:
      print(arg,end=" ")

   print("\n")
   for key,value in kwargs.items():
      print(f'{key}:{value}')

shippy("ahn suho","is","my","fav",street="40",city="surat",state="gujarat")