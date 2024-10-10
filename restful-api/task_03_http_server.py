#!/usr/bin/python3
import http.server
import json
from http import HTTPStatus


class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Endpoint Not Found")
            self.end_headers()

def run(server_class=http.server.HTTPServer, handler_class=HTTPRequestHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
