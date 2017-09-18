import socket

server = ("misc.chal.csaw.io", 4239)
flag = "" 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server)
while(True): 
        data = sock.recv(2048) 
        byte = data[-12:]
        d = byte[1:9]
        parity = byte[9]
        if  d.count('1') % 2 == int(parity):
                f += chr(int(d,2))
                print f
                sock.send("1")
        else:
                sock.send("0")
