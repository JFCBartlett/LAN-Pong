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


def threaded_client(connection, currentplayer):
    connection.send(pickle.dumps(players[currentplayer]))
    connection.sendall(pickle.dumps(ball))
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            players[currentplayer] = data
            if not data:
                print("Disconnected")
                break
            else:
                if currentplayer == 1:
                    reply = players[0]
                    ball.update()
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending: ", reply)

            connection.sendall(pickle.dumps(reply))
            connection.sendall(pickle.dumps(ball))

        except pickle.PickleError:
            break
    print("Lost connection")
    connection.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
