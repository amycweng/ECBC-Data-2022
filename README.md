# Ethical Consumption Before Capitalism Data+ Year 3

We combine close and distant reading techniques to evaluate the metaphorical and ethical language surrounding three major English trading companies from 1580 to 1641. These are the English East India, Levant, and Virginia companies. We include 1641 because some English texts were still dated using the Julian calendar instead of the Gregorian calendar, so some dates can be one year off. More than just the exchange of goods, we explore the early modern documentation of how these companies facilitated cultural, religious, political, and economic affairs both peacefully and violently, as well as how authors used various arguments to justify England's colonial aspirations abroad. 

## We build upon the work of previous Duke University Data+ and Bass Connections projects:   

Data+ Year 1 (2020) - For love of greed: tracing the early history of consumer culture 
https://bigdata.duke.edu/projects/love-greed-tracing-early-history-consumer-culture 

Data+ Year 2 (2021) - Ethical Consumption Before Capitalism 
https://bigdata.duke.edu/projects/ethical-consumption-capitalism
    Team Website: https://sites.google.com/view/ethical-consumption-before-cap/home 

Bass Connections (2021-2022) - Ethical Consumption Before Capitalism
https://bassconnections.duke.edu/project-teams/ethical-consumption-capitalism-2021-2022
    Team Website: https://sites.duke.edu/ecbc

## Common terms defined:
- **ECBC**: Ethical Consumption Before Capitalism
- **EEBO**: Early English Books Online
- **EIC**: English East India Company
- **TCP**: Text Creation Partnership (https://textcreationpartnership.org)
- **EP**: EarlyPrint (https://earlyprint.org)  
- **VEP**: Visualizing Early Print (https://graphics.cs.wisc.edu/WP/vep/)

## Folder & File Descriptions 

- *company.py*: Filters through body text and authors of EP files to generate an expanded corpus related to all three companies
- *functions.py*: Custom utility functions, e.g., functions for removing stopwords, extracting content from plain text files, and processing keywords
- *network.ipynb*: Social network visualization based on TCP metadata
- *select.py*: Code that helps copy relevant files into other folders. 
- *supervised.ipynb*: Supervised text classification with logistic regression (see file for citations)
- *topics.py*: LDA topic modeling w/ Gensim to generate 'topic words' for individual texts. Also generates word clouds of the topic words 
- *unsupervised.ipynb*: Unsupervised k-means clustering and visualization (see file for citations)
*vocab.ipynb*: TF-IDF analysis and visualization, term frequency word cloud generation and bigram models
- *wordembedbigram.ipynb*: Word embeddings w/ Word2Vec. PCA + heatmap visualizations  
- *characterCleaner.py*: Preprocessing of XML and TXT files from VEP-Pipeline (https://github.com/uwgraphics/VEP-pipeline/blob/master/characterCleaner.py)
- *conversion_dict.py*: Dictionary of ASCII equivalents of unicode characters in TCP from VEP Pipeline (https://github.com/uwgraphics/VEP-pipeline/blob/master/conversion_dict.py)

## Text_Files (Folder)
- *eebo_phase1_IDs_and_dates*: TCP Phase I text IDs and dates 
- *EEBO_Phase2_IDs_and_dates*: TCP Phase II text IDs and dates 
- *keywords*: Relevant keywords from TCP 
- *levantPeople*: People associated with the Levant Co. 
- *notes*: Miscellaneous notes 
- *terms*: Key commodities and ethical language
- *VirginiaCompanyTexts*: Texts written by men who are associated with or write about the Virginia Company 

### catalogue (Text_Files Sub-folder)
- *dateRangeTextNames*: All TCP texts that have ranged dates. 
- *EPmissing*: All TCP texts that are missing from the EP text library. 
- *EPunderscores*: All TCP texts that have been partitioned into several EP files 
- *relevant*: All TCP texts within our relevant time period 
- *relevantEPmissingPhaseI*: All TCP Phase I texts missing from the EP text library that are dated within 1580-1641, including texts with ranged dates. 
- *relevantEPmissingPhaseII*: All TCP Phase II texts missing from the EP text library that are dated within 1580-1641, including texts with ranged dates. 

### stageTwoFiles (Text_Files Sub-folder)
- *legomenaEPTUning.txt*: Words used only once in our EP tuning texts
- *mostcommon.txt*: Words and frequencies sorted by descending frequency from the EP corpus
- *nounsEPTuning.txt*: All nouns and their frequencies in each text from the EP tuning set
- *people*: Relevant people associated with the three companies 
- *special*: Words with special characters that occur in relevant EP texts.
- *specialEPTuning.txt*: Words with special characters that occur in our EP tuning set of 26 files


## Image_Files (Folder)
- *barTextsYear*: Bar graph of texts within 1580-1641, including texts with ranged dates 
- *dateRangeTexts*: The distribution of texts with ranged dates 
- *1600-1610 authors.html*: Author network visualization for TCP texts dating from 1600 to 1610 
- *keywords in 1600-1610 TCP texts*: Word cloud of the common keywords in TCP metadata from 1600-1610 
- *1600-1610 texts per year*: Bar graph for text counts in one decade 
- *virginiaAuthorsGrouped.html*: Author network visualization for spreadsheet_Virginia set based on groups generated by k-means clustering 

## stageOne (Folder)
- *catalog.ipynb*: Catalogs existing and missing EP & TCP files. Converts the relevant missing TCP files into csvs. Filters TCP texts by keywords and dates. 
- *dates.ipynb*: Extracts and converts date information from XML and TXT files. For date ranges, we simply examine the start date.  
- *metadata.py*: Takes in a folder of individual TCP XML files and writes the desired metadata into a separate CSV file. 
- *text.py*: Extracts either the text bodies or dedications from a specified EP folder

## stageTwo (Folder)
- *corrections.py*: Selective correction of words w/ missing characters, as well as lemmatization 
- *dots.txt*: List of selective correction of words w/ missing characters, in a text file
- *lemmas.txt*: List of selective standardization of important keywords, in a text file
- *notes.py*: Lists of interesting terms we came across, alongside groupings of related words and concepts
- *people.py*: Lists of key entities, along with their entire EP author tags and those that fall outside our date range
- *replace.ipynb*: Takes in a folder of texts, and produces an output folder of standardized, lemmatized and corrected words.
- *words.py*: Extracts and provides a list of all special characters, legomena or nouns (as needed) and their frequencies