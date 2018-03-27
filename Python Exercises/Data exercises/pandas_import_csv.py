import pandas as pd
import os

CSV_PATH = os.path.join('data sets', 'artwork_data.csv')

df = pd.read_csv(CSV_PATH, nrows=10, index_col='id')

print(df)