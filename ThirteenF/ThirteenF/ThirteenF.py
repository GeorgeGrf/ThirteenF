import requests
import json
import datetime


current_year = datetime.date.today().year
current_quarter = (datetime.date.today().month - 1) // 3 + 1
all_years = list(range(current_year-5, current_year))
quarters = ['QTR1', 'QTR2', 'QTR3', 'QTR4']
history = [(y, q) for y in all_years for q in quarters]
"""         TEST FTP FUNCTION


for i in range(1, current_quarter):
    history.append((current_year, 'QTR%d' % i))
quarterly_files = ['edgar/full-index/%d/%s/form.idx' % (x[0], x[1]) for x in history]

"""
url = "https://www.sec.gov/Archives/edgar/full-index/2020/QTR1/form.idx"
response = requests.get(url).content.decode("utf-8", "ignore").splitlines()
lines = [tuple(line.split('|')) for line in response[11:]]
print(lines)
