# from threading import Thread
# import time
# import json

# def delay(x):
#     time.sleep(5)
#     print('打印', x)

# # for x in range(5):
# #     t = Thread(target=delay, args=(x,))
# #     t.start()
# # t.join()

# # print('over')

# from tinydb import TinyDB, Query
# db = TinyDB('./db.json')
# # db.insert({'uid': 1001, 'pids': ['2001']})
# # db.insert({'uid': 1002002, 'pids': ['b']})

# q = Query()
# r = db.contains(q.uid==1001)
# print(r)

# ids = ['10109201723'+str(x) for x in range(9)]
# print(ids)

# import os
# import glob

# t = glob.glob('/Users/mtdp/Desktop/py/workspace/articles/**/*.txt')
# print(len(t))

# for lists in os.listdir('/Users/mtdp/Desktop/py/workspace/articles/5495166052/'):
#     pass
# print(len(lists))

for x in range(10):
    try:
        if x < 5:
            raise NameError
        print(x)
    except Exception:
        print('遇到错误', Exception)
