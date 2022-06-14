import pandas as pd 
from bs4 import BeautifulSoup
import re 
import os
import csv
from characterCleaner import simple_clean

'''
STAGE I FUNCTIONS 
'''

def authors(soup):
    '''
    Returns a string of all mentioned authors separated by semi-colons
    ''' 
    authors = soup.find_all('author')
    auth = ''
    for a in authors:
        if auth != '':
            if not re.search(a.get_text(),auth):
                auth = auth + '; ' + a.get_text()
        else: 
            auth += a.get_text()
    if auth == '':
        auth = 'Anonymous'
    return auth

def pubplace(str):
    pubplace = re.findall('\w+',str)
    count = 0
    for p in pubplace:
        if count == 0:
            count += 1
            cleanPlace = p 
        else: 
            cleanPlace = cleanPlace + ' ' + p
    return cleanPlace

def keywords(soup):
    '''
    Returns the keywords separated by semicolons 
    '''
    keywords = soup.find_all('keywords')
    if len(keywords) != 0:
        keywords = soup.find_all('keywords')[0].get_text()
        keywords = keywords.replace('\n','--')
        return keywords
    return 'No Keywords'

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

def dateTXT():
    '''
    Extracts the integer date or date range from the corresponding entry in TCP's official 
    documentation of all the EEBO IDs and dates. Returns a dictionary with the data from 
    both Phase I and II.  

    This function should only be called once. Afterwards, the user can directly refer to the 
    returned dictionary to find dates. 
    '''
    f1 = '/srv/data/eebo_phase1_IDs_and_dates.txt'
    f2 = '/srv/data/EEBO_Phase2_IDs_and_dates.txt' 
    names = {}
    data1 = open(f1,'r')
    data2 = open(f2,'r')
    data1 = data1.readlines()
    data2 = data2.readlines()
    data = data1 
    data.extend(data2)
    for d in data:
        datum = d.replace('\n','')
        datum = d.split('\t')
        id = datum[0]
        date = datum[1].replace('\n','')
        names[id] = date
    return names


def text(soup):
    '''
    Gets the body of the text file into string format.
    -----------------------------------
    Gets dedication but not title page 
    '''
    #text_list = []
    #for sibling in soup.find_all('w'):
    #    parent_attrs = [parent.attrs for parent in sibling.parents]
    #    parent_title = [ats['type'] for ats in parent_attrs if 'type' in ats.keys() and ats['type'] == 'title_page']
    #    if 'title_page' not in parent_title and re.search('lemma',str(sibling)) and str(sibling['lemma']) != 'n/a':
    #        text_list.append(sibling['lemma'])
    #return ' '.join(text_list)
    

    '''
    Does not get dedication or titlepage
    '''
    return ' '.join([sibling['lemma'] for sibling in soup.find_all('w') if 'front' not in [parent.name for parent in sibling.parents] and re.search('lemma',str(sibling)) and str(sibling['lemma']) != 'n/a' ])

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
            if i[0] == "STC":
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
