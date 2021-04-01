import socket

def getInfo():
  global HOST_NAME;
  HOST_NAME = socket.gethostname()
  global HOST_ADDRESS
  HOST_ADDRESS = socket.gethostbyname(HOST_NAME)
  print(HOST_NAME)
  print(HOST_ADDRESS)

def choosePort():
  global PORT;
  PORT = 1307
  # int(input("Port = "))

def createServer():
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
  soc.bind((HOST_ADDRESS, PORT))
  soc.listen(5)
  while True:
    clientConnection, clientAdress = soc.accept()
    print("Connected to Client: ", clientAdress) 
    content = "Server say hello Client"
    clientConnection.send(content.encode())
    content2 = clientConnection.recv(1024).decode()
    print(content2)

if (__name__ == "__main__"):
  getInfo()
  choosePort()
  createServer()

