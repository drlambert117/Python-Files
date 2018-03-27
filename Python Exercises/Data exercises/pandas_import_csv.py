import pandas as pd
import os

CSV_PATH = os.path.join('data sets', 'artwork_data.csv')

COLS_TO_USE = ['artistId', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

df = pd.read_csv(CSV_PATH, usecols=COLS_TO_USE)

df.to_pickle(os.path.join('data sets', 'data_frame.pickle'))

print(df) 