function parseQueryString(url) {
    var obj = {};
    var keyvalue = [];
    var key = "",
        value = "";
    var paraString = url.substring(url.indexOf("?") + 1, url.length).split("&");
    for (var i in paraString) {
        keyvalue = paraString[i].split("=");
        key = keyvalue[0];
        value = keyvalue[1];
        obj[key] = value;
    }
    console.log(obj)
}

var url = '/api/feed/profile/v1/?category=profile_all&visited_uid=95419130131&stream_api_version=88&count=20&offset=0&client_extra_params=%7B%22playparam%22%3A%22codec_type%3A1%22%7D&iid=101092017235&device_id=66021448895&ac=wifi&mac_address=AC%3A92%3A32%3A6A%3A29%3A10&channel=huawei&aid=13&app_name=news_article&version_code=757&version_name=7.5.7&device_platform=android&ab_version=662099%2C668774%2C1496424%2C1427394%2C765199%2C857803%2C660830%2C1444046%2C1397712%2C1479843%2C1434498%2C662176%2C801968%2C1419053%2C668775%2C1462526%2C1474414%2C1190525%2C1489307%2C1157750%2C1419598%2C1493796%2C1439625%2C1469498%2C668779%2C1464894&ab_group=94569%2C102751&ab_feature=94569%2C102751&ssmix=a&device_type=JKM-AL00b&device_brand=HUAWEI&language=zh&os_api=28&os_version=9&uuid=860201048257623&openudid=3970aeed73b9d90f&manifest_version_code=7571&resolution=1080*2255&dpi=480&update_version_code=75717&_rticket=1582362733197&plugin=18762&pos=5r_-9Onkv6e_eSUXeygqeCUfv7G_8fLz-vTp6Pn4v6esr6yzrqulpKyxv_H86fTp6Pn4v6eurLOvrKyur6yxv_zw_O3e9Onkv6e_eSUXeygqeCUfv7G__PD87dHy8_r06ej5-L-nrK-ss66rpaSssb_88Pzt0fzp9Ono-fi_p66ss6-srK6vrOA%3D&tma_jssdk_version=1.48.1.3&rom_version=emotionui_9.1.0_jkm-al00b+9.1.0.221%28c00e32r1p6%29&cdid=9d13e138-0e87-4efd-b2f7-df616bb954df&oaid=30b6ffff-f2ff-4351-ffff-dfdb7ad9632c'

parseQueryString(url)