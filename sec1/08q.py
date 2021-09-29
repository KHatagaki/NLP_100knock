def cipher(x):
    for i in x:
        if i.islower():
            x = x.replace(i,chr(219 - ord(i)))
    return x

string = 'My name is Koki Hatagaki.'
print(cipher(string))
print(cipher(cipher(string)))

