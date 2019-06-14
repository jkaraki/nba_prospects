import requests
import lxml.html as lh
import pandas as pd


from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse

from time import sleep
from multiprocessing import Pool

import html.parser
import time


def scrape_first(player_links):
    player_data_02 = []
    start = time.time()
    url_template = "http://www.barttorvik.com/{player}"
    for count in range ( 0,len(player_links)):
        url = url_template.format(player=player_links[count])     #Create a handle, page, to handle the contents of the website
        page = requests.get(url)
        #Store the contents of the website under doc
        doc = lh.fromstring(page.content)
        #Parse data that are stored between <tr>..</tr> of HTML
        tr_elements = doc.xpath('//tr')  
        #Create empty list
        col=['Yr','Cls','Ht','Player','Team','Conf.',
        'G','Min%', 'PRPG!', 'ORtg', 'Usg', 'eFG', 'TS', 'OR',
        'DR','Ast', 'TO','Blk','Stl', 'FTR','FT_raw','FT_pct',
        '2P_raw', '2P_pct','3P_raw', '3P_pct' ]
        ind = tr_elements[1]
        test_row = []
        leng = 0 
        for t in ind.iterchildren():
            data=t.text_content() 
            test_row.append(data)
        print(count, "...", test_row[3], "...", test_row[4], "...")


        if test_row[0] == '2009':
            ############
            # create an empty list to hold all the data
            #player_data_02.append(col)
            for j in range(1,5):
                #T is our j'th row
                T=tr_elements[j]
                

                
                #i is the index of our column
                i=0
                player_row = []
                #Iterate through each element of the row
                for t in T.iterchildren():
                    data=t.text_content() 
                    #Check if row is empty
                    if i>0:
                    #Convert any numerical value to integers
                        try:
                            data=int(data)
                        except:
                            pass
                    #Append the data to the empty list of the i'th column
                    player_row.append(data)
                    #Increment i for the next column
                    i+=1
                if j>1:
                    player_row= ["","","", ""]+player_row
                player_data_02.append(player_row) 
    end = time.time()
    print(end - start)
    return player_data_02 




#########################################################
####Fetching all URLS for players from a certain year####
#########################################################

