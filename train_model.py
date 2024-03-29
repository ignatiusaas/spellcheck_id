import time
import multiprocessing
from datetime import timedelta

from gensim.models import word2vec


if __name__ == '__main__':


    start_time = time.time()
    print('Training Word2Vec Model...')
    sentences = word2vec.LineSentence('wiki_id.txt')
    id_w2v = word2vec.Word2Vec(sentences, vector_size=200, workers=multiprocessing.cpu_count()-1)
    id_w2v.save('model/wiki_id_model.model')
    finish_time = time.time()

    print('Finished. Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))