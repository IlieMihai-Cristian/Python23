from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.bnr.ro/files/xml/nbrfxrates2023.htm')

table_head = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead')
# print(table_head.text)
table_body = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/tbody')
# print(table_body.text)

header = table_head.text.split('\n')
# print(header)
body = table_body.text.split('\n')
# print(body)

# print(len(header)) #32
# print(len(body)) #7936

body_rows = []
counter = 0
for i in range(0, len(body), len(header)):
    counter = i
    body_rows.append(body[counter:counter + len(header)])

# print(body_rows)

df = pd.DataFrame(body_rows, columns=header)
print(df)
df.to_excel('Curs_BNR_2023.xlsx', index=False)



# Tema
# https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00/
# https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00/
# https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00/
# https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00/
# https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-2/