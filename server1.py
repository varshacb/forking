import socket
import os
import multiprocessing 
from multiprocessing import Manager,Value

def handle_client(client_socket,client_list):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        for client in client_list:
            if client!=client_socket:
                client.send(data.encode())
 
    client_socket.close()

def start_chat_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen()
    manager = Manager()    
    client_list = manager.list()    


    print("Chat server is running")
   

    while True:
        client_socket, client_address = server_socket.accept()
        client_list.append(client_socket)
        print(f"Accepted connection from {client_address}")

        pid = os.fork()

        if pid == 0:  
            server_socket.close() 
            handle_client(client_socket,client_list)
            client_socket.close()
            os._exit(0) 
        else: 
            client_socket.close()  

if __name__ == "__main__":
    ports = [9003, 9001, 9002]
    processes = []

    for port in ports:
        process = multiprocessing.Process(target= start_chat_server,args=(port,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()






