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

entities = ['vasco de gama','francis drake','walter ralegh','palaeologus',
            'thomas mun','robert lewes','john sanderson', #sanderson is missing as an author
            'fynes moryson','john covel','william lithgow','suleiman','anthony jenkinson',
            #john covel & anthony jenkinson are also missing as authors 
            'richard shelley','henry jessey','peter heylyn','john layfield',
            #richard shelley & john layfield are missing as authors 
            'john tradescant','robert harcourt','prester john','prester jean',
            #prester is missing as an author 
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
            #does not show up as author tag: columbus, vespucci, desoto, murad iii (though murad iv does show up)
            # william harborne, richard staper, sebastian and john cabot, edward osborne, 
            # gabriel barbour, william cope, edward maria wingfield, john and nicholas ferrar, 
            # john harper, george peckham
            'turkey company', 
            ]

onlyauthor = ['Teixeira, José, 1543-1604', #we did not find a p.teixeira. J.T.'s works are voyages too 
                'Thévenot, Jean de, 1633-1', #the author under which M. de Thevenot's works are listed.
                #we might have to filter for the dates listed in the authors column too
                'Tradescant, John, 1608-1662.',
                'Mun, Thomas, 1571-1641.', #one of his texts is within our time range; another is not
                'Drake, Francis, Sir, d. 1637. World',
                'Lithgow, William, 1582-1645?', # ONE of his texts is NOT within our range 
                'Jessey, Henry, 1603-1663.', #all three of his texts are NOT within our range
                'Heylyn, Peter, 1600-1662.', #many of his works are outside our range 
                'Garrett, William, d. 1674 or 5.', #works outside our time range
                'Porter, Thomas, fl. 1654-1668.', #works outside range, also two other author tags, see below
                'Porter, T. (Thomas), 1636-1680.',
                'Porter, Thomas, d. 1667.',

                #the following are in our relevant corpus 
                'Kemys, Lawrence, d. 1618.',
                'Raleigh, Walter, Sir, 1552?-1618.',
                'Raleigh, Sir, Walter, 1552?-1618.',
                'Leo, Africanus, ca. 1492-',
                'Drake, Francis, Sir, d. 1637.',
                'Drake, Francis, Sir, d. 1637. Sir Francis',
                'Roberts, Lewes, 1596-1640.',
                'Harcourt, Robert, 1574?-1631.',
                'Leo, Africanus, ca. 1492-ca. 1550.'
                'Doddridge, John, Sir, 1555-1628.', #does not show up as a keyword in any search
                'Gilbert, Humphrey, Sir, 1539?-1583.',
                'Hakluyt, Richard, 1552?-1616.',
                'Rastell, John, 1532-1577.',
                'Sandys, Edwin, 1516?-1588.',
                'Sandys, Edwin, 1611 or 12-1642.',
                'Sandys, Edwin, Sir, 1561-1629.', #three edwin sandys author tags??
                'Sandys, George, 1578-1644.'
                ]

import pandas as pd
import os,re 
def getTexts(folder):
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
                        if name not in underscores.keys(): 
                                underscores[name] = text
                        else: underscores[name] = underscores[name] + ' ' + text
                else: 
                        name = file.split('.')[0]
                        fileToText[name] = text
                f.close()
        for name,text in underscores.items():
            fileToText[name] = text
        return fileToText

