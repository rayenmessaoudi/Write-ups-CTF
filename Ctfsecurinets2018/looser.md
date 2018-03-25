![](https://github.com/rayenmessaoudi/Write-ups-CTF/blob/master/Ctfsecurinets2018/xored.png)

```python

from itertools import izip, cycle
import string

def xor(message, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(message, cycle(key)))

key = '\xee'
buffer = open('flag.png.crypt','rb').read()
xored = xor(buffer, key)
file = open('out.png','wb')
file.write(xored)
file.close()
```
