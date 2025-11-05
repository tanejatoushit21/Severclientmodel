import socket
import threading
import time



PORT = 5050
HANDLE = 64    #bytes

SERVER = socket.gethostbyname(socket.gethostname())
ADDR= (SERVER,PORT)


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ADDR))


DISCONNECT_MSG = "quit"





def handle_client(conn, addr):     #to handle the connection
    print(f"NEW CONNECTION AT {addr}")

    connection = True
    while connection:
        msg_length= conn.recv(HANDLE).decode('utf-8').strip()
        msg_length = int(msg_length)
        data = conn.recv(msg_length)
        if not data :
            break
        msg = conn.recv(msg_length).decode('utf-8')
        print(f"{addr} , {msg}")
        
        if not msg_length:
            break  
        if msg == DISCONNECT_MSG:
            conn.close()
        

    conn.close()        
  
        
    



def start():                       #to start the server                         
    server.listen()
    print(f"Listening on {ADDR}")
    while True:
        conn ,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        






print("SERVER is starting...")
start()


       

     


