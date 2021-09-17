import socket
import os
import threading as thr
from datetime import datetime

# Environment Variables to the Socket
HOST = os.getenv('SOCKET_HOST', '127.0.0.1')
PORT = int(os.getenv('SOCKET_PORT', 5000))
CONNECTIONS = int(os.getenv('SOCKET_CONNECTIONS', 100))

# Function to connect to the server
def connection():
  if CONNECTIONS == 0:
    raise Exception("Connections number must be greater than 0!")
  
  try:
    # Create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(CONNECTIONS)

  except ValueError as err:
    raise Exception(err)
  
  return server

# Function to receive messages from a connection
def operator(conn, addr, clientList):
  conn.send(str.encode("Bem-vindo ao Chat de Bruno e Johann!"))
  conn.settimeout(None)
  print("New Connection: " + addr[0] + ':' + str(addr[1]))

  while True:
    try:
      # Receive a message from client
      message = conn.recv(1024).decode() 
      if message:
        # Get current date
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        messageSend = "<{} -- {}:{}> {}".format(now, addr[0], str(addr[1]), message)
        print (messageSend)
        # Send message to users in chat
        for client in clientList:
          #talvez esse if não precise
          if client != conn:
            try:
              client.send(messageSend.encode())
            except:
              client.close()
              if conn in clientList:
                clientList.remove(conn)
      else:
        if conn in clientList:
          clientList.remove(conn)
        break

    except:
      continue
  conn.close()

def Interrupt():
  a="meu pau"

# Function to create a user
def newUser(clientList, server, threadList):
  conn, addr = server.accept()
  clientList.append(conn)

  # Create a new Thread
  t = thr.Thread(target = operator, args=(conn, addr, clientList))
  threadList.append(t)
  t.start()
  
  return clientList

# Main function
def main():
  threadList = []
  clientList = []
  server = connection()
  while 1:
    clientList = newUser(clientList, server, threadList)

  # Stop all threds
  for t in threadList:
    #é bom comentar sobre o join 
    t.join()

  server.close()

if __name__ == "__main__":
  main()