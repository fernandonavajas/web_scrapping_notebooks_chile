import pandas as pd
import time

def search_offer():
  df = pd.read_csv('notebooks.csv')
  date_prices_columns = df.iloc[: , 10:]
  for _, row in date_prices_columns.iterrows():
    print(row)