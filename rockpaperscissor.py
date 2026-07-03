import random 
user_option=((input('enter rock,paper,scissor')).strip()).lower()
options=('rock','paper','scissor')
userscore=0
computerscore=0
tiescore=0
while True:
  if user_option =='rock' or user_option=='paper'or user_option=='scissor' :
    option=random.choice(options)
    print(f'computer choice {option}')
    print(f'your choice     {user_option}')
    
    
    if user_option=="rock" : 
         if option=="scissor":
          userscore+=1
         elif option=="rock":
           tiescore +=1
         else:
           computerscore+=1

    elif user_option=="scissor":
      if option=="paper":
        userscore+=1
      elif option=="scissor":
        tiescore +=1
      else:
        computerscore +=1
    
    else:
      if option=="rock":
        userscore+=1
      elif option=="paper":
        tiescore+=1
      else:
        computerscore+=1
      
    user_option=((input('next round ')).strip()).lower()

  elif user_option=="q":
    print(f"YOUR SCORE:{userscore}\nCOMPUTER SCORE{computerscore}:\nTIE SCORE:{tiescore}")
    break;
  else:
    user_option=(input('you can only enter rock paper and scissor').strip()).lower()
