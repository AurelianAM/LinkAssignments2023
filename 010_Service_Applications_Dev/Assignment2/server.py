import sqlite3
import jwt
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime, timedelta
import hashlib
import logging

KEY = "Lq6AdaUknveBu3eZegHNlCgPdJEZzmG21XLqSAPos2Yx1on73fgV2wSaXcfKOPME4ZUBUhkjvs0rtQRndHYyGjewudtqEttjuaVkRxTdmBu8yBTnQdUE65RY"


# Transform a string for security purposes - used for storing and transform passwords


# Database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()
# Create the table Customers in the db if not exists
cursor.execute("""CREATE TABLE IF NOT EXISTS Customers(
               id INTEGER PRIMARY KEY,
               name CHAR(20),
               surname CHAR(20),
               account CHAR(20) UNIQUE,
               password CHAR(20),
               token CHAR(120))""")
conn.commit()

# Insert some demo Customers if the Customers table is empty
customers = cursor.execute("""SELECT * FROM Customers""")
if (len(customers.fetchall()) == 0):
    demo_customers = [('1', 'john', 'johnson', '111111111', 'pwd1', ''),
                      ('2', 'jack', 'jackson', '222222222', 'pwd2', ''),
                      ('3', 'drew', 'andersen', '333333333', 'pwd3', '')]
    cursor.executemany(
        """INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?)""", demo_customers)
    conn.commit()
    print("Demo customers inserted into databese.")
else:
    print("Database is already populated.")


# Request handler
class RequestHandler(BaseHTTPRequestHandler):
    # Define the response to the client
    def send_response_to_client(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(str(data).encode())

    # Generate a token valid for 45s using the customer account
    def generateToken(self, account, password):
        expiration_time = datetime.utcnow() + timedelta(seconds=45)
        payload = {
            "account": account,
            "password": password,
            "exp": expiration_time
        }
        token = jwt.encode(payload, key=KEY, algorithm="HS256")
        return token

    # Verify if the given token is valid
    def isTokenValid(self, token):
        try:
            payload = jwt.decode(token, KEY, algorithms="HS256")
            print("Valid token provided...")
            return True
        except jwt.ExpiredSignatureError:
            print("Token has expired")
            return False
        except jwt.InvalidTokenError:
            print("Invalid token")
            return False

    # Returns the token from db for a certain account
    def getTokenFromDB(self, account, password):
        querry = """SELECT token FROM Customers WHERE account=? AND password=?"""
        token = cursor.execute(querry, (account, password))
        return token.fetchone()[0]

    # Insert the new token into db for a certain account
    def setTokenInDB(self, account, password, token):
        querry = """UPDATE Customers SET token=? WHERE account=? AND password=?"""
        cursor.execute(querry, (token, account, password))
        conn.commit()

    def getCustomerFromToken(self, token):
        payload = jwt.decode(token, KEY, algorithms="HS256")
        token_account = payload["account"]
        token_password = payload["password"]
        querry = """SELECT name, surname FROM Customers WHERE account=? AND password=?"""
        customer = cursor.execute(querry, (token_account, token_password))
        customer_data = customer.fetchone()
        return customer_data[0], customer_data[1], token_account

    # GET Method
    def do_GET(self):
        self.log_message("Incoming GET request...")
        data_passed = parse_qs(self.path[2:])
        passed_account = data_passed['account'][0]
        passed_password = data_passed['password'][0]

        try:
            # Verify if the passed account and password exists in the db
            querry = """SELECT * FROM Customers WHERE account = ? AND password = ?"""
            customer_from_db = cursor.execute(
                querry, (passed_account, passed_password))
            if (len(customer_from_db.fetchall()) == 0):
                self.send_response_to_client(400, 'Invalid login')
                return

            # Verify if the given customer has already a valid token in the db
            dbToken = self.getTokenFromDB(passed_account, passed_password)
            if self.isTokenValid(dbToken):
                self.send_response_to_client(
                    200, f'You already have a valid token: {dbToken}')
                return

            # Generate a new token for the given customer if not having one in the db
            token = self.generateToken(passed_account, passed_password)
            self.setTokenInDB(passed_account, passed_password, token)
            self.send_response_to_client(
                200, f'New Token (valid for 45 sec): {token}\nCopy and save your token!')

        except KeyError:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
        
    def do_POST(self):
        self.log_message("Incoming POST request...")
        try:
            token = parse_qs(self.path[2:])["token"][0]
            if (self.isTokenValid(token) == False):
                self.send_response_to_client(200, "Token not valid")
                return
        except:
            self.send_response_to_client(404, "Incorect parameters provided")
            self.log_message("Incorrect parameters provided")
            return
        
        name, surname, account = self.getCustomerFromToken(token)
        self.send_response_to_client(200, f"Login succesfull.\n {name} {surname} logged in for the account {account}")


if __name__ == "__main__":
    server_address = ("localhost", 8081)
    http_server = HTTPServer(server_address, RequestHandler)
    http_server.serve_forever()