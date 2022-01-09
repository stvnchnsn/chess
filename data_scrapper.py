from bs4 import BeautifulSoup as bs
import requests
url = 'https://www.pgnmentor.com/files.html'
page = requests.get(url)

soup = bs(page.content, "html.parser")
#print(soup.prettify())
tables = soup.findAll('table')

for i, table in enumerate(tables):
    if  i == 5:
        '''players table'''
        print('Players')
        print(len(table.findAll('a',class_ = 'view',)))
        downloads = table.findAll('a',class_ = 'view',)
        for i, d in enumerate(downloads):
            print(d.text)
        #print(table.findAll('a',class_ = 'view',))
        rows = table.findAll('td')
        player_list = []
        for r in rows:
            if r.text.find("games") > -1:
                if 'View' not in r.text:
                    player_list.append(r.text)
        print(len(player_list))
    if i == 9:
        print('\n\n')
        print('Modern Queen Pawn')
        #print(table.findAll('a',class_ = 'view',))
    if i == 11:
        print('\n\n')
        print('Classical Queen Pawn')
        #print(table.findAll('a',class_ = 'view',))
    if i == 13:
        print('\n\n')
        print('Modern King Pawn')
        #print(table.findAll('a',class_ = 'view',))
    if i == 17:
        print('\n\n')
        print('Flank and Unorthodox')
        #print(table.findAll('a',class_ = 'view',))
    if i == 20:
        print('\n\n')
        print('Tournaments')
        #print(table.findAll('a',class_ = 'view',))
    if i == 21:
        print('\n\n')
        print('Tournaments II')
        #print(table.findAll('a',class_ = 'view',))
    if i ==  23:
        print('\n\n')
        print('Candidates and Interzonals')
        #print(table.findAll('a',class_ = 'view'))
    if i ==  27:
        print('\n\n')
        print('World Championships')
        print(table.findAll('a',class_ = 'view'))
#print(results.prettify())