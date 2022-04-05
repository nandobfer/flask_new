# Import socket module
import socket            
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 7173              
 
# connect to the server on local computer
s.connect(('35.198.16.4', port))
s.send('patati e patata'.encode())
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close() 