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

def getSpecials(filepath,output):
    output = open(output,'a+')
    file = open(filepath,'r')
    data = file.readlines()
    str = ''
    for line in data:
        str += line
    str = str.replace('\n','')
    list = str.split(' ')
    for word in list: 
        if '●' in word:
            output.write(word + '\n')
    output.close()
    file.close()

getSpecials('/srv/data/sample.txt','/srv/data/ECBC-Data-2022/Text_Files/special.txt')
if __name__ == '__main__':
    folder = input('Enter folder path: ')
    output = input('Enter output TXT file path: ')
    for file in os.listdir(folder):
        path = os.path.join(folder,file)
        getSpecials(path,output)
