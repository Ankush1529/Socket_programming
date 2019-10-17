import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='localhost'
port=5000
s.connect((host,port))
