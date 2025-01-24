# HTTP PUT Server

A simple HTTP server that supports both PUT and GET methods, allowing file uploads and downloads.

## Features

- File upload via HTTP PUT
- File download via HTTP GET
- Web directory listing
- Configurable port
- Clean shutdown with CTRL+C

## Installation

```bash
git clone https://github.com/yourusername/http-put-server.git
cd http-put-server
chmod +x http-put-server.py
```

## Usage

Start server (default port 8080):
```bash
./http-put-server.py
```

Specify custom port:
```bash
./http-put-server.py -p 9000
```

## File Upload Examples

Linux (curl):
```bash
curl -T file.txt http://server:8080/file.txt
```

Windows (PowerShell):
```powershell
Invoke-WebRequest -Uri "http://server:8080/file.txt" -Method PUT -InFile file.txt
```


## Author

Michael Phidias (with Claude.ai)
