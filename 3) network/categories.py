# the 'general' list is for keywords metadata 
general = ['Discovery and exploration', 'Description and travel',
                'Voyages and travels', 'Discoveries  English',
                'Commerce', 'Balance of trade',
                'Weights and measures', 'Coinage', 
                'Import quotas', 'Customs administration', 
                'Tariff', 'Missions','Commercial policy', 
                'Fifth Monarchy Men', 'Economic aspects', 
                'Africa East', 'Foreign trade regulation', 
                'Silk industry', 'Trade regulation', 
                'Fish trade','Colonial companies', 
                'Corporations', 'Corporation of London', 
                'Navigation','Trading companies','Pirates',
                'Foreign exchange', 'Foreign relations',
                'Monopolies','Trades increase','Textile industry',
                'Colonies', 'Colonial period',
                'New England', 'Guyana', 'Colonization', 'Canada',
                'Massachusetts', 'Indians of North America', 
                'Newfoundland','Central America',
                'Pokonchi language', 'Latin America',
                'America', 'Spain','Bermuda Islands',
                'Smith Thomas','Gilbert Bartholomew',
                'Raleigh Walter','United States',
                'Northwest Passage','Tobacco industry',
                'Hides and skins trade']

#The following lists are for body texts 
levant = ['currans','turkey','levant',
            'suleiman','richard hakluyt',
            'edwin sandys','george sandys',
            'thomas mun','samuel purchas',
            'john sanderson','fynes moryson',
            'africa','muhammad','muhammadan',
            'sultan','venice']

eic = ['eastindia','east indies',
        'eastindies','east india',
        'indonesia','amboyna','india',
        'china','cathay','cataya','chinese',
        'cataia','malacca']

virginia = ['walter raleigh', 'virginia',
            'virginia company','plantation',
            'colony','guyana','newfoundland',
            'america','bermuda','northwest passage',
            'tobacco','beaver','bever','canada',
            'massachusetts','newengland',
            'north america','somers','cuba',] 

keyTerms = ['commodity','trade','merchandise',
        'commodious','merchandizing','profit','coffee',
        'sugar','sassafras','winauk','beaver',
        'beaver','bever','furres','nullius','adventurer',
        'adventure','copper','pearl','perles','mulberry',
        'silk','turpentine','fantasia','virginiola',
        'virginia','bermuda','whale','whaling',
        'orient','glutton','gluttony','greed','greedy',
        'busy','busyness','business','idleness','indies',
        'indian','india','plymouth','plimmoth','massachusetts',
        'colony','plantation','planter','spain',
        'spanish','spaniard','hispanola','hispanis','venice',
        'france','french','antwerp','levant','spices',
        'indigo','currans','corrants','import','export',
        'importation','exportation','raisins','cloth',
        'giaour','infidel','cape','vasco','lepanto',
        'pirates','piracy','moores','barbary','barbaries','customs',
        'shippe','ship','joint','stock','trades','trading','traffic',
        'merchant','merchants','insurance','aegypt','eqypt',
        'excessive','defense','bullion','pleasure','indentured',
        'negroes','negro','captives','strabo','novelty',
        'exchanging','exchange','barter','bartering','drugs',
        'jews','christendom','christian','company',
        'arab','arabia','cochinele','cochineal','oriental','england','money']

entities = ['vasco de gama','francis drake','walter ralegh','palaeologus',
            'thomas mun','robert lewes','john sanderson', #sanderson is missing as an author
            'fynes moryson','john covel','william lithgow','suleiman','anthony jenkinson',
            'richard shelley','henry jessey','peter heylyn','john layfield',
            'john tradescant','robert harcourt','prester john','prester jean',
            'muhammad sultan', 
            'john ferrar', 'nicholas ferrar', 'john harper', 
            'humphrey gilbert', 'george peckham', 'richard hakluyt',
            'john rastell', 'thomas porter', 
            'edward maria wingfield', 'bartholomew gosnold', 'thomas smith',
            'john dodderidge', 'edwin sandys', 'george sandys',
            'william cope', 'gabriel barbour',
            'sebastian cabot', 'john cabot', 'edward osborne',
            'richard staper', 'william harborne', 'murad', 'desoto',
            'william garret', 'amerigo vespucci', 'christopher columbus',
            'turkey company' 
            ]

tobacco = 'tobacco|tobaco|tobacca|tobacconist'
drug = 'drug|drugge|drugg|elixir|apothecary|confection|confect|medicinable|medicine|medecine|medicament|arsenic|poppey|chemic|medicinal|intoxicate|tacamahaca|potion|mithridate|antimony|opiate|opium'

import pandas as pd
import os,re 
def getTexts(folder,searchList):
    fileToText = {}
    underscores = {}
    for root,dirs,files in os.walk(folder):
        for file in files:
                if '.txt' not in file: continue
                path = os.path.join(folder,file)
                f = open(path,'r')
                text = f.readlines()[0]
                if '_' in file: 
                        name = file.split('_')[0]
                        if name not in searchList: continue
                        if name not in underscores.keys(): 
                                underscores[name] = text
                        else: underscores[name] = underscores[name] + ' ' + text
                else: 
                        name = file.split('.')[0]
                        if name not in searchList: continue
                        fileToText[name] = text
                f.close()
        for name,text in underscores.items():
            fileToText[name] = text
        return fileToText

meta = pd.read_csv('/srv/data/metadata/tuning/relevant.csv')
generalFeatures = open('/srv/data/periodFeatures/period5features/featuresPeriod1635.txt','a+')# #
keyFeatures = open('/srv/data/periodFeatures/period5features/drugTobaccoPeriod1635.txt','a+')# #

from timePeriods import period5 #
featuresDict = {}
tobaccoDrug = {}
period = period5 #

search = levant.copy()
search.extend(eic)
search.extend(virginia)
search.extend(keyTerms)
search.extend(entities)
search = list(set(search))
searchStr = '|'.join(search)

specificSearch = tobacco + '|' + drug

textInfo = getTexts('/srv/data/relevantEPBodySTOP',period)
print(f'Will process {len(textInfo)}')
progress = 0
for idx, TCPID in enumerate(meta['id']):
        TCPID = TCPID.strip()
        if TCPID in period: 
                featuresDict[TCPID] = []
                tobaccoDrug[TCPID] = []
                '''check text for general terms and entities'''
                inText = re.findall(searchStr,textInfo[TCPID])
                featuresDict[TCPID].extend(inText)
                '''check text for drug or tobacco'''
                specific = re.findall(specificSearch,textInfo[TCPID])
                tobaccoDrug[TCPID].extend(specific)
                progress+= 1
                if not progress % 100: print(progress)
print(progress)
for TCPID in featuresDict.keys():
        generalFeatures.write(TCPID + ': '+ ' '.join(featuresDict[TCPID])+'\n')
for TCPID in tobaccoDrug.keys():
        keyFeatures.write(TCPID + ': '+ ' '.join(tobaccoDrug[TCPID])+'\n')
