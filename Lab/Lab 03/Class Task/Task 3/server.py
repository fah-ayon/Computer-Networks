import socket
import threading

port  =5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
buffer =  16
format = 'utf8'
disconnected = 'END'


server_socket_add  = (host_ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_add)

server.listen()
print('Server is listening')

def handle_connection(conn,addr):
    print ('Connected to', addr)
    connected = True
   
    while connected:
       message_length = conn.recv(buffer).decode(format)
       print('Length of message', message_length)
       
       if  message_length:
           message_length= int(message_length)
           msg = conn.recv(message_length).decode(format)
           if msg == disconnected:
               conn.send('Good Bye'.encode(format))
               print('Terminating connection with', addr)
               connected = False
           else:
               vowels = 'aeiouAEIOU'
               count = 0
               for i in msg:
                   if i in vowels:
                       count += 1
               if count == 0:
                   conn.send('Not enough vowels'.encode(format))
               elif count <=2:
                   conn.send('Enough vowels I guess'.encode(format))    
               else:
                   conn.send('Too many vowels'.encode(format))
                    
    conn.close()           
           
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_connection, args=(conn, addr))
    thread.start()