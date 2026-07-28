import json

data={"name":"nandini",
      "age":"18",
      "fav thing":"studying-workingout"}

file_path="C:/Users/NANDINI TANWAR/OneDrive/Desktop/output.txt"

try:

  with open(file_path,"w") as f:
    json.dump(data,f,indent=4)
    print(f"json file {file_path} is ceated")

except FileExistsError:
  print("file already exists")