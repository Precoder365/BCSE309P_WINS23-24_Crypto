import socket

def receive_file(file_name, server_socket):
    with open(file_name, 'wb') as file:
        data = server_socket.recv(1024)
        while data:
            file.write(data)
            data = server_socket.recv(1024)

def print_file_content(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to server.")

    file_name = 'output.txt'  
    receive_file(file_name, client_socket)

    print("File received successfully:", file_name)
    print_file_content(file_name)

    client_socket.close()

if __name__ == "__main__":
    main()
