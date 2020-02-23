from toutiao import get_user_articles, get_detail
from trans import translate
from wp import publish
import json
import urllib3
import colorful as cf

divider = """*******************
*******************"""

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# def start2():
#     data = get_user_articles()
#     for x in data:
#         # print(x)
#         content = json.loads(x['content'])
#         if content and content['display_url']:
#             id = content['item_id']
#             print('content', id)
#             r = get_detail(id)
#             if r:
#                 print_msg('获取详情成功')
#             detail = '#####'.join(get_detail(id))
#             trans = translate(detail)
#             print_msg('翻译成功')
#             p = publish(trans[0], trans[1], trans[2])
#             if p:
#                 print_msg('发布成功')


def start(uid):
    articles = get_user_articles(uid)
    log = cf.bold_cyan('用户【{}】当前文章数量:{}'.format(uid, len(articles)))
    print(log)
    print(divider)
    for x in articles:
        content = json.loads(x['content'])
        pid = content['item_id']
        log = cf.yellow('文章id:{}'.format(pid))
        print(log)

        detail = get_detail(pid)
        log = cf.green('获取到详情标题：{}'.format(detail[0]))
        print(log)

        with open('./datas/{}-{}.txt'.format(uid, pid), 'w') as f:
            f.write('#####'.join(detail))
        log = cf.white('文件写入成功')
        print(log)

# start('95419130131')

with open('./datas/95419130131-6547847444770587143.txt', 'r') as f:
    txt = f.read()
    print(type(txt))
    data = translate('你好吗')
    print(data)