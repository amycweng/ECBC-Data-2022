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

def text(soup):
    '''
    Gets the body of the text file into string format without newline characters. 
    '''
    text = soup.body.get_text()
    text = text.replace('\n',' ')
    
    # while text.count(''):
    #     text.remove('')
    # text = ' '.join(text)
    
    return text 
    

def idno(soup):
    idnums = soup.find_all('idno', attrs={'type': 'stc'})
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

def convert(folder,file):
    '''
    Master function for converting each XML file into a dataframe 
    '''
    fileName = os.path.join(folder,file)
    name = file.rpartition('.P4')[0]
    data = simple_clean(fileName)
    soup = BeautifulSoup(data,'html.parser')
    # Parse all the information that we need for each dataframe 
    title = soup.title.string
    a,d,t,k = authors(soup),date(soup),text(soup),keywords(soup)
    publisher = soup.find_all('publisher')[1].string
    pubplace = soup.find_all('pubplace')[1].string
    idInfo = idno(soup)
    dict = {'id':name,'stc':idInfo[0],'estc':idInfo[1],
            'title':title,'author':a,
            'publisher':publisher,'pubplace':pubplace, 'keywords':k,
            'date':d,'text':t}
    return pd.DataFrame(data=dict,index=[0])
    
if __name__ == '__main__':
    folder = input('Enter folder path: ')
    newCSV = input ('Enter the path of your output CSV file: ')
    count = 0
    for file in os.listdir(folder):
        count += 1
        if count % 100 == 0 and count != 0:
            print("Processed " + str(count) + " files so far")
        if count == 1: 
            outFile = convert(folder,file)
            continue
        df = convert(folder,file)
        outFile = pd.concat([outFile,df],ignore_index = True)
    print('The number of total files is ' + str(count))
    outFile.to_csv(newCSV)
