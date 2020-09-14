
import subprocess
import os

import pandas as pd
import numpy as np

from datetime import datetime

import requests
import json


def get_john_hopkins_data():
    '''
        Git repo John Hopkins data : https://github.com/CSSEGISandData/COVID-19.git
        Get john hopkins data by a git pull request
        Result is stored in the predefined csv structure
    '''
    git_pull = subprocess.Popen("/usr/bin/git pull",
                                cwd=os.path.dirname('../data/raw/COVID-19/'),
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    (out, error) = git_pull.communicate()

    print("Error : " + str(error))
    print("out : " + str(out))


if __name__ == '__main__':
    get_john_hopkins_data()
