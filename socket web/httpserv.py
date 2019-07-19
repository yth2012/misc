from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler



class my_server(ThreadingHTTPServer):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9090
        ThreadingHTTPServer.__init__(self, (self.host, self.port), my_req_handler)


    
class my_req_handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header("content-type", "text/html")
        self.end_headers()

        html_file = open("C:\\Users\\yth2012\misc\\socket web\\index.html","rb")

        self.wfile.write(html_file.read())

if __name__ == "__main__":
    s = my_server()
    s.serve_forever()