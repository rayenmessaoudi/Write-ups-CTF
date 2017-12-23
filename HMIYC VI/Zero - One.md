```python
from pwn import *
conn = remote('137.74.166.111',443)
a = conn.recvline()
while 1:
  b = conn.recvline()
  print b
  data = b.replace("ZERO","0").replace("ONE","1").strip()
  f = ''.join(chr(int(data[i:i+8], 2)) for i in range(0, len(data), 8))
  conn.send(f)
  c = conn.recvline()
  print c
```
