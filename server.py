import socket,threading
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(1)

a=[]
c,addr=s.accept()
a.append(c)
print("got connection",addr)
def broadcast():
	while True:
		
		message=input()
		if message:
			c.send(str.encode(message))
		 
		
thread_client = threading.Thread(target=broadcast)
thread_client.start()
while True:
	
		data=c.recv(2048)
		
		print(data)
		
			

c.close()


