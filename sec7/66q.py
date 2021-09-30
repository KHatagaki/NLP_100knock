from gensim.models import KeyedVectors
import numpy as np
from scipy.stats import spearmanr

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)

list = []
with open('./combined.csv', 'r') as f:
    next(f)
    for line in f:
        line = [s.strip() for s in line.split(',')]
        line.append(model.similarity(line[0],line[1]))
        list.append(line)

human = np.array(list).T[2]
w2v = np.array(list).T[3]
correlation, pvalue = spearmanr(human, w2v)

print(f'スピアマン相関係数: {correlation:.3f}')
