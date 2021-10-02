f = open("./popular-names.txt",'r')

list = f.read()

for i in list:
    if(i == '\t'):
        list = list.replace(i,' ')

print(list)

f.close()