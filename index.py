from toutiao import get_user_articles, get_detail
import json
import urllib3
import colorful as cf
import os
import time
import threading

divider = """*******************
*******************"""

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




def write_file(uid, pid, data):
    uid_folders = './articles/{}'.format(uid)
    if not os.path.exists(uid_folders):
        os.makedirs(uid_folders)
    with open('{}/{}.txt'.format(uid_folders, pid), 'w', encoding='utf-8') as f:
        f.write(data)
        log = cf.white('文件写入成功')
        print(log)

def save_detail(uid, x):
    content = json.loads(x['content'])
    pid = content['item_id']
    log = cf.yellow('文章id:{}'.format(pid))
    print(log)

    detail = get_detail(pid)
    log = cf.green('获取到详情标题：{}'.format(detail[0]))
    print(log)

    write_file(uid, pid, '#####'.join(detail))


def start(uid, offset=0):
    articles = get_user_articles(uid, offset)
    log = cf.bold_cyan('用户【{}】当前文章数量:{}'.format(uid, len(articles['data'])))
    print(log)
    print(divider)
    start_time = time.time()
    print(start_time)

    threads = []
    for x in articles['data']:
        t = threading.Thread(target=save_detail, args=(uid, x,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    end_time = time.time()
    log = cf.orange('本轮耗时：{}'.format(end_time-start_time))
    print(log)

    if articles['has_more']:
        log = cf.green('还有更多数据')
        print(log)
        print(divider)
        start(uid, articles['offset'])

start('6503268807')

# 50731867122
# 61186032861
# 78725370991
# 5495166052
# 6503268807

# with open('./datas/95419130131-6547847444770587143.txt', 'r') as f:
#     txt = f.read()
#     print(type(txt))
#     data = translate('你好吗')
#     print(data)
