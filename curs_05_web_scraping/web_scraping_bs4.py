import pandas as pd
import requests
from bs4 import BeautifulSoup

# pip install requests

req = requests.get('https://bnr.ro/Cursul-de-schimb--7372.aspx')
# print(req)
link = BeautifulSoup(req.text, features='html.parser') # lxml, html5lib
# print(link)

main = link.find_all('div', attrs={'id': 'contentDiv'})
# main = link.find_all('table')
# print(main)
# print(type(main))
header_list = []
dataset = []

for obj in main:
    for table_id in obj.find_all('table'):
        for table_trs in table_id.find_all('tr'):
            if table_trs.find_all('th'):
                for header_data in table_trs.find_all('th'):
                    header_list.append(header_data.get_text())
            else:
                list_with_td = []
                for body_data in table_trs.find_all('td'):
                    list_with_td.append(body_data.get_text())
                dataset.append(list_with_td)
# print(header_list)
# print('-----------------------')
# print(dataset)

df = pd.DataFrame(dataset, columns=header_list)
print(df)
df.to_excel('Curs_BNR.xlsx', index=False)