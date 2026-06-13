symbol=(input("enter your desired symbol")).strip()
rows=int(input("enter the rows of rectangle"))
columns=int(input("enter the columns of rectangle"))

for y in range(rows):
   
   for x in range(columns):
     print(f"{symbol}",end="")
   print() 
   