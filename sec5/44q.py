import MeCab
import CaboCha
import pydot
from IPython.display import Image,display_png
from graphviz import Digraph

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

with open('./ans45.txt', 'w') as f:
  for sentence in sentence:
    for chunk in sentence.chunks:
      for morph in chunk.morphs:
        if morph.pos == '動詞':
          cases = []
          for src in chunk.srcs:
            cases = cases + [morph.surface for morph in sentence.chunks[src].morphs if morph.pos == '助詞']
          if len(cases) > 0:
            cases = sorted(list(set(cases)))
            line = '{}\t{}'.format(morph.base, ' '.join(cases))
            print(line, file=f)
          break