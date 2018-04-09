# Counts the number of unique artists in the dataset

import pandas as pd
import os

df = pd.read_pickle(os.path.join('data sets', 'data_frame.pickle'))

artists = df['artist']

number_of_artists = len(pd.unique(artists))

print(number_of_artists)