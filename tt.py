import requests

params = {
# 'category':'profile_short_video',
'visited_uid':'1750026969678792',
# 'stream_api_version':'88',
'count':'20',
'offset':'1581842812990',
'iid':'101092017235',
# 'device_id':'66021448895',
# 'ac':'wifi',
# 'mac_address':'AC%3A92%3A32%3A6A%3A29%3A10',
'channel':'huawei',
'aid':'13',
'app_name':'news_article',
'version_code':'757',
# 'version_name':'7.5.7',
'device_platform':'android',
# 'ab_version':'662176%2C801968%2C1419049%2C668775%2C1462526%2C1469461%2C1190525%2C1489304%2C1157750%2C1413881%2C1419598%2C1479732%2C1439625%2C1357842%2C1469498%2C668779%2C662099%2C1477262%2C1464847%2C668774%2C1487144%2C1396152%2C765191%2C857804%2C660830%2C1439347%2C1397712%2C1434499%2C1464894',
# 'ab_group':'94569%2C102751',
# 'ab_feature':'94569%2C102751',
# 'ssmix':'a',
'device_type':'JKM-AL00b',
# 'device_brand':'HUAWEI',
# 'language':'zh',
# 'os_api':'28',
'os_version':'9',
# 'uuid':'860201048257623',
# 'openudid':'3970aeed73b9d90f',
# 'manifest_version_code':'7571',
# 'resolution':'1080*2255',
# 'dpi':'480',
# 'update_version_code':'75717',
# '_rticket':'1582088409408',
# 'plugin':'18762',
# 'pos':'5r_-9Onkv6e_eSUXeygqeCUfv7G_8fLz-vTp6Pn4v6esr6yzrqulqq6usb_x_On06ej5-L-nrqyzr6ysrq6vsb_88Pzt3vTp5L-nv3klF3soKnglH7-xv_zw_O3R8vP69Ono-fi_p6yvrLOuq6Wqrq6xv_zw_O3R_On06ej5-L-nrqyzr6ysrq6v4A%3D%3D',
# 'tma_jssdk_version':'1.48.1.3',
# 'rom_version':'emotionui_9.1.0_jkm-al00b+9.1.0.221%28c00e32r1p6%29',
# 'cdid':'9d13e138-0e87-4efd-b2f7-df616bb954df',
# 'oaid':'30b6ffff-f2ff-4351-ffff-dfdb7ad9632c',
}

def get_url(offset):  
    params = {
        'visited_uid':'1750026969678792',
        'count':'20',
        'offset': str(offset),
        'iid':'101092017235',
        'channel':'huawei',
        'aid':'13',
        'app_name':'news_article',
        'version_code':'757',
        'device_platform':'android',
        'device_type':'JKM-AL00b',
        'os_version':'9',
    }
    p = ''
    for x in params:
        p += x+'='+params[x]+'&'

    url = 'https://api3-normal-c-hl.snssdk.com/api/feed/profile/v1/?'+p
    return url

headers = {
# 'Host': 'api3-normal-c-hl.snssdk.com',
# 'Cookie': 'd_ticket=c500faa7c08d1d9ec6d0a491936c5f4fdda06; msh=AjCZq95rzM8OPVzxMnfeBTY7tW8; sid_guard=d4539a5637b0e5651e4501defdd03917%7C1579838876%7C5184000%7CTue%2C+24-Mar-2020+04%3A07%3A56+GMT; uid_tt=44765fa29b9e7b708c74dd98c07c1c72; sid_tt=d4539a5637b0e5651e4501defdd03917; sessionid=d4539a5637b0e5651e4501defdd03917; UM_distinctid=17022c01c9947-08663c7ba2de15-39010b1b-448e0-17022c01c9caf; odin_tt=bf54627f688800b919a191a1fb18ab1f0d64c5db3871e10b0454e2ddef66ec5817efb9af87ff93e07ed0b1bf54f2d1fe; WIN_WH=360_696; install_id=101092017235; ttreq=1$d32e3b1d52e99333819ba1be0c60550b64b5cd4c',
# 'x-ss-req-ticket': '1582088409412',
# 'sdk-version': '2',
# 'x-tt-token': '00d4539a5637b0e5651e4501defdd03917e847c4703a0f2799ef7d8843363cd3044c9bc2753eb783780e9366bb0936182f4b',
# 'passport-sdk-version': '10',
# 'x-ss-dp': '13',
# 'x-tt-trace-id': '00-5bd152bc09f5f2f5cbfe336f0540000d-5bd152bc09f5f2f5-01',
'user-agent': 'com.ss.android.article.news/7571 (Linux; U; Android 9; zh_CN_#Hans; JKM-AL00b; Build/HUAWEIJKM-AL00b; Cronet/TTNetVersion:3e14bd94 2019-12-05)',
# 'x-khronos': '1582088409',
# 'x-gorgon': '0401607d0000dd482bca1c0f86e4f326c6317317f36bb8f8a150',
}

