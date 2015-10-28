## Shaishufang Lib Usage
### To get a simply run, check out the main.py and run, ater finishes, u will get a list of ISBNs
```bash
./main.py
```

### To integrate into ur own program, import UserIsbns
```python
# import lib first
from UserIsbns import UserIsbns

# set uid and cookie
uid = '258536'
cookie = 'shaishufang=Mjc5MTYwfGZmY2VmYzIyYmMxZjhlZThjNzgzYjFlOGIxOWUwODg2'

# create object and run it
ui = UserIsbns(uid, cookie)
ui.run() # this will return a list that contains isbn
```
