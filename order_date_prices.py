
import pandas as pd
import time
import pdb

today = time.strftime("%d/%m/%y", time.localtime())

def order_date_prices(objets, path='', order=''):
  df = pd.read_csv(path)
  verify_integrity(df, objets)
  add_prices(df, objets)
  order_list_by(df, label=order)
  mean_price_x_days_ago(df, target="price" ,days=4)
  calculate_diff_price(df, target="diff price")
  converts_to_int(df)
  df.to_csv(path, index=False)

# Verifica que esten presentes todos los objetos
# si un objeto no esta presente, lo agrega
def verify_integrity(df, objets):
  for objet in objets:
      row = df[df['id'] == objet['id']]
      if row.empty:
        df.loc[len(df.index)] = objet

# añade los precios correspondientes al día de hoy en una nueva columna
def add_prices(df, objets):
  for objet in objets:
      row = df[df['id'] == objet['id']]
      if row.empty == False:
        df.loc[row.index, today] = int(objet['price'])

# Ordena la lista dado el nombre de la columna, de forma descendente
def order_list_by(df, label="price"):
  df.sort_values(by=label, ascending=False, kind='quicksort', inplace=True)

# Calcula el precio promedio de los últimos X días
def mean_price_x_days_ago(df, target="price", days=4):
  header_prices = []
  for header in list(df.columns.values):
    if (len(header.split('/')) == 3):
      header_prices.append(header)
  df[target] = df[header_prices].mean(axis=1, numeric_only=True)

# Calcula la diferencia del precio con respecto al promedio
def calculate_diff_price(df, target="diff price"):
  df[target] = df["price"] - df[today]

def converts_to_int(df):
# Transformar todas las columnas float a int64
  float_col = df.select_dtypes(include=['float64'])
  for col in float_col.columns.values:
    df[col] = df[col].astype('int64', errors = 'ignore')