import os,re,time
from collections import Counter
from bs4 import BeautifulSoup, SoupStrainer 

def legomena(strings,output):
    outfile = open(output,'a+')
    bigString = ' '.join(strings)
    list = []
    text = bigString.split(' ')
    words = dict(Counter(text))
    for w,freq in words.items():
        if len(w) <= 2: continue
        if freq == 1 or freq == 2: 
            list.append(w)
    outfile.write(str(list)) 

def special(strings):
    specials = []
    for string in strings: 
        text = string.split(' ')
        for t in text: 
            if '●' in t: 
                specials.append(t)
    return specials

def specialNouns(file):
    specials = []
    file = open(file,'r')
    data = file.readlines()
    file.close()
    for line in data: 
        line = line.split(':')
        for item in line: 
            if '●' in item: 
                specials.append(item)
    return specials

option = input('Enter legomena or special or nouns or specialNouns: ')
start = time.time()


if option != 'nouns': 
    output = input('Enter output TXT file path: ')
    if option == 'specialNouns': 
        file = input('Enter path of TXT file with noun info: ')
        data = specialNouns(file)
        outfile = open(output,'a+')
        outfile.write(str(data))
    
    strings = []
    folder = input('Enter input folder path: ')
    for file in os.listdir(folder):
        path = os.path.join(folder,file)
        f = open(path,'r')
        line = f.readlines()[0]
        strings.append(line)
        f.close()
    if option == 'legomena': legomena(strings,output)
    if option == 'special':  
        specials = special(strings)
        outfile = open(output,'a+')
        outfile.write(str(dict(Counter(specials).most_common(n=100000)).keys()))
else: 
    option2 = input('Enter fileNouns or allNouns: ')
    epFolder = input('Enter EP folder: ')
    output = input('Enter output TXT file path: ')
    outfile = open(output,'w+')
    nouns = ['nn1','nn2','n1','n2','ng1','ng2']
    allNouns = []
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
        if option2 == 'fileNouns':
            nounCounts = dict(Counter(nounList))
            outfile.write(file + ': ' + str(nounCounts) + '\n')
        elif option2 == 'allNouns':
            allNouns.extend(nounList)

if option2 == 'allNouns':
    outfile.write(str(dict(Counter(allNouns))))
end = time.time()
print("The time of execution is :", end-start, ' seconds')

