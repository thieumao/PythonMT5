import socket

def chooseServer():
  global SERVER_ADDRESS;
  SERVER_ADDRESS = "169.254.7.198"
  # input("SERVER_ADDRESS = ")
  global PORT;
  PORT = 1307
  # int(input("PORT = "))

def createClient():
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
  soc.connect((SERVER_ADDRESS, PORT))
  content1 = soc.recv(1024).decode()
  print(content1)
  content2 = "Client say hello Server"
  soc.send(content2.encode())
  soc.close()

if (__name__ == "__main__"):
  chooseServer()
  createClient()
