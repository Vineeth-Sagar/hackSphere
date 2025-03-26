from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="public", **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    print(f"Server running at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
