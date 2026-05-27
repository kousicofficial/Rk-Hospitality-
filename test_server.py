import http.server
import socketserver
import threading
import time
import os

# Serve the directory
PORT = 8080
DIRECTORY = r"d:\Rk hospitality"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(1) # wait for server to start

# We don't have selenium/playwright easily available unless we install it.
# Let's just output a diagnostic HTML page that we can fetch which includes JS to measure scrollWidth.
# Actually, I can't easily run a browser. 
# But I can just check the CSS for min-widths.

print("Server started on port 8080.")
