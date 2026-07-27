try:
    num=int(input("enter a number"))
    result=100/num
    print(result)


except ZeroDivisionError:
    num=int(input("dude that's 0 not applicable"))
except ValueError:
   num=int(input("sybau🥀,that's not even a number"))
else:
    print("everything is good")
finally:
    print("this runs no matter what")