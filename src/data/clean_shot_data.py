import pandas as pd

def format_name(name):
    '''
        Function to clean the player name

        arguments:
        name = name of the player to clean
    '''
    # if two names, find the first and second then concatenate with space
    if ', ' in name:
        split_name = name.split(', ')
        f_name = split_name[1]
        l_name = split_name[0]
        full_name = f_name + ' ' + l_name
    # if only one name then leave
    else:
        full_name = name
    # return upper case name for easier joining
    return(full_name.upper())

def change_shot_result(result):
    '''
        Function to convert shot result column to boolean (0 or 1)

        arguments:
        result = result of the shot to clean
    '''
    if result == 'made':
        return 1
    else:
        return 0

def clean_shot_data(project_path='/home/mpare/src/nba_shot_quality'):
    '''
        Function to clean the shot data

        arguments:
        project_path = path of the project directory
    '''
    df = pd.read_csv('{}/data/raw/shot_logs.csv'.format(project_path))

    # fill the n/as - shot clock was turned off
    df["SHOT_CLOCK"].fillna(0, inplace = True)

    # clean the name data for easier joining
    df['CLOSEST_DEFENDER'] = df['CLOSEST_DEFENDER'].apply(format_name)
    df['player_name'] = df['player_name'].apply(lambda x: x.upper())

    # clean the shot result
    df['SHOT_RESULT'] = df['SHOT_RESULT'].apply(change_shot_result)

    df.to_csv('{}/data/interim/shot_logs.csv'.format(project_path))


if __name__ == '__main__':
    clean_shot_data()
