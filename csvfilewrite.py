import json
import csv

employee=[["name","age","fav food"],
          ["nandini","18","pasta"],
          ["shaurya","12","cake"]]

file_path="C:/Users/NANDINI TANWAR/OneDrive/Desktop/output.csv"

try:

  with open(file_path,"w",newline="") as f:
    writer=csv.writer(f)
    for row in employee:
      writer.writerow(row)
  print(f"csv file {file_path} is ceated")

except FileExistsError:
  print("file already exists")
