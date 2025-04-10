import socket
import tkinter as tk
from tkinter import scrolledtext

HOST = '127.0.0.1'
PORT = 32000

def send_message():
    message = entory.get()
    if not message:
        return
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)

    chat_area.insert(tk.END, f"送信: {message}\n")
    chat_area.insert(tk.END, f"受信: {data.decode()}\n")
    entory.delete(0, tk.END)

root = tk.Tk()
root.title("クライアント")

chat_area = scrolledtext.ScrolledText(root, width=40, height=10)
chat_area.pack(padx=10, pady=10)

entory = tk.Entry(root, width=30)
entory.pack(padx=10, pady=5)

send_button = tk.Button(root, text="送信", command=send_message)
send_button.pack(pady=5)

root.mainloop()