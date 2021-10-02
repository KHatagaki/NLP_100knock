f = open("./col.txt", "w")
f_col1 = open("./col1.txt", "r")
f_col2 = open("./col2.txt", "r")

list = f_col1.readlines()
list2 = f_col2.readlines()

for i,j in zip(list,list2):
    i = i.replace('\n','')
    j = j.replace('\n','')
    f.write(i + "\t" + j + "\n")

f.close()
f_col1.close()
f_col2.close()

