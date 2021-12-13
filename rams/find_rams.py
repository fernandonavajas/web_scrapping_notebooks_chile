from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_rams(driver):
  print("Searching rams", end="  pages  => ")
  rams = []
  for index in range(1, 99):
    # Obtener los rames
    driver.get('https://www.solotodo.cl/rams?total_capacity_start=197555&types=130774&formats=130761&frequency_start=758024&ordering=offer_price_usd&page='+str(index)+'&')
    rams_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not rams_elements:
      break
    for ram_element in rams_elements:
      ram = {
        'id': int(ram_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': ram_element.find_element(By.XPATH,'.//h3/a').text,
        'capacity': ram_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'type': ram_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'frecuency': ram_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'format': ram_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
        'volts': ram_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]').text,
        'url': ram_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(ram_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      rams.append(ram)
    # Cambiar la pagina
    print(f'{str(index)}', end=", ")
  print("")
  # Guardar la lista de rames
  order_date_prices(rams, path='items/rams.csv')

