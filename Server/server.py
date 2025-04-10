import socket
import threading

HOST = '127.0.0.1'
PORT = 32000

def handle_client(conn, addr):
    print(f"接続: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"受信: {data.decode()}")
            conn.sendall(b"Hello, Client!")
    print(f"切断: {addr}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"サーバが {HOST}:{PORT} で待機中……")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()