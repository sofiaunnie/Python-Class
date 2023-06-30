# import requests
#
# # response = requests.get("https://holidays.abstractapi.com/v1/?api_key=6bd0c6b504454c469458edcd734d069e&country=US&year=2022&month=7&day=04")
# # print(response.status_code)
# # print(response.content)
#
# response = requests.get("https://holidays.abstractapi.com/v1/?api_key=6bd0c6b504454c469458edcd734d069e&country=NG&year=2022&month=7&day=11")
# print(response.status_code)
#print(response.content)

import requests
from pprint import pprint
myapi = "6bd0c6b504454c469458edcd734d069e"
url = "https://holidays.abstractapi.com/v1/?"
country = input("Which Country: ").upper()
year = input("Which year: ")
month = input("Which month: ")
day = input("Day in month: ")
response = requests.get(f"{url}api_key={myapi}&country={country}&year={year}&month={month}&day={day}")
pprint(response.status_code)
holiday = response.json()
pprint(holiday)
pprint("holiday : ",holiday[0]['name'])
