import requests
import json

text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
# print(text)
curr = 'BYN'
num = 2

all_value = json.loads(text)
if all_value["Valute"][curr]["Value"] != "":
    num = float(num) * all_value["Valute"][curr]["Value"]
print(num)
