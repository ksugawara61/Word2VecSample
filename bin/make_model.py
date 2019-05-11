from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('./sentence/sample-userdic-wakati.txt')

model = word2vec.Word2Vec(sentences, size=200, min_count=1, window=15)
model.save("./model/app.model")