# Ethical Consumption Before Capitalism Data+ Year 3

We combine close and distant reading techniques to evaluate the metaphorical and ethical language surrounding three major English trading companies from 1580 to 1641. These are the English East India, Levant, and Virginia companies. We include 1641 because these English texts were dated using the Julian calendar instead of the Gregorian calendar, so some dates can be one year off. More than just the exchange of goods, we explore the early modern documentation of how these companies facilitated cultural, religious, political, and economic affairs both peacefully and violently, as well as how authors used various arguments to justify England's colonial aspirations abroad. 

## We build upon the work of previous Duke University Data+ and Bass Connections projects:   

Data+ Year 1 (2020) - For love of greed: tracing the early history of consumer culture 
https://bigdata.duke.edu/projects/love-greed-tracing-early-history-consumer-culture 

Data+ Year 2 (2021) - Ethical Consumption Before Capitalism 
https://bigdata.duke.edu/projects/ethical-consumption-capitalism
    Team Website: https://sites.google.com/view/ethical-consumption-before-cap/home 

Bass Connections (2021-2022) - Ethical Consumption Before Capitalism
https://bassconnections.duke.edu/project-teams/ethical-consumption-capitalism-2021-2022
    Team Website: https://bassconnections.duke.edu/project-teams/ethical-consumption-capitalism-2021-2022 

## Common terms defined:
- **ECBC**: Ethical Consumption Before Capitalism
- **EEBO**: Early English Books Online
- **EIC**: English East India Company
- **TCP**: Text Creation Partnership (https://textcreationpartnership.org)
- **EP**: EarlyPrint (https://earlyprint.org)  
- **VEP**: Visualizing Early Print (https://graphics.cs.wisc.edu/WP/vep/)

## File Descriptions
- *stageOne.py*: Stage I processing, i.e., Relevant XML -> CSV Conversion. 'Relevant' means within our date range. 
- *stageTwo.py*: Stage II processing, i.e., Additional Orthographic and Character Conversion 
- *dates.ipynb*: Extracts and converts date information from XML and TXT files. For date ranges, we simply examine the start date.  
- *catalog.ipynb*: Catalogs existing and missing EP & TCP files. Converts the relevant missing TCP files into csvs. 
- *characterCleaner.py*: Preprocessing of XML and TXT files from VEP-Pipeline (https://github.com/uwgraphics/VEP-pipeline/blob/master/characterCleaner.py)
- *conversion_dict.py*: Dictionary of ASCII equivalents of unicode characters in TCP from VEP Pipeline (https://github.com/uwgraphics/VEP-pipeline/blob/master/conversion_dict.py)

## Text_Files (Folder)
- *dateRangeTextNames*: All TCP texts that have ranged dates. 
- *EPmissing*: All TCP texts that are missing from the EP text library. 
- *EPunderscores.txt*: All TCP texts that have been partitioned into several EP files 
- *relevant.txt*: All TCP texts within our relevant time period 
- *relevantEPmissingPhaseI*: All TCP Phase I texts missing from the EP text library that are dated within 1580-1641, including texts with ranged dates. 
- *relevantEPmissingPhaseII*: All TCP Phase II texts missing from the EP text library that are dated within 1580-1641, including texts with ranged dates. 
- *special.txt*: Words with special characters that occur in relevant EP texts. 
- *xml tags*: Miscellaneous notes 

## Image_Files (Folder)
- *barTextsYear*: Bar graph of texts within 1580-1641, including texts with ranged dates 
- *dateRangeTexts*: The distribution of texts with ranged dates 
