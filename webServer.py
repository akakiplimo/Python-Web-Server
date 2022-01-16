#!/usr/bin/python3
""" Module that defines a Python 3 web server example """


from socketserver import TCPServer
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import time, os
from io import BytesIO
import ssl

hostName = "localhost"
serverPort = 8001

class MyServer(BaseHTTPRequestHandler):
    """ class that defines a web server """
    def do_GET(self):
        """ GET request """
        # Parse query data to find out what was requested
        parsedParams = urlparse(self.path)

        # See if the file requested exists, else mod_rewrite
        if os.access('.' + os.sep + parsedParams.path, os.R_OK):
            # File exists, serve it up
            f = open(os.curdir + os.sep + self.path, 'rb')
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(f.read())
        else:
            # redirect to index.html; mod_rewrite implementation
            self.send_response(302)
            self.send_header('Content-Type', 'text/html')  
            self.send_header('location', '/index.html')  
            self.end_headers()

    def do_POST(self):
        """ POST request """
        contentLength = int(self.headers["Content-Length"])
        body = self.rfile.read(contentLength)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is a POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

if __name__ == "__main__":
    webServer = TCPServer((hostName, serverPort), MyServer)
    webServer.socket = ssl.wrap_socket(webServer.socket,
                                       keyfile="./OpenSSL/key.pem",
                                       certfile="./OpenSSL/cert.pem", server_side=True)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
