import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host='adminit-HP-Compaq-8000-Elite-CMT-PC'
port=5000
host='192.168.43.92'
s.connect((host,port))
while(True):
	rpl=raw_input('client: ')
	s.send(rpl)
	if rpl=='see ya':
		break
	data=s.recv(1024)
	print'Server: ',data	
s.close()
