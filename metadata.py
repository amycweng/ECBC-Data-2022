from bs4 import SoupStrainer,BeautifulSoup
import re,os,csv,time

'''
STAGE I METADATA PROCESSING 
Takes a folder of individual EEBO-TCP XML files and writes the metadata into a separate CSV file. 

For Stage I text processing, see text.py 
'''
def title(data):
    '''
    Returns the title of the text within a XML file 
    '''
    tags = SoupStrainer('title')
    soup = BeautifulSoup(data,parse_only=tags,features='html.parser')
    title = soup.find_all('title')[0].get_text()
    return title

def authors(data):
    '''
    Returns a string of all mentioned authors separated by semi-colons
    ''' 
    tags = SoupStrainer('author')
    soup = BeautifulSoup(data,parse_only=tags,features='html.parser')
    authors = soup.find_all('author')
    auth = ''
    for a in authors:
        if auth != '':
            auth = auth + '; ' + a.get_text()
        else: 
            auth += a.get_text()
    if auth == '':
        auth = 'Anonymous'
    return auth

def pubplace(data):
    tags = SoupStrainer('pubplace')
    soup = BeautifulSoup(data,parse_only=tags,features='html.parser')
    pubplace = soup.find_all('pubplace')
    if len(pubplace) == 2:
        str = pubplace[1].string
        pubplace = re.findall('\w+',str)
        count = 0
        for p in pubplace:
            if count == 0:
                count += 1
                cleanPlace = p 
            else: 
                cleanPlace = cleanPlace + ' ' + p
        return cleanPlace
    return 'No pubplace'

def publisher(data):
    tags = SoupStrainer('publisher')
    soup = BeautifulSoup(data,parse_only=tags,features='html.parser')
    pubs = soup.find_all('publisher')
    if len(pubs) == 2:
        pub = pubs[1].string
        words = re.findall('\w+',pub)
        return ' '.join(words)
    return 'No publisher'

def keywords(data):
    '''
    Returns the keywords separated by semicolons 
    '''
    tags = SoupStrainer('keywords')
    soup = BeautifulSoup(data,parse_only=tags,features='html.parser')
    keywords = soup.find_all('term')
    list = []
    if len(keywords) != 0:
        for part in keywords:
            list.append(part.get_text())
        final = ' -- '.join(list)
        return final
    return 'No Keywords'
    
def idno(data):
    tags = SoupStrainer('idno')
    soup = BeautifulSoup(data,parse_only=tags,features='html.parser')
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

def oldIDNO(soup):
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

def dateTXT():
    '''
    Extracts the integer date or date range from the corresponding entry in TCP's official 
    documentation of all the EEBO IDs and dates. Returns a dictionary with the data from 
    both Phase I and II.  

    This function should only be called once. Afterwards, the user can directly refer to the 
    returned dictionary to find dates. 
    '''
    f1 = '/srv/data/ECBC-Data-2022/Text_Files/eebo_phase1_IDs_and_dates.txt'
    f2 = '/srv/data/ECBC-Data-2022/Text_Files/EEBO_Phase2_IDs_and_dates.txt' 
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

def convert(folder,file):
    '''
    Master function for converting each XML file into a dataframe 
    '''
    fileName = os.path.join(folder,file)
    name = file.split('.')[0]
    data = open(fileName,'r')
    data = data.read()
    
    # Parse the metadata that we need for each dataframe 
    t = title(data)
    a = authors(data)
    pub = publisher(data)
    pp = pubplace(data)
    k = keywords(data)
    id = idno(data)
    d = dates[name]

    # Input all of the relevant column info into a dictionary to be returned as a dataframe 
    dict = {'id':name,'stc':id[0],'estc':id[1],
            'title':str(t),'author':str(a),
            'publisher':pub,'pubplace':pp, 
            'keywords':k, 'date':str(d)
            }
    return dict

if __name__ == '__main__':
    '''
    Initializes and writes metadata to a new CSV file. 
    '''
    folder = input('Enter path to your folder of XML files: ')
    newCSV = input ('Enter the desired path of your metadata CSV file, including the name of the new CSV: ')
    
    start = time.time()
    count = 0
    dates = dateTXT()
    outfile = open(newCSV,'a+')
    columns = ['id', 'stc', 'estc','title','author','publisher','pubplace','keywords','date']
    writer = csv.DictWriter(outfile, fieldnames=columns)
    writer.writeheader()
    for file in os.listdir(folder):
        count += 1
        if count % 100 == 0:
            print("Processed " + str(count) + " files so far")
        dict = convert(folder,file)
        writer.writerow(dict)
    print('The number of total files is ' + str(count))
    end = time.time()
    print("The time of execution is :", end-start, ' seconds')

