import os,re
import pandas as pd

# import nltk
# nltk.download('stopwords')

from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

def remove_stopwords(data):
    stopwords.extend(['neve', 'printed', 'earlier', 'may', 'placed', 'unto', 'whereof', 
                'began', 'inasmuch', 'shall', 'de', 'we', 'sir', 'later', 'until', 
                'could', 'two', 'years', 'mr', 'long', 'till', 'thereof', 'indeed', 
                'ie', 'himself', 'neither', 'doth', 'thence', 'seem', 'part', 'old', 
                'definite', 'would', 'iq', 'aforesaid', 'ever', 'might', 'upon', 'how', 
                'therein', 'through', 'done', 'begin', 'little', 'last', 'certain', 
                'also', 'ew', 'etc', 'full', 'second', 'though', 'place', 'more', 'his', 
                'must', 'whereas', 'thy', 'thee', 'themselves', 'he', 'why', 'seldom', 
                'hear', 'what', 'think', 'matter', 'time', 'et cetera', 'present', 'great', 
                'do', 'before', 'made', 'there', 'thereforeunto', 'when', 'whilst', 'herself', 
                'definitely', 'her', 'arrived', 'per', 'afterward', 'far', 'dr', 'saying', 
                'char', 'whereby', 'or', 'third', 'seems', 'mentioned', 'go', 'esq', 'year', 
                'likewise','must', 'know', 'arrive', 'pag', 'conerning', 'earliest', 'ditto', 
                'hath', 'without', 'self', 'lib', 'three', 'and', 'itself', 'suchtwo', 'otherwise', 
                'seeing', 'him', 'latest', 'often', 'cannot', 'et', 'thou', 'est', 'it', 
                'which', 'can', 'most', 'early', 'let', 'almost', 'say', 'places', 'late', 
                'hereby', 'every', 'wherein', 'always', 'either', 'much', 'come', 'said', 
                'day', 'else', 'near', 'cap', 'likewise', 'esq.', 'viz', 'heard', 'fol', 
                'like', 'within', 'become', 'have', 'thus', 'first', 'certainly', 'one', 
                'make', 'rather', 'she', 'eg', 'where', 'ne', 'since', 'four', 'fourth', 
                'includes', 'even', 'us', 'gone', 'five', 'anno', 'went','thing'])

    return [[word for word in simple_preprocess(str(doc))
            if word not in stop_words] for doc in data]
    
def getTexts(folder):
    '''
    Takes in plain text files and outputs a tuple of lists, with the first being the text
    within each file as a string and the second list being the IDs of each text. 
    '''
    textStrings = []
    fileNames = []
    for file in os.listdir(folder):
        path = os.path.join(folder,file)
        f = open(path,'r')
        text = f.readlines()[0]
        textStrings.append(text)
        name = file.split('.')[0]
        fileNames.append(name)
        f.close()
    return textStrings,fileNames

def keywords(csv):
    '''
    Returns a dictionary in this format {id : (keywords,date)}
    '''
    df = pd.read_csv(csv)
    keywords = df['keywords']
    ids = df['id']
    dates = df['date']
    numFiles = len(ids)
    count = 0
    dict = {}
    while count < numFiles:
        words = set(keywords[count].split('--'))
        # removing unnecessary keywords
        words.discard('')
        # Removing unnecessary dates  
        newWords = []
        for w in words: 
            w = w.replace('.','')
            w = re.sub(r'\([^)]*\)','',w)
            w = re.sub(r' ca|-|[0-9]{4}|,','',w)
            if re.search('Sultan of the Turks',w):
                w = 'Sultan of the Turks'
            if re.search('Süleyman',w):
                w = 'Süleyman'
            w = w.strip()
            newWords.append(w)
        newWords = set(newWords)
        newWords.discard('')
        newWords.discard('-')
        newWords.discard('17th century')
        newWords.discard('Early works to')
        newWords.discard('To')
        newWords.discard('No Keywords')
        newWords.discard('Great Britain')
        dict[ids[count]] = (newWords,dates[count])
        count += 1
    return dict 

def date(soup):