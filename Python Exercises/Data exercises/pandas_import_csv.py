#Imports
import pandas as pd
import os

#Defines file path
CSV_PATH = os.path.join('data sets', 'artwork_data.csv')

#Defines keys to pull from dataset
COLS_TO_USE = ['artistId', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

#re
df = pd.read_csv(CSV_PATH, usecols=COLS_TO_USE)

#Saves dataframe to pickle format in data sets folder
# df.to_pickle(os.path.join('data sets', 'data_frame.pickle'))

# print(df) 