number1=float(input("enter your first number"))
number2=float(input("enter second number"))
operator=input("enter the operator")

if operator=="+":
    print(round(number1+number2))
elif operator=="-":
    print(round(number1-number2))
elif operator=="*":
    print(round(number1*number2)) 
elif operator=="/":
    print(round(number1/number2))
elif operator=="%":
    print(round(number1%number2))
else:
    print("please insert eligible operator")