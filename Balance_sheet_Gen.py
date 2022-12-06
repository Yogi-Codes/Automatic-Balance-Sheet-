import csv
import requests
import json
import urllib
import sys
from termcolor import colored, cprint
from colored import fg
import time

color1 = fg('#F4B400')
color2 = fg('#E6337A')
color3 = fg('#22FB4F')
color4 = fg('#E3BFE1')





company = input("Enter Company Code EXAMPLE MSFT FB GOOG or ANY OTHER [Default AAPL   (apple)]\n $>") or "AAPL"





CSV_URL_full = f'https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/{company}?apikey=c89d4c202df584ed18ab0d6bef0ec6f0'

with requests.Session() as s:
  download_json = s.get(CSV_URL_full)
  decoded_content_json = download_json.content.decode('utf-8')
  open('json1.csv', 'wb').write(download_json.content)
  with open('json1.csv', 'r') as f_in, open('table1.txt', 'w') as f_out:
    content = f_in.read().replace(',', '\t')
    f_out.write(content)






CSV_URL = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?datatype=csv&apikey=c89d4c202df584ed18ab0d6bef0ec6f0'

with requests.Session() as s:
  download = s.get(CSV_URL)
  decoded_content = download.content.decode('utf-8')
  open('account.csv', 'wb').write(download.content)
  with open('account.csv', 'r') as f_in, open('table.txt', 'w') as f_out:
    content = f_in.read().replace(',', '\t')
    f_out.write(content)


    

with open('table.txt') as f:
  date = f.readline()
  date = date.split('\t')
f = open("table.txt", 'r')
a = 1
print("Enter the year as per following scheme")
k = -1
date[-1] = date[-1].strip("\n")
for d in date:
  if k == -2:
    k = k + 1
    continue
  print(color3+f"{d} : {k+1}")
  k = k + 1
year = int(input("$> "))


print("Fetching required data ...")
time.sleep(2)


new = download_json.json()
new2= json.dumps(new[year-2])
new2=new2.split(", ")
color5 =fg("#00b8ff")
for line in new2:
  print(color5+line)
  time.sleep(0.1)





for aline in f:
  values = aline.split('\t')
  if values[0] =="":
    for i in range(2, 3):
      if values[2] != "":
        print(color2 + f"{values[1]} : ", end="")
        print(color1 + f" ${values[year]}", end="")
        print(color3 + f"\t[({date[year]})]", end="")
        print()
      else:
        print(color2 + f"{values[1]}")

  else:
    if values[0] != "date":
      print(color4 + "-" * 100)
      print(color4 + f"{values[0]} :")
      print(color4 + "-" * 100)
      
      

  a = a + 1
f.close()