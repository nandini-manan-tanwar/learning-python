# List comprehension A concise way to create lists in Python
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]


# without list comprehension 
doubles=[]
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

#with list comprehension
doubles = [(x*2) for x in range(1,11)]
print(doubles)


#2
fruits=['apple','cherry','banana']
fruits=[fruit.upper() for fruit in fruits]
print(fruits)