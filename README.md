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
git clone https://github.com/vietsou/httput.git
cd httput
chmod +x httput.py
```

## Usage

Start server (default port 8080):
```bash
./httput.py
```

Specify custom port:
```bash
./httput.py -p 9000
```

## File Upload Examples

Linux (curl):
```bash
curl -T file.txt http://server_ip:8080/file.txt
```

Windows (PowerShell):
```powershell
Invoke-WebRequest -Uri "http://server_ip:8080/file.txt" -Method PUT -InFile file.txt
```

## Shortcut
Move the script into your local bin folder to execute it directly from any folder location
```
mv httput.py ~/.local/bin/httput

# Usage
httput -p 9000
```

## Author

Michael Phidias (with Claude.ai)
