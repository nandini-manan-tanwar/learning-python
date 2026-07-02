# a stand of food items just like in threaters 
foods = {'pizza': 350,
         'pasta': 400,
         'samosa': 100,
         'ice cream': 80}

print("                MENU                  ")
print("--------------------------------------")
keys=foods.keys()
values=foods.values()
for key,value in foods.items():
    print((f"{key}:{value}").upper()) 

cart=[]
total=0

while True:
    food=input(('enter desired food from menu \n (enter q for quiting)').lower()).strip()
    if food=="q":
      print("------------------YOUR CART IS READY------------------")
      break
    elif foods.get(food) is not None :
       cart.append(food)
    else:
       food=input('you can only enter food from menue')


print(f"\n \nyour items:{cart}")       

for food in cart:
   total +=  foods.get(food)  

print(f"YOUR TOTAL PRICE IS : {total} ")