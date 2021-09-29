import re

str = 'Now I need a drink, alcoholic of cource, after the heavy lectures involving quantum mechanics.'
str = re.sub('[,.]', '', str)
token = str.split()
ans = [len(i) for i in token]

print(ans)