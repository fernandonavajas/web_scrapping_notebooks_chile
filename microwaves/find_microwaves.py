from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_microwaves(driver):
  microwaves = []
  for index in range(1, 99):
    # Obtener los microwavees
    driver.get('https://www.solotodo.cl/ovens?brands=354832&brands=1158587&brands=355005&brands=355037&brands=355045&brands=355063&o_types=355077&o_types=355093&ordering=offer_price_usd&page='+str(index)+'&')
    microwaves_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not microwaves_elements:
      break
    for microwave_element in microwaves_elements:
      microwave = {
        'id': int(microwave_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': microwave_element.find_element(By.XPATH,'.//h3/a').text,
        'type': microwave_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'power': microwave_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'capacity': microwave_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'url': microwave_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(microwave_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      microwaves.append(microwave)
    # Cambiar la pagina
    print("cambio la pagina " + index)

  # Guardar la lista de microwavees
  order_date_prices(microwaves, path='microwaves/microwaves.csv', order='price')

