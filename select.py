import os
import shutil

# input a a list of TCP IDs for the texts you're wanting to copy
search = open('/srv/data/ECBC-Data-2022/Text_Files/catalogue/relevant.txt', 'r')

# specify which folder you're searching through
# dir = '/srv/data/originaldata/allTCP'
dir = '/srv/data/originaldata/eebotcp'

# matches name in the supplied list to file names, copies over if it exists in specified folder
for line in search:
    s = line.strip()
    count = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.xml'):
                name = file.split('.')[0]
                if s in name:
                    print(s,'has been copied!')
                    count += 1
                    
                    # make sure to specify destination folder here!!
                    shutil.move(os.path.join(root, file), '/srv/data/relevantEPFiles')
                
                else: continue
    if count == 0:
        print(s,'is not in the folder :((((')