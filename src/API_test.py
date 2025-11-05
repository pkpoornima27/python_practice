import json
import requests
url = 'https://fake-json-api.mock.beeceptor.com/users'

res = requests.get(url)
if res.status_code == 200:
    users = res.json()
    #print(users)
    for user in users:
        #print(user)
        id = user['id']
        #print(id)
        name = user.get("name")
        #print(name)
        company = user.get("company")
        #print(company)

url2 = "https://www.themealdb.com/api/json/v1/1/filter.php?a=Indian"



url3 = "https://dummy-json.mock.beeceptor.com/continents"
res = requests.get(url3)
if res.status_code == 200:
    records = res.json()
    for record in records:
        print(record['code'])
        print(record['lines'])
        print(record['developedCountries'])

re = requests.post()