meta = pd.read_csv('/srv/data/metadata/tuning/target.csv')
outfile = open('/srv/data/moreFeaturesTrade.txt','a+')
supervisionSet = ['A13290', 'A15050', 'A19590', 'A15387', 'A08829', 'A80633', 'A13172', 'A02614', 'A12788', 'A46842', 'A34674', 'A02324', 'A02495', 'A03065', 'A03144', 'A03149', 'A05237', 'A05597', 'A06137', 'A07768', 'A07769', 'A07834', 'A10357', 'A10821', 'A12718', 'A13294', 'A13821', 'A14722', 'A15033', 'A16309', 'A17981', 'A19072', 'A19368', 'A21108', 'A26262', 'A31106', 'A41427', 'A43507', 'A43514', 'A43524', 'A43528', 'A43531', 'A43533', 'A43535', 'A43545', 'A43553', 'A57329', 'A57355', 'A57360', 'A57532', 'A57590', 'A57652', 'A62166', 'A68617', 'A68619', 'A68764', 'A71305', 'A71306', 'A71307', 'A10368', 'A08874', 'A07883', 'A02239', 'A02826', 'A20847', 'A05074', 'A13574', 'A68132', 'A19476', 'A13173', 'A07466', 'A09195', 'A19622', 'A07894', 'A16282', 'A11408', 'A20983', 'A01395', 'A14194', 'A97352', 'A14916', 'A01095', 'A01342', 'A08017', 'A02464', 'A68197', 'A17808', 'A14028', 'A09208', 'A00617', 'A07448', 'A16206', 'A12535', 'A07267', 'A01403', 'A11862', 'A08536', 'A97346', 'A68163', 'A13043', 'A11931', 'A02775', 'A09169', 'A07559', 'A10743', 'A12317', 'A13042', 'A14293', 'A12461', 'A68659', 'A05410', 'A07439', 'A17810', 'A55555', 'A68944', 'A01231', 'A17958', 'A05569', 'A05594', 'A12533', 'A11383', 'A68445', 'A68465', 'A13830', 'A11516', 'B11307', 'A13049', 'A07363', 'A11863', 'A07680', 'A11954', 'A12598', 'A14770', 'A13053', 'A02858', 'A05412', 'A08239', 'A05339', 'A01864', 'A03411', 'A19232', 'A01512', 'A02848', 'A09741', 'A00580', 'A09197', 'A13415', 'A83496', 'A04194', 'A10389', 'A13217', 'A16286', 'B13659', 'A07225', 'A68463', 'A01115', 'A21106', 'A09500', 'A10231', 'A14292', 'A67927', 'A12609', 'A16482', 'A19602', 'A07628', 'A68475', 'A17140', 'A01764', 'A03066', 'A07415', 'A16489', 'A11467', 'A19211', 'A43598', 'A18974', 'A01364', 'B00136', 'A21071', 'A03096', 'A16264', 'A05289', 'A01160', 'A09569', 'A68283', 'A10690', 'A20238', 'A04911', 'A17848', 'A05184', 'A01043', 'A16308', 'A17832', 'A02484', 'A18028', 'A07280', 'A17310', 'A11878', 'A10668', 'A13980', 'A01991', 'A01128', 'A11493', 'A05105', 'A01811', 'A05335', 'A16275', 'A01161', 'A67926', 'A05751', 'A04863', 'A06471', 'A23464', 'A12119', 'A10228', 'A11464', 'A12824', 'A13820', 'A12738', 'A16248', 'A06134', 'A19179', 'A06425', 'A18501', 'A68202', 'A22928', 'A05331', 'A06786', 'A67922', 'A19354', 'A05094', 'A10417', 'A10436', 'A10439', 'A10440', 'A34659', 'A34936', 'A68633', 'A68635', 'A00201', 'A00268', 'A01749', 'A01932', 'A02494', 'A02655', 'A04813', 'A05601', 'A07605', 'A07886', 'A08052', 'A08166', 'A09899', 'A11788', 'A11831', 'A11842', 'A11884', 'A12458', 'A12460', 'A12466', 'A12596', 'A14510', 'A14803', 'A15069', 'A16221', 'A19313', 'A21083', 'A25867', 'A34856', 'A35994', 'A37432', 'A37936', 'A43513', 'A43537', 'A43543', 'A43544', 'A43550', 'A43552', 'A43556', 'A45999', 'A47317', 'A47319', 'A48714', 'A49991', 'A51598', 'A55497', 'A56021', 'A57347', 'A57367', 'A57374', 'A57391', 'A57453', 'A57465', 'A57483', 'A57518', 'A57525', 'A57589', 'A57605', 'A57617', 'A62162', 'A62165', 'A65185', 'A66847', 'A69046', 'A69149', 'A70942', 'A83297', 'A85817', 'A86296', 'A86306', 'A88366', 'A90869', 'A94198', 'A94783', 'B00052', 'B00963', 'A13128', 'A19029', 'A07512', 'A06935', 'A22171', 'A07516', 'A17074', 'A57517', 'A12615', 'A18694', 'A09213', 'A02333', 'A02171', 'A02795', 'A68000', 'A12470', 'A07788', 'A13705', 'A68903', 'A03251', 'A10376', 'A01216', 'A10822', 'A05269', 'A20442', 'A18686', 'A01003', 'A03229', 'A16495', 'A05570', 'A04795', 'A15706', 'A17788', 'A19863', 'A03123', 'A02472', 'A22340', 'A01871', 'B16236', 'A04364', 'A00214', 'A10774', 'B01237', 'A71317', 'A09209', 'A09478', 'A33630', 'A07903', 'A68945', 'A15466', 'A01622', 'A78796', 'A14026', 'A20784', 'A09733', 'A74609', 'A14850', 'A15862', 'A20114', 'A34660', 'A67457', 'A73929', 'A22559', 'A11027', 'A10530', 'A00985', 'A09011', 'A02606', 'A78325', 'A00271', 'A21082', 'A16993', 'A11529', 'A08162', 'A06788', 'A02059', 'B00767', 'A12313', 'A68946', 'A14164', 'A69334', 'A69175', 'A02764', 'A16718', 'A38817', 'A22173', 'A67893', 'A02626', 'A08440', 'A09909', 'A08210', 'A10314', 'A22250', 'A12218', 'A37552', 'A13417', 'A11056', 'A72217', 'A00947', 'A07915', 'A72397', 'A12274', 'B14980', 'A11416', 'A03476', 'A06317', 'A16711', 'A08258', 'A00518', 'A73547', 'A13460', 'A16313', 'A67125', 'A22364', 'A08538', 'A04763', 'A08150', 'A10354', 'A07510', 'A05165', 'A01108', 'A19312', 'A16490', 'A73966', 'A14517', 'A08154', 'A14516', 'A67920', 'A14512', 'A08698', 'A03451', 'B00838', 'A14519', 'A12830', 'A01017', 'A36830', 'A20443', 'A68509', 'A12691', 'A21080', 'A10378', 'B00564', 'A12545', 'A30295', 'A10373', 'A69354', 'A14514', 'A73588', 'A13781', 'A10725', 'A22435', 'A14871', 'A13959', 'A14671', 'A09826', 'A11767', 'B14988', 'A19942', 'A22195', 'A69205', 'A16306', 'A13423', 'A09010', 'A00549', 'A04223', 'A10588', 'A04581', 'A05182', 'A22537', 'A68246', 'A22439', 'A20509', 'A06701', 'B09574', 'A14958', 'A13516', 'A03461', 'A17374', 'A06694', 'A09900', 'A12330', 'A02421', 'A10591', 'A14511', 'A13506', 'A14521', 'A22447', 'A51736', 'A19763', 'A16139', 'A00021', 'A22354', 'A22169', 'A02201', 'A03734', 'A15309', 'A59054', 'A35908', 'A21084', 'A15036', 'A14526', 'A07604', 'A69259', 'A01426', 'A14513', 'A14520', 'A03477', 'A13057', 'A03702', 'A17260', 'A22363', 'A22328', 'A22327', 'A14524', 'A11786', 'A16507', 'A78324', 'A10526', 'A14518', 'A34504'] 
additional = ['A00008', 'A00499', 'A00611', 'A00709', 'A00816', 'A00924', 'A00983', 'A01064', 'A01371', 'A01857', 'A01867', 'A02325', 'A02404', 'A02605', 'A02673', 'A02794', 'A02874', 'A03330', 'A04099', 'A04334', 'A04494', 'A04899', 'A05059', 'A05414', 'A05421', 'A06285', 'A06339', 'A06473', 'A06785', 'A06789', 'A06790', 'A06791', 'A07165', 'A07216', 'A07388', 'A07509', 'A07532', 'A07612', 'A07619', 'A07623', 'A07792', 'A07832', 'A07840', 'A07958', 'A08108', 'A08122', 'A08123', 'A08124', 'A08125', 'A08307', 'A08700', 'A08965', 'A09493', 'A09810', 'A10235', 'A10377', 'A10672', 'A10713', 'A10859', 'A11082', 'A11204', 'A11214', 'A11283', 'A11330', 'A11385', 'A11774', 'A11779', 'A11782', 'A11787', 'A11791', 'A11795', 'A11797', 'A11802', 'A11806', 'A11808', 'A12467', 'A12471', 'A12677', 'A12689', 'A12690', 'A13110', 'A13394', 'A13478', 'A13484', 'A13485', 'A13508', 'A13513', 'A13519', 'A14203', 'A14275', 'A14325', 'A14328', 'A14338', 'A14591', 'A14615', 'A14618', 'A14621', 'A14719', 'A15072', 'A15097', 'A15589', 'A15591', 'A15685', 'A16207', 'A16220', 'A16303', 'A17595', 'A18057', 'A18071', 'A18098', 'A18326', 'A18465', 'A18476', 'A18477', 'A18769', 'A18907', 'A19359', 'A19376', 'A19381', 'A19384', 'A19439', 'A19470', 'A19674', 'A19729', 'A19774', 'A19775', 'A19864', 'A19936', 'A19937', 'A20435', 'A20596', 'A20838', 'A20849', 'A20982', 'A22009', 'A22013', 'A22097', 'A22103', 'A22113', 'A22157', 'A22210', 'A22230', 'A22300', 'A22520', 'A22547', 'A22571', 'A22574', 'A22634', 'A22683', 'A22719', 'A22727', 'A40409', 'A57437', 'A57520', 'A57831', 'A57840', 'A63520', 'A65782', 'A68252', 'A68345', 'A68472', 'A68498', 'A68648', 'A69118', 'A69151', 'A69345', 'A69361', 'A71313', 'A78294', 'A85685', 'A89497', 'A00142', 'A00209', 'A00292', 'A00688', 'A01503', 'A02335', 'A03450', 'A03800', 'A04070', 'A04690', 'A04691', 'A04966', 'A05051', 'A05067', 'A06245', 'A06793', 'A06803', 'A06892', 'A07531', 'A07548', 'A07549', 'A07551', 'A07552', 'A07554', 'A07594', 'A07831', 'A07920', 'A08085', 'A08087', 'A08090', 'A08105', 'A08110', 'A08306', 'A08332', 'A08430', 'A08539', 'A08570', 'A08582', 'A08584', 'A09051', 'A09178', 'A09289', 'A09554', 'A09559', 'A09561', 'A09562', 'A09563', 'A09864', 'A09897', 'A10503', 'A10587', 'A10752', 'A11585', 'A11644', 'A13218', 'A13742', 'A13912', 'A13948', 'A14202', 'A14624', 'A16189', 'A17891', 'A19325', 'A19758', 'A21094', 'A22005', 'A22010', 'A22015', 'A22025', 'A22067', 'A22068', 'A22075', 'A22081', 'A22083', 'A22090', 'A22110', 'A22122', 'A22142', 'A22151', 'A22156', 'A22161', 'A22180', 'A22181', 'A22183', 'A22186', 'A22204', 'A22208', 'A22217', 'A22287', 'A22294', 'A22306', 'A22388', 'A22392', 'A22396', 'A22436', 'A22440', 'A22441', 'A22444', 'A22479', 'A22502', 'A22508', 'A22532', 'A22536', 'A22573', 'A22696', 'A22705', 'A22706', 'A22748', 'A22749', 'A23570', 'A34354', 'A37557', 'A68562', 'A68706', 'A68818', 'A69339', 'A69340', 'A69349', 'A72336', 'A72554', 'A72783', 'A72812', 'A72884', 'A73114', 'A73131', 'A73138', 'A73156', 'A73201', 'A73979', 'A73985', 'A73990', 'A74681', 'A75963', 'A77923', 'A79060', 'A80308', 'A84935', 'A86519', 'A95552', 'A96414', 'B00466', 'B00559', 'B00623', 'B00849', 'B01022', 'B02947', 'B07949', 'B08156', 'B08204']
supervisionSet.extend(additional)
missing = ['A96414', 'B00466', 'B00559', 'B00623', 'B00849', 'B01022', 'B02947', 'B07949', 'B08156', 'B08204']
featuresDict = {}

search = levant.copy()
search.extend(eic)
search.extend(virginia)
search.extend(keyTerms)
search.extend(entities)
search = list(set(search))
searchStr = '|'.join(search)

texts1 = getTexts('/srv/data/targetCorpusSTOP/original')
texts2 = getTexts('/srv/data/targetCorpusSTOP/additional')
textInfo = texts1|texts2
print(f'Total number of texts in directory is {len(textInfo)}')
print(f'Will process {len(supervisionSet)}')
progress = 0
for idx, TCPID in enumerate(meta['id']):
        TCPID = TCPID.strip()
        if TCPID in missing: 
                featuresDict[TCPID] = []
                '''check text'''
                inText = re.findall(searchStr,textInfo[TCPID])
                featuresDict[TCPID].extend(inText)
                '''author column'''
                authors = meta['author'][idx]
                authors = authors.split(';')
                for auth in authors: featuresDict[TCPID].append(auth)
                progress+= 1
                if not progress % 100: print(progress)
print(progress)
for TCPID in featuresDict.keys():
        outfile.write(TCPID + ': '+ ' '.join(featuresDict[TCPID])+'\n')
