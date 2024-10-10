#!/usr/bin/python3
"""testing if we need documentation"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HTTPRequestHandler(BaseHTTPRequestHandler):
    """get definition to see the url."""
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint Not Found")

def run(server_class=HTTPServer, handler_class=HTTPRequestHandler, port=8000):
    """run the http server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port {}...".format(port))
    httpd.serve_forever()

if __name__ == '__main__':
    """starts the programm."""
    run()
