from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_televisions(driver):
  televisions = []
  for index in range(1, 4): # 3 páginas
    # Obtener los televisiones
    driver.get('https://www.solotodo.cl/televisions?types=958742&types=656851&types=1410221&types=281176&brands=281011&brands=281102&brands=281115&size_family_value_start=40&ordering=offer_price_usd&page='+str(index)+'&')
    televisions_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    for television_element in televisions_elements:
      television = {
        'id': int(television_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': television_element.find_element(By.XPATH,'.//h3/a').text,
        'type': television_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'size': television_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'resolution': television_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'smartTV': television_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
        'url': television_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(television_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      televisions.append(television)
    # Cambiar la pagina
    print("cambio la pagina")

  # Guardar la lista de televisiones
  order_date_prices(televisions, path='televisions/televisions.csv', order='price')

