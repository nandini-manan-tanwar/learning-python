import random
number=random.randint(570,580)

dice=((input('do you wanna roll a dice ?(yes or no)')).lower()).strip()

if dice=="yes":
    print(f"your number is - {number}")
else:
    print("ok bye")
