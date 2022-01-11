#!/usr/bin/python3
""" Module that defines a Python 3 web server example """

from socketserver import TCPServer
from http.server import BaseHTTPRequestHandler
import time
from io import BytesIO
import ssl

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    """ class that defines a web server """
    def do_GET(self):
        """ GET request """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Pesapal Python Web Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body><p>This is the %s web service.</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

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
