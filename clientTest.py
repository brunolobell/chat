import socket

HOST = '127.0.0.1'
PORT = 5000       

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  while 1:
    data = s.recv(255).decode()
    if data:
      print(data)
    input()
    s.sendall(b'Hello, world')
