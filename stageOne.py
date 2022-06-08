import pandas as pd 
from bs4 import BeautifulSoup
import re 
import os
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

def keywords(soup):
    '''
    Returns the keywords separated by semicolons 
    '''
    keywords = soup.find_all('keywords')
    if len(keywords) != 0:
        keywords = soup.find_all('keywords')[0].get_text()
        keywords = keywords.replace('\n',' ')
        keywords = keywords.replace('--','')
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
    Gets the body of the text file into string format but still gets title page etc. 
    '''
    return ' '.join([sibling['lemma'] for sibling in soup.find_all('w') if re.search('lemma',str(sibling)) and str(sibling['lemma']) != 'n/a' ])
    
def idno(soup):
    idnums = soup.find_all('idno', attrs={'type': 'STC'})
    if len(idnums) == 2:
        stc = idnums[0].string
        s = stc.split(' ')
        estc = idnums[1].string
        e = estc.split(' ')
        return (s[1],e[1])
    elif len(idnums) == 1:
        id = idnums[0].string
        i = id.split(' ')
        if i[0] == "STC":
            return(i[1],  "None")
        else:
            return("None", i[1])
    else:
        return("None", "None")

def convert(folder,file,dates):
    '''
    Master function for converting each XML file into a dataframe 
    '''
    fileName = os.path.join(folder,file)
    name = file.split('.')[0]
    data = simple_clean(fileName)
    soup = BeautifulSoup(data,'html.parser')
    
    # Parse all the information that we need for each dataframe 
    title = soup.find_all('ep:title')[0].string
    a,t,k = authors(soup),text(soup),keywords(soup)
    publisher = soup.find_all('publisher')[1].string
    pubplace = soup.find_all('pubplace')[1].string
    pubplace = re.findall('\w+',pubplace)[0]
    idInfo = idno(soup)
    d = dates[name]

    # Input all of the relevant column info into a dictionary to be returned as a dataframe 
    dict = {'id':name,'stc':idInfo[0],'estc':idInfo[1],
            'title':title,'author':a,
            'publisher':publisher,'pubplace':pubplace, 'keywords':k,
            'date':d,'text':t}
    return pd.DataFrame(data=dict,index=[0])
    
if __name__ == '__main__':
    folder = input('Enter folder path: ')
    newCSV = input ('Enter the path of your output CSV file: ')
    count = 0
    dates = dateTXT()
    for file in os.listdir(folder):
        count += 1
        if count % 100 == 0 and count != 0:
            print("Processed " + str(count) + " files so far")
        if count == 1: 
            outFile = convert(folder,file,dates)
            continue
        df = convert(folder,file,dates)
        outFile = pd.concat([outFile,df],ignore_index = True)
    print('The number of total files is ' + str(count))
    outFile.to_csv(newCSV)
