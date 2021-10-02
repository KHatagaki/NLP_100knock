def ngram(str, int):
    ans = []
    for i in range(len(str)-int+1):
        ans.append(str[i:i+int])
    return list(ans)

def sum(X, Y):
    Z = X | Y
    return Z

def mul(X, Y):
    Z = X & Y
    return Z

def min(X, Y):
    Z = X - Y
    return Z

str = 'paraparaparadise'
str2 = 'paragraph'

X = set(ngram(str,2))
Y = set(ngram(str2,2))

print(sum(X,Y))
print(mul(X, Y))
print(min(X, Y))

if X & {'se'}:
    print('X include se')
else:
    print('X not include se')
if Y & {'se'}:
    print('Y include se')
else:
    print('Y not include se')
