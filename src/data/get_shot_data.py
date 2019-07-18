import kaggle

# download shot data
def download_data(path='/home/mpare/src/nba_shot_quality/data/raw'):
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('dansbecker/nba-shot-logs', path=path, unzip=True)

if __name__ == '__main__':
    download_data()
