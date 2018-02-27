```python
import re
s = 0
with open('even_more_numbers_with_some_mild_inconveniences.txt') as f:
    for line in f:
        match = re.findall(r'\d+?\d*', line)
        for i in range(len(match)):
            s+=int(match[i])

print(s)
```
