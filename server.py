import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.209.1.195',9000))
server.listen(1)
print("Tudo Ok!")

connection, address = server.accept()
namefile = connection.recv(1024).decode()

with open(namefile, 'rb') as file:
        for data in file .readline():
                connection.send(data)

        print(f"{namefile} \n Arquivo Enviado")
