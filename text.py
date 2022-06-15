from bs4 import BeautifulSoup
import re,os,time
from characterCleaner import simple_clean, txt_clean

'''
STAGE I TEXT PROCESSING for both body text and dedications. 
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
        if not any(x in parent_name for x in ['front', 'table', 'back']) and re.search('lemma',str(sibling)) and str(sibling['lemma']) != 'n/a':
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

def convert(folder,file, textfolder):
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


if __name__ == '__main__':
    '''
    Initializes and writes metadata to a new CSV file. 
    '''
    folder = input('Enter folder path: ')
    textfolder = input('Enter the folder path for your output text files: ')
    
    start = time.time()
    count = 0
    for file in os.listdir(folder):
        count += 1
        if count % 10 == 0 and count != 0:
            print("Processed " + str(count) + " files so far")
        convert(folder,file,textfolder)
    print('The number of total files is ' + str(count))
    end = time.time()
    print("The time of execution is :", end-start, ' seconds')

