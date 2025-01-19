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


msg_to_send(f'IP address of client is {host_ip} and the device name {hostname}')
msg_to_send(disconnected)