my_string = "Texas A&M Corpus Chris,Abilene Christian,Air Force,Akron,Alabama,Alabama A&M,Alabama St.,Albany,Alcorn St.,American,Appalachian St.,Arizona,Arizona St.,Arkansas Pine Bluff,Arkansas,Arkansas St.,Army,Auburn,Austin Peay,Ball St.,Baylor,Belmont,Bethune Cookman,Binghamton,Boise St.,Boston College,Boston University,Bowling Green,Bradley,Brown,Bryant,Bucknell,Buffalo,Butler,BYU,Cal Poly,Cal St. Fullerton,California,Cal Baptist,Campbell,Canisius,Central Arkansas,Central Connecticut,Central Michigan,Charleston Southern,Charlotte,Chattanooga,Chicago St.,Cincinnati,Clemson,Cleveland St.,Coastal Carolina,College of Charleston,Colgate,Colorado,Colorado St.,Columbia,Coppin St.,Cornell,Creighton,Cal St. Bakersfield,Cal St. Northridge,Dartmouth,Davidson,Dayton,Delaware,Delaware St.,Denver,DePaul,Detroit,Drake,Drexel,Duke,Duquesne,East Carolina,Eastern Illinois,Eastern Kentucky,Eastern Michigan,Eastern Washington,Elon,East Tennessee St.,Evansville,Fairfield,Fairleigh Dickinson,Florida Gulf Coast,FIU,Florida Atlantic,Florida,Florida A&M,Florida St.,Fordham,Fort Wayne,Fresno St.,Furman,Georgia Southern,Gardner Webb,George Mason,George Washington,Georgetown,Georgia,Georgia St.,Georgia Tech,Gonzaga,Grambling St.,Grand Canyon,Green Bay,Hampton,Hartford,Harvard,Hawaii,High Point,Hofstra,Holy Cross,Houston,Houston Baptist,Howard,Idaho,Idaho St.,Illinois Chicago,Illinois,Illinois St.,Incarnate Word,Indiana,Indiana St.,Iona,Iowa,Iowa St.,IUPUI,Jackson St.,Jacksonville,Jacksonville St.,James Madison,Kansas,Kansas St.,Kennesaw St.,Kent St.,Kentucky,La Salle,Louisiana Monroe,Lafayette,Lamar,Lehigh,Liberty,Lipscomb,Little Rock,LIU Brooklyn,Long Beach St.,Longwood,Louisiana Lafayette,Louisiana Tech,Louisville,Loyola Chicago,Loyola MD,Loyola Marymount,LSU,Maine,Manhattan,Marist,Marquette,Marshall,Maryland,Massachusetts,McNeese St.,Memphis,Mercer,Miami FL,Miami OH,Michigan,Michigan St.,Middle Tennessee,Milwaukee,Minnesota,Mississippi St.,Mississippi Valley St.,Missouri,Missouri St.,Monmouth,Montana,Montana St.,Morehead St.,Morgan St.,Mount St. Mary's,Murray St.,North Carolina A&T,North Carolina Central,Navy,Nebraska,Nevada,New Hampshire,New Mexico,New Mexico St.,New Orleans,Niagara,Nicholls St.,NJIT,Norfolk St.,North Alabama,North Carolina,North Carolina St.,North Dakota,North Dakota St.,North Florida,North Texas,Northeastern,Northern Arizona,Northern Colorado,Northern Illinois,Northern Kentucky,Northwestern,Northwestern St.,Notre Dame,Oakland,Ohio,Ohio St.,Oklahoma,Oklahoma St.,Old Dominion,Mississippi,Nebraska Omaha,Oral Roberts,Oregon,Oregon St.,Pacific,Penn,Penn St.,Pepperdine,Pittsburgh,Portland,Portland St.,Prairie View A&M,Presbyterian,Princeton,Providence,Purdue,Quinnipiac,Radford,Rhode Island,Rice,Richmond,Rider,Robert Morris,Rutgers,Sacramento St.,Sacred Heart,St. Francis PA,Saint Joseph's,Saint Louis,Saint Mary's,Saint Peter's,Sam Houston St.,Samford,San Diego,San Diego St.,San Francisco,San Jose St.,Santa Clara,Savannah St.,Seattle,Seton Hall,Stephen F. Austin,Siena,SIU Edwardsville,SMU,South Alabama,South Carolina,South Carolina St.,South Dakota,South Dakota St.,South Florida,Southeast Missouri St.,Southeastern Louisiana,USC,Southern Illinois,Southern Miss,Southern,Southern Utah,St. Bonaventure,St. Francis NY,St. John's,Stanford,Stetson,Stony Brook,Syracuse,TCU,Temple,Tennessee,Tennessee St.,Tennessee Tech,Texas,Texas A&M,Texas Southern,Texas St.,Texas Tech,The Citadel,Toledo,Towson,Troy,Tulane,Tulsa,UAB,UC Davis,UC Irvine,UC Riverside,UC Santa Barbara,UCF,UCLA,Connecticut,UMass Lowell,UMBC,Maryland Eastern Shore,UMKC,UNC Asheville,UNC Greensboro,UNC Wilmington,Northern Iowa,UNLV,USC Upstate,UT Arlington,Tennessee Martin,Utah,Utah St.,Utah Valley,UTEP,UT Rio Grande Valley,UTSA,Valparaiso,Vanderbilt,VCU,Vermont,Villanova,Virginia,Virginia Tech,VMI,Wagner,Wake Forest,Washington,Washington St.,Weber St.,West Virginia,Western Carolina,Western Illinois,Western Kentucky,Western Michigan,Wichita St.,William & Mary,Winthrop,Wisconsin,Wofford,Wright St.,Wyoming,Xavier,Yale,Youngstown St."
my_list = my_string.split(",")
player_links=[]
url_template_team = "http://www.barttorvik.com/team.php?team={parsed}&year=2009"
count = 0
print(2009)
for team in my_list:
    parsed = urllib.parse.quote_plus(team)
    print(count, "...", team)
    count+=1
    url = url_template_team.format(parsed=parsed)
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    links_with_text = []
    for a in soup.find_all('a', href=True): 
        if a.text: 
            links_with_text.append(a['href'])
        
    for b in links_with_text:
        if 'playerstat.php?year=2009&p' == b[:26]:
            player_links.append(b)


import csv
with open('player_urls_2009', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(player_links)

##########################################
####Fetching player data from each URL####
##########################################







new_data = scrape_first(player_links)
merged_data = new_data

col= ['Yr','Cls','Ht','Player','Team','Conf.',
        'G','Min%', 'PRPG!', 'ORtg', 'Usg', 'eFG', 'TS', 'OR',
        'DR','Ast', 'TO','Blk','Stl', 'FTR','FT_raw','FT_pct',
        '2P_raw', '2P_pct','3P_raw', '3P_pct' ]
df = pd.DataFrame(merged_data)

df.to_csv('player_data_2009.csv')








#for player in player_links:



