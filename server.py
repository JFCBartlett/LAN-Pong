import socket
from _thread import *
from player import player
from ball import ball
import pickle

server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server started")

players = [player(30, 10, 40, 160, (255, 255, 255)), player(930, 10, 40, 160, (255, 255, 255))]
ball = ball(500, 300, 20, 20, (255, 255, 255))


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = " "
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                    ball.update()
                    print(ball)


                else:
                    reply = players[1]


                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
            conn.sendall(pickle.dumps(ball))

        except:
            break
    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
