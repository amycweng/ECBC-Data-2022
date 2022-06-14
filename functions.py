from gensim.utils import simple_preprocess
import os,re
import pandas as pd
from collections import Counter

# import nltk
# nltk.download('stopwords')
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

def keywords(csv,groups):
    df = pd.read_csv(csv)
    keywords = df['keywords']
    ids = df['id']
    numFiles = len(ids)
    count = 0
    dict = {}
    while count < numFiles:
        words = set(keywords[count].split('--'))
        # removing unnecessary keywords
        words.discard(' Early works to 1800.')
        words.discard('')
        # Removing unnecessary dates  
        newWords = []
        for w in words: 
            w = w.replace('.','')
            w = re.sub(r'\([^)]*\)','',w)
            w = re.sub(r' ca|-|[0-9]{4}|,','',w)
            w = w.strip()
            newWords.append(w)
        newWords = set(newWords)
        newWords.discard('')
        newWords.discard('-')
        newWords.discard('17th century')
        newWords.discard('To')
        dict[ids[count]] = newWords
        count += 1
    for k,v in groups.items():
        print(f'Group {k}')
        keyterms = []
        for name in v: 
            keyterms.extend(dict[name])
        print(Counter(keyterms))

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

def remove_stopwords(data):
    stop_words.extend(['thus', 'thereof', 'thence', 'thee', 'therein', 
                    'wherein', 'whereby', 'whereas', 'also', 'us', 'upon', 
                    'would', 'within', 'indeed', 'become', 'viz', 'per', 'anno', 
                    'whilst', 'shall','may','unto','say','day','one','make',
                    'two','come','time','place'])
    
    return [[word for word in simple_preprocess(str(doc))
            if word not in stop_words] for doc in data]
