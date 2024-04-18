import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print("Disconnected from server.")
                break
            print(f"Received message from server: {message}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_messages(client_socket):
    while True:
        try:
            message = input("Enter message: ")
            if not message:
                continue
            client_socket.send(message.encode())
        except Exception as e:
            print(f"Error sending message: {e}")
            break

def connect_to_server(host, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        send_thread = threading.Thread(target=send_messages, args=(client_socket,))
        send_thread.start()

        receive_thread.join()
        send_thread.join()

    except Exception as e:
        print(f"Error connecting to server: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    host = 'localhost'
    port = 9000  
    connect_to_server(host, port)
