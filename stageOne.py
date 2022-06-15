import pandas as pd 
from bs4 import BeautifulSoup
import re 
import os
import csv
from characterCleaner import simple_clean

'''
STAGE I FUNCTIONS 
'''

def text(soup):
    '''
    Gets the body of the text file into string format.
    -----------------------------------
    Does not grab any text in the tag <front> which contains div tags such as ['title_page', 'dedication',
    'to_the_reader', 'list'...] that are not part of the main text. 

    Does not grab any text in the tag <back> which contains div tags such as ['errata', 'index', 
    'supplied_by_editor', ...] that are not part of the main text. 

    Does not grab any text under the <table> tag
    '''
    text_list = []
    for sibling in soup.find_all('w'):
        parent_name = [parent.name for parent in sibling.parents]
        parent_attrs = [parent.attrs for parent in sibling.parents]
        div = [ats['type'] for ats in parent_attrs if 'type' in ats.keys() and ats['type'] == 'coat_of_arms']
        if not any(x in parent_name for x in ['front', 'table', 'back']) and 'coat_of_arms' not in div and re.search('lemma',str(sibling)) and str(sibling['lemma']) != 'n/a':
            text_list.append(sibling['lemma'])
    return ' '.join(text_list)


def dedicationEP(soup):
    text_list = []
    for sibling in soup.find_all('w'):
        parent_attrs = [parent.attrs for parent in sibling.parents]
        parent_title = [ats['type'] for ats in parent_attrs if 'type' in ats.keys() and ats['type'] == 'dedication']
        if 'dedication' in parent_title and re.search('lemma',str(sibling)) and str(sibling['lemma']) != 'n/a':
            text_list.append(sibling['lemma'])
    return ' '.join(text_list)


def idno_test(soup):
    idnums_u = soup.find_all('idno', attrs={'type': 'STC'})
    idnums_l = soup.find_all('idno', attrs={'type': 'stc'})
    s = "None"
    e = "None"

    if len(idnums_u) != 0:
        for id in idnums_u:
            idstr = id.string
            i = idstr.split(' ')
            if i[0] == "STC" or i[0] == "Wing":
                s = i[-1]
            if i[0] == "ESTC":
                e = i[-1]
    if len(idnums_l) != 0:
        for id in idnums_l:
            idstr = id.string
            i = idstr.split(' ')
            if i[0] == "STC" or i[0] == "Wing":
                s = i[-1]
            if i[0] == "ESTC":
                e = i[-1]

    return (s,e)


def idno(soup):
    idnums_u = soup.find_all('idno', attrs={'type': 'STC'})
    idnums_l = soup.find_all('idno', attrs={'type': 'stc'})
    if len(idnums_u) == 3:
        stc = idnums_u[0].string
        s = stc.split(' ')
        estc = idnums_u[-1].string
        e = estc.split(' ')
        return (s[-1],e[-1])
    elif len(idnums_l) == 3:
        stc = idnums_l[0].string
        s = stc.split(' ')
        estc = idnums_l[-1].string
        e = estc.split(' ')
        return (s[-1],e[-1])
    elif len(idnums_u) == 2:
        stc = idnums_u[0].string
        s = stc.split(' ')
        estc = idnums_u[1].string
        e = estc.split(' ')
        return (s[-1],e[-1])
    elif len(idnums_l) == 2:
        stc = idnums_l[0].string
        s = stc.split(' ')
        estc = idnums_l[1].string
        e = estc.split(' ')
        return (s[-1],e[-1])
    elif len(idnums_u) == 1 and len(idnums_l) == 0:
        id = idnums_u[0].string
        i = id.split(' ')
        if i[0] == "STC":
            return(i[-1],  "None")
        else:
            return("None", i[-1])
    elif len(idnums_u) == 0 and len(idnums_l) == 1:
        id = idnums_l[0].string
        i = id.split(' ')
        if i[0] == "STC":
            return(i[-1],  "None")
        else:
            return("None", i[-1])
    elif len(idnums_u) == 1 and len(idnums_l) == 1:
        id_u = idnums_u[0].string
        i_u = id_u.split(' ')
        id_l = idnums_l[0].string
        i_l = id_l.split(' ')
        if i_u[0] == "STC":
            return(i_u[-1], i_l[-1])
        else:
            return(i_l[-1], i_u[-1])
    else:
        return("None", "None")

