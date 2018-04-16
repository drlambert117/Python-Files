import pandas as pd
import os

#Read .pickle file
df = pd.read_pickle(os.path.join('data sets', 'data_frame.pickle'))

small_df = df.iloc[49980:50019, :].copy()

grouped = small_df.groupby('artist')
type(grouped)

for name, group_df in grouped:
    min_year = group_df['acquisitionYear'].min()
    print("{}: {}").format(name, min_year)
    break
