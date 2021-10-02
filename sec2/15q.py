f = open("popular-names.txt","r")
list = f.readlines()
n = input()
cnt = 0

for i in reversed(list):
    print(i)
    cnt += 1
    if cnt == int(n):
        break

f.close()
