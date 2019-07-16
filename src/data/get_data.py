import sys
import kaggle

# import project path
project_path = sys.argv[1]

# download shot data
kaggle.api.authenticate()
kaggle.api.dataset_download_files('dansbecker/nba-shot-logs', path='%s/data/raw/' % project_path, unzip=True)
