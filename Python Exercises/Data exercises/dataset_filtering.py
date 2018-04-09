#Counts number of works a user-specified artist has created in the dataset

import pandas as pd
import os

df = pd.read_pickle(os.path.join('data sets', 'data_frame.pickle'))

artists = df['artist']

artist_first_name = input('Please enter the first name of the artist: ')
artist_last_name = input('Please enter the last name of the artist: ')
artist_name_to_filter = artist_last_name + ', ' + artist_first_name

artist_counts = df['artist'].value_counts()
number_of_works = artist_counts[artist_name_to_filter]

print(artist_first_name +  ' ' + artist_last_name + ' has created ' + str(number_of_works) + ' works in the dataset')