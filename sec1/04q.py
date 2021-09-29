import re
dic = {}

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. '\
      'New Nations Might Also Sign Peace Security Clause Arthur King Can.'
check = [0,4,5,6,7,8,14,15,18]

str = re.sub('[./]','',str)
str = str.split()

for i in range(20):
    if i in check:
        dic[i+1] = str[i][0:1]
    else:
        dic[i+1] = str[i][0:2]

print(dic)