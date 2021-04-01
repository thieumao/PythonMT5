import socket
import time

def getInfo():
  global HOST_NAME
  HOST_NAME = socket.gethostname()
  global HOST_ADDRESS
  HOST_ADDRESS = socket.gethostbyname(HOST_NAME)
  print(HOST_NAME)
  print(HOST_ADDRESS)

def choosePort():
  global PORT
  PORT = 1307
  # int(input("Port = "))

def createServer():
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  soc.bind((HOST_ADDRESS, PORT))
  soc.listen(5)

  time.sleep(1)

  client, addr = soc.accept()

  try:
    print('Connected by', addr)
    count = 0
    while True:
      data = client.recv(1024).decode()
      count = count + 1
      print(count)
      print("Client: " + data)

  finally:
    client.close()

if (__name__ == "__main__"):
  getInfo()
  choosePort()
  createServer()
