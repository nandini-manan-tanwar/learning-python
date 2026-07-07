numbers =['1','2','3','4']

for number in reversed(numbers):
    print(number)


name="nandini tanwar"
first_name = ""
last_name = ""
space_found = False

for character in name:
    if character == " ":
        space_found = True
    elif not space_found:
        first_name += character
    else:
        last_name += character

print(last_name, first_name)