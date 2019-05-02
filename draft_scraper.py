from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url_template = "http://www.basketball-reference.com/draft/NBA_{year}.html"
draft_df = pd.DataFrame()
for year in range(2008, 2019):  # for each year
    url = url_template.format(year=year)  # get the url
    
    html = urlopen(url)  # get the html
    soup = BeautifulSoup(html, 'html5lib') # create our BS object
    

    # get our player data
    data_rows = soup.findAll('tr')[2:] 
    player_data = [[td.getText() for td in data_rows[i].findAll('td')]
                for i in range(len(data_rows))]
    column_headers = ['Pk', 'Tm', 'Player', 'College', 'Yrs', 'G', 'MP', 'PTS', 'TRB',
       'AST', 'FG_Perc', '3P_Perc', 'FT_Perc', 'MP_per_G', 'PTS_per_G',
       'TRB_per_G', 'AST_per_G', 'WS', 'WS_per_48', 'BPM', 'VORP']
    len(column_headers)
    # Turn yearly data into a DatFrame
    year_df = pd.DataFrame(player_data, columns = column_headers)
    # create and insert the Draft_Yr column
    year_df.insert(0, 'Draft_Yr', year)
    
    # Append to the big dataframe
    draft_df = draft_df.append(year_df, ignore_index=True)
draft_df.head()
draft_df.tail()
draft_df = draft_df.convert_objects(convert_numeric=True)

# Get rid of the rows full of null values
draft_df = draft_df[draft_df.Player.notnull()]

# Replace NaNs with 0s
draft_df = draft_df.fillna(0)

# Rename Columns
draft_df.rename(columns={'WS/48':'WS_per_48'}, inplace=True)
# Change % symbol
draft_df.columns = draft_df.columns.str.replace('%', '_Perc')
# Add per_G to per game stats
draft_df.columns.values[15:19] = [draft_df.columns.values[15:19][col] + 
                                  "_per_G" for col in range(4)]

# Changing the Data Types to int
draft_df.loc[:,'Yrs':'AST'] = draft_df.loc[:,'Yrs':'AST'].astype(int)

# Delete the 'Rk' column
draft_df['Pk'] = draft_df['Pk'].astype(int) # change Pk to int

draft_df.dtypes
draft_df.isnull().sum()
draft_df.to_csv("draft_data.csv")
