from threading import Thread
import time
import json

def delay(x):
    time.sleep(5)
    print('打印', x)

# for x in range(5):
#     t = Thread(target=delay, args=(x,))
#     t.start()
# t.join()

# print('over')

from tinydb import TinyDB, Query
db = TinyDB('./db.json')
# db.insert({'uid': 1001, 'pids': ['2001']})
# db.insert({'uid': 1002002, 'pids': ['b']})

q = Query()
r = db.contains(q.uid==1001)
print(r)