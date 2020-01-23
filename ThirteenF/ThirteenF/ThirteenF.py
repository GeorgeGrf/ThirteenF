import requests
import json
url = "https://www.sec.gov/Archives/edgar/full-index/2020/QTR1/index.json"
response = requests.get(url=url)
data = response.json()
print(data[])
