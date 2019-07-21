import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_player_advanced_stats(year=2014,project_path='/home/mpare/src/nba_shot_quality'):
    '''
        Function to scrape the player advanced stats from basketball reference

        arguments:
        year = year to scrape
        project_path = path of the project directory
    '''
    # URL page we will scraping
    url = "https://www.basketball-reference.com/leagues/NBA_{}_advanced.html".format(year)
    # this is the HTML from the given URL
    html = urlopen(url)
    soup = BeautifulSoup(html)

    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)[1:]
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    # exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
    headers = headers[1:]

    # avoid the first header row
    rows = soup.findAll('tr')[1:]
    # convert to a list of lists
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

    # create dataframe and output
    stats_df = pd.DataFrame(player_stats, columns = headers)
    stats_df.to_csv('{}/data/raw/player_advanced_data.csv'.format(project_path))

if __name__ == '__main__':
    scrape_player_advanced_stats()
