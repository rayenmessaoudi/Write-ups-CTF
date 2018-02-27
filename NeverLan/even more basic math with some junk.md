```python
import re
s = 0
with open('ga.txt') as f:
    for line in f:
        match = re.findall(r'\d+?\d*', line)
        for i in range(len(match)):
            s+=int(match[i])

print(s)
```
