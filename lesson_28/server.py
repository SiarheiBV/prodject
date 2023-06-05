import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5001))
sock.listen()

BUF_SIZE = 4096

while True:
    print("server is ready")
    client, addr = sock.accept()
    print(f"Connection recieved from {addr}")
    while True:
        data = client.recv(BUF_SIZE)
        if not data:
            break
        print(data)
        req = input()
        client.sendall(bytes(req))
