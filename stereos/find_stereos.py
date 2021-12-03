from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException

from order_date_prices import order_date_prices

def find_stereos(driver):
  print("Searching Stereos")
  stereos = []
  for index in range(1, 99):
    # Obtener los equipos de audio
    driver.get('https://www.solotodo.cl/stereo_systems?brands=371408&brands=371454&brands=994212&brands=800910&brands=1141477&brands=371588&ordering=offer_price_usd&page='+str(index)+'&')
    stereos_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not stereos_elements:
      break
    for stereo_element in stereos_elements:
      stereo = {
        'id': int(stereo_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': stereo_element.find_element(By.XPATH,'.//h3/a').text,
        'type': stereo_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'brand': stereo_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'power': stereo_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'url': stereo_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(stereo_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      stereos.append(stereo)
    # Cambiar la pagina
    print("cambio la pagina " + str(index))
  print("")
  # Guardar la lista de equipos de audio
  order_date_prices(stereos, path='items/stereos.csv')

