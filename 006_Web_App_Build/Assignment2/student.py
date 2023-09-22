import sqlite3
db = 'university.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Student (
                            cardNumber INT PRIMARY KEY,
                            name TEXT,
                            lastName TEXT,
                            avgGrade INT) """)
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    return conn
    
def lastCard():
    with create_connection() as conn:
        cursor = conn.cursor()
        return cursor.execute("""SELECT cardNumber FROM Student order by cardNumber DESC limit 1""").fetchone()[0]
    
def insert_student(student):
    query = """INSERT INTO Student (cardNumber, name, lastName, avgGrade) VALUES (?, ?, ?, ?)"""
    with create_connection() as conn:
        cursor = conn.cursor()
        exists = cursor.execute(f"""SELECT COUNT(*) FROM Student WHERE name = \"{student.name}\" AND lastName = \"{student.lastName}\"""").fetchone()[0]
        if exists == 0:
            values = (student.cardNumber, student.name, student.lastName, student.avgGrade)
            cursor.execute(query, values)
            conn.commit()
            print('Student added')
        else:
            cursor.execute(f"""UPDATE Student SET avgGrade = {student.avgGrade} WHERE name = \"{student.name}\" AND lastName = \"{student.lastName}\" """)
            conn.commit()
            print('Student updated')

def get_student(card):
    if isinstance(card, int):
        if card >=1000 and card <= lastCard():
            query = f"""SELECT * FROM Student WHERE cardNumber={card}"""
            with create_connection() as conn:
                cursor = conn.cursor()
                result = cursor.execute(query).fetchone()
                student = Student(result[1], result[2], result[3])
                student.cardNumber = result[0]
                return student

class Student():
    def __init__(self, name, lastName, avgGrade):
        self.__cardNumber = lastCard()+1
        self.__name = name
        self.__lastName = lastName
        self.__avgGrade = avgGrade
    
    def __str__(self):
        return f'{self.__cardNumber};{self.__name};{self.__lastName};{self.__avgGrade}'
    
    @property
    def cardNumber(self):
        return self.__cardNumber
    
    # use only when instantiating a student from the database
    @cardNumber.setter
    def cardNumber(self, newCardNumber):
        self.__cardNumber = newCardNumber
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, newName):
        if ("'" not in newName) and ('"' not in newName) and (not isinstance(newName, int)):
            self.__name = newName
        else:
            pass
    @property
    def lastName(self):
        return self.__lastName
    @name.setter
    def name(self, newName):
        if ("'" not in newName) and ('"' not in newName) and (not isinstance(newName, int)):
            self.__lastName = newName
        else:
            pass
    @property
    def avgGrade(self):
        return self.__avgGrade
    @avgGrade.setter
    def avgGrade(self, newGrade):
        if isinstance(newGrade, int) or isinstance(newGrade, float):
            if newGrade > 0 and newGrade <= 10:
                self.__avgGrade = newGrade
