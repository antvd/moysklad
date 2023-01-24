import requests
import json

token = 'TOKEN'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
params = {
    'stockType': 'quantity',
    'include': 'zeroLines',
}

#получение каталога
response = requests.get('https://online.moysklad.ru/api/remap/1.2/entity/assortment', headers=headers)
result = response.json()

with open('catalog.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
print("catalog json data saved as a file")

#получение остатков
response = requests.get('https://online.moysklad.ru/api/remap/1.2/report/stock/all/current', params=params, headers=headers)
result = response.json()

with open('stock.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
print("stock json data saved as a file")

#получение оборота по товарам
response = requests.get('https://online.moysklad.ru/api/remap/1.2/report/turnover/all', headers=headers)
result = response.json()

with open('turnover.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
print('turnover json data saved as a file')

