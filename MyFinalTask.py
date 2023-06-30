import requests
from pprint import pprint
url = "http://127.0.0.1:3000/cities/"
response = requests.get(url)
print(response.status_code)
user = response.json()

states_list, zipcode_list = [], []
for i in range(len(cities["data"])):
    states_list.append((cities["data"][i]['state']))
    zipcode_list.append((cities["data"][i]['zip code']))
print(dict(zip(states_list,zipcode_list)))
