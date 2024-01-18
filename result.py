from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


subject = input('Ievadiet specializaciju: ')

output_file_path = "atrastie_kursi.txt"

def scrape_coursera(subject):
    service_coursera = Service()
    option_coursera = webdriver.ChromeOptions()
    option_coursera.add_argument("--start-maximized")
    driver_coursera = webdriver.Chrome(service=service_coursera, options=option_coursera)

    url_coursera = "https://www.coursera.org"
    driver_coursera.get(url_coursera)
    time.sleep(2)

    find_coursera = driver_coursera.find_element(By.ID, "onetrust-accept-btn-handler")
    find_coursera.click()
    time.sleep(2)

    find_coursera = driver_coursera.find_element(By.CLASS_NAME, "react-autosuggest__input")
    find_coursera.send_keys(subject)
    find_coursera.send_keys(Keys.ENTER)
    time.sleep(6)

    page_source_coursera = driver_coursera.page_source

    soup_coursera = BeautifulSoup(page_source_coursera, 'html.parser')

    data_block_coursera = soup_coursera.find('div', class_="cds-9 css-0 cds-11 cds-grid-item cds-56 cds-81")

    data_list_coursera = []

    if data_block_coursera:
        h3_elements_coursera = data_block_coursera.find_all('h3')[:4]

        with open(output_file_path, "w", encoding="utf-8") as file: 
            file.write("Coursera piedavatie kursi:\n\n")
            for h3_coursera in h3_elements_coursera:
                nosaukums_coursera = h3_coursera.get_text(strip=True)
                href_coursera = h3_coursera.find_parent('a')['href']
                full_url_coursera = url_coursera + href_coursera
                bloka_info_coursera = h3_coursera.find_next('div', class_="cds-ProductCard-body")
                papildus_info_coursera = bloka_info_coursera.get_text(strip=True) if bloka_info_coursera else "Nav papildus informacijas"
                ratings_block_coursera = h3_coursera.find_next('div', class_="cds-CommonCard-ratings")
                ratings_info_coursera = ratings_block_coursera.get_text(strip=True) if ratings_block_coursera else "No informacijas par reitingu"
                data_list_coursera.append({'title': nosaukums_coursera, 'full_url': full_url_coursera, 'additional_info': papildus_info_coursera, 'ratings_info': ratings_info_coursera})

                file.write(f"Nosaukums: {nosaukums_coursera}\n")
                file.write(f"URL: {full_url_coursera}\n")
                file.write(f"Papildus Info: {papildus_info_coursera}\n")
                file.write(f"Ratings Info: {ratings_info_coursera}\n")
                file.write("\n")

    driver_coursera.quit()
    return data_list_coursera

def scrape_mit(subject):
    option_mit = webdriver.ChromeOptions()
    option_mit.add_argument("--start-maximized")
    driver_mit = webdriver.Chrome(options=option_mit)

    url_mit = "https://ocw.mit.edu/"
    driver_mit.get(url_mit)
    time.sleep(3)

    find_mit = driver_mit.find_element(By.NAME, "q")
    time.sleep(2)
    find_mit.send_keys(subject)
    find_mit.send_keys(Keys.ENTER)
    time.sleep(6)

    page_source_mit = driver_mit.page_source

    soup_mit = BeautifulSoup(page_source_mit, 'html.parser')

    data_block_mit = soup_mit.find('section', {'role': 'feed', 'aria-busy': 'false', 'aria-label': 'OpenCourseWare Search Results'})

    data_list_mit = []

    if data_block_mit:
        card_headers_mit = data_block_mit.find_all('div', class_="lr-row course-title")
        saturs_elements_mit = data_block_mit.find_all('div', class_="lr-subtitle listitem")
        papildus_elements_mit = data_block_mit.find_all('div', class_="lr-subtitle listitem topics-list")
        href_elements_mit = data_block_mit.find_all('a', class_="w-100")

        for card_header_mit, content_element_mit, papildus_element_mit, href_element_mit in zip(card_headers_mit, saturs_elements_mit, papildus_elements_mit, href_elements_mit):
            nosaukums_mit = card_header_mit.get_text(strip=True)
            href_mit = urljoin(url_mit, href_element_mit['href']) if href_element_mit else None
            professor_info_mit = content_element_mit.get_text(strip=True) if content_element_mit else None
            papildus_info_mit = papildus_element_mit.get_text(strip=True) if papildus_element_mit else None
            data_list_mit.append({'nosaukums': nosaukums_mit, 'href': href_mit, 'professor_info': professor_info_mit, 'papildus_info': papildus_info_mit})

        with open(output_file_path, "a", encoding="utf-8") as file:
            file.write("\n\n")
            file.write("MIT OpenCourseWare piedavatie kursi:\n\n") 
            for i in range(min(4, len(data_list_mit))):
                file.write(f"Nosaukums: {data_list_mit[i]['nosaukums']}\n")
                file.write(f"URL: {data_list_mit[i]['href']}\n")
                file.write(f"Professors: {data_list_mit[i]['professor_info']}\n")
                file.write(f"Papildus: {data_list_mit[i]['papildus_info']}\n")
                file.write("\n")

    driver_mit.quit()
    return data_list_mit

def scrape_edx(subject):
    option_edx = webdriver.ChromeOptions()
    option_edx.add_argument("--start-maximized")
    driver_edx = webdriver.Chrome(options=option_edx)

    url_edx = "https://www.edx.org/"
    driver_edx.get(url_edx)
    time.sleep(2)

    find_edx = driver_edx.find_element(By.ID, "onetrust-accept-btn-handler")
    find_edx.click()
    time.sleep(2)

    find_edx = driver_edx.find_element(By.NAME, "searchfield-input")
    time.sleep(2)
    find_edx.send_keys(subject)
    find_edx.send_keys(Keys.ENTER)
    time.sleep(6)

    page_source_edx = driver_edx.page_source

    soup_edx = BeautifulSoup(page_source_edx, 'html.parser')

    data_block_edx = soup_edx.find('div', class_="mw-lg px-xl-0 container-mw-lg container-fluid")

    data_list_edx = []

    if data_block_edx:
        card_headers_edx = data_block_edx.find_all('div', class_="pgn__card-header-content")
        href_elements_edx = data_block_edx.find_all('a', class_="base-card-link")
        for card_header_edx, href_element_edx in zip(card_headers_edx, href_elements_edx):
            nosaukums_edx = card_header_edx.get_text(strip=True)
            href_edx = href_element_edx['href'] if href_element_edx else None
            full_href_edx = urljoin(url_edx, href_edx) if href_edx else None
            saisinats_href_edx = full_href_edx.split('?')[0] 
            parts_edx = nosaukums_edx.split("…")
            kursa_nosaukums_edx = parts_edx[0].strip()
            university_name_edx = parts_edx[1].strip()
            data_list_edx.append({'course_name': kursa_nosaukums_edx, 'link': saisinats_href_edx, 'university_name': university_name_edx})

        with open(output_file_path, "a", encoding="utf-8") as file:
            file.write("\n\n")
            file.write("eDx piedavatie kursi:\n\n")
            for i in range(min(3, len(data_list_edx))):
                file.write(f"Nosaukums: {data_list_edx[i]['course_name']}\n")
                file.write(f"URL: {data_list_edx[i]['link']}\n")
                file.write(f"Universitate: {data_list_edx[i]['university_name']}\n")
                file.write("\n")

    driver_edx.quit()
    return data_list_edx


scrape_coursera(subject)
scrape_mit(subject)
scrape_edx(subject)
