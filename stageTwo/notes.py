
interesting = {'macao', # gambling card game
            'bellarmine', #jug
            'indebt',
            '†',
            'esay',
            'seducer',
            'ethnic',
            'lavish',
            'adulterous',
            'concupiscence',
            'servingman',
            'harlot',
            'swine',
            'seduce',
            'chrysostom', #archbishop of constantinople; 7k mentions 
            'eusebius', #another church figure; 7k mentions 
            'galen',
            'antichristian',
            'antioch',
            'manna',
            'fig',
            'venomous',
            'turkish',
            'whoredom', #4.8k mentions
            'whoremonger', #1.1k mentions 
            'addict', #4.8k mentions
            'froward',
            'debtor',
            'publican',
            'ague', #violent fever
            'brute',
            'leprosy',
            'discommodity',
            'insufficient',
            'beastly',
            'currant', #4k mentions 
            'homily', #kind of sermon
            'brutish',
            'choler', #type of galenic humor 
            'concubine', #3.6k mentions 
            'noisome',
            'eunuch', #3.5k mentions 
            'avarice', #3.5k mentions 
            'heathenish',
            'prejudicial',
            'sloth', #3.1k mentions 
            'slavery',
            'tumour',
            'tyrannical',
            'ungodliness',
            'usurper',
            'selflove', #2.2k mentions 
            'manful',
            'unfruitful',
            'irreligion','eunuch','damascus','university',
            'paris','hell','powhatan','malacca','ignorance',
            'idolatry','sumatra','amity','revenge',
            'tyrant','slaughter','nutmeg','juice','kindness',
            'physician','tribe','cannibal','astracan',
            'science','suburb','mutiny','rebellion','plague',
            'nun','israel','quicksilver','indulgence',
            'charity','armada','galleon','salmon',
            'treatise','murder','monster','customer',
            'plenty','scarcity','unicorn','inquisition',
            'malice','ivory','displeasure','merit','levant',
            'concubine','fortunate','prosperity','rumour',
            'heretic','cacao','fertility','conflict',
            'corruption','robbery','peregrination','mesopotamia',
            'nicaragua','jamaica','adultery','malta','troy',
            'california','mecca','malefactor','safeguard',
            'savour','girl','amboyna','gibraltar','pestilience',
            'peso','splendour','visitor','drunkenness',
            'bonaventure','godfrey','vizier',
            'newengland','lamentation','bribe','lawyer',
            'oppression','nabob','whore','monk','incest',
            'salem','minion','glut','offendor','bribery'
}

'''This keyTerms list is from the Google Doc of key terms that our PIs gave us'''
keyTerms = ['commodity','trade','merchandise',
        'commodious','merchandizing','profit','coffee',
        'tobacco','sugar','sassafras','winauk','beaver',
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

popeRelated = ['papal','papist','popery'
                'popish','pope','popedom',
                'popaian','papist','poperie',
                'papish','papistrie','papistry',
                'papistical']

chinaRelated = ['cataya','cathaya','catay','cathay','canton', 'chineses','chinese']

#some of these spain-related ones are from EEBO rather than EP 
spainRelated = ['spanishe', 'spanished', 'spanisshe',  'spanysh', 'spanyshe', 'seville', 'spanyssh', 'spanysshe','spaynysshe','spaine','spayne', 'spayn','espanna', 'hispanus', 'hispaniola', 'castille', 'castilian','barselona', 'granada']

geographic = ['banda', 'plymouth', 'poland', 'venetia', 'scotland', 
'denmark', 'damascus', 'guinea', 'paris', 'cyprus', 'powhatan', 
'bengala', 'britain', 'prussia', 'agra', 'malacca', 'cuba', 'antwerp', 
'sumatra', 'hispaniola', 'moha','aethiopia', 'havana', 'pechora', 'venetian',
 'seville', 'moscovia', 'cibola', 'oxford', 'provence', 'castro',
 'livonia', 'soldania', 'paracoussy', 'cataia', 'morea', 'biscay','muscovite',
 'portugal', 'spaniard', 'england', 'spain', 'india', 'tartar', 'mexico', 
 'france', 'russia', 'venice', 'peru', 'persia', 'egypt', 'jerusalem',
 'america', 'constantinople', 'rial', 'flanders', 'cochin', 'cananor', 'arica',
 'zeila', 'camden', 'assyria', 'borneo', 'east-indies', 'hudson', 'yeraslave',
 'galicia']

people = ['johannes','sanderson','nicolo', 'john', 'thomas', 'william',
'henry','richard', 'hollander', 'francis', 'elizabeth', 'antonio', 
'sebastian', 'andrew', 'abraham', 'francisco', 'joseph', 'lewis', 'hawkins',
'laurence', 'matthew', 'diego', 'janni', 'augustine', 'reys', 'arias',
'pheodorowich', 'isabel', 'josephus', 'sio', 'sarmiento', 'rawlins',
'anna', 'vasilowich', 'selim', 'cantan', 'mendoça','tartarian','welshman']

doubleCheck = {
    'cath●ya':'cataya',# double check 
    }
