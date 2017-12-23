Change the date system to "2011-01-14" and run this dirty script :p 

```python
#gdb -x script.py ./TN-R3V
import gdb
gdb.execute("break *0x4007b6",True,True)
gdb.execute("r",True,True)	
flag =""
while 1:
	k = str(gdb.execute("p/x $rdx",True,True))
	flag+=chr(int(k[5:],16))
	print(flag)
	for i in range(10):
		gdb.execute("ni",True,True)

```
![](https://github.com/aminekaabachi/hackmeifyoucan6/blob/master/Rev/Tunisian%20Revolution/chall.png?raw=true)
