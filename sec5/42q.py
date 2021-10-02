import MeCab
import CaboCha

class Morph:
    def __init__(self,x):
        surface, info = x.split('\t')
        info = info.split(',')
        self.surface = surface
        self.base = info[6]
        self.pos = info[0]
        self.pos1 = info[1]

class Chunk:
    def __init__(self,morphs,dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

class Sentence():
    def __init__(self,chunks):
        self.chunks = chunks
        for i, chunk in enumerate(self.chunks):
            if chunk.dst != -1:
                self.chunks[chunk.dst].srcs.append(i)

fname = './ai.ja.txt.parsed'
sentence = []
chunks = []
morphs = []
with open(fname, mode='r') as f:
    for line in f:
        #print(line)
        if line[0] == '*':
            if len(morphs) > 0:
                chunks.append(Chunk(morphs, dst))
                morphs = []
            dst = int(line.split(' ')[2].rstrip('D'))
        elif line != 'EOS\n':
            morphs.append(Morph(line))
        else:
            chunks.append(Chunk(morphs, dst))
            sentence.append(Sentence(chunks))
            morphs = []
            chunks = []

sentence = sentence[2]
for chunk in sentence.chunks:
  if int(chunk.dst) != -1:
    modifier = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
    modifier_pos = [morph.pos for morph in chunk.morphs]
    modifiee = ''.join([morph.surface if morph.pos != '記号' else '' for morph in sentence.chunks[int(chunk.dst)].morphs])
    modifiee_pos = [morph.pos for morph in sentence.chunks[int(chunk.dst)].morphs]
    if '名詞' in modifier_pos and '動詞' in modifiee_pos:
      print(modifier, modifiee, sep='\t')