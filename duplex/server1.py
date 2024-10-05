import socket
import threading

# Server configuration
HOST = '192.168.200.73'  # Accept connections on all available interfaces
PORT = 8000             # Arbitrary port to use

clients = []
lock = threading.Lock()  # To ensure thread-safe access to clients list

# Function to handle receiving and broadcasting messages
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    with lock:
        clients.append(conn)
        print(f"Current client: {[client.getpeername() for client in clients]}")

    with conn:
        while True:
            try:
                # Receive messages from client
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"[{addr}]Received message: {data}")
                broadcast(data, conn)
                print(f"Broadcast called with message: {data}")
            except ConnectionResetError:
                print(f"[DISCONNECT ERROR] {addr} disconnected abruptly.")
                break

    # Remove client after disconnecting
    print(f"[DISCONNECT] {addr} disconnected.")
    
    with lock:
        clients.remove(conn)
    
    conn.close()

# Function to broadcast messages to other clients
def broadcast(message, sender_conn):
    with lock:  # Ensure safe access to clients list
        for client in clients:
            if client != sender_conn:
                try:
                    client.sendall(message.encode('utf-8'))
                    print(f"Type")
                except BrokenPipeError:
                    print("[ERROR] Broken pipe, client disconnected unexpectedly.")
                    continue

# Main server loop
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

# Start the server
if __name__ == "__main__":
    print("[STARTING] Server is starting...")
    start_server()

