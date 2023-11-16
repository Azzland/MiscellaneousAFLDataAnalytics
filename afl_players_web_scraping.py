import bs4 as bs
import requests
import pandas as pd
import numpy as np

file_debug = open('C:/Users/Azzla/Downloads/code_debug3.txt', 'w')
output_directory = 'C:/Users/Azzla/Downloads/AFL/'
Adelaide = 'https://afltables.com/afl/stats/alltime/adelaide.html'
BrisbaneLions = 'https://afltables.com/afl/stats/alltime/brisbanel.html'
Carlton = 'https://afltables.com/afl/stats/alltime/carlton.html'
Collingwood = 'https://afltables.com/afl/stats/alltime/collingwood.html'
Essendon = 'https://afltables.com/afl/stats/alltime/essendon.html'
Fremantle = 'https://afltables.com/afl/stats/alltime/fremantle.html'
Geelong = 'https://afltables.com/afl/stats/alltime/geelong.html'
GoldCoast = 'https://afltables.com/afl/stats/alltime/goldcoast.html'
GreaterWesternSydney = 'https://afltables.com/afl/stats/alltime/gws.html'
Hawthorn = 'https://afltables.com/afl/stats/alltime/hawthorn.html'
Melbourne = 'https://afltables.com/afl/stats/alltime/melbourne.html'
NorthMelbourne = 'https://afltables.com/afl/stats/alltime/kangaroos.html'
PortAdelaide = 'https://afltables.com/afl/stats/alltime/padelaide.html'
Richmond = 'https://afltables.com/afl/stats/alltime/richmond.html'
StKilda = 'https://afltables.com/afl/stats/alltime/stkilda.html'
Sydney = 'https://afltables.com/afl/stats/alltime/swans.html'
WestCoast = 'https://afltables.com/afl/stats/alltime/westcoast.html'
WesternBulldogs = 'https://afltables.com/afl/stats/alltime/bullldogs.html'

AllClubsLinks = []
AllClubsLinks.append(Adelaide)
AllClubsLinks.append(BrisbaneLions)
AllClubsLinks.append(Carlton)
AllClubsLinks.append(Collingwood)
AllClubsLinks.append(Essendon)
AllClubsLinks.append(Fremantle)
AllClubsLinks.append(Geelong)
AllClubsLinks.append(GoldCoast)
AllClubsLinks.append(GreaterWesternSydney)
AllClubsLinks.append(Hawthorn)
AllClubsLinks.append(Melbourne)
AllClubsLinks.append(NorthMelbourne)
AllClubsLinks.append(PortAdelaide)
AllClubsLinks.append(Richmond)
AllClubsLinks.append(StKilda)
AllClubsLinks.append(Sydney)
AllClubsLinks.append(WestCoast)
AllClubsLinks.append(WesternBulldogs)

AllClubs = ['Adelaide', 'Brisbane Lions', 'Carlton', 'Collingwood', 'Essendon', 'Fremantle', 'Geelong', 'Gold Coast', 'Greater Western Sydney', 'Hawthorn', 'Melbourne', 'North Melbourne', 'Port Adelaide', 'Richmond', 'St Kilda', 'Sydney', 'West Coast', 'Western Bulldogs']

ClubState = ['SA','QLD','VIC','VIC','VIC','WA','VIC','QLD','NSW','VIC','VIC','VIC','SA','VIC','VIC','VIC','WA','VIC']
for i in range(len(AllClubsLinks)):
    try:
        r = requests.get(AllClubsLinks[i])
        print(str(AllClubs[i]) + ' link successful!')
        soup = bs.BeautifulSoup(r.content, features="html.parser")
        my_list = []
        #df = pd.DataFrame(columns=['Cap','Number','FirstName','LastName','DOB','Height','Weight','Games_WDL','Goals','Seasons','Debut','Last'])
        table = soup.find('table')
        for row in table.tbody.find_all('tr'):    
        # Find all data for each column
            columns = row.find_all('td')
            #print(columns)
            if(len(columns) > 2):
                cap = columns[0].text.strip()
                number = columns[1].text.strip()
                player = columns[2].text.strip()
                player = player.split(', ')
                firstname = player[1]
                lastname = player[0]
                dob = columns[3].text.strip()
                height = columns[4].text.strip()
                weight = columns[5].text.strip()
                games_wdl = columns[6].text.strip()
                goals = columns[7].text.strip()
                seasons = columns[8].text.strip()
                debut = columns[9].text.strip()
                last = columns[10].text.strip()
                array = [cap, number, firstname, lastname, dob, height, weight, games_wdl, goals, seasons, debut, last]
                #print(array)
                write_to_df = {}
                write_to_df['Cap'] = cap
                write_to_df['Number'] = number
                write_to_df['FirstName'] = firstname
                write_to_df['LastName'] = lastname
                write_to_df['DOB'] = dob
                write_to_df['Height'] = height
                write_to_df['Weight'] = weight
                write_to_df['Games_WDL'] = games_wdl
                write_to_df['Goals'] = goals
                write_to_df['Seasons'] = seasons
                write_to_df['Debut'] = debut
                write_to_df['Last'] = last
                write_to_df['Club'] = AllClubs[i]
                write_to_df['State'] = ClubState[i]
                #print(write_to_df)
                my_list.append(write_to_df)
                #print(player)
        df = pd.DataFrame.from_records(my_list)
        df.head()
        df.to_csv(output_directory+str(AllClubs[i])+'.csv')
    except:
        print(str(AllClubs[i]) + ' link NOT successful!')


    
