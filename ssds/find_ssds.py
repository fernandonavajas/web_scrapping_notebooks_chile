from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_ssds(driver):
  print("Searching ssds")
  ssds = []
  for index in range(1, 99):
    # Obtener los ssdes
    driver.get('https://www.solotodo.cl/solid_state_drives?capacity_start=532195&formats=867502&has_dram=1460588&has_dram=1460592&ordering=offer_price_usd&page='+str(index)+'&')
    ssds_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not ssds_elements:
      break
    for ssd_element in ssds_elements:
      ssd = {
        'id': int(ssd_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': ssd_element.find_element(By.XPATH,'.//h3/a').text,
        'capacity': ssd_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'format': ssd_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'bus': ssd_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'url': ssd_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(ssd_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      ssds.append(ssd)
    # Cambiar la pagina
    print(f'{str(index)}')
  print(("-"*60).center(100))
  # Guardar la lista de ssdes
  order_date_prices(ssds, path='items/ssds.csv')

