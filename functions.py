import re
import pandas as pd

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