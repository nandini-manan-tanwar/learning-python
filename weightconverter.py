weight=float(input("enter the desired weight"))
unit=((input("enter unit kg or lb")).lower()).strip()

if unit=='kg':
  new_weight= weight*2.20462
  print(f"{new_weight}lb")

elif unit=='lb':
 new_weight = (weight*0.453592)
 print(f"{new_weight}kg")

else:
 print("enter valid unit")