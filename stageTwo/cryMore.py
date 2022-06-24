#NOTE KEYS = LEMMA FOR THIS LIST, run code to reverse later
lemmas = {
    'raleigh':'ralegh', #need feedback on names! which to correct to?
    'raleana':'raliana',
    'berreo':'bereo',
    'lawrence':'laurence',
    'smith':'smythe',
    'john':'iohn',
    'bargrave':'bargraue',
    'henry':'henrie',
    'magellan':'magellanes',
    'magellan':'magellane',
    'christendom':'christendome',
    'virginia':'virginian', #revisit after talking to PIs about spain/spanish
    'plymouth':'plimmouth', 
    'plymouth':'plimouth',
    'japan':'japon',
    'trinidad':'trinidado',
    'peru':'peruvian', #same issue for adj/noun
    'cuba':'havana', #hmmmmm
    'belgium':'belgila',
    'belgium':'begala',
    'belgium':'flanders', #maybe
    'constantinople':'constantinop',
    'turkey':'seraglio', #hmmmmmm
    'turkey':'anatolia',
    'portugal':'portingal',
    'america':'american',
    'guyana':'guiana', #using modern spelling?
    'bengal':'bengala', #india? bangladesh? or keep bengal?
    'carthage':'cartagena',
    'britain':'british',
    'britain':'briton',
    'britain':'britania',
    'england':'english', #also to check
    'england':'bristol',
    'mongolia':'mogoll',
    'jew':'jewes',
    'jew':'jews',
    'jesuit':'jesuites',
    'jesuit':'jesuite',
    'bermuda':'virginiola',
    'bermuda':'somers',
    'ethopia':'aethiopia',
    'egypt':'aegypt',
    'egypt':'egyptian',
    'greek':'grecian',
    'islam':'islamic',
    'scotland':'scottish',
    'geography':'geographiqve',
    'geography':'geographique',
    'geography':'geographic',
    'ceylon':'seylon',
    'port':'puerto',
    'austria':'vienna',
    'armenia':'armenians',
    'italy':'sicilia',
    'tunisia':'tunis',
    'flower':'flowers',
    'flower':'flores'
}

#still to lemmatize
'euphrates',
        'colmogro','valentia','angola',
        'cambaia','peru','nestorian',
        'cambalu','limon','balsara',
        'ormuz','priaman','tropic','','cambaya',
        'vologda','dominican','moluccas',
        'jacartra','tanais','dominica',
        'antiochia','mandarin','madera','mesina',
        'ambassage','moscovite','bahar','normandy',
        'netherlands','bohemia','mosambique',
        'parma','groneland','mecha','uirginia','salomons',
        'castilia','tamerlan','burgundy','mute',
        'javan','african','carthagena','polonia',
        'saxony','malabar','capon','rhine','navarre',
        'honduras','poutrincourt','malaca','sinai','mahumetans',
        'algiers','friesland','cypress','dominicke',
        'jenero','macao','paquin','mendoza','sqguenay',
        'netherlander','athens','libyan','lahor',
        'canaria','piru','cilicia','dorado','taurica',
        'alger','niger','macedon','moteçuma',
        'casal','sigismond','bohemiantartar',
        'scythian','canaan','armenian','tlaxcallan',
        'orenoco','gama','christiani','carapana',
        'saxon','hamet','saragosa','moscovie',
        'japonian','gaul','muscovia','eastindian',
        'portugese','marselia','johannes','bassa',
        'bantam','saracen','florence','florida',
        'aleppo','chinois','roman','moscow',
        'barbary','surat','mexican','cairo',
        'irish','frenchman','greek','rio','alexandria',
        'tripoli','placentia','tartary','fleming',
        'milan','lisbon','castille','congo',
        'russ','genoa','persian','lorraine','tangut',
        'suevia','genovois','salisbury','mosquita','almeida',
        'scandia','alba','vatican','spartan','manila',
        'jaquatra','catalonia','cephalonia','genoese',
        'catelina','josua','pongo','mahumetanisme',
        'magellanes','somerset','plymmouth','soltan',
        'caria','spania','genovese','guianian',
        'tuscany','brandenbourg','irland','bulgarian',
        'brandenburg','magelane','turkeman',
        'creta','salem','sussex','colima','transilvania',
        'tuscany','phaenicians',

noclue = [
    'japarra',
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
    'russia':['russ', 'russe', 'russi', 'rvssia', 'moscovia','mosko','moscow', 'siberia', 'astracan', 'novogrod'],    
    'popery':['popaian','papist','poperie','papish','popish','papistrie','papistry'],
    'prussia':['prvissa', 'prussian', 'prussians', 'sprussia'],   
    'spain':['spanishe', 'spanished', 'spanisshe',  'spanysh', 'spanyshe', 'seville', 'spanyssh', 'spanysshe','spaynysshe','spaine','spayne', 'spayn','espanna', 'hispanus', 'hispaniola', 'castille', 'castilian','barselona', 'granada', 'inca','incan'],
    'spaniard':['spainard', 'spainards','spaniarde' ,'spaniardes', 'spaniards',   'spanierds', 'spanyard', 'spanyardes', 'spanyards'],
    'tartar':['tartarian', 'tartarorum', 'tartaria'], #??
    'venice':['venetian','venitians','venisia','venetia']
}