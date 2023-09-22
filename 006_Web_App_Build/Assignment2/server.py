from student import Student, insert_student, get_student
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message('Incoming GET request...')
        try:
            cardNumber = int(parse_qs(self.path[2:])['cardNumber'][0])
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message('Incorrect parameters provided')
            return
        student = get_student(cardNumber)
        if student == None:
            self.send_response_to_client(400, 'Student not found')
            self.log_message('Student not found')
        else:
            self.send_response_to_client(200, student)
    
    def do_POST(self):
        self.log_message("Incomintg POST request...")
        data = parse_qs(self.path[2:])
        name = data['name'][0]
        lastName = data['lastName'][0]
        avgGrade = float(data['avgGrade'][0])
        print(name, type(name), lastName, type(lastName), avgGrade, type(avgGrade))
        try:
            newStudent = Student(name, lastName, avgGrade)
            insert_student(newStudent)
            self.send_response_to_client(200,'Student added')
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message('Incorrect parameters provided')
        # print(data)
        # print(type(data))

    def send_response_to_client(self, status_code, data):
        # Send OK status
        self.send_response(status_code)
        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
     
        # Send the response
        self.wfile.write(str(data).encode())

server_address = ('127.0.0.1', 8080)
http_server = HTTPServer(server_address, RequestHandler)
http_server.serve_forever()