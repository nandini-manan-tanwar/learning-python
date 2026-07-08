# matchcase statement(switch)- alternative for using elif statement 
# if value matches the case executes the code block under it 
# benefit - cleaner syntax 

def day_of_week (day):
 match day:
     case 1:
        return "it's monday"
     case 2:
        return "it's tuesday"
     case 3:
        return "it's wednesday"
     case 4:
        return "it's thursady"
     case 5:
        return "it's friday"
     case 6:
        return "it's saturday"
     case 7:
        return "it's sunday"
     case _:
        return 'invalid'
    
day=int(input('enter the number'))
print(day_of_week(day))


def is_weekend (day2):
 match day2:
      case "sunday"|"staurday":
       return True
      case 'monday'| "tuesday"|"wednesday"|"thursday"|"friday":
       return False
      case _:
       return False
    
day2=input('enter your day')
print(is_weekend(day2))