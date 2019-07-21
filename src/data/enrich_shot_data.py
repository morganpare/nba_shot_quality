import pandas as pd

def enrich_shot_data(project_path='/home/mpare/src/nba_shot_quality'):
    '''
        Function to enrich the shot data with advanced player stats from
        previous season

        arguments:
        project_path = path of the project directory
    '''
    # load the shot and player data
    shot_df = pd.read_csv('{}/data/interim/shot_logs.csv'.format(project_path))
    player_df = pd.read_csv('{}/data/interim/player_advanced_data.csv'.format(project_path))

    # create a df with offensive features to add
    offense_df = player_df[['Player','TS%']]

    # create a df with defensive features to add
    defense_df = player_df[['Player','DWS','DBPM','BLK%']]
    defense_df.columns = ['Player','Defender_DWS','Defender_DBPM','Defender_BLK%']

    # merge the shot df with the offense and defense dfs
    full_df = pd.merge(shot_df, offense_df, left_on = 'player_name', right_on = 'Player', how = 'inner')
    full_df.drop('Player', axis = 1, inplace = True)
    full_df = pd.merge(full_df, defense_df, left_on = 'CLOSEST_DEFENDER', right_on = 'Player', how = 'inner')
    full_df.drop('Player', axis = 1, inplace = True)

    # keep the desired columns
    cols_to_keep = ['PERIOD','SHOT_CLOCK','DRIBBLES','TOUCH_TIME','SHOT_DIST',
    'SHOT_RESULT','CLOSE_DEF_DIST','TS%','Defender_DWS','Defender_DBPM',
    'Defender_BLK%']
    full_df = full_df[cols_to_keep]

    full_df.to_csv('{}/data/processed/shot_logs.csv'.format(project_path))


if __name__ == '__main__':
    enrich_shot_data()
