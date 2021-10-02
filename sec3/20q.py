import json

with open("jawiki-country.json") as f:
    for list in f:
        list = json.loads(list)
        if list['title'] == 'イギリス':
            print(list['text'])
