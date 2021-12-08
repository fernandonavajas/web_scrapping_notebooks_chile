from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_all_in_ones(driver):
  print("Searching all_in_ones")
  all_in_ones = []
  for index in range(1, 99):
    # Obtener los audifonos
    driver.get('https://www.solotodo.cl/all_in_ones?processor_lines=880039&processor_lines=1406811&processor_lines=721516&processor_lines=514757&ram_quantity_start=753455&ordering=offer_price_usd&page='+str(index)+'&')
    all_in_ones_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not all_in_ones_elements:
      break
    for all_in_one_element in all_in_ones_elements:
      all_in_one = {
        'id': int(all_in_one_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': all_in_one_element.find_element(By.XPATH,'.//h3/a').text,
        'processor': all_in_one_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'screen': all_in_one_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'ram': all_in_one_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'hard drive': all_in_one_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]/ul').text,
        'url': all_in_one_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(all_in_one_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      all_in_ones.append(all_in_one)
    # Cambiar la pagina
    print("cambio la pagina " + str(index))
  print("")
  # Guardar la lista de audifonos
  order_date_prices(all_in_ones, path='items/all_in_ones.csv')

