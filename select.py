import os
import shutil

#search = input('Enter your text TCP ID here: ')
search = open('/srv/data/ECBC-Data-2022/Text_Files/VirginiaCompanyTexts.txt', 'r')
# dir = '/srv/data/allPhase1Extract'
#dir = '/srv/data/allPhase2Extract'
dir = '/srv/data/eebotcp/texts'

#for each id search
for line in search:
    s = line.strip()
    count = 0
    for folders in os.listdir(dir):
        folder = os.path.join(dir, folders)
        #phase 1
        if folder != '/srv/data/allPhase1Extract/.DS_Store':
        #phase 2
        #if folder != '/srv/data/allPhase2Extract/.DS_Store':
            for file in os.listdir(folder): 
                text = os.path.join(folder, file)
                if text.endswith('.xml'):
                    #for phase1 or phase2 extract folders:
                    # name = text.split('/')[5].split('.')[0]
                    
                    #for EP eebotcp folder
                    name = text.split('/')[6].split('.')[0]
                    if s in name:
                        print(s,'has been copied!')
                        count += 1
                        shutil.copy(text, '/srv/data/VirginiaTextsEP')
                    
                    else: continue
    if count == 0:
        print(s,'is not in the folder :((((')

