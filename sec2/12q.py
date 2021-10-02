f = open("./popular-names.txt", "r")
f_col1 = open("./col1.txt", "w")
f_col2 = open("./col2.txt", "w")

list = f.readlines()
for i in list:
    f_col1.write(i.split()[0] + "\n")
    f_col2.write(i.split()[1] + "\n")

f.close()
f_col1.close()
f_col2.close()