
import pandas as pd
import time

def order_date_prices(notebooks):
  df = pd.read_csv('notebooks.csv')

  verify_integrity(df, notebooks)
  add_prices(df, notebooks)

  df.to_csv("notebooks.csv", index=False)

# Verifica que esten presentes todos los notebooks
# si un notebook no esta presente, lo agrega
def verify_integrity(df, notebooks):
  for notebook in notebooks:
      row = df[df['id'] == notebook['id']]
      if row.empty:
        df.loc[len(df.index)] = notebook

# añade los precios correspondientes al día de hoy
# en una nueva columna
def add_prices(df, notebooks):
  today = time.strftime("%d/%m/%y", time.localtime())
  for notebook in notebooks:
      row = df[df['id'] == notebook['id']]
      if row.empty == False:
        df.loc[row.index, today] = notebook['price']

