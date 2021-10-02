import MeCab
import CaboCha
mecab = MeCab.Tagger("-Ochasen")
c = CaboCha.Parser()
s = "鉛筆を使ってキャンパスに絵を描く"
tree = c.parse(s)
#print(tree.toString(CaboCha.FORMAT_TREE))

class Morph:
    def __init__(self,x):
        surface, info = x.split('\t')
        info = info.split(',')
        self.surface = surface
        self.base = info[6]
        self.pos = info[0]
        self.pos1 = info[1]

fname = './ai.ja.txt.parsed'
sentence = []
morphs = []
with open(fname, mode='r') as f:
    for line in f:
        #print(line)
        if line[0] == '*':
            continue
        elif line != 'EOS\n':
            morphs.append(Morph(line))
        else:
            sentence.append(morphs)
            morphs = []

for m in sentence[2]:
    print(vars(m))
