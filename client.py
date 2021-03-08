import socket
import threading
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12345
s.connect((host,port))
print("connected to"+str(host)+"on port"+str(port))

def broadcast():
	while True:
		
		message=input()
		if message:
			s.send(str.encode(message))
		
thread_client = threading.Thread(target=broadcast)
thread_client.start()

				
while True:
		
	data=s.recv(2048)
	
	print(data)
		
			

	
s.close()
	

	

