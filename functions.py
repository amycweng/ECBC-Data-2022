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

def keywords(csv):
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
    return dict 

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


def date(soup):
    '''
    Converts the contents of the SECOND date tag in each XML file. 
    Function keeps the contents unaltered if it is an estimated date range, but converts 
    all other dates into a single date (type = string). 
    For all other edge cases, the function returns "Date Unknown"
    '''
    dateStr = soup.find_all('date')[1].string
    # keep dateStr unaltered if it is a date range, e.g., [between XXXX and XXXX] or [between XXXX-XXXX]
    estimates = re.search('between',dateStr)
    if estimates != None:
        return dateStr
    # otherwise, convert dateStr to a single date 
    intDates = re.findall(r'\d{4}',dateStr)
    if len(intDates) != 0:
        for d in intDates:
            if int(d) in range(1470,1800):
                return d
    return 'Date Unknown'