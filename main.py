# Lab 7
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time



driver = webdriver.Chrome(executable_path="chromedriver/chromedriver")
os.remove("output.txt")
file = open("output.txt", "w+", encoding= "utf8")
try:
    for page in range(1,4):
        file.write("Страница №" + str(page) + '\n')
        url = f"https://www.avito.ru/perm/muzykalnye_instrumenty?p={page}&q=%D0%B3%D0%B8%D1%82%D0%B0%D1%80%D0%B0+%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F"
        driver.get(url=url)
        items = driver.find_elements(By.CLASS_NAME, 'iva-item-sliderLink-uLz1v')
        i = 1
        for item in items[:2]:
            page_url = item.get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(url=page_url)
            price = driver.find_element(By.CLASS_NAME, 'style-item-price-PuQ0I').text.split('\n')[0]
            file.write(f"Объявление {i}: {driver.find_element(By.CLASS_NAME, 'title-info-title-text').text}\n"
                  f"Строимость: {price}Р\n"
                  f"{driver.find_element(By.CLASS_NAME, 'style-item-description-pL_gy').text}\n\n")
            i += 1
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
    file.close()
