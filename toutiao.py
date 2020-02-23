import requests
import json

# 获取分类下的用户
# https://is-hl.snssdk.com/user/relation/user_recommend/v1/vertical_category_users/?channel_id=2

# 获取用户下的文章
# https://api3-normal-c-hl.snssdk.com/api/feed/profile/v1/?

# 获取文章详情
# https://a6-ipv6.pstatp.com/article/full/24/1/{0}/{0}/1/0/0/0/

def get_params(params):
    p = ''
    for x in params:
        p += x+'='+params[x]+'&'
    return p


def get_url(uid, offset):
    params = {
        'category': 'profile_article',
        'visited_uid': str(uid),
        'count': '20',
        'offset': str(offset),
        'iid': '101092017235',
        'channel': 'huawei',
        'aid': '13',
        'app_name': 'news_article',
        'version_code': '757',
        'device_platform': 'android',
        'device_type': 'JKM-AL00b',
        'os_version': '9',
    }
    p = get_params(params)

    url = 'https://api3-normal-c-hl.snssdk.com/api/feed/profile/v1/?'+p
    return url


headers = {
    'user-agent': 'com.ss.android.article.news/7571 (Linux; U; Android 9; zh_CN_#Hans; JKM-AL00b; Build/HUAWEIJKM-AL00b; Cronet/TTNetVersion:3e14bd94 2019-12-05)',
}

def get_channel_users(channel):
    url = 'https://is-hl.snssdk.com/user/relation/user_recommend/v1/vertical_category_users/?channel_id={}'.format(channel)
    r = requests.get(url, headers=headers, verify=False)
    print(r.json())

get_channel_users(2)

def get_user_articles(uid, offset=0):
    print('offset', offset)
    r = requests.get(get_url(uid, offset), headers=headers, verify=False)
    res = r.json()
    return res['data']


def get_detail(id):
    url = 'https://a6-ipv6.pstatp.com/article/full/24/1/{0}/{0}/1/0/0/0/'.format(
        id)
    r = requests.get(url, headers=headers, verify=False)
    res = r.json()
    title = res['data']['title']
    description = res['data']['abstract'] or title
    content = res['data']['content']

    return [title, description, content]

# get_all()