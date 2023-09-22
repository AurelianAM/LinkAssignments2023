import requests

# function for processing a GET request
def getName(name):
    r = requests.get("http://127.0.0.1:8080/", params={"name":name})
    print(f'Request method: GET\nStatus code: {r.status_code}\nResponse data: {r.text}\n')

# function for processing a POST request
def setName(name, lastName):
    r = requests.post("http://127.0.0.1:8080/", params = {'name':name, 'last_name':lastName})
    print(f'Request method: POST\nStatus code: {r.status_code}\nResponse data: {r.text}\n')

# function for processing a PUT (modification) request
def setLastName(name, newLastName):
    r = requests.put("http://127.0.0.1:8080/", params = {'name':name, 'last_name':newLastName})
    print(f'Request method: PUT\nStatus code: {r.status_code}\nResponse data: {r.text}\n')

# function for processing a DELETE request
def delName(name):
    r = requests.delete("http://127.0.0.1:8080/", params={"name":name})
    print(f'Request method: DELETE\nStatus code: {r.status_code}\nResponse data: {r.text}\n')


getName('chris')
setName('peter', 'peterson')
setName('david', 'jones')

getName('x')
delName('davi')

setLastName('david', 'flenderson')
setLastName('x', 'flend')

delName('peter')


