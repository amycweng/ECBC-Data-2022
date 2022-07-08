import os,re
import pandas as pd
from gensim.utils import simple_preprocess

def remove_stopwords(data):
    '''
    Additional stopwords beyond the ones removed in stageTwo, especially for topic modeling
    '''
    stop_words = ['if','of','because','since','part','yet','whether',
                    'many','day','great','qua','out','man','time',
                    'first','one','two','second','well','see','call',
                    'against','never','john','word','place','therefore',
                    'way','still','new']

    return [[word for word in simple_preprocess(str(doc))
            if word not in stop_words] for doc in data]
    
def getTexts(folder):
    '''
    Takes in plain text files and outputs a tuple of lists, with the first being the text
    within each file as a string and the second list being the IDs of each text. 
    '''
    textStrings = []
    fileNames = []
    underscores = {}
    for root,dir,files in os.walk(folder):
        for file in files:
            if '.txt' not in file: continue
            path = os.path.join(folder,file)
            f = open(path,'r')
            text = f.readlines()[0]
            if '_' in file: 
                name = file.split('_')[0]
                if name not in underscores.keys(): 
                    underscores[name] = text
                    fileNames.append(name)
                else: underscores[name] = underscores[name] + ' ' + text
            else: 
                textStrings.append(text)
                name = file.split('.')[0]
                fileNames.append(name)
            f.close()
        for text in underscores.values():
            textStrings.append(text)
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
            w = re.sub(r'[."\'-?:!;]', '', w)
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
        newWords.discard('th century')
        newWords.discard('I')
        newWords.discard('Early works to')
        newWords.discard('To')
        newWords.discard('No Keywords')
        newWords.discard('Great Britain')
        dict[ids[count]] = (newWords,dates[count])
        count += 1
    return dict 