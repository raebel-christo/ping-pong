from threading import Thread
from time import sleep  
import socket


UDP_RX_IP = "127.0.0.1"
UDP_RX_PORT = 3001

sockRX = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sockRX.bind((UDP_RX_IP, UDP_RX_PORT))

temp = 0


def two():
    global temp
    while True:
          data, addr = sockRX.recvfrom(1024) # buffer size is 1024 bytes
          temp += 1
          JsonStr = data.decode('utf_8')
          print(JsonStr)



p2 = Thread(target = two)
p2.setDaemon(True)
p2.start()

while True:  
     # Run your main code here. 
      
     sleep(1)