import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.209.1.195', 7777))
print("conectado ! \n")

namefile = str(input('Arquivo'))
client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.serv(1000000)
        if not data:
            break
        file.write(data)
print("Recebido")