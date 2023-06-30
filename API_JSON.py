#The API is a messenger(Attendant) that queries the server (API Call) and returns a JSON
# Objet as a response

#COMPANIES STORE BACK END INFORMATION SOME OF WHICH CAN BE ACCESSED AS JSON OBJECTS

#A JSON OBJECT( JAVASCRIPT OBJECT NOTATION ) IS A STRUCTURED FORM OF DATA WHICH ALLOWS PROGRAMMERS
# TO ACCESS DATA FOR THEIR APPLICATIONS

#THINKING OF API'S AS MESSENGERS

#API ENDPOINT IS ANY CUSTOM URL GIVEN WHICH LINKS US TO JSON DATA.
#THEY ARE USUALLY MADE PUBLICLY AVAILABLE TO PROGRAMMERS WHO REQUIRE JSON INFORMATION OR DATA
#e.g http://demo.codingnomads.co:8080/tasks_api/users

#We can QUERY ENDPOINTS(MAKE API CALLS) AND GET INFORMATION

#A STATUS CODE (200) AND STATUS MESSAGE TELLS US IF OUR QUERY WAS SUCCESSFUL

#JSON IS GENERALLY USED IN BACK-END PROGRAMMING

#UTF-8 IS THE ENCODED FORMAT OF THE JSON DATA
#UTF-8 converts Unicode data through a mathematical algorithm so that UTF-8 uses 8 data bits to
# encode the data

#WE USE THE REQUESTS MODULE TO REQUESTS MODULE TO REQUEST FOR A WEBPAGE OR URL IN PYTHON
#


import requests
from pprint import pprint
url = "http://demo.codingnomads.co:8080/tasks_api/users"
#POSTING DATA TO APIS
#WHEN POSTING DATA TO APIS, IT HAS TO BE IN A DICTIONARY FORMAT
new = {
    "email" : "sofiatadeyemi78@gmail.com",
    "first_name" : "Sofia",
    "last_name" :"Bang",
}
mypost = requests.post(url,json=new)   #Posts our data
print(mypost.status_code)     #Checks to see if posting is successful
print("New data added!")      #Follow-up message


# import requests
# from pprint import pprint
# url = "http://demo.codingnomads.co:8080/tasks_api/users"
# response = requests.get(url)
# print(f"Response statuscode : {response.status_code}")
# #print(f"Response content : \n {response.content}")
# users = response.json()       #converting to python dictionary
#pprint(users["data"][-1])

# pprint(users["data"][4]['id'])
# pprint(users["data"][4]['email'])
# pprint(users["data"][4]['first_name'])
# pprint(users["data"][4]['last_name'])

# list of all first names
# s = []
# for i in range(len(users["data"])):
#     s.append((users["data"][i]['first_name']))
# pprint(s)
#
# print('------------------------------------')
#
# list of all emails
# p = []
# for i in range(len(users["data"])):
#     p.append((users["data"][i]['email']))
# pprint(p)

#dictionary
#my solution
# s = []
# for i in range(len(users["data"])):
#     s.append((users["data"][i]['id']))
#
# p = []
# for i in range(len(users["data"])):
#     p.append((users["data"][i]['email']))
#
# this_dict = dict(zip(p,s))
# print(this_dict)

#method 1
# id_list, email_list = [], []
# for i in range(len(users["data"])):
#     id_list.append((users["data"][i]['id']))
#     email_list.append((users["data"][i]['email']))
# print(dict(zip(id_list,email_list)))

#method 2                #dictionary comprehension method
# emaildict = {x["id"]: x["email"] for x in users["data"]}
# print(emaildict)
# #or
# emaildict2 = {users["data"][i]["id"]: users["data"][i]["email"] for i in range(len(users["data"]))}
