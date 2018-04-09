import pandas as pd
import os

df = pd.read_pickle(os.path.join('data sets', 'data_frame.pickle'))

artists = df['artist']

artist_name_to_filter = input('Please enter the name of a artist in "Last Name, First Name" format to see how many pieces they have created.')

artist_counts = df['artist'].value_counts()
number_of_works = artist_counts[artist_name_to_filter]

print(artist_name_to_filter + ' has created ' + str(number_of_works) + ' works in the dataset')