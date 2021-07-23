# web_scrapping_notebooks_chile
Web App to Search Notebook Offers In Chile
# Python 3.5
## 1. Crear virtual env
py -3 -m venv venv  # Windows

python3 -m venv venv  # Linux

## 2. Activar el virtual env
. venv/bin/activate  # Linux

venv\Scripts\activate  # Windows

# 3. Instalación
pip freeze > requirements.txt
 
pip install -r requirements.txt  

# 4. Levantar servidor
export FLASK_ENV=development
export FLASK_APP=manage
flask run

# 5. Listo
Abre tu navegador: http://127.0.0.1:5000/

