import re
a_file = open("harry #1.txt", "r",encoding='utf8')
lines = a_file.readlines()

a_file.close()

new_file = open("harry2.txt", "w+",encoding='utf8')


for line in lines:
   # print(re.match(r'^Page | [1-9]{1,}',line))
    match=re.match(r'^Page | [1-9]{1,}',line)
    #print(match!=None)
    if(match!=None):
        continue
    else:
         new_file.write(line.lower())

new_file.close()
