import requests

BASE_URL = "http://127.0.0.1:5000/"

data = [{"user_name": "faroxx", "e-mail": "mefaruk92@gmail.com", "password": "ThiSisAPassWord1!@#$%^&*"},
        {"user_name": "faruk", "e-mail": "fdemiroz@live.nl", "password": "ThiSisAPassWord1!@#$%^&*"},
        {"user_name": "elena", "e-mail": "no-email", "password": "ThiSisAPassWord1!@#$%^&*"}]

for i in range(len(data)):
	try:
		response = requests.put(BASE_URL + "user/" + str(i), data[i])
		print(response.json())
	except requests.exceptions.HTTPError as err:
		print(err)

# input()
# response = requests.delete(BASE_URL + "user/0")
# print(response)
input()
response = requests.get(BASE_URL + "user/2")
print(response.json())


