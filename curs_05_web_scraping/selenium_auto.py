from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.emag.ro/')

element = driver.find_element(by=By.ID, value="searchboxTrigger")
element.send_keys("iphone16")
element.submit()

count_phones = driver.find_elements(by=By.CLASS_NAME, value="card-v2")
# //*[@id="card_grid"]
# print(len(count_phones))
# count = 0
for i in range(1, len(count_phones)+1):
    try:
        phones = driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[{i}]')
    except Exception:
        phones = False

    if phones:
        if "Pro" in phones.text and "Desert" in phones.text:
            # print(phones.text)
            # print(" ------------------------------------------------------------------------ ")
            # count += 1
            price = driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[{i}]/div/div/div[4]/div[1]/p[2]').text
            # # 7.199,98 Lei
            # 7199.98
            comparing_price = price.strip().replace('.', '').replace(',', '.').split(' ')[0]
            # print(comparing_price)
            # print(" ------------------------------------------------------------------------ ")
            if 5500 < float(comparing_price) < 6000:
                driver.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[{i}]/div/div/div[4]/div[2]/form/button').submit()
                break
# print(count)