#!/usr/bin/env python3
"""
Servidor HTTP simples com CORS habilitado. Permite que arquivos
locais sejam acessados por scripts em outras origens.
Uso: python3 cors_server.py [porta]
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow requests from any origin
        self.send_header('Access-Control-Allow-Origin', '*')
        # Ideally, also allow common methods
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

if __name__ == '__main__':
    # usage: python cors_server.py [port]
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f"Serving HTTP on port {port} with CORS enabled...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
