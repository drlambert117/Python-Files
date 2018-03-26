import pandas as pd
import numpy as np

my_numpy_array = np.random.rand(3,2)

# my_series = pd.Series(my_numpy_array, index=["First", "Second", "Third"])

df = pd.DataFrame(my_numpy_array, index=["First Row", "Second Row", "Third Row"], columns=["First Column", "Second Column"])

print(df)