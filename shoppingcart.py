foods=[]
prices=[]
quantities=[]
total_amount=0
 
while True:
    food = input("Enter food: ")
    print(f"You entered: {food}")

    if food == "end":
      break
    else :
     price=float(input(f'enter price for {food}= ₹'))
     quantity=int(input(f'enter quantity for {food}'))
     foods.append(food)
     quantities.append(quantity)
     prices.append(price)

print("---------your cart---------")

for i in range(len(foods)):
  item_amount= prices[i]*quantities[i]  
  print(f"item:{foods[i]} : quantity={quantities[i]} : price={prices[i]} : item amount={item_amount} ")
  total_amount=total_amount+item_amount

print(f'your total amount is = ₹ {total_amount} ')