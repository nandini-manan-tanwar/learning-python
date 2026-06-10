principal_amt=int((input("enter the amount to be deposited")).strip())
time=int((input("enter the time for deposit")).strip())
rate=int((input("enter rate of interest")).strip())
rate=rate/100
n=int((input("number of times interest added")).strip())
v=0 
current_principal=principal_amt
total_interest=0
while v<time:
    interest=current_principal*(rate/n)
    v=v+1
    total_interest=interest+total_interest
    current_principal=current_principal+interest

total_amount=principal_amt+total_interest
print(f"your total amount for principal amount : {principal_amt:<10},for time: {time:<10} , for rate: {rate:<10}is")
print(f"total amount = {total_amount:<10} ")
