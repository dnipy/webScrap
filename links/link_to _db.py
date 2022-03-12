import json
import os

json_file = open("linkList.json")
blank_file = open('links.json','w')

blank_file.write('[ \n')

data = json.load(json_file)

x1= "{"
x2= "}"

num = 0
for x in data:
    blank_file.write(f' {x1}  "{num}"  :  "{x}"  {x2}, \n')
    num +=1

blank_file.write('\n ]')

blank_file.close()
json_file.close()