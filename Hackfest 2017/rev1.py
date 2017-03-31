"""
[HackFest Qualification 2017]
not the most elegent code :p
flag : hackfest{it_was_b58}
"""


def ff(x):
	p = 1
	while True:
		s = p
		p = p << 8
		if p > x :
			return s
			


ch = '2GYhdiSLoJTRvASGXjIHtatb9Kdr'
ch = ch[::-1]
b = '123456789NOPQRSTUWXYZACDEFGHIJKLMnopqrstuvwxzabcdefghijklm'

x = 0
for i in range(len(ch))[::-1]:
        m = b.find(ch[i])
        x = x * 58 + m


liste = []
while x > 0 :
	a , b = divmod(x,ff(x))
	liste.append(a)
	x = b

r = ''
for i in liste:
	r+=chr(i)

print "The flag is : ",r
