import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from engine import run_check

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"state": "healthy"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *_):
        pass

def test_expected_status_and_json():
    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        result = run_check({"url": f"http://127.0.0.1:{server.server_port}/",
                            "expected_status": 200, "json_contains": {"state": "healthy"}})
        assert result["passed"] is True
    finally:
        server.shutdown()
        thread.join()