def convertEP(folder,file,dates, textfolder):
    '''
    Master function for converting each XML file into a dataframe 
    '''
    fileName = os.path.join(folder,file)
    name = file.split('.')[0]
    data = open(fileName,'r')
    data = data.read()
    soup = BeautifulSoup(data,'html.parser')
    #call text function to output the body text as a plain text file 
    with open(os.path.join(textfolder, name + '.txt'), 'a+') as file:
        toFile = text(soup)
        file.write(toFile) 

    # Parse the metadata that we need for each dataframe 
    title = soup.find_all('ep:title')[0].string
    a,k = authors(soup),keywords(soup)
    publisher = soup.find_all('publisher')[1].string
    pubplaceStr = soup.find_all('pubplace')[1].string
    pp = pubplace(pubplaceStr)
    idInfo = idno_test(soup)
    d = dates[name]
    ded = dedicationEP(soup)

    # Input all of the relevant column info into a dictionary to be returned as a dataframe 
    dict = {'id':str(name),'stc':str(idInfo[0]),'estc':str(idInfo[1]),
            'title':str(title),'author':str(a),
            'publisher':str(publisher),'pubplace':str(pp), 'keywords':str(k),
            'date':str(d),'dedication':str(ded)}
    return dict
    
def dedicationTCP(soup):
    dedication = soup.find_all('div1', attrs={'type': 'dedication'})
    dedExists = False
    fullDed = []
    if len(dedication) != 0:
        for ded in dedication: 
            d = ded.get_text()
            d = d.split('\n')
            while d.count(''):
                d.remove('')
            d = ' '.join(d)
            fullDed.append(d)
        dedExists = True
    if dedExists == True:
        return ' '.join(fullDed)
    return 'None' 
    
def textTCP(soup):
    '''
    Gets the body of the text file into string format without newline characters. 
    '''
    text = soup.body.get_text()
    text = text.split('\n')
    while text.count(''):
        text.remove('')
    text = ' '.join(text)
    return text

def convertTCP(folder,file,dates):
    '''
    Master function for converting each XML file into a dataframe 
    '''
    fileName = os.path.join(folder,file)
    name = file.split('.')[0]
    data = simple_clean(fileName)
    soup = BeautifulSoup(data,'html.parser')
    
    # Parse all the information that we need for each dataframe 
    title = soup.title.string 
    a,t,k = authors(soup),textTCP(soup),keywords(soup)
    publisher = soup.find_all('publisher')[1].string
    pubplaceStr = soup.find_all('pubplace')[1].string
    pp = pubplace(pubplaceStr)
    idInfo = idno(soup)
    d = dates[name]
    ded = dedicationTCP(soup)
    # Input all of the relevant column info into a dictionary to be returned as a dataframe 
    dict = {'id':name,'stc':idInfo[0],'estc':idInfo[1],
            'title':title,'author':a,
            'publisher':publisher,'pubplace':pp, 'keywords':k,
            'date':d,'dedication':ded,'text':t}
    return pd.DataFrame(data=dict,index=[0])

if __name__ == '__main__':
    '''
    Initializes and writes metadata to a new CSV file. 
    '''
    folder = input('Enter folder path: ')
    newCSV = input ('Enter the desired path of your metadata CSV file, including the name of the new CSV: ')
    textfolder = input('Enter the folder path for your output text files: ')
    version = input('Enter the type of file you want to convert (either TCP or EP). TCP refers to the original TCP XML files. EP refers to the processed Early Print XML files. Type here: ')
    
    count = 0
    dates = dateTXT()
    outfile = open(newCSV,'a+')
    columns = ['id', 'stc', 'estc','title','author','publisher','pubplace','keywords','date','dedication']
    writer = csv.DictWriter(outfile, fieldnames=columns)
    writer.writeheader()
    for file in os.listdir(folder):
        count += 1
        # if count % 100 == 0 and count != 0:
        print("Processed " + str(count) + " files so far")
        if version == 'EP':
            df = convertEP(folder,file,dates,textfolder)
        if version == 'TCP':
            df = convertTCP(folder,file,dates,textfolder)

        writer.writerow(df)
    print('The number of total files is ' + str(count))
