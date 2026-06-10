import socket

HOST = 'localhost'
PORT = 9999

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"[*] Connected to {HOST}:{PORT}")
        while True:
            msg = input("You: ")
            if msg.lower() in ('exit', 'quit'):
                break
            client.sendall(msg.encode())
            response = client.recv(1024).decode()
            print(f"Server: {response}")

if __name__ == "__main__":
    main()