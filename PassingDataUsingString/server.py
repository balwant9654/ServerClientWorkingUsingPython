import socket
from _thread import *

server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
     s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]),int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0, 0), (100, 100)]

def Multi_clients(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("DISCONNECTED!!")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received : ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("Lost Connection")
    conn.close()

CurrentPlayer = 0

while True:

    conn, addr = s.accept()
    print("Connected to : ", addr)

    start_new_thread(Multi_clients, (conn, CurrentPlayer))

    CurrentPlayer += 1