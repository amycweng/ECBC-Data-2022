words = ['commodity','commodities','trade','merchandise',
        'commodious','merchandizing','profit','coffee',
        'tobacco','sugar','sassafras','winauk','beavers',
        'beaver','bever','furres','nullius','adventurer',
        'adventurers','adventures','adventure',
        'copper','pearls','pearl','perles','mulberry',
        'silk','turpentine','fantasia','virginiola',
        'virginia','bermuda','whales','whaling','whale',
        'orient','glutton','gluttony','greed','greedy',
        'busy','busyness','business','idleness','indies',
        'indian','india','plymouth','plimmoth','massachusetts',
        'colony','colonies','plantation','planter','spain',
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
        'jews','iewes','mahomet','christendom','christian','company','companies',
        'arabs','arabia','cochinele','cochineal','oriental','england','money']
dot = '●'
variants = {}
for word in words: 
    charList = []
    charList[:0] = word 
    for idx,char in enumerate(charList):
        newWord = charList.copy()
        if idx == 0: 
            variants[word] = []
        newWord[idx] = dot 
        newWord = ''.join(newWord)
        variants[word].append(newWord)
    charList.append(dot)
    lastWord = ''.join(charList)
    variants[word].append(lastWord)
print(variants)

corrections = {'l●sse': 'loss',
    'w●e':'woe',
    'w●st':'west',
    's●a':'sea',
    '●rade':'trade',
    '●iver':'river',
    'fi●h':'fish',
    'sea●':'sea',
    'land●':'land',
    'ship●':'ship',
    'ke●pe':'keep',
    's●ll':'sell',
    'sp●niards':'spaniard', # lemma singular?
    'u●e':'use',
    'us●':'use',
    'cap●':'cape', 
    'diu●rs':'diverse', 
    'i●land':'island',
    'paracous●y':'paracousey', #flagged for correct spelling?
    'indian●':'indian',
    'spaniard●':'spaniard',
    'wa●re':'ware',
    'turk●':'turk', 
    'k●ng':'king', 
    'portugal●':'portugal', 
    'co●st':'coast',
    'abo●rd':'aboard', 
    'par●s':'parts',
    'r●uer':'river', 
    'citi●':'city', 
    'di●ers':'diverse', 
    'countre●':'country',
    'good●':'good', 
    's●aine':'spain', 
    's●aves':'slaves', #doublecheck 
    'spain●':'spain', 
    'hop●':'hope', 
    'englishm●n':'englishmen', 
    'leagues●':'leagues', 
    'boa●':'boat', 
    'league●':'league', #lemma singular?
    'help●':'help', 
    '●ighest':'highest',
    'batta●le':'battale', 
    'm●ster':'master', #other poss?
    'england●':'england', 
    'person●':'person', 
    'fi●lde':'field', 
    'comm●nded':'commend', #lemma root verb
    'vo●age':'voyage', 
    'couns●ll':'counsel', 
    'r●maine':'roman',
    '●laine':'plain', #wouldn't be slaine right..?
    '●amous':'famous', 
    'gr●ene':'green',
    'countrey●':'country', #lemma singular
    'sa●led': 'sail', #lemma root verb
    't●wne':'town', 
    'en●lish':'english', 
    'south●':'south', 
    'chief●':'chief', 
    '●arth':'earth', #wont be anything else..? 
    'ank●red':'anchored',
    'river●':'river', #lemma singular 
    'b●asts':'beast', #lemma singular
    'sain●':'saint', 
    'fra●ce':'france', 
    'boh●mia':'bohemia', 
    'people●':'people', 
    'souldi●rs':'soldier', #singular
    'rive●':'river', 
    'ch●na':'china', 
    'north●':'north', 
    'norwegia●':'norwegian', # are we lemmatizing
    'b●rbarie':'barbary', 
    'cataya●':'catalonia', #??? should correct to spain or catalan?
    'spaine●':'spain', 
    'spania●d':'spaniard', 
    'inca●':'incan', #referring to spanish? also lemmatizing?
    'tartari●':'tartar', #lemma tartar
    's●uage':'savage',
    'comp●ny':'company', 
    '●mbarked':'embarked', 
    'jesu●':'jesus', 
    'canari●':'canary', #?
    'w●men':'woman', #lemma singular
    'wood●':'wood', 
    'dominio●s':'dominion', #lemma singular
    'guin●●':'guinea', 
    'furnishe●': 'furnished', #to lemma furnish (root vb) or keep?
    'molestation●':'molestation', 
    'ta●ta●ia':'tartar', #lemma tartar
    'g●rmany':'germany', 
    'geo●gia': 'georgia', 
    'law●s':'laws', #i hope 
    'russe●':'russia', #i hope
    'merchandise●':'merchandize', 
    'queene●':'queen', #lemma singular
    'engli●hmen':'englishmen', 
    'cott●n':'cotton', 
    'angol●':'angola', 
    'barga●ne':'bargain', 
    'canaries●':'canary', #lemma singular
    'ven●ce':'venice', 
    'merc●hants':'merchant', #lemma singular 
    'merchaunt●':'merchant', 
    'nigr●':'negro', 
    'portuga●':'portugal', 
    'sh●ppes':'ship', #lemma singular
    'gre●ke':'greek', #adj or proper noun aa
    'man●ians':'mansion', #i hope? lemma singular 
    'borne●':'borneo', 
    'pe●u':'peru', 
    'skin●e':'skin', #i hope?
    'curtes●e':'courtesy', 
    'spani●rds':'spaniard', 
    'u●scount':'viscount', 
    'inhabitants●':'inhabitant', 
    'ta●taria':'tartar', #lemma tartar
    'edward●':'edward', 
    'ru●sia':'russia', 
    'princ●●':'prince', #uh not princess right..?
    'isl●':'isle', 
    'authorise●':'authorise', #do we need to do authorized?
    's●ede':'seed', #i hope
    'golde●':'golden', #lemma to gold?
    'shippe●':'shipped', #lemma to ship?
    'sunn●':'sun', 
    'wi●es':'wife', #lemma singular 
    'leather●':'leather', 
    'turke●':'turkey',
    'plain●':'plain', 
    'per●ian':'persian', #i hope
    'jenkin●on': 'jenkinson',
    'excha●ges':'exchange', #lemma singular
    'necess●tie':'necessity', 
    'per●●an':'persian', 
    'k●ngs':'king', #lemma singular
    '●ivers':'river', #could be a variation of diverse?
    'rom●':'rome', #to roman?
    'barbar●●s':'barbarous', #i hope 
    'je●uites':'jesuit', #lemma singular
    '●artes':'part', #lemma singular
    '●hip':'ship', #not chip..? 
    'domi●ions':'dominion', #lemma singular
    'in●erecession':'intercession', 
    'jenkinson●':'jenkinson', 
    'g●od':'good', 
    'ea●●erly':'eagerly', #i hope
    '●orce':'force', #i hope
    'venic●':'venice', 
    'indie●':'indies', 
    'forbidden●':'forbidden', 
    'plimmouth●':'plymouth', #i hope
    'peru●':'peru', 
    'ta●tar':'tartar', 
    'emperour●':'emperor',
    'treasure●':'treasure', 
    'tak●n':'taken', #lemma root verb
    'magellan●':'magellan', 
    'victuals●':'victual', #lemma singular
    'christian●':'christian', #potentially lemma singular/adj
    'ri●h':'rich', 
    'm●rcator':'mercator', 
    'grain●':'grain', 
    'squemishly●':'squeamishly', 
    'sib●ria':'siberia', 
    'wands●':'wand', 
    'in●a':'inca', #same flag as inca above
    'mountaines●●●':'mountains', 
    'commodi●es':'commodity', #lemma singular 
    'company●':'company', 
    'magog●':'magog', 
    'a●tracan':'astracan', #i hope?
    's●iling':'sailing', 
    'boat●':'boat', #lemma singular
    'consul●':'consul', 
    'v●nice':'venice', 
    'mines●':'mine', 
    'naple●':'naple', 
    'tartar●':'tartar', 
    'tartar●●':'tartar', 
    'riche●':'riches', 
    'engla●d':'england', 
    '●ou●neys':'journey', 
    'island●':'island', 
    's●rue':'serve', #i hope
    'deceive●':'deceive', 
    'ru●●ia':'russia', 
    'h●●panis':'hispanus', #combine with spain? 
    'historia●':'history', 
    'john●':'john', 
    'commande●':'commander', 
    'wes●':'west', 
    'master●':'master', #lemma singular
    '●sland':'island', 
    'soldaia●':'soldier', 
    'gre●ce':'greece', 
    'di●●covered':'discovered', 
    'france●':'france', 
    '●nglish':'english', #to england?
    'roman●':'roman', #to rome?
    'b●lgaria':'bulgaria', 
    'stones●':'stone', #lemma singular
    'forcibl●':'forcible', 
    'flood●':'flood', 
    'phisi●ians':'physician', #lemma singular
    'f●orentia':'florentine', #adj or just florence?  
    'trinidad●':'trinidad',
    'monte●':'monte', 
    'ri●ers':'river', 
    '●urnished':'furnish', 
    'ar●est':'arrest', 
    'o●ientali':'oriental', 
    'indi●●':'indies',
    'grai●s':'grains', 
    '●ortugals':'portugal',
    'f●llow':'follow', 
    'gui●nians':'guianians',
    'cape●':'cape', 
    'georgia●':'georgia',
    'law●':'law', 
    'swed●n':'sweden', 
    'colonien●●●●':'colonies', 
    'arabi●●':'arabia',
    'peac●':'peace',
    'q●eenes':'queen',
    'town●s':'town',
    'infinit●':'infinity',
    'i●on':'iron',
    'po●tugals':'portugal', 
    'bett●r':'better',
    'jud●cious':'judicious',
    'portugall●':'portugal',
    'russ●n':'russian',
    '●orces':'sources',
    'h●ngaria':'hungary',
    'tu●ke':'turk',
    'fru●●ion':'fruition',
    'harbo●●':'harbor',
    'hau●n':'harbor',
    'histo●●●':'history',
    'chin●':'china',
    'discou●red':'discover',
    'fre●':'free',
    's●ruants':'servant',
    '●paine':'spain', 
    'giu●n':'given', 
    'sp●●iards':'spaniard',
    'franciscu●':'franciscus', 
    'savage●':'savage', 
    'b●ought':'bring', 
    '●lorence':'florence', 
    'nichola●':'nicholas',
    'water●':'water',
    'damascu●':'damascus',
    'naked●':'naked',
    '●mpire':'empire',
    'persi●':'persia', 
    'ta●tarorum':'tartar',
    'sl●ues':'slaves',
    'russiae●':'russia',
    'warr●●':'war',
    'rea●on':'reason',
    'nicho●as':'nicholas',
    'ja●a':'java',
    'hea●en':'heaven',
    'scotland●':'scotland',
    'no●uagians':'norweigians',
    'portugallie●':'portugal',
    'r●uers':'river',
    'jo●dan':'jordan',
    '●ountries':'country',
    'fishe●':'fish', 
    'honourable●':'honourable',
    '●ruit':'fruit',
    '●eagues':'league',
    'world●':'world',
    'unpeopled●':'unpeopled',
    'royal●':'royal',
    'aeth●opia':'ethiopia',
    'lord●':'lord',
    'pla●ted':'plant',
    'pr●mise':'promise',
    'shipp●':'ship',
    '●ufficient':'sufficient',
    's●ipped':'ship',
    'take●':'take',
    'bulga●ia':'bulgaria',
    'gold●':'gold',
    'jame●':'james',
    'g●rmanie':'germany',
    'noblem●n':'nobleman',
    'russi●':'russia',
    'ordinances●':'ordinance',
    'cast●le':'castile',
    'go●ds':'good',
    'hispani●la':'spain',
    '●mbassadour':'ambassadour',
    '●urnish':'furnish',
    'jap●n':'japan',
    'engli●hman':'englishman',
    'woo●s':'woods',
    'joh●':'john',
    'portug●ls':'portugal',
    '●amine':'famine',
    'informed●':'informed',
    'god●':'god',
    'authorit●e':'authority',
    'india●s':'indian',
    'tartar●ights':'tartar', 
    'paradis●':'paradise',
    'flo●d':'flood',
    'span●ards':'spaniard',
    'gentlemen●':'gentlemen',
    'prussians●':'prussian',
    'af●ica':'africa',
    'diver●':'diverse',
    'idol●':'idol',
    'cosmopoli●es':'cosmopolities',
    'hungari●':'hungary',
    '●ames':'james',
    '●hina':'china',
    'w●rlde':'world',
    'clo●h':'cloth',
    'nig●o':'negro',
    'and●ew':'andrew',
    'eliz●beth':'elizabeth',
    'earth●':'earth',
    'wo●ke':'work',
    'consta●tinople':'constantinople',
    'cath●ya':'catalonia',
    'for●es':'forces',
    'englishmen●':'englishmen',
    'constan●inople':'constantinople',
    'na●ion':'nation',
    'londo●':'london',
    'china●':'china',
    'souldiers●':'soldier',
    '●ich':'rich',
    'complain●●':'complain',
    'portinga●s':'portuguese',
    'portingals●':'portuguese',
    'sh●ps':'ship',
    'wom●n':'woman' #assumed singular (lemma)
    }

confused = ['esto●iland',
    'scon●land',
    'dro●es',
    'p●pe',
    'inh●bited',
    's●ford',
    'marpu●g', 
    'wel●elo-merchants', 
    '●unnes', 
    '●●wes', 
    'sigi●mond',
    'sit●', 
    'chincitai●',
    'f●ll',
    'russ●',
    'n●we',
    'wi●e', 
    't●ne', 
    'puer●o',
    '●oast',
    '●avour', 
    'd●ni●l', 
    'travell●', 
    'fra●●es', 
    '●hore',
    '●are', 
    'p●pper', 
    '●east',
    'owne●', 
    'l●nd',
    'man●', 
    '●orts', 
    '●aste',
    'h●ll',
    's●ip',
    '●ead',
    '●ore', 
    '●ast', 
    'pa●t', 
    'm●ny', 
    '●ands', 
    'be●', 
    's●nne',
    't●ken', 
    '●unne', 
    '●ish', 
    'r●nne', 
    'sor●', 
    'man●r', 
    '●land', 
    's●e', 
    'ri●er', 
    'cha●les', 
    '●aine', 
    'c●pe', 
    'men●', 
    'po●t',
    'li●es'
    ]