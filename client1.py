import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='localhost'
port=5004
s.connect((host,port))
data=raw_input ("Enter the value: ")
s.send(data)
data=s.recv(12)
print "The ans is :", data
s.close()
