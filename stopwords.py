from gensim.utils import simple_preprocess
# import nltk
# nltk.download('stopwords')
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