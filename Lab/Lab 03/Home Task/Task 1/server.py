import socket

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

while True:
    conn, addr = server.accept()
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
               msg_int = int(msg)
               if msg_int <= 40:
                    conn.send(f'Your salary is {msg_int * 200}'.encode(format))
               else:
                    conn.send(f'Your salary is {msg_int * 300 + 8000}'.encode(format))
                                  
    conn.close()           
           
