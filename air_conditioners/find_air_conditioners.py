from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException

from order_date_prices import order_date_prices

def find_air_conditioners(driver):
  print("Searching air_conditioners")
  air_conditioners = []
  for index in range(1, 99):
    # Obtener las aspiradoras
    driver.get('https://www.solotodo.cl/air_conditioners?ordering=offer_price_usd&page='+str(index)+'&')
    air_conditioners_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not air_conditioners_elements:
      break
    for air_conditioner_element in air_conditioners_elements:
      air_conditioner = {
        'id': int(air_conditioner_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': air_conditioner_element.find_element(By.XPATH,'.//h3/a').text,
        'btu': air_conditioner_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'efficiency': air_conditioner_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'inverter': air_conditioner_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
        'url': air_conditioner_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(air_conditioner_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      air_conditioners.append(air_conditioner)
    # Cambiar la pagina
    print(f'{str(index)}')
  print("")
  # Guardar la lista de aspiradoras
  order_date_prices(air_conditioners, path='items/air_conditioners.csv')

