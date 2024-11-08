import http.server
import socketserver
import cgi

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_type, pdict = cgi.parse_header(self.headers['Content-Type'])
        if content_type == 'multipart/form-data':
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            pdict['CONTENT-LENGTH'] = int(self.headers['Content-Length'])
            fields = cgi.parse_multipart(self.rfile, pdict)
            file1 = fields.get('file1')[0]
            file2 = fields.get('file2')[0]
            print("file")
            # print(file2)
            if file1 and file2:
                print("Received file1: ", file1)
                print("Received file2: ", file2)
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Success')
            else:
                self.send_response(400)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Missing files')
        else:
            self.send_response(400)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid content-type')

PORT = 5000

with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
