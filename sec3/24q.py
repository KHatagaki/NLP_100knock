import json
import re

with open("jawiki-country.json") as f:
    for list in f:
        list = json.loads(list)
        if list['title'] == 'イギリス':
            text = list['text']

match_text = '\[\[ファイル:(.*?)(?:\|.*)'
result = '\n'.join(re.findall(match_text, text, re.MULTILINE))
print(result)
#print(re.findall(match_text, text, re.MULTILINE))