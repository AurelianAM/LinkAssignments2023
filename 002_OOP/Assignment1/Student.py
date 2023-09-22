class Student:
    def __init__(self, name:str, adress:str, phone:str, course:str, index_number:str):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.course = course
        self.index_number = index_number
    
    def getInfo(self):
        return f'Name: {self.name}\nAdress: {self.adress}\nPhone: {self.phone}\nIndex Number: {self.index_number}\n'
    