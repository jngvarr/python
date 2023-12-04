import socket
import threading
from time import sleep

ya_sock = socket.socket()
addr = ("77.88.55.242", 443)
ya_sock.connect(addr)

data_out = b"GET / HTTP/1.1\r\n\Host:ya.ru\r\n\r\n"
ya_sock.send(data_out)

data_in = b""

def recieving():
    global data_in
    while True:
        data_chank = ya_sock.recv(1024)
        data_in = data_in + data_chank 
        # 1024 - размер буфера

rec_thread = threading.Thread(target = recieving())
rec_thread.start()

sleep(4)
print(data_in)