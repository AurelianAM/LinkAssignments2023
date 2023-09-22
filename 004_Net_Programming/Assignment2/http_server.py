from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


names_dict = {'john':'smith',
            'david':'jones',
            'michael':'johnson',
            'chris':'lee'}

class RequestHandler(BaseHTTPRequestHandler):
    # Handler for the GET request
    def do_GET(self):
        self.log_message("Incoming GET request...")
        try:
            name = parse_qs(self.path[2:])['name'][0]
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return
 
        if name in names_dict.keys():
            self.send_response_to_client(200, names_dict[name])
        else:
            self.send_response_to_client(404, 'Name not found')
            self.log_message("Name not found")
    
    # Handler for the POST request
    def do_POST(self):
        self.log_message('Incoming POST request...')
        data = parse_qs(self.path[2:])
        try:
            names_dict[data['name'][0]] = data['last_name'][0]
            self.send_response_to_client(200, names_dict)
        except KeyError:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
    
    # Handler for the PUT request: modify the last name for an existing name
    def do_PUT(self):
        self.log_message('Incoming PUT request...')
        data = parse_qs(self.path[2:])
        try:
            if data['name'][0] in names_dict.keys():
                names_dict[data['name'][0]] = data['last_name'][0]
                self.send_response_to_client(200, names_dict)
            else:
                self.send_response_to_client(404, 'Name not found')
                self.log_message("Name not found")
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message('Incorrect parameters provided')
    
    # Handler for the DELETE request
    def do_DELETE(self):
        self.log_message('Incoming DELETE request...')
        try:
            name = parse_qs(self.path[2:])['name'][0]
        except:
            self.send_response_to_client(404, 'Incorect parameters provided')
            self.log_message('Incorect parameters provided')
            return
        
        if name in names_dict.keys():
            names_dict.pop(name)
            self.send_response_to_client(200, names_dict)
        else:
            self.send_response_to_client(404, 'Name does not exist')
            self.log_message('Name does not exist')

    # Send the response to the client
    def send_response_to_client(self, status_code, data):
        # Send OK status
        self.send_response(status_code)
        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
 
        # Send the response
        self.wfile.write(str(data).encode())
 
server_address = ('127.0.0.1', 8080)
http_server = HTTPServer(server_address, RequestHandler)
http_server.serve_forever()