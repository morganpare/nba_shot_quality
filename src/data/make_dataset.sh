#!/usr/bin/env bash

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/bin/python3.6
export VIRTUALENVWRAPPER_VIRTUALENV=/bin/virtualenv
source /bin/virtualenvwrapper.sh
workon NBA

if [ -z ${PROJECT_PATH+/home/mpare/src/nba_shot_quality} ]; \
then PROJECT_PATH='/home/mpare/src/nba_shot_quality'; \
else echo "PROJECT_PATH is set to '$PROJECT_PATH'"; fi

python $PROJECT_PATH/src/data/get_data.py $PROJECT_PATH
