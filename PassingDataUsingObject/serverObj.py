import socket
from _thread import *
from player import Player
import pickle

server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
     s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started")

players = [Player(0,0,50,50,(255,0,0)),Player(100,100,50,50,(0,255,0))]

def Multi_clients(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("DISCONNECTED!!")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received : ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
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