# r = requests.get(url, headers=headers, verify=False)
# print(r.json())

# res = r.json()
# print(type(res))
# print(res.get('has_more'))

def get_all(offset=0):
    print('offset', offset)
    r = requests.get(get_url(offset), headers=headers, verify=False)
    res = r.json()
    print(res)
    if(res.get('has_more')):
        get_all(res.get('offset'))

get_all()

# curl -H 'Host: a6-ipv6.pstatp.com' -H 'x-ss-dp: 13' -H 'x-tt-trace-id: 00-5c1b8c2209f5f2f5cbffeab193e6000d-5c1b8c2209f5f2f5-01' -H 'user-agent: com.ss.android.article.news/7571 (Linux; U; Android 9; zh_CN_#Hans; JKM-AL00b; Build/HUAWEIJKM-AL00b; Cronet/TTNetVersion:3e14bd94 2019-12-05)' -H 'x-khronos: 1582093273' -H 'x-gorgon: 0401e0800000992beafc3473a18a11d1b2632501610aa5966f57' --compressed 'https://a6-ipv6.pstatp.com/article/full/24/1/6781152365346030092/6781152365346030092/1/0/0/0/?iid=101092017235&device_id=66021448895&ac=wifi&mac_address=AC%3A92%3A32%3A6A%3A29%3A10&channel=huawei&aid=13&app_name=news_article&version_code=757&version_name=7.5.7&device_platform=android&ab_version=662099%2C1477262%2C1464847%2C668774%2C1487144%2C1396152%2C765191%2C857804%2C660830%2C1439347%2C1397712%2C1434499%2C662176%2C801968%2C1419049%2C668775%2C1462526%2C1469461%2C1190525%2C1489304%2C1157750%2C1413881%2C1419598%2C1479732%2C1439625%2C1357842%2C1469498%2C668779%2C1464894&ab_group=94569%2C102751&ab_feature=94569%2C102751&ssmix=a&device_type=JKM-AL00b&device_brand=HUAWEI&language=zh&os_api=28&os_version=9&uuid=860201048257623&openudid=3970aeed73b9d90f&manifest_version_code=7571&resolution=1080*2255&dpi=480&update_version_code=75717&_rticket=1582093273763&plugin=18762&pos=5r_-9Onkv6e_eSUXeygqeCUfv7G_8fLz-vTp6Pn4v6esr6yzrqulpK6qsb_x_On06ej5-L-nrqyzr6ysr6Wssb_88Pzt3vTp5L-nv3klF3soKnglH7-xv_zw_O3R8vP69Ono-fi_p6yvrLOuq6Wkrqqxv_zw_O3R_On06ej5-L-nrqyzr6ysr6Ws4A%3D%3D&tma_jssdk_version=1.48.1.3&rom_version=emotionui_9.1.0_jkm-al00b+9.1.0.221%28c00e32r1p6%29&cdid=9d13e138-0e87-4efd-b2f7-df616bb954df&oaid=30b6ffff-f2ff-4351-ffff-dfdb7ad9632c'