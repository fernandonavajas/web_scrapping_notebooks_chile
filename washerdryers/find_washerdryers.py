from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_washerdryers(driver):
  print("Searching Washerdryers", end="  pages  => ")
  washerdryers = []
  for index in range(1, 99):
    # Obtener los washerdryeres
    driver.get('https://www.solotodo.cl/washing_machines?w_types=362007&ordering=offer_price_usd&page='+str(index)+'&')
    washerdryers_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not washerdryers_elements:
      break
    for washerdryer_element in washerdryers_elements:
      washerdryer = {
        'id': int(washerdryer_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': washerdryer_element.find_element(By.XPATH,'.//h3/a').text,
        'type': washerdryer_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'power': washerdryer_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'washing capacity': washerdryer_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'drying capacity': washerdryer_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
        'door position': washerdryer_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]').text,
        'url': washerdryer_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(washerdryer_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      washerdryers.append(washerdryer)
    # Cambiar la pagina
    print(f'{str(index)}', end=", ")
  print("")
  # Guardar la lista de washerdryeres
  order_date_prices(washerdryers, path='items/washerdryers.csv')

