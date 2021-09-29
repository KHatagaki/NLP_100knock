cnt = 0
n = input()
n_cnt = 0
file_list =[]
if 2780 % int(n) != 0:
    print("2780で割り切れる数字を入力する必要があります")
    exit()

f = open("popular-names.txt","r")
list = f.readlines()

#分割用のファイル作成とファイル変数の動的作成
#split_n.txtというファイルがn個作成される
for i in range(int(n)):
    file_name = 'split_' + str(i) + '.txt'
    file_list.append(file_name)

for i in file_list:
    file_var = open(i, 'w')
    for j in list[n_cnt:n_cnt+(2780//int(n))]:
        file_var.write(j)
        cnt += 1
        if cnt == 2780 / int(n):
            n_cnt += 2780 // int(n)
            break

f.close()




