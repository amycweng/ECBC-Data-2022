import pandas as pd
import re
import os 
import gensim
import gensim.corpora as corpora
from stopwords import remove_stopwords


def model(bodyText):
    data = remove_stopwords(bodyText)
    
    id2word = corpora.Dictionary(data)
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in data]
    num_topics = 1
    lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                        id2word=id2word,
                                        num_topics=num_topics)
    for idx, topic in lda_model.show_topics(formatted=False):
        return ('{}'.format(' '.join([w[0] for w in topic])))

if __name__ == '__main__':
    folder = input('Enter input folder path: ')
    for file in os.listdir(folder):
        path = os.path.join(folder,file)
        f = open(path,'r')
        text = f.readlines()
        print(file)
        print(model(text))
        f.close()