from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

subject = input('Ievadiet specializaciju: ')

service = Service()
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.coursera.org/"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.ID, "onetrust-accept-btn-handler")
find.click()
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "react-autosuggest__input")
find.send_keys(subject)
find.send_keys(Keys.ENTER)
time.sleep(6)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

data_block = soup.find('div', class_="cds-9 css-0 cds-11 cds-grid-item cds-56 cds-81")

data_list = []

if data_block:
    print("Coursera piedavatie kursi:")
    h3_elements = data_block.find_all('h3')[:5]
    for h3 in h3_elements:
        title = h3.get_text(strip=True)
        href = h3.find_parent('a')['href']

        # Объединяем базовый URL с найденной ссылкой
        full_url = url + href

        product_card_body = h3.find_next('div', class_="cds-ProductCard-body")
        additional_info = product_card_body.get_text(strip=True) if product_card_body else "No additional information available"

        ratings_block = h3.find_next('div', class_="cds-CommonCard-ratings")
        ratings_info = ratings_block.get_text(strip=True) if ratings_block else "No ratings information available"

        data_list.append({'title': title, 'full_url': full_url, 'additional_info': additional_info, 'ratings_info': ratings_info})

for item in data_list:
    print(f"Nosaukums: {item['title']}")
    print(f"Full URL: {item['full_url']}")
    print(item['additional_info'])
    print(f"Reitings: {item['ratings_info']}")
    print()

driver.quit()
