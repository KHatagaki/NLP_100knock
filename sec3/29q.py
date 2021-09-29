import requests
import re
import json

def get_url(text):
    url_file = text['国旗画像'].replace(' ', '_')
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    return re.search(r'"url":"(.+?)"', data.text).group(1)

with open("jawiki-country.json") as f:
    for list in f:
        list = json.loads(list)
        if list['title'] == 'イギリス':
            text = list['text']
print(get_url(text))