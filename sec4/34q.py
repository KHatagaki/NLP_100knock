fname = './neko.txt.mecab'

sentences = []
morphs = []
with open(fname, "r") as f:
    for line in f:
        if line != 'EOS\n':
            fields = line.split('\t')
            if len(fields) != 2 or fields[0] == '':
                continue
            else:
                attr = fields[1].split(',')
                morph = {'surface': fields[0], 'base': attr[6], 'pos': attr[0], 'pos1': attr[1]}
                morphs.append(morph)
        else:
            sentences.append(morphs)
            morphs = []

ans = set()
for sentence in sentences:
  nouns = ''
  num = 0
  for morph in sentence:
    if morph['pos'] == '名詞':
      nouns = ''.join([nouns, morph['surface']])
      num += 1
    elif num >= 2:
      ans.add(nouns)
      nouns = ''
      num = 0
    else:
      nouns = ''
      num = 0
  if num >= 2: 
    ans.add(nouns)

print(f'連接名詞の種類: {len(ans)}\n')
print('---サンプル---')
for n in list(ans)[:10]:
  print(n)