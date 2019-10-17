import socket
HOST='localhost'
PORT=5003
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
	command=raw_input("type of operation:")
	a=raw_input("first number:")
	b=raw_input("second number")
	command=command+'#'+a+'#'+b+'#'
	s.send(command)
	data=s.recv(1024)
	print 'output :',data
s.close()
