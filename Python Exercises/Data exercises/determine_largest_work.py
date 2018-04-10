#Determines the artwork with the largest area

import pandas as pd
import os

df = pd.read_pickle(os.path.join('data sets', 'data_frame.pickle'))

#Try to convert and force NaN's
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

area = df['height'] * df['width']
df = df.assign(area=area)


largest_work = df.loc[df['area'].idxmax(), :]
work_title = df.loc[df['area'].idxmax(), 'title']
work_artist = df.loc[df['area'].idxmax(), 'artist']
work_area = df.loc[df['area'].idxmax(), 'area']
work_units = df.loc[df['area'].idxmax(), 'units']

names_array = work_artist.split(',')

print('The largest work in the Tate collection is called ' + str(work_title) +
      ' by the artist' + str(names_array[1]) + ' ' + str(names_array[0]) + ' which has an area of ' + str(work_area) + 
      ' ' + str(work_units))