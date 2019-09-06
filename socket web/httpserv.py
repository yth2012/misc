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
        path = self.path.lstrip("/")

        if path:
            req_path = "C:\\Users\\yth2012\\misc\\socket web\\{}".format(path)
        else:
            req_path = "C:\\Users\\yth2012\\misc\\socket web\\index.html"

        data = ""
        with open(req_path, "rb") as html_file:
            data = html_file.read()
        
        if data:
            self.wfile.write(data)
        else:
            self.err404()

    def err404(self):
        self.send_error(404, "cant find rsc")

if __name__ == "__main__":
    s = my_server()
    s.serve_forever()