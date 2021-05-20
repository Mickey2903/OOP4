import socket
import psutil 
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if data == b'End':
                break

            elif data == b'CpuUse':
                conn.sendall(str(psutil.cpu_percent()).encode("utf-8"))

            elif data == b'Name':
                conn.sendall(psutil.users()[0].name.encode("utf-8"))

            elif data == b'Space':
                conn.sendall(str(psutil.disk_usage('/').used).encode('utf-8'))

            elif data == b'Uptime':
                conn.sendall(str(psutil.boot_time()).encode("utf-8"))

            elif data == b'Bank':
                conn.sendall("You dont have the right permissions for this information".encode("utf-8"))