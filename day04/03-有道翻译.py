import requests
import time
import random
from hashlib import md5

def get_salt_sign_ts_bv(word):
    #获取ts
    ts = str(int(time.time()*1000))
    #获取bv
    string = '5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36(KHTML,like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    s = md5()
    s.update(string.encode())
    bv = s.hexdigest()
    #获取salt
    salt = ts + str(random.randint(0,9))
    #获取sign
    sign_string = "fanyideskweb" + word + salt + "@6f#X3=cCuncYssPsuRUE"
    s = md5()
    s.update(sign_string.encode())
    sign = s.hexdigest()

    # print(ts,'\n',bv,'\n',salt,'\n',sign)
    return ts,bv,salt,sign

def attack_yd(word):
    ts,bv,salt,sign = get_salt_sign_ts_bv(word)
    #post的url:F12-network-General-Request URL
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    #定义headers
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9;",
        "Connection": "keep-alive",
        "Content-Length": "251",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-2112278548@10.169.0.83; JSESSIONID=aaafqwav5aAhT5ti6FhSw; OUTFOX_SEARCH_USER_ID_NCOO=2033425382.581202; ___rl__test__cookies=1559198978831",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    #定义data字典：Form表单数据
    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }

    res = requests.post(
        url=url,
        data=data,
        headers=headers
    )
    res.encoding = 'utf-8'
    print(res.text)
    result = res.json()['translateResult'][0][0]['tgt']
    print(result)

if __name__ == '__main__':
    word = input('请输入要翻译的单词:')
    attack_yd(word)
