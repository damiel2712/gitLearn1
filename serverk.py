import socket
import Tkinter as tk

def main():
    root = tk.tk()
    
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 8111))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)
    print(data)
    server_socket.close()
    client_socket.close()
    while True:
        x = input("what do you want?\n")
        my_socket = socket.socket()
        my_socket.connect(("127.0.0.1", x))
        my_socket.send(str(x))
        my_socket.close()

        server_socket = socket.socket()
        server_socket.bind(("0.0.0.0", x))
        server_socket.listen(1)
        client_socket, address = server_socket.accept()
        data = client_socket.recv(1024)
        newport = data[-4]





if __name__ == '__main__':
    main()
