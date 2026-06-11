import time
user_time=int(input("ENTER THE TIME FOR THE ALARM CLOCK"))

for x in range(user_time,0,-1):
 second=x % 60
 minutes=int(x/60)%60
 hours=int(x/3600)%60
 print(f"{hours:02}:{minutes:02}:{second:02}")
 time.sleep(1)
 if second==0:
  break
 else:
  continue
  
   

print("TIME'S UP")
