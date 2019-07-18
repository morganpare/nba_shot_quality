import pandas as pd

def clean_data(project_path='/home/mpare/src/nba_shot_quality'):
    df = pd.read_csv('{}/data/raw/shot_logs.csv'.format(project_path))
    # fill the n/as - shot clock was turned off
    df["SHOT_CLOCK"].fillna(0, inplace = True)
    df.to_csv('{}/data/interim/shot_logs.csv'.format(project_path))

if __name__ == '__main__':
    clean_data()
