import logging
import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from config import Config


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        response = requests.get(
            Config.URL,
            headers={
                "X-Yandex-API-Key": Config.API_KEY
            },
            timeout=5
        )
        data = json.loads(response.content.decode())
        self.wfile.write(json.dumps(
            data["forecast"]["parts"][0]).encode("utf-8"))


if __name__ == '__main__':
    server = HTTPServer((Config.HOST, int(Config.PORT)), RequestHandler)
    logging.getLogger().setLevel(logging.INFO)
    try:
        logging.log(logging.INFO, "Server started")
        server.serve_forever()
    except KeyboardInterrupt:
        logging.log(logging.INFO, "Server closed by user")
        server.server_close()
    finally:
        server.server_close()
