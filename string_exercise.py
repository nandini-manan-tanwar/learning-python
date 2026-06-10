# input valid name from user
# must not be more than 12 character
# must not contain spaces
# must not contain digit

name=input(("enter the username")).strip()


if len(name)>12 or name.count(" ")>0 or name.isalpha()==False :
    print("please enter valid username ")
    print("it must not contain spaces and number")
    print("length must not be more than 12 character")

else :
    print(f"username is : {name}")
