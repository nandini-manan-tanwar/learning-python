# Membership operators = used to test whether a value or varia is found in a sequence
# (string, list, tuple, set, or dictionary)
# 1. in
# 2. not in  

email=input("enter your email")

while True:
 if "@" in email and '.' in email :
    print(f"{email} is valid email")
    break;
 else:
    email=input("please enter valid email ")
    