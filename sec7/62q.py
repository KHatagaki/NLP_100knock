from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from gensim.test.utils import common_texts

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)
print(model.most_similar('United_States',topn=10))