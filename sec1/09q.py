import random

def change(dest_small,dest_big,str_a):
    str_a = list(str_a)
    tmp = str_a[dest_small]
    str_a[dest_small] = str_a[dest_big]
    str_a[dest_big] = tmp
    return "".join(str_a)

message = 'I couldn\'t believe that I could actually understand what I was reading' \
    ' : the phenomenal power of the human mind .'

message = message.split()
to_message = []

for i in message:
    if len(i) >= 5:
        for cnt in range(100):
            x = random.randint(1,len(i)-2)
            y = random.randint(1,len(i)-2)
            change(x,y,i)
        to_message.append(change(x,y,i))
    else:
        to_message.append(i)
print(" ".join(to_message))