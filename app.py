from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = os.getenv("MESSAGE", "Hello from Docker!")

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Server listening on port 8000")
server.serve_forever()
