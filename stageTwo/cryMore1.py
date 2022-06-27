#NOTE KEYS = LEMMA FOR THIS LIST, run code to reverse later
lemmas = {
    'raleigh':'ralegh', 
    'raleana':'raliana',
    'berreo':'bereo',
    'lawrence':'laurence',
    'smith':'smythe',
    'john':'iohn',
    'bargrave':'bargraue',
    'henry':'henrie',
    'magellan':'magellanes',
    'magellan':'magellane',
    'magellan':'magelane',
    'christendom':'christendome',
    'plymouth':'plimmouth', 
    'plymouth':'plimouth',
    'japan':'japon',
    'trinidad':'trinidado',
    'belgium':'belgila',
    'belgium':'begala',
    'suleiman':'solyman',
    'suleiman':'soliman',
    'constantinople':'constantinop',
    'turkey':'anatolia',
    'portugal':'portingal',
    'guyana':'guiana',
    'bengal':'bengala',
    'carthage':'cartagena',
    'britain':'britania',
    'britain':'britannia',
    'mughal':'mogoll',
    'jew':'jewes',
    'jew':'jews',
    'jew':'iewes',
    'jew':'iew',
    'jew':'iews',
    'jesuit':'jesuites',
    'jesuit':'jesuite',
    'jesuit':'iesuite',
    'jesuit':'iesuites',
    'bermuda':'virginiola',
    'bermuda':'somers',
    'ethopia':'aethiopia',
    'egypt':'aegypt',
    'greek':'grecian',
    'islam':'islamic',
    'geography':'geographiqve',
    'geography':'geographique',
    'geography':'geographic',
    'ceylon':'seylon',
    'armenian':'armenians',
    'tunisia':'tunis',
    'flower':'flowers',
    'flower':'flores',
    'cambaye':'cambaia', #cotton cloth made in Bengal & other parts of India 
    'valencia':'valentia',
    'cambaye':'cambaya',
    'pariaman':'priaman', #coastal city in Indonesia 
    'volga':'vologda',
    'jakarta':'jacartra',
    'antioch':'antiochia', #ancient city in Syria 
    'messina':'mesina', #Italian port city
    'moscow':'moscovia',
    'moscow':'mosko',
    'moscow':'moscovite',
    'moscow':'muscovia',
    'moscow':'moscovie',
    'castile':'castilia',
    'carthagena':'carthage',
    'poland':'polonia',
    'malacca':'malaca', 
    'mahumetan':'manhumetans',
    'dominica':'dominicke',
    'lahore':'lahor',
    'canary':'canaria',
    'peru':'piru',
    'algiers':'alger',
    'macedonia':'macedon',
    'mecca':'mecha',
    'christian':'christani',
    'japanese':'japonian',
    'chinois':'chinese',
    'castile':'castille',
    'islam':'mahumetanisme', #double check! 
    'plymouth':'plymmouth',
    'russia':'russ',
    'genoese':'genovois',
    'genoese':'genovese',
    'flanders':'flander',
    'scandinavia':'scandia',
    'jakarta':'jaquatra',
    'sultan':'soltan',
    'phoenician':'phaenicians',
    'joshua':'josua',
    'turk':'turkeman',
    'crete':'creta',
    'transylvania':'transilvania', 
    'head':'cephalonia', #double check 
    'ireland':'irland',
    'brandenburg':'brandenbourg'
}
interesting = {'macao', # gambling card game
            }

#still to lemmatize
        'ambassage','bahar',
        'groneland','salomons',
        ,'tamerlan'
       'capon',
        'poutrincourt',
        '','friesland'
        'jenero','macao','paquin','mendoza'
        'cilicia','dorado','taurica',
        ,'moteçuma',
        'casal','sigismond','bohemiantartar',
        'tlaxcallan',
        'orenoco','carapana',
        ,'hamet','saragosa','',
        'bassa','saracen',
        'tripoli','placentia',
       'tangut',
        'suevia','mosquita','almeida',
        '','alba'
        'catelina','','pongo',
        'caria','spania','','guianian'

noclue = [
    'japarra'
]

#ask about spaniard/spain/spanish and extend to other regions
listlemmas = {
    'abraham':['abram', 'ibrahim'],
    'bishop':['bishopric', 'bishopriches', 'bishoprics'],
    'brazil':['brasill', 'brasilia','brasilian','brasil', 'brasile'],
    'canada':['cannada', 'amsterdam','newfoundland'], #is this a good decision
    'china':['cataya','cathaya','catay','cathay','canton', 'chineses','chinese'],    
    'germany':['germ','germa','germani','germanie','germanies','germanye','germanyes'],
    'indonesia':['jakarta','batavia', 'java', ], #condensing cities to country?
    'korea':['corea','coria', 'coreyra','corean','corayan' ], #check this is all referencing korea    
    'muhammad':['mohammed', 'mahumet', 'mahomet', 'mahometans'], #are mahometans muslim people??? should this be lemmatized to muhammad or no
    'russia':['russ', 'russe', 'russi', 'rvssia', 'siberia', 'astracan', 'novogrod'],    
    'popery':['popaian','papist','poperie','papish','popish','papistrie','papistry'],
    'prussia':['prvissa', 'prussian', 'prussians', 'sprussia'],   
    'spain':['spanishe', 'spanished', 'spanisshe',  'spanysh', 'spanyshe', 'seville', 'spanyssh', 'spanysshe','spaynysshe','spaine','spayne', 'spayn','espanna', 'hispanus', 'hispaniola', 'castille', 'castilian','barselona', 'granada'],
    'spaniard':['spainard', 'spainards','spaniarde' ,'spaniardes', 'spaniards',   'spanierds', 'spanyard', 'spanyardes', 'spanyards'],
    'tartar':['tartarian', 'tartarorum', 'tartaria'], #??
    'venice':['venetian','venitians','venisia','venetia']
}