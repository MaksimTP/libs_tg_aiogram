import requests
from bs4 import BeautifulSoup
import json
url = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.min.json'

req = requests.get(url).json()

rows = req['rows']
print(type(rows))
print(rows[:10])

count = 0

for dic in rows:
    dic['url'] = f'https://pypi.org/project/{dic["project"]}/'
    print(dic['url'])

    try:
        req_for_url = requests.get(dic['url'])
        soup = BeautifulSoup(req_for_url.text, 'lxml')
        project_description = soup.find('div', {'class': 'project-description'}).text
        dic['description'] = project_description
        count += 1
        print(f'{dic["project"]}: Have been appended to dict :)\n {count} items have been added.')
    except:
        dic['url'] = 'Couldnt find...'
        dic['description'] = 'No url - no description'
        print(f'{dic["project"]}: Havent been appended to dict :(')

    with open(f'12_libs_artem\data\\{count}_{dic["project"]}.json', 'w', encoding='utf-8') as file:
        json.dump( dic,file, indent=4,ensure_ascii=False)

rows[:10]

