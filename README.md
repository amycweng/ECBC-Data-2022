# Ethical Consumption Before Capitalism Data+ Year 3

We combine close and distant reading techniques to evaluate the ethical, economic, and medical language surrounding tobacco and opium from 1580 to 1641, a time period marked by the rise of mercantile trade and monopolies. Our computational work includes (1) text and metadata extraction, (2) selective spelling correction and standardization, (3) social network visualization of n-grams with feature engineering and k-means clustering, (4) visualization of cosine similarities of select word-pairs over time, (5) part of speech visualizations, and (6) an R Shiny app to showcase our work. We include 1641 because some English texts were still dated using the Julian calendar instead of the Gregorian calendar, so some dates can be one year off. 

View our poster here: https://drive.google.com/file/d/1xIM-4AAsxqGlntNn_HXnPJBhezGZqU-B/preview

**A comment on workflow**: All four of us worked in a shared folder on a virtual machine, and usually one of us pushed to the Git repo for all our work. Moreover, since we often collaborate on the files, we have chosen not to provide authorial details for individual files. If you have any questions, feel free to reach out to any of us. 

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
- **TCP**: Text Creation Partnership (https://textcreationpartnership.org)
- **EP**: EarlyPrint (https://earlyprint.org)  
- **VEP**: Visualizing Early Print (https://graphics.cs.wisc.edu/WP/vep/)

## generalCode (Folder)
- *catalog.ipynb*: Catalogs existing and missing EP & TCP files. Converts the relevant missing TCP files into csvs. Filters TCP texts by keywords and dates. Creates word clouds for keywords metadata.
- *company.py*: Filters through body text and authors of EP files to generate an expanded corpus related to all three companies
- *select.py*: Code that helps copy relevant files into other folders. 
- *vocab.ipynb*: TF-IDF analysis and visualization, term frequency word cloud generation and bigram models

## stageOne (Folder)
- *dates.ipynb*: Extracts and converts date information from XML and TXT files. For date ranges, we simply examine the start date.  
- *metadata.py*: Takes in a folder of individual TCP XML files and writes the desired metadata into a separate CSV file. 
- *text.py*: Extracts either the text bodies or dedications from a specified EP folder

## stageTwo (Folder)
- *clean.ipynb*: Extract body texts, clean special characters, and remove stopwords  
- *corrections.py*: Selective correction dictionary of words w/ missing characters, as well as lemmatization 
- *dots.txt*: List of selective correction of words w/ missing characters, in a text file
- *lemmas.txt*: List of selective standardization of important keywords, in a text file
- *notes.py*: Lists of interesting terms we came across, alongside groupings of related words and concepts
- *people.py*: Lists of key entities, along with their entire EP author tags and those that fall outside our date range
- *replace.ipynb*: Takes in a folder of texts, and produces an output folder of standardized, lemmatized and corrected words.
- *words.py*: Extracts and provides a list of all special characters, legomena or nouns (as needed) and their frequencies

## network (Folder)
- *allfeatures.txt*: Instances of general key terms that occur in the 10k relevant body texts ('relevant' means within our time period)
- *allopiumgrams.txt*: All n-grams containing opium and four other associated terms (opiate, poppy, poppey, laudanum) in relevant texts 
- *allTobaccoDrug.txt*: Instances of drug or tobacco terms that occur in relevant texts 
- *alltobaccograms.txt*: All n-grams containing tobacco in relevant texts
- *alltopics.txt*: All topic words for relevant texts 
- *topics.py*: LDA topic modeling w/ Gensim to generate 'topic words' for individual texts. Also generates word clouds of the topic words 
- *categories.py*: Catalog instances of key terms that occur in body texts 
- *finalTexts.py*: Lists of TCP IDs for tobacco and opium texts by time period 
- *ngrams.ipynb*: Extracts tobacco and opium bigrams and trigrams from body texts
- *topics.ipynb*: LDA topic modeling w/ Gensim to generate 'topic words' for individual texts. Also generates word clouds of the topic words 

### opium (network Sub-folder)
- *opiumClustering.ipynb*: Unsupervised k-means clustering w/ feature engineering and visualization. Print out clustering documentation in HTML text format.  
- *opiumNetwork.ipynb*: Author network with n-gram edges using pyvis.network package. Nodes are colored using results from clustering. Edges are colored based on n-gram groupings. Print out text and n-gram information in HTML text format. 
- *opiumNGramGroupings.py*: Lists of opium n-gram groups 

### tobacco (network Sub-folder)
- *tobaccoClustering.ipynb*: Unsupervised k-means clustering w/ feature engineering and visualization 
- *tobaccoNetwork.ipynb*: Author network with n-gram edges using pyvis.network package. Nodes are colored using results from clustering. Edges are colored based on n-gram groupings. Print out text and n-gram information in HTML text format. 
- *tobaccoNgramGroups.py*: Lists of tobacco n-gram groups 

## wordEmbeddings (Folder)
- *embed.ipynb*: Word embeddings w/ Word2Vec Skip-Gram model. PCA + heatmap visualizations  
- *overtime.ipynb*: Examine cosine similarities of word-pairs over time 
- *sevenTimePeriods.py*: Lists of TCP IDs grouped by time period 

## posVisualizations
- *wordGraph.py* contains the flack backend for the webpage
- *cleaningFunctions* containes the functions for extracting and cleaning the text and pos tags from EP
- *static contains the css, img, and javascript files the webpage uses
- *database.ipynb* is the notebook that creates *both.db* which is used store al the pos data

## shinyapp (Folder)
- *app.R*: Codes for the entire shiny app, including UI and server
- *data+.Rproj*, *.Rhistory*, *.RData*: Default files for the shiny app project

## rsconnect (shinyapp Sub-folder)
- *dataplus.dcf* : File to publish shiny app on web

## www (shinyapp Sub-folder)
- *tobaccoPeriod(.)Network.html* : social network of time period (.) for texts related to tobacco
- *opiumPer(.)Network.html* : social network of time period (.) for texts related to opium
- *tobaccoPer(.)doc.html* : documentation of social network of time period (.) for texts related to tobacco
- *opiumPer(.)doc.html* : documentation of social network of time period (.) for texts related to opium
- *tobaccosideDoc.html* : general documentation of corpus and n-grams of texts related to tobacco
- *opiumSideDoc.html* : general documentation of corpus and n-grams of texts related to opium
- *tobaccohist.png* : histogram of number of texts related to tobacco vs. time period
- *opiumhist.png* : histogram of number of texts related to opium vs. time period
- *tobaccoper(.)cluster.png* : PCA graph of clusters of time period (.) for texts related to tobacco
- *opiumPer(.)Cluster.png* : PCA graph of clusters of time period (.) for texts related to opium
- *tob(n;v;adj;adv).png* : 10 most common words around tobacco across time, separated by part of speech
- *op(n;v;adj;adv).png* : 10 most common words around opium across time, separated by part of speech
- *(colonialism; custom; ethnicities; gender; intoxicate; medical; moral; religion)Tobacco.png* : chronological changes of cosine similarity scores between each desired word and tobacco
- *(colonialism; custom; ethnicities; gender; intoxicate; medical; moral; religion)Opium.png* : chronological changes of cosine similarity scores between each desired word and opium

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
- *poster.png*: Final project poster 

