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

noresult = ['john wrothe', 'erasmus ferrar', 'tristram conyam', 'john posar',
            'lott peere','robert sturmy',"laurent d'arvieux",'monsieur de thevenot',
            'thomas dallam', 'john prory',]