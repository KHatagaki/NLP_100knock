import re 
import json

with open("jawiki-country.json") as f:
     for list in f:
        list = json.loads(list)
        if list['title'] == 'イギリス':
            text = list['text']

search_text = '\{\{基礎情報.*?$(.*?)^\}\}'
search_result = re.findall(search_text, text, re.MULTILINE + re.DOTALL)
match_text = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
del_text = '\'{2,5}'
del_text_1 = r'\[\[(.*?)#?(.*?)\|?(.*?)\]\]'
del_text_2 = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
result = dict(re.findall(match_text, search_result[0], re.MULTILINE + re.DOTALL))
for i, j in result.items():
    i = re.sub(del_text,'',i)
    j = re.sub(del_text,'',j) 
    j = re.sub(del_text_1, r'\1',j)
    print(i + ': ' + j)