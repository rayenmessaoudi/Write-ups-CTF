```python

import requests
import urllib2

login = urllib2.urlopen("http://shattered.io/static/shattered-1.pdf").read()[:500];
password = urllib2.urlopen("http://shattered.io/static/shattered-2.pdf").read()[:500];

params = { 'login': login, 'password' : password }
 
r = requests.get('https://www.youp0wn.com/chll/ch11/', params);

print r.text
```
