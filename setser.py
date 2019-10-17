import socket
s=socket.socket()
host="127.0.0.1"
port= 9997
s.bind(('',port))
s.listen(5)
#while True:
c,addr=s.accept()
data="Ankush"
c.send(data)
print 'got connection from ',addr
c.close()
