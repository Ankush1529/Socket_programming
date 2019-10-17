import socket
HOST='localhost'
PORT=5004
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
print "server is ready"
conn,addr=s.accept()
#print 'conn done!'
while True:
	data=conn.recv(1024)
	#print'data received',data
	t=data.split('#',3)
	command=t[0]
	
	if command=='+':
		a=t[1]
		b=t[2]
		reply=int(a)+int(b)
		
	elif command=='-':
		a=t[1]
		b=t[2]
		reply=int(a)-int(b)
		
	elif command=='/':
		a=t[1]
		b=t[2]
		reply=int(a)/int(b)
		
	elif command=='*':
		a=t[1]
		b=t[2]
		reply=int(a)*int(b)
		
	conn.send(str(reply))
conn.close()

