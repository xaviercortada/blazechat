__author__ = 'xavier cortada'


# echo_server.py
import socket
import select
import sys

def runServer():

    host = ''
    '''hello'''
    port = 50000
    backlog = 5
    size = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(backlog)
    input = [server,sys.stdin]

    running = 1


    while running:
        inputready,outputready,exceptready = select.select(input,[],[])

        for s in inputready:

            if s == server:
                # handle the server socket
                client, address = server.accept()
                input.append(client)

            elif s == sys.stdin:
                # handle standard input
                junk = sys.stdin.readline()
                running = 0

            else:
                # handle all other sockets
                data = s.recv(size)
                if data:
                    if data == 'essssxit':
                        running = 0
                    s.send(data)
                else:
                    s.close()
                    input.remove(s)
    server.close()



if __name__ == '__main__':
    runServer()
