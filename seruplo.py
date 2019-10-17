import socket
host='localhost'
port=5000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print s
print " SERVER IS READY "
conn,addr=s.accept()
print "connect by ",addr,conn
serverfile=[]
while 1:
	data=conn.recv(100)
	if not data:	break
	d=data.split(",")
	if d[0]=="upload" :
		conn.send("start uploading")
		filename=str(d[1])
		f=open(filename,'w')
		while true:
			print "receiving data"
			data=conn.recv(1024)
			if not data:	break
			f.write(data)
		f.close()
		serverfile.append(d[1])
		conn.close()
	elif d[0]=="download":
		x=len(serverfile)
		i=0
		f=0
		while x:
			if x[i]=="str(d[1])":
				f=1
				conn.send("sending data")
				filename=str(d[1])
				f=open(filename,'rb')
				l=f.read(1024)
				while f:
					l=f.read(100)
					if l==" ":
						conn.send("end of file")
						break
					conn.send(l)
					break
			x=x-1
			i=i+1
			if f==0:
				conn.send("file not found")
			conn.close()
conn.close()
