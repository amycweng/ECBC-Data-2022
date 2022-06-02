import pandas as pd 
import re 
import os

'''
STAGE II FUNCTIONS 
'''
def filterDate(dateColumn):
    '''
    This function is for Stage II filtering to find texts within our time period, 1580-1640. 
    It takes the date column entry for a text in a CSV file and returns a tuple: 
        - (False,0) for a text that is not within our range OR has an unknown date
        - (True, date) for a text that is dated within our time period  
    '''
    estimates = re.search('between',dateColumn)
    if estimates != None:
        dateRange = re.findall(r'\d{4}',dateColumn)
        # currently, this only looks at the START date in the estimated range 
        date = int(dateRange[0]) 
    elif dateColumn == 'Date Unknown':
        return (False,0)
    else:
        date = int(dateColumn)
    if date in range(1580,1640+1):
        return(True,date)
    else:
        return(False,0)