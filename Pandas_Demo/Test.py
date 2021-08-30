import pandas as pd
pd.set_option("display.max_columns", None)
reviews = pd.read_csv('wine.csv')

left = reviews.set_index(['points'])
print(left)