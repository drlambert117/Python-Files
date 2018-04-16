import pandas as pd
import os

df = pd.read_pickle(os.path.join('data sets', 'data_frame.pickle'))

small_df = df.iloc[49980:50019, :].copy()

small_df.to_excel("data sets/dataframe.xlsx", index =False, columns=["artist", "title", "year"])