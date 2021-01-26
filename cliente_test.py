import socket
import csv

address = 'localhost'
port = 8001
add = ((address,port))
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(add)

with open('arquivoOut.csv', 'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    #line = ['Rafael', 'Ramos']
    for line in csv_reader:
        clientSock.sendto(repr(line).encode('utf-8'),(address, port))
    csv_file.close()
clientSock.close()