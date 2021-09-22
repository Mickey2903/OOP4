import socket
import time
import datetime

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'CpuUse')
    CPU_Usage = s.recv(1024)
    time.sleep(1)

    s.sendall(b'Name')
    serverName = s.recv(1024)
    time.sleep(1)

    s.sendall(b'Space')
    diskSpace = s.recv(1024)
    time.sleep(1)

    s.sendall(b'Bank')
    BankAccount = s.recv(1024)
    time.sleep(1)

    s.sendall(b'Uptime')
    seconds_input = s.recv(1024).decode("utf-8")
    Uptime = datetime.datetime.fromtimestamp(float(seconds_input)).strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(1)

    print("Cpu usage: ", CPU_Usage.decode("utf-8"), "%\n")
    print("Server name: ", serverName.decode("utf-8"), '\n' )
    print("Diskspace available", diskSpace.decode("utf-8"), " Byte\n")
    print("Up since: ", str(Uptime), "\n")
    print("Bankaccount: ", BankAccount.decode("utf-8"), "\n")

    s.sendall(b'END')