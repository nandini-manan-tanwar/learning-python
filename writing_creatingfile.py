employees=["barbie","ken","rachel"]
file_path="C:/Users/NANDINI TANWAR/OneDrive/Desktop/output.txt"

try:

  with open(file_path,"w") as f:
    for employee in employees:
      f.write(f"{employee}\n") 
    print(f"your file '{file_path}' is created ")

except FileExistsError:
  print("file already exists")
