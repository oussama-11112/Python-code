from selenium.webdriver.common.by import By



def get_products_urls(driver):
    url = "https://www.tunisianet.com.tn/smartphone-tunisie/66222-smartphone-benco-y11-3g-1-go-32-go-double-sim-blue.html"
    driver.get(url)
    urls = []
    
    title = driver.find_elements(By.Class_Name, "product_title")
    for title in title:
        anchor = title.find_element(By.Tag_Name, "a")
        link = anchor.get_attribute("href")
        urls.append(link)
        
    return urls