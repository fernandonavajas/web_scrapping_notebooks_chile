from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException

from order_date_prices import order_date_prices

def find_refrigerators(driver):
  refrigerators = []
  for index in range(1, 99):
    # Obtener los refrigeradores
    driver.get('https://www.solotodo.cl/refrigerators?width_end=700&height_start=1686&refrigerator_capacity_start=250&freezer_capacity_start=79&ordering=offer_price_usd&page='+str(index)+'&')
    refrigerators_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not refrigerators_elements:
      break
    for refrigerator_element in refrigerators_elements:
      refrigerator = {
        'id': int(refrigerator_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': refrigerator_element.find_element(By.XPATH,'.//h3/a').text,
        'type': (' ').join(refrigerator_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text.split(" ")[1:]),
        'frosting': refrigerator_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'liters refrigerator': int(float(refrigerator_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text.split(" ")[0])),
        'liters frezzer': int(float(refrigerator_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text.split(" ")[0])),
        'efficiency': refrigerator_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]').text,
        'Kwh/month': refrigerator_element.find_element(By.XPATH,'.//div[2]/dl/dd[6]').text.split(" ")[0],
        'url': refrigerator_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(refrigerator_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      refrigerators.append(refrigerator)
    # Cambiar la pagina
    print("cambio la pagina " + index)

  # Guardar la lista de refrigeradores
  order_date_prices(refrigerators, path='refrigerators/refrigerators.csv', order='price')

