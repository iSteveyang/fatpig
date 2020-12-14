import requests
import time
import re
import os

number = input('Number:')
uid = input('Uid:')

token = requests.get(
    'http://120.78.144.40:9180/service.asmx/UserLoginStr?name=121956840&psw=142536')
print('Token OK')

readyM = requests.get(
    'http://120.78.144.40:9180/service.asmx/mkHM2Str?token=%s&xmid=77914&hm=%s&op=1&pk=&rj=121956840' % (token.text, number))
print('Ready msg: %s' % (readyM.text))

sendM = requests.get(
    'http://fatpigchain.com/index.php?r=app2/send-sms&phone=%s' % (number))
print(sendM.text)

for i in range(12):
    receiveM = requests.get(
        'http://120.78.144.40:9180/service.asmx/GetYzm2Str?token=%s&xmid=77914&hm=%s&sf=1' % (token.text, number))
    if len(receiveM.text) > 10:
        release = requests.get(
            'http://120.78.144.40:9180/service.asmx/sfHmStr?token=%s&hm=%s' % (token.text, number))
        if release.text == '1':
            print('Get msg release OK')
        else:
            print(release.text)
        code = re.findall(r"为(.+?),", receiveM.text)
        print(code)
        # Change or set transaction password
        url = 'http://fatpigchain.com/index.php?r=app2/change-transaction-password'
        d = {'phone': number, 'confirm_transpwd': '12345678',
                'code': code, 'transpwd': '12345678'}
        response = requests.post(url, data=d)
        print(response.text)
        break
    else:
        if receiveM.text == '1':
            print('...')
        else:
            if receiveM.text == '-3':
                time.sleep(5)
            else:
                print('Get msg wrong, code: %s' % (receiveM.text))
                release = requests.get(
                    'http://120.78.144.40:9180/service.asmx/sfHmStr?token=%s&hm=%s' % (token.text, number))
                if release.text == '1':
                    print('Release OK')
                else:
                    print(release.text)
                break
        time.sleep(5)

readyM = requests.get(
    'http://120.78.144.40:9180/service.asmx/mkHM2Str?token=%s&xmid=77914&hm=%s&op=1&pk=&rj=121956840' % (token.text, number))
print('Ready msg 2: %s' % (readyM.text))

sendM = requests.get(
    'http://fatpigchain.com/index.php?r=app2/send-sms&phone=%s' % (number))
print(sendM.text)

for i in range(12):
    receiveM = requests.get(
        'http://120.78.144.40:9180/service.asmx/GetYzm2Str?token=%s&xmid=77914&hm=%s&sf=1' % (token.text, number))
    if len(receiveM.text) > 10:
        release = requests.get(
            'http://120.78.144.40:9180/service.asmx/sfHmStr?token=%s&hm=%s' % (token.text, number))
        if release.text == '1':
            print('Get msg release OK')
        else:
            print(release.text)
        code = re.findall(r"为(.+?),", receiveM.text)
        print(code)
        # uid = requests.get(
        #     'http://fatpigchain.com/index.php?r=app/get-my-invite&page=116&code=8878Pf')

        # change btc address
        url = 'http://fatpigchain.com/index.php?r=app2/change-btc-address'
        dt = {'phone': number, 'confirm_btc_address': '0x0EA020684102D32ee1E850Ca6e524a6cD2a901ac',
                'code': code, 'btc_address': '0x0EA020684102D32ee1E850Ca6e524a6cD2a901ac', 'uid': uid}
        response = requests.post(url, data=d)
        print(response.text)
        break
    else:
        if receiveM.text == '1':
            print('...')
        else:
            if receiveM.text == '-3':
                time.sleep(5)
            else:
                print('Get msg wrong, code: %s' % (receiveM.text))
                release = requests.get(
                    'http://120.78.144.40:9180/service.asmx/sfHmStr?token=%s&hm=%s' % (token.text, number))
                if release.text == '1':
                    print('Release OK')
                else:
                    print(release.text)
                break
        time.sleep(5)
