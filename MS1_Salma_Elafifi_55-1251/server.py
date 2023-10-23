import socket
import threading

PORT = 5605
ADDR = ('127.0.0.1', PORT)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        data = conn.recv(1024)
        if not data:
            print(f"[CONNECTION CLOSED] {addr} disconnected.")
            break
        
        
        response = data.decode().upper()
        conn.send(response.encode())

    conn.close()

def main():
    print("Server is starting...")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)
    
    print(f"Server is listening on {ADDR}")
    
    while True:  
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        
        
        threading.Thread(target=handle_client, args=(conn, addr)).start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()
