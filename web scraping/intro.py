
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)
url = "https://www.tunisianet.com.tn/smartphone-tunisie/66222-smartphone-benco-y11-3g-1-go-32-go-double-sim-blue.html"

driver.get(url)

product = {}

# get data
title_element = driver.find_element(By.CLASS_NAME, "h1")
title = title_element.text
product["title"] = title

refference_element = driver.find_element(By.CLASS_NAME, "product-reference")
reference = refference_element.text
product["reference"] = reference

description_element = driver.find_element(
    By.ID, "product-description-short-66222")
description = description_element.text
product["description"] = description
price_element = driver.find_element(By.CLASS_NAME, "current-price")
price = price_element.text




product['avalable'] = available

all_images = driver.find_elements(By.TAG_NAME, "img")
image = all_images[1].get_attribute("src")
product["brand_image"] = brand_image
print(product)

time.sleep(1)
driver.close()