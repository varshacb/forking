import socket
import multiprocessing

MAX_CONNECTIONS = 2

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print(f"Client {client_address} disconnected")
                break

            print(f"Received message from {client_address}: {message}")
            
            for client in clients:
                print("inside for")
                print(len(clients))
                if client != client_socket:
                    print("inside if")
                    client.send(message.encode())
                    print("after send")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break

    client_socket.close()
    with lock:
        clients.remove(client_socket)

def start_chat_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)
    print(f"Server listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        with lock:
            if len(clients) >= MAX_CONNECTIONS:
                print(f"Connection from {client_address} rejected. Maximum connections reached.")
                client_socket.close()
                continue

            clients.append(client_socket)
            print(clients)
        client_process = multiprocessing.Process(target=handle_client, args=(client_socket, client_address))
        client_process.start()

clients = []
lock = multiprocessing.Lock()

if __name__ == "__main__":
    ports = [9000, 9001, 9002]
    processes = []

    for port in ports:
        process = multiprocessing.Process(target=start_chat_server, args=(port,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
