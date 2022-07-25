import os
import shutil

# input a a list of TCP IDs for the texts you're wanting to copy
# search = open('/srv/data/metadata/textCounts/target.txt', 'r')
search = ['A68060', 'B24138', 'A86305', 'A57390', 'B14268', 'A80618', 'A09573', 'A08092', 'A58086', 'B20731', 'A70377', 'B11348', 'A91917', 'A34686', 'A34698', 'A16527', 'A10419', 'B12972', 'A43506', 'A15796', 'A19579', 'B14007', 'B24137', 'A10426']
# specify which folder you're searching through
dir = '/srv/data/originaldata/eebotcp'
# dir = '/srv/data/otherTexts'

# matches name in the supplied list to file names, copies over if it exists in specified folder
missing=[]
copy=[]
for s in search:
    #s = line.strip()
    count = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.xml'):
                name = file.split('.')[0]
                if s in name:
                    #print(s,'has been copied!')
                    count += 1
                    copy.append(s)
                    # make sure to specify destination folder here!!
                    shutil.copy(os.path.join(root, file), '/srv/data/testTCP')
                
                else: continue
    if count == 0:
        #print(s,'is not in the folder :((((')
        missing.append(s)

print('copied:', len(copy), copy)
print('missing:', len(missing), missing)
