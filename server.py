import socket            
 
# next create a socket object
s = socket.socket()        
 
# reserve a port
port = 8080               
 
# bind to the port
s.bind(('', port))        
print(f'socket binded to {port}')
 
# put the socket into listening mode, number of max connections while server is busy 
s.listen(5)    
print("socket is listening")           
 
# a forever loop
while True:
 
# Establish connection with client.
  c, addr = s.accept()    
  print('Got connection from', addr )
 
  # send data to the client. encoding to send byte type.
  c.send('galinha pintadinha'.encode())
  
  # print data received from client, decoded as string
  print(c.recv(1024).decode())
 
  # Close the connection with the client
  c.close()
   
  # Breaking once connection closed
#   break