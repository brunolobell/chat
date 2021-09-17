import socket

HOST = '127.0.0.1'
PORT = 5000       

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  while True:
    #print("TO ANTES DO RECV")

    try:
      data = s.recv(1024).decode()
      s.settimeout(2)
    except socket.timeout:
      pass

    if data:
      print(data)

    message=input()
    #print("Peguei a messagem")
    s.sendall(str.encode(message))
    #print("envie a mensagem ai ohooooo")
