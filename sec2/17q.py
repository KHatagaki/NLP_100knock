f = open("popular-names.txt", "r")
sum = set()

list = f.readlines()

for i in list:
    sum.add(i.split()[0])

print(len(sum))

f.close()