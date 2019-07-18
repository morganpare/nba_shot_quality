import sys
from src import data

project_path=sys.argv[1]

# get the data
data.download_data('%s/data/raw' % project_path)
