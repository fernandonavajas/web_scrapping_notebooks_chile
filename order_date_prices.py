
import pandas as pd
import time
import pdb

today = time.strftime("%d/%m/%y", time.localtime())

def order_date_prices(notebooks):
  df = pd.read_csv('notebooks.csv')
  verify_integrity(df, notebooks)
  add_prices(df, notebooks)
  order_list_by(df, label="score")
  prepare_to_mean(df, type=str)
  mean_price_x_days_ago(df, target="price" ,days=4)
  prepare_to_mean(df, type=int)
  calculate_diff_price(df, target="diff price")
  df.to_csv("notebooks.csv", index=False)

# Verifica que esten presentes todos los notebooks
# si un notebook no esta presente, lo agrega
def verify_integrity(df, notebooks):
  for notebook in notebooks:
      row = df[df['id'] == notebook['id']]
      if row.empty:
        df.loc[len(df.index)] = notebook

# añade los precios correspondientes al día de hoy en una nueva columna
def add_prices(df, notebooks):
  for notebook in notebooks:
      row = df[df['id'] == notebook['id']]
      if row.empty == False:
        df.loc[row.index, today] = int(notebook['price'])
  float_col = df.select_dtypes(include=['float64'])
  # Transformar todas las columnas float a int64
  for col in float_col.columns.values:
    df[col] = df[col].astype('int64')

# Ordena la lista dado el nombre de la columna, de forma descendente
def order_list_by(df, label="score"):
  df.sort_values(by=label, ascending=False, kind='quicksort', inplace=True)

# Para aplicar el calculo del promedio, es necesario
# cambiar el tipo de todos los campos que no quieren ser
# incluidos en el promedio a String
def prepare_to_mean(df, type=str):
    df["id"]= df["id"].astype(type)
    df["score"]= df["score"].astype(type)
    df["price"]= df["price"].astype(type)
    df["diff price"]= df["diff price"].fillna(0).astype(type)

# Calcula el precio promedio de los últimos X días
def mean_price_x_days_ago(df, target="price", days=4):
  # pdb.set_trace()
    df[target] = df.mean(axis=1, numeric_only=True)

# Calcula la diferencia del precio con respecto al promedio
def calculate_diff_price(df, target="diff price"):
  df[target] = df["price"] - df[today]
