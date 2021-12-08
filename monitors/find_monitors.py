from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_monitors(driver):
  print("Searching monitors")
  monitors = []
  for index in range(1, 99):
    # Obtener los monitores
    driver.get('https://www.solotodo.cl/monitors?size_raw_start=27&resolution_start=112085&video_ports=112396&panel_types=111165&ordering=offer_price_usd&page='+str(index)+'&')
    monitors_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not monitors_elements:
      break
    for monitor_element in monitors_elements:
      monitor = {
        'id': int(monitor_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': monitor_element.find_element(By.XPATH,'.//h3/a').text,
        'size': monitor_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'resolution': monitor_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'ms': monitor_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'hz': monitor_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]').text,
        'g-sync': monitor_element.find_element(By.XPATH,'.//div[2]/dl/dd[6]').text,
        'freesync': monitor_element.find_element(By.XPATH,'.//div[2]/dl/dd[7]').text,
        'url': monitor_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(monitor_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      monitors.append(monitor)
    # Cambiar la pagina
    # print("cambio la pagina " + str(index))
  print("")
  # Guardar la lista de monitores
  order_date_prices(monitors, path='items/monitors.csv')

