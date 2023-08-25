from selenium import webdriver
import time

from get_product import get_product
from save_product import save_product

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver = webdriver.chrome(options=options)
urls = get_products_urls(driver)

for url in urls:
    product = get_product(driver, url)
    save_product(product)
    time.sleep(1)
    
    
time.sleep(1)
driver.close()