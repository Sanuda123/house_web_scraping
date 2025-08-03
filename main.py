from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


PATH = r"C:\Program Files (x86)\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
time.sleep(3)  # Wait for the browser to open

# city = input("Enter the city name: ")
# driver.get("https://rentals.ca/van" + city)

driver.get("https://rentals.ca/vancouver")

try: 
    container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".page-search-results__list.d-none.d-lg-block"))
    )
except:
    print("Element not found within the specified time.")
    driver.quit()
    sys.exit()
    

houses = container.find_elements(By.CSS_SELECTOR, ".listing-card-container.col-12")

for house in houses:
    price = house.find_element(By.CSS_SELECTOR, ".listing-card__price.d-inline-block").text
    print(f"Price: {price}")

input("Press Enter to close the browser...")
driver.quit()






