import os, socket 

HOST = "127.0.0.1"  
PORT = 8000  
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ss.bind((HOST, PORT))
ss.listen(2)
print("host binded")


def handle_client(conn, addr, i):
    while True:
        data=conn.recv(1024).decode()
        print(f"from client: {data}")
        if not data:
            break
        conn.sendall(data.encode())
   

def server():
    i = 1
    while i<=2:
        conn, addr = ss.accept()
        print(f"Connected by {addr}")
        child_pid = os.fork()
        if child_pid == 0:
                print("\nconnection successful with client " + str(i) + str(addr) + "\n")
                # handle_client(conn, addr, i)
                while True:
                    data=conn.recv(1024).decode()
                    print(f"from client: {data}")
                    if not data:
                        break
                    conn.sendall(data.encode())
        else:
            i+=1

server()


