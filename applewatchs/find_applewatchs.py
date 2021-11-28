from selenium.webdriver.common.by import By
from order_date_prices import order_date_prices

def find_applewatchs(driver):
  applewatchs = []
  for index in range(1, 7): # 6 páginas
    # Obtener los refrigeradores
    driver.get('https://www.solotodo.cl/wearables?types=864844&brands=872174&ordering=offer_price_usd&page='+str(index)+'&')
    applewatchs_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    for applewatch_element in applewatchs_elements:
      applewatch = {
        'id': int(applewatch_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': applewatch_element.find_element(By.XPATH,'.//h3/a').text,
        'type': applewatch_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'screen': applewatch_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'size': applewatch_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'hearth rate': applewatch_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
        'waterproof': applewatch_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]').text,
        'conectividad': applewatch_element.find_element(By.XPATH,'.//div[2]/dl/dd[6]/ul').text,
        'url': applewatch_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(applewatch_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      applewatchs.append(applewatch)
    # Cambiar la pagina
    print("cambio la pagina")

  # Guardar la lista de refrigeradores
  order_date_prices(applewatchs, path='applewatchs/applewatchs.csv', order='price')
