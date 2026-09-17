#!/usr/bin/env python3
"""Answer everything the static locations did not serve with Hugo's 404 page.

The web locations serve public/ directly, and the router forwards whatever
they miss to the application upstream. With no upstream listening those misses
came back as Upsun's "502 Bad Gateway" page, which is both ugly and wrong:
crawlers treat a 502 as transient and keep the dead URL around. This server
exists only to turn those requests into a real 404.
"""

import os
import pathlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

APP_DIR = pathlib.Path(os.environ.get("PLATFORM_APP_DIR", "."))
FALLBACK = b"<!DOCTYPE html><title>404 Not Found</title><h1>404 Not Found</h1>\n"

try:
    BODY = (APP_DIR / "public" / "404.html").read_bytes()
except OSError:
    BODY = FALLBACK

# Kept in sync with the headers block in config.yaml; the static locations are
# served by the router, so it never sees these responses.
HEADERS = {
    "Content-Type": "text/html; charset=utf-8",
    "Cache-Control": "no-store",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "X-Frame-Options": "SAMEORIGIN",
    "Strict-Transport-Security": "max-age=31536000",
}


class NotFoundHandler(BaseHTTPRequestHandler):
    # HTTP/1.1 so the router can keep connections alive; that needs an
    # accurate Content-Length on every response, including HEAD.
    protocol_version = "HTTP/1.1"
    server_version = "notfound"
    sys_version = ""

    def version_string(self):
        return self.server_version

    def respond(self, with_body):
        self.send_response(404)
        for name, value in HEADERS.items():
            self.send_header(name, value)
        self.send_header("Content-Length", str(len(BODY)))
        self.end_headers()
        if with_body:
            self.wfile.write(BODY)

    def do_GET(self):
        self.respond(True)

    def do_HEAD(self):
        self.respond(False)

    def do_POST(self):
        self.respond(True)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", int(os.environ["PORT"])), NotFoundHandler)
    server.daemon_threads = True
    server.serve_forever()
