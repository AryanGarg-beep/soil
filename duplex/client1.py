import socket
import threading

def receive_messages(s):
    while True:
        try:
            # Listen for messages from the server
            data = s.recv(1024).decode('utf-8')
            if not data:
                print("Server closed the connection.")
                break
            print("Received:", data)
        except ConnectionAbortedError:
            print("Connection closed by server.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

def send_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect(('192.168.200.73', 11115))  # Replace with your server IP
    
    # Start a thread to listen for incoming messages
    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()

    while True:
        message = input("Enter message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            s.send("exit".encode('utf-8'))
            break

        # Send message to the server
        s.send(message.encode('utf-8'))

    s.close()
    print("Connection closed.")

# Run the client
send_message()

