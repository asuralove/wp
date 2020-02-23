from threading import Thread
import time
import json


from tinydb import TinyDB, Query
db = TinyDB('./db.json')
# db.insert({'uid': 1001, 'pids': ['2001']})
# db.insert({'uid': 1002002, 'pids': ['b']})

q = Query()
r = db.contains(q.uid==1001)
print(r)