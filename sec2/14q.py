n = input()
f = open('./popular-names.txt','r')
list = f.readlines()
cnt = 0

#print(i for i in list) ジェネレーターが返される...

for i in list:
    print(i,end='')
    cnt += 1
    if cnt == int(n):
        break

"""
コマンドライン引数を用いた実装
import sys

sys.argv[0]
"""
f.close()