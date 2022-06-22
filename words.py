import os,re,time
from collections import Counter
from tkinter import N 
from bs4 import BeautifulSoup, SoupStrainer 

def legomena(string,output,file):
    outfile = open(output,'a+')
    list = []
    text = string.split(' ')
    words = dict(Counter(text))
    for w,freq in words.items():
        if len(w) <= 2: continue
        if freq == 1 or freq == 2: 
            list.append(w)
    outfile.write(file + ': ' + str(list)+ '\n') 

def special(string):
    specials = []
    text = string.split(' ')
    for t in text: 
        if '●' in t: 
            specials.append(t)
    return specials

option = input('Enter legomena or special or nouns: ')
start = time.time()


if option != 'nouns': 
    folder = input('Enter input folder path: ')
    output = input('Enter output TXT file path: ')
    specials = []
    for file in os.listdir(folder):
        path = os.path.join(folder,file)
        f = open(path,'r')
        line = f.readlines()[0]
        f.close()
        if option == 'special': specials.extend(special(line))
        if option == 'legomena': legomena(line,output,file)

    if option == 'special':  
        outfile = open(output,'a+')
        outfile.write(str(dict(Counter(specials).most_common(n=5000))))
else: 
    epFolder = input('Enter EP folder: ')
    output = input('Enter output TXT file path: ')
    outfile = open(output,'w+')
    nouns = ['nn1','nn2','n1','n2','ng1','ng2']
    for file in os.listdir(epFolder):
        fileName = os.path.join(epFolder,file)
        print(file)
        f = open(fileName,'r')
        data = f.read()
        f.close()
        tags = SoupStrainer('w')
        soup = BeautifulSoup(data,parse_only=tags,features='html.parser')
        text = ''
        nounList = []
        # this part of code is adapted from text.py text(soup) function
        for sibling in soup.find_all('w'):
            parent_name = [parent.name for parent in sibling.parents]
            parent_attrs = [parent.attrs for parent in sibling.parents]
            divType = [ats['type'] for ats in parent_attrs if 'type' in ats.keys() and ats['type'] == 'coat_of_arms']
            divLat = [ats['xml:lang'] for ats in parent_attrs if 'xml:lang' in ats.keys() and ats['xml:lang'] == 'lat']
            if not any(x in parent_name for x in ['front', 'table', 'back','foreign']) and 'coat_of_arms' not in divType and 'lat' not in divLat:
                if re.search('pos',str(sibling)) and str(sibling['pos']) != 'n/a':
                    if sibling['pos'] in nouns: 
                        nounList.append(sibling['lemma'].lower())
        nounCounts = dict(Counter(nounList))
        outfile.write(file + ': ' + str(nounCounts) + '\n')

end = time.time()
print("The time of execution is :", end-start, ' seconds')

