import socket
import sys

portas = [21, 22 , 80 , 8080 , 443 , 3306]
host = sys.argv[1]

for porta in range(1, 65536):
    ipAdress = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    ipAdress.settimeout(0.5)

    code = ipAdress.connect_ex((host, porta))

    if code == 0:
        ipAdress.connect((host , porta))

        try:
            banner = ipAdress.recv(1024).decode().replace("\n" , "")
        except:
            banner = "Não identificado"
        print(porta, banner)

        ipAdress.close()