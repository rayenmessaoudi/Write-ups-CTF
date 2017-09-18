>  nc misc.chal.csaw.io 4239

>  8-1-1 even parity. Respond with '1' if you got the byte, '0' to retransmit.



Just googling name challenge (serial) with 8-1-1 we got the first link of [wikipedia](https://en.wikipedia.org/wiki/8-N-1)
8-N-1 is a common shorthand notation for a serial port parameter setting or configuration in asynchronous mode, in which there are eight (8) data bits, no (N) parity bit, and one (1) stop bit.


![ss](https://github.com/rayenmessaoudi/Write-ups-CTF/blob/master/CSAW%202017/50d2066fce395fc43b000000.png)

Starting bit[0] always = 0    
Ending bit[10] always = 1    
Parity bit[9] if the number of '1' is even, the parity bit should be 0, and if it is odd the parity bit should be 1   
Data bit[1-8]

We need just to check parity and then append data (character) representation of that byte to our flag


```
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
                flag += chr(int(d,2))
                print flag
                sock.send("1")
        else:
                sock.send("0")

```

```
flag{@n_int3rface_betw33n_data_term1nal_3quipment_and_d@t@_circuit-term1nating_3quipment}
```

![sss](https://raw.githubusercontent.com/rayenmessaoudi/Write-ups-CTF/master/CSAW%202017/Capture.PNG)
