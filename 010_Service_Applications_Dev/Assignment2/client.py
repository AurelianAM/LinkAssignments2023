import requests

SERVER = "http://127.0.0.1:8081/"

haveToken = input("Do you have a token? (y/n): ")

if (haveToken.lower() == "y"):
    token = input("Provide token: ")
    response = requests.post(SERVER, params={"token": token})
    print(
        f"Request method: POST \nResponse status_code: {response.status_code}\n Response data: {response.text}")
elif (haveToken.lower() == "n"):
    account = input("Enter account: ")
    password = input("Enter password: ")
    response = requests.get(
        SERVER, params={"account": account, "password": password})

    print(
        f"Request method: GET \nResponse status_code: {response.status_code}\n Response data: {response.text}")

else:
    print("Wrong action")
