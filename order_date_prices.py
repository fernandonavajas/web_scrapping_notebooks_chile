
import pandas as pd
import time
import pdb

today = time.strftime("%d/%m/%y", time.localtime())

def order_date_prices(objets, path='', order='diff percent', order_ascending=False):
  df = pd.read_csv(path)
  verify_integrity(df, objets)
  mean_price_x_days_ago(df, target="price" ,days=4)
  add_prices(df, objets)
  calculate_diff_price(df)
  order_list_by(df, label=order, order_ascending=order_ascending)
  is_offer(df, path)
  df.to_csv(path, index=False, float_format='{:.0f}'.format)

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
def order_list_by(df, label, order_ascending=False):
  df.sort_values(by=label, ascending=order_ascending, kind='quicksort', inplace=True)

# Calcula el precio promedio de los últimos X días
def mean_price_x_days_ago(df, target="price", days=4):
  header_prices = []
  for header in list(df.columns.values):
    if (len(header.split('/')) == 3):
      header_prices.append(header)
  df[target] = df[header_prices].mean(axis=1, numeric_only=True)

# Calcula la diferencia del precio con respecto al promedio y lo muestra como porcentaje de descuento
def calculate_diff_price(df):
  df["diff price"] =  df[today] - df["price"]
  df["today"] = df[today]
  df['diff percent'] = (1-(df[today]/df["price"]))*100

# Lista las ofertas del día por consola
def is_offer(df, path):
  for _, row in df.iterrows():
    if (row['diff percent'] > 10):
      category = path[6:-4]
      name = row["name"]
      percentage = round(row["diff percent"], 2)
      today = format(int(row["today"]), ',d')
      avg = format(int(row["price"]), ',d') 
      url = row["url"]
      # notebooks: 23%↓ today: 990.000 avg: 1.299.000 Lenovo h3... url...
      print(f'{category}: {percentage}%↓ today: {today} avg: {avg} {name} {url}')
  
