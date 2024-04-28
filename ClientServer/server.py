import socket

def send_file(file_path, client_socket):
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server listening on port", port)

    client_socket, client_address = server_socket.accept()
    print("Connection from:", client_address)

    file_path = 'helloWorld.txt'  
    send_file(file_path, client_socket)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
