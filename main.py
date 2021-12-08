from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from all_in_ones.find_all_in_ones import find_all_in_ones
from earphones.find_earphones import find_earphones

from microwaves.find_microwaves import find_microwaves
from notebooks.find_notebooks import find_notebooks
from applewatchs.find_applewatchs import find_applewatchs
from rams.find_rams import find_rams
from refrigerators.find_refrigerators import find_refrigerators
from ssds.find_ssds import find_ssds
from stereos.find_stereos import find_stereos
from televisions.find_televisions import find_televisions
from washerdryers.find_washerdryers import find_washerdryers
from monitors.find_monitors import find_monitors

# Cargar las opcines del web driver
chrome_options = Options()
chrome_options.add_argument("--headless")
s = Service('/bin/chromedriver')
driver = webdriver.Chrome(service= s, options=chrome_options)

find_all_in_ones(driver)
find_applewatchs(driver)
find_earphones(driver)
find_microwaves(driver)
find_monitors(driver)
find_notebooks(driver)
find_rams(driver)
find_refrigerators(driver)
find_ssds(driver)
find_stereos(driver)
find_televisions(driver)
find_washerdryers(driver)

# Cerrar el navegador falso
driver.quit()
