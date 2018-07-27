import socket

hote = "localhost"
port = 25565

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connection on {}".format(port))

socket.send(b"Hey my name is Olivier!")

print("Close")
socket.close()
