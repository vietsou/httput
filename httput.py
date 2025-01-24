#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import signal
import sys
import socket
import argparse

class PUTHandler(SimpleHTTPRequestHandler):
    def do_PUT(self):
        path = os.path.join(os.getcwd(), self.path.lstrip('/'))
        length = int(self.headers['Content-Length'])
        
        with open(path, 'wb') as f:
            f.write(self.rfile.read(length))
        
        self.send_response(201)
        self.end_headers()

def signal_handler(sig, frame):
    print('\nServeur arrêté.')
    server.socket.close()
    server.server_close()
    sys.exit(0)

def check_port_available(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('0.0.0.0', port))
        sock.close()
        return True
    except socket.error:
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Serveur HTTP avec méthode PUT')
    parser.add_argument('-p', '--port', type=int, default=8080,
                      help='Port d\'écoute (défaut: 8080)')
    
    args = parser.parse_args()
    
    if not check_port_available(args.port):
        print(f"Erreur: Le port {args.port} n'est pas disponible")
        sys.exit(1)

    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        server = HTTPServer(('0.0.0.0', args.port), PUTHandler)
        server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print(f"Serveur démarré sur le port {args.port}...")
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServeur arrêté.')
        server.socket.close()
        server.server_close()
        sys.exit(0)
