'''
Expanding our corpus of the Virginia, East India, and Levant companies 
by filtering through body texts as well as by author. 
'''
import os,time,csv
import pandas as pd

'''
Entering 'text' will identify texts
Entering 'metadata' will make a metadata for the identified texts 
'''
option = input('Enter text or metadata: ')

if option == 'text':
    from stageTwo.people import entities,onlyauthor
    folder = input('Enter path to input folder: ')
    start = time.time()

    texts = []
    entityTexts,authorTexts = 0,0
    '''Texts from 1580-1641 that mention relevant entities'''
    for file in os.listdir(folder):
        f = open(os.path.join(folder,file),'r')
        text = f.readlines()[0]
        tcpID = file.split('.')[0]
        for name in entities:
            if name in text: 
                texts.append(tcpID)
                entityTexts += 1
                break
        f.close()

    '''Texts from all EP that have relevant authors '''
    epMissingFile = open('/srv/data/ECBC-Data-2022/Text_Files/catalogue/EPmissing.txt','r')
    epMissing = epMissingFile.readlines()
    epMissingFile.close()

    for csvFile in os.listdir('/srv/data/metadata/TCP metadata'):
        data = pd.read_csv(os.path.join('/srv/data/metadata/TCP metadata',csvFile))
        for idx,tcpID in enumerate(data['id']):
            for auth in onlyauthor:
                if auth in data['author'][idx] and tcpID not in epMissing: 
                    texts.append(tcpID)
                    authorTexts += 1 
                    break

    outFile = open('/srv/data/peopleTexts.txt','w+')
    outFile.write(str(set(texts)))
    print(str(entityTexts)+' entityTexts\n'+str(authorTexts) + ' authorTexts\n')
    print('Total num of identified texts is '+str(len(texts)))
    end = time.time()
    print("The time of execution is :", end-start, ' seconds')

if option == 'metadata':
    start = time.time()
    idFile = open('/srv/data/ECBC-Data-2022/Text_Files/stageTwoFiles/peopleTexts.txt','r')
    ids = idFile.readlines()[0].split(',')
    for idx,tcpID in enumerate(ids):
        ids[idx] = tcpID.replace(r"'",'').strip()
    idFile.close()

    outFile = open('/srv/data/metadata/tuning/people.csv','a+')
    columns = ['id','title','author','publisher','pubplace','keywords','date']
    writer = csv.DictWriter(outFile, fieldnames=columns)
    writer.writeheader()
    count = 0
    for csvFile in os.listdir('/srv/data/metadata/TCP metadata'):
        data = pd.read_csv(os.path.join('/srv/data/metadata/TCP metadata',csvFile))
        for idx,tcpID in enumerate(data['id']):
            if tcpID in ids:
                print(tcpID)
                count += 1
                row = {'id':data['id'][idx],
                        'title':data['title'][idx],
                        'author':data['author'][idx],
                        'publisher':data['publisher'][idx],
                        'pubplace':data['pubplace'][idx],
                        'keywords':data['keywords'][idx],
                        'date':data['date'][idx]}
                writer.writerow(row)
    print(str(count)+'\n')
    end = time.time()
    print("The time of execution is :", end-start, ' seconds')




    





