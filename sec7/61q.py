from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from gensim.test.utils import common_texts

#model = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)
#model.save("word2vec.model")

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)
print(model.similarity('United_States','U.S.'))