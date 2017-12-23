```python
convert 1.png 2.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" flag.png
```
