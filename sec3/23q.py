import json
import re

with open("jawiki-country.json") as f:
    for list in f:
        list = json.loads(list)
        if list['title'] == 'イギリス':
            text = list['text']

match_text = '^(\={2,})\s*(.*?)\s*(\={2,})'
result = '\n'.join(i[1] +  ':' + str(len(i[0])-1) for i in re.findall(match_text, text, re.MULTILINE))
print(result)
#print(re.findall(match_text, text, re.MULTILINE))