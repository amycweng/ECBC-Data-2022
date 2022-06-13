import pandas as pd 
import re 
import shutil
import os
import numpy as np

'''
STAGE II FUNCTIONS 
'''
def avgDate(df):
    df['date'] = df['date'].apply(lambda x: round(np.mean([int(y) for y in re.findall(r'\d{4}', x)])) if type(x)==str and re.search('[0-9]+',x) != None else x)


