import re

def ngram(str, int):
    ans = []
    #str = str.split()
    for i in range(len(str)-int+1):
        ans.append(str[i:i+int])
    return list(ans)

str = 'I am an NLPer'
int = 2
str = re.sub('[,.]','',str)
print(ngram(str,int))
print(ngram(str.split(),int))