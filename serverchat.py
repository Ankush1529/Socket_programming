import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='192.168.43.92'
port=5000
s.bind((host,port))
s.listen(5)
#print s
print 'SERVER IS READY!'
conn,addr=s.accept()
while(1):
	data=conn.recv(1024)
	print 'Client: ',data
	if data=='see ya':
		break
	rpl=raw_input('Server: ')
	conn.send(rpl)
conn.close()
