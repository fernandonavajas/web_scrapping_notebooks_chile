from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from get_notebooks import find_notebooks
from get_processors import find_processes
from order_date_prices import order_date_prices
from search_offer import search_offer

# Cargar las opcines del web driver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='/bin/chromedriver', options=chrome_options)

find_notebooks(driver)