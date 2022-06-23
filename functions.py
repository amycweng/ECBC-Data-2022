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

from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

def remove_stopwords(data):
    stop_words.extend(['thus', 'thereof', 'thence', 'thee', 'therein', 
                    'wherein', 'whereby', 'whereas', 'also', 'us', 'upon', 
                    'would', 'within', 'indeed', 'become', 'viz', 'per', 'anno', 
                    'whilst', 'shall','may','unto','say','day','one','make',
                    'two','come','time','place','whereof','thou','thy', 
                    'afterward','rather','etc','eg', 'ie', 'either', 'else',
                    'ever','even','ew','often','seldom','ever','even','likewise'
                    'must','without', 'thus', 'thereof', 'thence', 'thee', 'therein', 
                    'wherein', 'whereby', 'whereas', 'whereof','also', 'us', 'upon', 
                    'would', 'within', 'indeed', 'become', 'viz', 'per', 'anno', 
                    'whilst', 'shall','may','unto','say','day','one','make','such'
                    'two','come','time','place','said','hath','made','much','mr',
                    'sir','how','like','full','three','four','five','say','thou','thy',
                    'done','do','have','know','heard','hear','saying','think','rather',
                    'either','neither','or','and','till','until','might','could','begin',
                    'began','went','last','matter','seeing','go','gone','little','without',
                    'long','aforesaid','old','can','afterward','before','therefore'
                    'unto','part','through','let','neve','ne','de','est','et','though',
                    'printed','doth','iq','esq','esq.','first','second','third','fourth',
                    'dr','ditto','self','almost','conerning','near','far','since','always',
                    'otherwise','hereby','inasmuch','includes','char','seems','seem','cannot',
                    'themselves','himself','herself','itself','it','likewise','mentioned',
                    'he','we','she','her','his','him','her','fol','pag','lib','cap','must',
                    'th●','●he','●nd','a●d','an●','wi●h','●or','th●y','t●e','the●',
                    'th●m','ou●','no●','tha●','w●re','th●se','●ound','th●n','●hat',
                    'etc','et cetera','b●ing','s●me','si●e','great','present','late','later','early',
                    'earlier','earliest','latest','th●t','se●','●ll','bu●','●ut','w●ll','th●ir',
                    'which','what','why','where','when','there','wh●ch','hi●','●ee','th●re',
                    'al●o', '●ame','●rom','w●th','l●ke','w●ich','●ight','l●st','●et','●re',
                    'le●t','thei●','me●','whi●h','fi●e','●ad', 'above','about',
                    'he●', '●is','c●me','●●e','fo●','af●er', 'ha●', 'abou●', 'fi●st','w●nt',
                    'grea●', 'the●e', 'wa●', '●hey', '●ot', '●ow', '●ome', '●and', 'th●●', 'o●her', 
                    'h●m', 'h●s', 'call●d', '●hen', 'thi●', '●ave', 'wer●', '●it', 'ha●e', 
                    'ye●','w●s','a●l','ha●h','fa●re','no●e','●ay', 'som●', 't●●', 'ar●', 'o●●', 
                    'h●ue', 'we●e', '●●●', 'f●om','s●nd','do●','we●', 'n●w', '●ooke', 'f●r', 'al●', 
                    'ther●', 'th●s', '●heir', 'the●r', 'h●d', 'fro●', 'of●', 's●●', '●an', 'thre●', 
                    'a●ter', 'a●●', '●ur', 'da●es', 'lo●', 'sa●e', '●ent', 'hal●e', 'ma●●', 'a●e', '●ell', 
                    'wo●ld', 'them●', '●ther','s●t', '●here', '●ort', 'wit●', '●ere', 'fr●m', 
                    'c●lled', 'ma●', 'h●re', 'p●rt', 'co●', 'ma●e', 's●nt', 'o●e', '●ide', '●at', 'h●e','ne●t', 
                    'every','place','places','placed','sen●', 'se●ne', 's●ore', 'h●r', 'o●r', '●old', 
                    'ou●r', 'tho●e', 'sou●h', '●me', '●all', 'ba●ke', '●om', '●nto', 'eu●ry', 'thr●e', 'go●', '●hich', 
                    '●ith', 'u●ry', '●ath', '●eare', 'bo●h', 'l●ft', 'hau●', '●e●', 'oth●rs', 'place●', 
                    '●ill', 't●ey', '●oure', 'thos●', 'la●', '●ew', '●uery', 'se●t', 'whi●e', 'm●●', 
                    'sa●d', 'co●e', 'b●t', 'm●y', '●ne', '●ire', 'on●','c●rtaine','certainly','certain',
                    '●en', 'gr●at', '●ake', '●ing','●ither', '●eere', '●hose', 'kn●w', 'aft●r', 
                    'definite','definitely','years','year','arrive','arrived','most','more'])
    set(stop_words)
    return [[word for word in simple_preprocess(str(doc))
            if word not in stop_words] for doc in data]

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