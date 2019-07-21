import pandas as pd

def clean_player_data(project_path='/home/mpare/src/nba_shot_quality'):
    '''
        Function to clean the player data

        arguments:
        project_path = path of the project directory
    '''
    # define columns and load in data
    cols = ['Player','Pos','Age','Tm','G','MP','PER','TS%','3PAr','FTr','ORB%','DRB%','TRB%','AST%','STL%',
        'BLK%','TOV%','USG%','blank1','OWS','DWS','WS','WS/48','blank2','OBPM','DBPM','BPM','VORP']
    df = pd.read_csv('{}/data/raw/player_advanced_data.csv'.format(project_path),
        index_col=0, names = cols, header = 0)

    # drop empty rows
    df.dropna(axis=0, how='all',inplace=True)

    # drop weird columns
    df.drop(['blank1','blank2'], axis = 1, inplace = True)

    # finally remove any remaining nulls, these are players that took no shots
    df.dropna(axis=0, how='any',inplace=True)

    # find players that played on multiple teams and take the total stats
    multi_team_players = df[df['Tm'] == 'TOT']['Player']
    multi_team_df = df[df['Player'].isin(multi_team_players)]
    multi_team_df = multi_team_df[multi_team_df['Tm'] != 'TOT']
    df.drop(multi_team_df.index, inplace=True)

    # make the names upper case
    df['Player'] = df['Player'].apply(lambda x: x.upper())

    df.to_csv('{}/data/interim/player_advanced_data.csv'.format(project_path))

if __name__ == '__main__':
    clean_player_data()
