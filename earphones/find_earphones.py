from selenium.webdriver.common.by import By

from order_date_prices import order_date_prices

def find_earphones(driver):
  print("Searching earphones")
  earphones = []
  for index in range(1, 99):
    # Obtener los audifonos
    driver.get('https://www.solotodo.cl/headphones?brands=769114&brands=769069&brands=769475&brands=769599&brands=772166&brands=769988&brands=769720&connectivities=768984&has_active_noise_cancelling=1&ordering=offer_price_usd&page='+str(index)+'&')
    earphones_elements = driver.find_elements_by_xpath('//*[@id="category-browse-results-card"]/div/div[2]/div/div[@class = "d-flex flex-column category-browse-result"]')
    if not earphones_elements:
      break
    for earphone_element in earphones_elements:
      earphone = {
        'id': int(earphone_element.find_element(By.XPATH,'.//h3/a').get_attribute('href').split("-")[0].split("/")[-1]),
        'name': earphone_element.find_element(By.XPATH,'.//h3/a').text,
        'type': earphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[1]').text,
        'hz': earphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[2]').text,
        'size driver': earphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[3]').text,
        'microphone': earphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[4]').text,
        'connection': earphone_element.find_element(By.XPATH,'.//div[2]/dl/dd[5]/ul').text,
        'url': earphone_element.find_element(By.XPATH,'.//h3/a').get_attribute('href'),
        'price': int(earphone_element.find_element(By.XPATH,'.//div[3]/div/a').text.split(" ")[1].replace(".",""))
      }
      earphones.append(earphone)
    # Cambiar la pagina
    print("cambio la pagina " + str(index))
  print("")
  # Guardar la lista de audifonos
  order_date_prices(earphones, path='items/earphones.csv')

