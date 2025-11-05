import socket

HEADER = 64
PORT = 5050

SERVER = "192.168.100.182"
ADDR = (SERVER,PORT)

client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode('utf-8')
    message_length = len(msg)
    send_length = str(message_length).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length))
    print(send_length)
    client.send(send_length)
    client.send(message)


send("Janvi Golgappa")
send("quit")
