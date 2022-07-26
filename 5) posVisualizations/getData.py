import os
import ast
import pandas as pd

def input(dir):
    allTimePeriods = []
    for folder in os.listdir(dir):
        texts = []
        if folder[0] != '.':
            for file in folder:
                if file[0] != '.':
                    path = os.path.join(folder,file)
                    f = open(path,'r')
                    data = f.read()
                    textList = ast.literal_eval(data)
                    texts.append(textList)
            allTimePeriods.append(texts)
    return allTimePeriods

def getSurWords(pos, timePeriod):
    surroundingWords = []
    for text in timePeriod:
        for idx, word in enumerate(text):
            if word[0] in ['tobacco','tobaco','tobacca','tobacconist']:
                if idx >5 or idx < len(text)-5:
                    
                    surroundingWords.append(text[idx-3][0]) if text[idx-5][1] == pos else None
                    surroundingWords.append(text[idx-3][0]) if text[idx-5][1] == pos else None
                    
                    surroundingWords.append(text[idx-3][0]) if text[idx-3][1] == pos else None
                    surroundingWords.append(text[idx-2][0]) if text[idx-2][1] == pos else None
                    surroundingWords.append(text[idx-1][0]) if text[idx-1][1] == pos else None

                    surroundingWords.append(text[idx+1][0]) if text[idx+1][1] == pos else None
                    surroundingWords.append(text[idx+2][0]) if text[idx+2][1] == pos else None
                    surroundingWords.append(text[idx+3][0]) if text[idx+3][1] == pos else None
                    
                    surroundingWords.append(text[idx-3][0]) if text[idx+4][1] == pos else None
                    surroundingWords.append(text[idx-3][0]) if text[idx+5][1] == pos else None
                

    return surroundingWords

def getTopTenMain(pos):
    dir = '/Users/rossrichesin/dataplus/output'
    allTimePeriods = input(dir)
    dates = [date1,date2,date3,date4,date5]
    date1=[],date2=[],date3=[],date4=[],date5=[]
    for datePeriod, timePeriod in zip(dates,allTimePeriods):
        surroundingWords = getSurWords(pos, timePeriod)
        ser = pd.Series(surroundingWords)
        topTen = list(ser.value_counts().index[:10])
        datePeriod.append(topTen)
    return date1, date2, date3, date4, date5