URLlist = []
PagesFound = 0
PagesScraped = 0


import requests
from bs4 import BeautifulSoup

Req = requests.get('https://www.bbc.co.uk/news/entertainment-arts-46452747') #this is the webpage I scraped
Soup = BeautifulSoup(Req.text,'html.parser')



for link in Soup.find_all('a', {'class': 'unit__link-wrapper'}): #I scraped the pages that came up as a 'suggested article' on the given webpage
    href = 'https://www.bb' 'c.co.uk' + link.get('href')
    if href not in URLlist:
            URLlist = URLlist + [href]
            PagesFound += 1
PagesScraped += 1

while len(URLlist) < 100 and PagesScraped < PagesFound: #I capped the loop so only 100 new pages are found, also it was necessary to impose PagesScraped < PagesFound otherwise wed get an issue with the list.
    Req = requests.get(URLlist[PagesScraped])
    Soup = BeautifulSoup(Req.text, 'html.parser')
    for link in Soup.find_all('a', {'class': 'unit__link-wrapper'}):

        if 'ww.bbc.co.uk' not in link.get('href'):
            href = 'https://www.bb' 'c.co.uk' + link.get('href') #I got a few bad links that werent from the bbc and these commands are to filter them out
        else:
            href = link.get('href')

        if href not in URLlist and 'news' in href:
            URLlist = URLlist + [href]
            PagesFound += 1   #I then added the original webpages found to an empty list and discarded duplicates
    PagesScraped += 1
    #print(URLlist)
    #print(len(URLlist))
    #print(PagesScraped)




print(URLlist)
print(len(URLlist))
print(PagesScraped)