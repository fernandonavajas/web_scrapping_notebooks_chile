from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from microwaves.find_microwaves import find_microwaves
from notebooks.find_notebooks import find_notebooks
from applewatchs.find_applewatchs import find_applewatchs
from refrigerators.find_refrigerators import find_refrigerators
from stereos.find_stereos import find_stereos
from televisions.find_televisions import find_televisions
from washerdryer.find_washerdryers import find_washerdryers


# Cargar las opcines del web driver
chrome_options = Options()
chrome_options.add_argument("--headless")
s = Service('/bin/chromedriver')
driver = webdriver.Chrome(service= s, options=chrome_options)

find_notebooks(driver)
find_applewatchs(driver)
find_refrigerators(driver)
find_televisions(driver)
find_stereos(driver)
find_washerdryers(driver)
find_microwaves(driver)

# Cerrar el navegador falso
driver.quit()
