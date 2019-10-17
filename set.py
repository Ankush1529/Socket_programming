import socket
s=socket.socket()
host="127.0.0.1"
port= 9997
s.connect(('',port))
tm=s.recv(1024)

print " time from host : ",tm
s.close()
