from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen
import csv

# For this assignment, we need to load in the following modules
import requests
import io
import zipfile
import scipy.stats

# your code here
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
type(requests.get(url).content)
s = io.StringIO(requests.get(url).content.decode('utf-8'))
countries = pd.read_csv(s)
countries.head()

response = urlopen(url).content.decode('utf-8')
csvFile = csv.reader(response)
type(csvFile)
for row in csvFile:
    print(row)
