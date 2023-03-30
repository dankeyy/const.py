# const.py
```py
import const

BANANA = 2

BANANA = 3
```

```python
$ python test.py
Traceback (most recent call last):
  File "/home/dankey/dev/projects/const.py/const.py", line 32, in visit_Assign
    raise SyntaxError("get const'd lol").with_traceback(tb)
  File "/home/dankey/dev/projects/const.py/test.py", line 5, in <module>
    BANANA = 3
SyntaxError: get const'd lol
```
for various excuses, no elaborate q&a this time\
have a nice day
