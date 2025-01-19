import socket

port  =5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
format = 'utf8'
buffer = 16
disconnected = 'END'

server_socket_add  = (host_ip, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_socket_add)


def msg_to_send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    msg_length = str(msg_length).encode(format)
    msg_length += b' '*(buffer-len(msg_length))
    
    client.send(msg_length)
    client.send(message)
    
    print(client.recv(2048).decode(format))


while True:
    inpt = input('How many hours did you work this month?: ')
    if inpt == disconnected:
        msg_to_send(disconnected)
        break
    else:
        hours_worked = int(inpt)
        msg_to_send(str(hours_worked))