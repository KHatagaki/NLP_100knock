from gensim.models import KeyedVectors
from gensim.test.utils import common_texts

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)
vector = model['Spain'] - model['Madrid'] + model['Athens']
print(vector)
print(model.most_similar(vector,topn=10))