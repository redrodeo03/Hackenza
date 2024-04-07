# Hackenza - 2024 - https://hackenza.streamlit.app/
### *Project Overview*

This project aims to create a ranking system for Computer Science (CS) institutions in India, focusing on research output relevant to the Indian academic landscape.
We address the limitations of existing ranking systems, such as CSRankings (https://csrankings.org/) for the year 2023, which prioritize expensive, international conferences often inaccessible to Indian researchers.


### *Target Institutions*

The initial focus will be on premier Indian CS institutions, including:
Indian Institutes of Technology (IITs)
Birla Institute of Technology and Science (BITS) campuses
National Institutes of Technology (NITs)

For the purpose of this demo, the only colleges considered are:
Indian Institute of Technology Bombay
Indian Institute of Technology Kanpur
Indian Institute of Technology Kharagpur
Indian Institute of Technology Delhi
Indian Institute of Technology Madras
Indian Institute of Technology Guwahati
Indian Institute of Technology (BHU) Varanasi
Indian Institute of Technology Hyderabad
Indian Institute of Technology Gandhinagar
BITS KK Birla Goa Campus
BITS Pilani
BITS Hyderabad
NIT Rourkela
NIT Surathkal
NIT Tiruchirapalli

### *Methodology*

#### *Faculty Data Scraping:*

A Selenium script was used to extract faculty names from the CS department websites of IITs and NITs. These extracted names were then updated to the names as would appear on Google scholar for these professors. This was done by running an organic google scholar search using scholarly with the names we extracted using selenium. Giving us our final faculty database.

#### *Publication Data Acquisition:*
The 2023 DBLP dataset for all computer science journals and proceedings (https://dblp.org/) was downloaded in XML format.
Only publications under type Articles, proceedings, and in-proceedings were extracted and relevant features (title, authors, year, book title, journal) retained.

#### *High-Quality Publication Identification*
Names of Q1 journals were extracted from https://www.scimagojr.com/journalrank.php. Since the names extracted from DBLP database were in iso4 format we had to convert these to iso4 format as well.

A/A* conferences were identified from http://portal.core.edu.au/conf-ranks/.

#### *Data Refinement:*

The publication data extracted from DBLP was filtered to include papers of only Q1 journals and A*/A* conferences.
This data will be further filtered to include only those publications that were authored by the faculty in our database.

#### *Ranking and Visualization:*

After we had the list of these publications ready, we found out how many authors have co-authored a paper and then assigned partial credit to all the co-authors.
Total credit for a paper = 1.
Credit to 1 author for a paper co-authored by n people is 1/n.
The partial credits for all papers for each author are summed to get the credits for that author.
University credit is the summation of all the partial credits of its professors.
Universities will be ranked based on their university credit.
The rankings will be displayed on a user-friendly front end.

### *Research Areas*
A potential solution on how to categorize the research areas has been implemented by us. To ensure we follow the same research areas given by CSRankings we used Gemini (LLM) api calls and asked it to categorize based on the CSRanking categories. 

### *Future Scope*
1. Including the classification of research papers into different computer science research areas.
2. Improve the ranking formula by doing this segmentation and adjusting the formula as on csrankings.org
3. The pipeline is set in such a way that this can easily be expanded to other IIT's and NIT's and other esteemed organizations of India. The data dump we have created is crucial for the same.

### Data Dump Link - Contains relevant subset of DBLP Database Dump in 2023
(https://drive.google.com/drive/folders/1XARQJLkhXWKr1SEXg1ommHUJgFARaUNJ?usp=drive_link)
